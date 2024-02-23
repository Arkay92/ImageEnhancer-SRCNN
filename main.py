from flask import Flask, request, jsonify, safe_join
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array, load_img
import numpy as np
import base64
from PIL import Image
import io
import os

app = Flask(__name__)

# Assuming 'srcnn_model.h5' is in the same directory as this script
MODEL_PATH = 'srcnn_model.h5'

# Load the trained SRCNN model
srcnn_model = load_model(MODEL_PATH)

def preprocess_image(image_path, target_size=(256, 256)):
    """Load and preprocess the image for the SRCNN model."""
    try:
        img = load_img(image_path, target_size=target_size)
        img = img_to_array(img)
        img = np.expand_dims(img, axis=0)  # Model expects a batch of images
        return img
    except Exception as e:
        raise ValueError(f"Error processing image at {image_path}: {e}")

def upscale_image(model, image):
    """Use the SRCNN model to upscale the image."""
    try:
        return model.predict(image)
    except Exception as e:
        raise ValueError(f"Error during model prediction: {e}")

def save_image(image, path="upscaled_image.jpg"):
    """Save the upscaled image to a file."""
    try:
        im = Image.fromarray(image)
        im.save(path)
        return path
    except Exception as e:
        raise ValueError(f"Error saving image to {path}: {e}")

def encode_image_base64(image):
    """Encode the upscaled image in base64 format."""
    try:
        buffered = io.BytesIO()
        im = Image.fromarray(image)
        im.save(buffered, format="JPEG")
        return base64.b64encode(buffered.getvalue()).decode()
    except Exception as e:
        raise ValueError(f"Error encoding image to base64: {e}")

@app.route('/upscale', methods=['POST'])
def upscale():
    """Endpoint to receive an image path and return the upscaled image."""
    data = request.get_json()

    if 'image_path' not in data:
        return jsonify({'error': 'No image path provided'}), 400

    try:
        # Ensure the path is safe to use
        base_dir = os.path.abspath("path_to_images")  # Define your base directory for images
        image_path = safe_join(base_dir, data['image_path'])

        original_image = preprocess_image(image_path)
        upscaled_image = upscale_image(srcnn_model, original_image)

        # Convert upscaled image to a format that can be saved or encoded
        upscaled_image = np.clip(upscaled_image.squeeze(), 0, 255).astype('uint8')

        # Save the image or encode it in base64
        if data.get('save_to_file', False):
            # Save the image to a file and return the path
            output_path = save_image(upscaled_image)
            return jsonify({'message': 'Image upscaled successfully', 'file_path': output_path})
        else:
            # Encode the image in base64 and return the string
            base64_image = encode_image_base64(upscaled_image)
            return jsonify({'message': 'Image upscaled successfully', 'base64_image': base64_image})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
