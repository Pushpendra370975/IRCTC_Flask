# admin.py - Placeholder content
from flask import Blueprint, request, jsonify
from services.train_service import add_train

admin_bp = Blueprint('admin', __name__)

@admin_bp.route('/trains', methods=['POST'])
def create_train():
    api_key = request.headers.get('Authorization')
    if api_key != "Bearer <your_api_key>":
        return jsonify({"error": "Unauthorized"}), 403
    return add_train(request.json)

