# booking.py
from flask import Blueprint, request, jsonify
from services.booking_service import book_seat, get_booking

booking_bp = Blueprint('booking', __name__)

@booking_bp.route('/book', methods=['POST'])
def book():
    return book_seat(request.json)

@booking_bp.route('/booking/<int:booking_id>', methods=['GET'])
def get_booking_details(booking_id):
    return get_booking(booking_id)# booking.py - Placeholder content
