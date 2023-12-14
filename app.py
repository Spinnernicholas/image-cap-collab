from flask import Flask, jsonify, send_from_directory
import yaml
import os
from server.database import db
from server.image import Image
from server.annotation import Annotation

app = Flask(__name__, static_folder='public')

with open('config.yaml', 'r') as file:
    config = yaml.safe_load(file)

app.config.update(config)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, app.config['database']['filename'])

db.init_app(app)
with app.app_context():
    db.create_all()

    # Insert database records for all images in the dataset directory
    dataset_dir = app.config['app']['dataset_path']
    import_stats = [0, 0]
    for filename in os.listdir(dataset_dir):
        if filename.endswith('.jpg') or filename.endswith('.png'):
            if not Image.query.filter_by(filename=filename).first():
                import_stats[0] += 1
                image = Image(filename=filename)
                db.session.add(image)
                
                annotation = Annotation(caption="Bulbasaur is a grass/poison type Pokémon with a plant bulb on its back.")
                image.annotations.append(annotation)
            else:
                import_stats[1] += 1
    db.session.commit()

    print(f"Imported {import_stats[0]} new images, skipped {import_stats[1]} existing images.")

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    if path != "" and os.path.exists(app.static_folder + '/' + path):
        return send_from_directory(app.static_folder, path)
    else:
        return send_from_directory(app.static_folder, 'index.html')

@app.route('/hello')
def hello():
    return {'name': app.config['app']['hello']}

@app.route('/api/images/<filename>', methods=['GET'])
def get_image_file(filename):
    return send_from_directory(app.config['app']['dataset_path'], filename)

@app.route('/api/images', methods=['GET'])
def get_images():
    images = Image.query.all()
    return jsonify([image.to_dict() for image in images])

@app.route('/api/images/<int:image_id>', methods=['GET'])
def get_image(image_id):
    image = Image.query.filter_by(id = image_id).first()
    return jsonify(image.to_dict())

@app.route('/api/images/<int:image_id>/annotations', methods=['GET'])
def get_annotations(image_id):
    annotations = Annotation.query.filter_by(image_id=image_id).all()
    return jsonify([annotation.to_dict() for annotation in annotations])

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description="Run the Flask server for the Svelte app.")
    parser.add_argument('--dev', action='store_true', help="Run in development mode.")
    args = parser.parse_args()

    app.run(debug=args.dev, port=5000)