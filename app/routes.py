from flask import Blueprint, jsonify, request
from app.models import Slot
from app import db

slots_bp = Blueprint('slots', __name__)

@slots_bp.route('/slots', methods=['GET'])
def get_available_slots():
    available_slots = Slot.query.filter_by(is_booked=False).all()
    return jsonify([slot.time for slot in available_slots]), 200

@slots_bp.route('/slots/<int:slot_id>/book', methods=['POST'])
def book_slot(slot_id):
    slot = Slot.query.get_or_404(slot_id)
    if slot.is_booked:
        return jsonify(error='Slot already booked'), 400
    slot.is_booked = True
    db.session.commit()
    return jsonify(success=f'Slot {slot_id} booked'), 200
