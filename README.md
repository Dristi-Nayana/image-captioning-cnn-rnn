# image-captioning-cnn-rnn
This project presents a deep learning-based approach for automatically generating descriptive captions from images by combining Computer Vision and Natural Language Processing.

# Vision2Text: Image Captioning using CNN-RNN Framework

## 🚀 Overview

- Developed an image captioning system using a hybrid CNN-RNN architecture  
- Extracted visual features using CNN (VGG16)  
- Generated captions using RNN (LSTM)  
- Trained on Flickr8k dataset (8K images, 40K captions)
- Bridges the gap between visual understanding and language generation

## 🧠 Methodology

- CNN (VGG16) → feature extraction  
- RNN (LSTM) → caption generation  
- Sequence modeling using startseq and endseq tokens

## Workflow
1. Input image
2. CNN extracts feature vector
3. Feature vector passed to RNN
4. RNN generates caption sequence

## 📂 Dataset

📊 [Dataset](https://www.kaggle.com/datasets/adityajn105/flickr8k)

## 🔧 Preprocessing
# Image Processing
 - Resized images to fixed input size (224×224)
 - Normalized pixel values
# Text Processing
 - Converted text to lowercase
 - Removed special characters
 - Added sequence tokens

## Example:

 - Before: Two dogs are playing on the road
 - After: startseq two dogs are playing on the road endseq

## 🏗 System Architecture

CNN (VGG16) → Feature Vector → RNN (LSTM) → Caption Output

## 💻 Code Structure
feature_extraction.py → Extracts image features using VGG16
caption_model.py → Defines CNN-RNN architecture
generate_caption.py → Generates captions from images
sample.jpg → Example input image

## ▶️ How to Run
1. Install dependencies
pip install -r requirements.txt

2. Run caption generation
python src/generate_caption.py

## 📦 Pre-trained Model & Features

Due to size limitations, model and features are hosted externally:

🔗 Model (best_model.h5): [ADD_GOOGLE_DRIVE_LINK](https://drive.google.com/file/d/1xL4ZDDvlgQIg1EliaDINmc8lo0Lgv1yM/view?usp=sharing)
🔗 Features (features.pkl): [ADD_GOOGLE_DRIVE_LINK ](https://drive.google.com/file/d/1MXinTCh7naSOInGsQkepnZWQKdzeCKeq/view?usp=sharing)

## 📊 Applications
- Assistive technology for visually impaired individuals
- Image search and retrieval systems
- Automated content generation
- Social media and digital asset tagging

## ⚠️ Note

This repository demonstrates the implementation pipeline of an image captioning system.
Additional components such as tokenizer and vocabulary mapping can be extended for full training and evaluation.

## 🔗 Future Work
Implement attention mechanisms (Show, Attend and Tell)
Evaluate using BLEU score
Use transformer-based architectures
Improve caption quality with pre-trained embeddings


