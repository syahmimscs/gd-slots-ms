from app import db
from datetime import datetime
from flask import jsonify

class Slot(db.Model):
    __tablename__ = 'gym_slots'
    id = db.Column(db.Integer, primary_key=True)
    time = db.Column(db.DateTime, nullable=False, unique=True)
    is_booked = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Slot {self.time} booked: {self.is_booked}>'

    def json(self):
        return {
            'id': self.id,
            'time': self.time.isoformat(),  # Convert datetime to ISO 8601 string
            'is_booked': self.is_booked,
            'created_at': self.created_at.isoformat()  # Convert datetime to ISO 8601 string
        }

