# train.py - Placeholder content
# train.py
from flask import Blueprint, request, jsonify
from services.train_service import get_trains

train_bp = Blueprint('train', __name__)

@train_bp.route('/trains', methods=['GET'])
def get_train_availability():
    source = request.args.get('source')
    destination = request.args.get('destination')
    return get_trains(source, destination)

