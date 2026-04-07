import numpy as np
import pickle
from tensorflow.keras.models import load_model
import matplotlib.pyplot as plt

# Load model
model = load_model("best_model.h5")

# Load features
with open("features.pkl", "rb") as f:
    features = pickle.load(f)

print("Model and features loaded successfully!")

# Dummy caption (since tokenizer not included)
def generate_caption():
    return "a dog is playing on the road"

# Test
caption = generate_caption()
print("Generated Caption:", caption)

# Show sample image
img = plt.imread("sample.jpg")
plt.imshow(img)
plt.title(caption)
plt.axis('off')
plt.show()