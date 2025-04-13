from flask import Blueprint, request, jsonify
from app.utils import run_inference
import os

# Create a Blueprint for the routes
sadtalker_routes = Blueprint('sadtalker_routes', __name__)

@sadtalker_routes.route('/api/sadtalker/generate_static', methods=['POST'])
def sadtalker_static_file():
    """API route to call inference.py with a given filename."""
    # Get the filename from the request
    data = request.json
    if not data or 'filename' not in data:
        return jsonify({'error': 'Filename is required'}), 400

    filename = data['filename']
    print(f"filename uploaded: {filename}")
    # Validate the file path
    source_image_path = os.path.join('/home/ubuntu/SadTalker/examples/source_image', filename)
    if not os.path.isfile(source_image_path):
        return jsonify({'error': f'File {filename} does not exist in examples/source_image/'}), 404

    # Run the inference script
    try:
        output = run_inference(source_image_path, action='static')
        return jsonify({'success': True, 'message': 'Inference completed successfully', 'output': output})
    except Exception as e:
        return jsonify({'error': f'An error occurred: {str(e)}'}), 500

@sadtalker_routes.route('/api/sadtalker/generate_response', methods=['POST'])
def sadtalker_gen_response():
    """API route to call inference.py with a given filename."""
    # Get the filename from the request
    data = request.json
    if not data or 'filename' not in data:
        return jsonify({'error': 'Filename is required'}), 400

    filename = data['filename']
    # Validate the file path
    source_image_path = os.path.join('/home/ubuntu/SadTalker/examples/source_image', filename)
    if not os.path.isfile(source_image_path):
        return jsonify({'error': f'File {filename} does not exist in examples/source_image/'}), 404

    # Run the inference script
    try:
        output = run_inference(source_image_path, action='response')
        return jsonify({'success': True, 'message': 'Inference completed successfully', 'output': output})
    except Exception as e:
        return jsonify({'error': f'An error occurred: {str(e)}'}), 500