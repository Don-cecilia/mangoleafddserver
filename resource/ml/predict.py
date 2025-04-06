import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import os
import sys


model_path = os.path.join(os.path.dirname(__file__), 'mango_disease_detector.h5')

# Load the trained model
model = load_model(model_path)

# Define image size (must match training image size)
img_size = 128

# Define class labels (must match training order)
class_labels = ['anthracnose', 'healthy', 'powdery_mildew']  # Update this if needed

from PIL import Image
import numpy as np

def predict_image(img):  # Now accepts image directly (not just path)
    # If input is a file path (backward compatibility)
    if isinstance(img, str):
        img = Image.open(img)
    
    # If input is a file-like object (e.g., from upload)
    elif hasattr(img, 'read'):
        img = Image.open(img)
    
    # If already PIL Image or array, proceed
    
    # Resize and preprocess
    img = img.resize((img_size, img_size))  # Resize to expected dimensions
    img_array = np.array(img) / 255.0      # Convert to array & normalize
    
    # Add batch dimension if needed
    if len(img_array.shape) == 3:
        img_array = np.expand_dims(img_array, axis=0)
    
    # Predict
    prediction = model.predict(img_array)
    class_index = np.argmax(prediction)
    class_label = class_labels[class_index]
    confidence = np.max(prediction) * 100

    print(f"\nPrediction: {class_label} ({confidence:.2f}% confidence)")
    return class_label
    # Load and preprocess the image
    img = image.load_img(img_path, target_size=(img_size, img_size))
    img_array = image.img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    # Predict
    prediction = model.predict(img_array)
    class_index = np.argmax(prediction)
    class_label = class_labels[class_index]
    confidence = np.max(prediction) * 100

    print(f"\nPrediction: {class_label} ({confidence:.2f}% confidence)")
    return class_label

# Example usage
# if __name__ == "__main__":
#     test_image_path = "test_leaf.jpg"  # Replace with your image path
#     predict_image(test_image_path)
