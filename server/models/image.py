from ..database import db

class Image(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(255))
    filename = db.Column(db.String(255))
    annotations = db.relationship('Annotation', backref='image', lazy=True)

    def to_dict(self):
        return {
            'id': self.id,
            'filename': self.filename,
            # Add your other fields here
        }

    def __repr__(self):
        return f"Image(id={self.id}, filename='{self.filename}', path='{self.path}')"
