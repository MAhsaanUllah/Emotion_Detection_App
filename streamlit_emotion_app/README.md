---
title: Emotion Detection App
emoji: 😻
colorFrom: purple
colorTo: pink
sdk: docker
app_file: app.py
pinned: false
license: mit
short_description: Emotion detection using BERT and Streamlit
---

# Emotion Detection App 😄😢😡😱😍

This is a simple Streamlit-based web application that detects emotions from English text using a fine-tuned BERT model. The model can classify the following six emotions:

- **Joy** 😊  
- **Sadness** 😢  
- **Anger** 😡  
- **Fear** 😱  
- **Love** ❤️  
- **Surprise** 😲  

## 🚀 How to Use

1. Enter any English sentence in the input box.  
2. Click the "Detect Emotion" button.  
3. The app will predict and display the most likely emotion and emoji.

Example:  
> `"I'm so excited for tomorrow!"` → `Joy 😊`

## 🧠 Model Used

The app uses a Hugging Face model from:  
👉 [sickboi25/emotion-detector](https://huggingface.co/sickboi25/emotion-detector)

## 🔧 Tech Stack

- Python 🐍  
- Streamlit  
- Hugging Face Transformers  
- PyTorch  
- Emoji

## 📦 Installation (for local use)

```bash
pip install -r requirements.txt
streamlit run app.py

👤 Made with ❤️ by sickboi25 aka MAhsaanUllah 