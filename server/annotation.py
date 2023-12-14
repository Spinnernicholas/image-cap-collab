from .database import db

class Annotation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    image_id = db.Column(db.Integer, db.ForeignKey('image.id'), nullable=False)
    caption = db.Column(db.String(255), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'image_id': self.image_id,
            'caption': self.caption,
            # Add your other fields here
        }

    def __repr__(self):
        return f"Image(id={self.id}, filename='{self.filename}', path='{self.path}')"
