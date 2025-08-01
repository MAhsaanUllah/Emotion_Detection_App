%%writefile app.py
import streamlit as st
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

# Page settings
st.set_page_config(page_title="Emotion Detector", page_icon="🧠", layout="centered") # Reverted to set_page_config

# Load trained model and tokenizer
model = AutoModelForSequenceClassification.from_pretrained("emotion_model")
tokenizer = AutoTokenizer.from_pretrained("emotion_model")
model.eval()

# Define id2label based on the dataset used in training (from Phase 6)
id2label = {
    0: 'anger',
    1: 'fear',
    2: 'joy',
    3: 'love',
    4: 'sadness',
    5: 'surprise'
}

# Add emojis for each emotion (excluding neutral as it's not in the dataset)
emotion_emojis = {
    "sadness": "😢 Sadness",
    "joy": "😊 Joy",
    "love": "❤️ Love",
    "anger": "😠 Anger",
    "fear": "😨 Fear",
    "surprise": "😲 Surprise"
}


# App header
st.markdown("<h1 style='text-align: center; color: #4A90E2;'>🧠 Emotion Detection App</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Enter a message below to detect its emotional tone.</p>", unsafe_allow_html=True)

# Input form
with st.form(key='emotion_form'):
    user_input = st.text_area("📝 Your Message:", height=150)
    submit_button = st.form_submit_button(label="🔍 Detect Emotion")

if submit_button:
    if user_input.strip() == "":
        st.warning("Please enter some text.")
    else:
        # Tokenize input
        inputs = tokenizer(user_input, return_tensors="pt", truncation=True, padding=True)
        inputs = {k: v.to(model.device) for k, v in inputs.items()}

        # Predict
        with torch.no_grad():
            outputs = model(**inputs)
            # Ensure probabilities are calculated across the correct dimension (dim=1 for batch)
            probs = torch.nn.functional.softmax(outputs.logits, dim=1)

        pred_id = torch.argmax(probs, dim=1).item()
        pred_label = id2label[pred_id]
        confidence = probs[0][pred_id].item()

        # Get emotion text with emoji
        # Use get with a default to handle any unexpected labels, though id2label should prevent this.
        emotion_text_with_emoji = emotion_emojis.get(pred_label, f"❓ {pred_label.capitalize()}")


        # Result Display
        st.markdown(f"""
            <div style='background-color:#E6F4EA; padding:20px; border-radius:10px; text-align:center;'>
                <h2 style='color:#2E8B57;'>{emotion_text_with_emoji}</h2>
                <p style='font-size: 16px;'>Confidence: {confidence:.2%}</p>
            </div>
        """, unsafe_allow_html=True)

        # Bar chart for all emotion scores
        # Ensure we iterate through the correct number of labels and use the correct mapping
        score_dict = {id2label[i]: float(probs[0][i]) for i in range(len(id2label))} # Use len(id2label) for correct range
        st.markdown("### 🔍 Emotion Confidence Scores")
        st.bar_chart(score_dict)