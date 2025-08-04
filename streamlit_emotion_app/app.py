import streamlit as st
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

# 🚀 Set up the Streamlit page
st.set_page_config(page_title="Emotion Detector", page_icon="🧠", layout="centered")

# 📦 Load fine-tuned emotion detection model
model = AutoModelForSequenceClassification.from_pretrained("emotion_model")
tokenizer = AutoTokenizer.from_pretrained("emotion_model")
model.eval()

# 🏷️ Label mapping
id2label = {
    0: 'anger',
    1: 'fear',
    2: 'joy',
    3: 'love',
    4: 'sadness',
    5: 'surprise'
}

# 😄 Emoji for each emotion
emotion_emojis = {
    "anger": "😠 Anger",
    "fear": "😨 Fear",
    "joy": "😊 Joy",
    "love": "❤️ Love",
    "sadness": "😢 Sadness",
    "surprise": "😲 Surprise"
}

# 🧠 App UI
st.markdown("<h1 style='text-align: center; color: #4A90E2;'>🧠 Emotion Detection App</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Enter a message below to detect its emotional tone.</p>", unsafe_allow_html=True)

# 📝 Input Form
with st.form(key='emotion_form'):
    user_input = st.text_area("📝 Your Message:", height=150)
    submit_button = st.form_submit_button(label="🔍 Detect Emotion")

# 🔍 Prediction
if submit_button:
    if user_input.strip() == "":
        st.warning("Please enter some text.")
    else:
        inputs = tokenizer(user_input, return_tensors="pt", truncation=True, padding=True)
        inputs = {k: v.to(model.device) for k, v in inputs.items()}

        with torch.no_grad():
            outputs = model(**inputs)
            probs = torch.nn.functional.softmax(outputs.logits, dim=1)

        pred_id = torch.argmax(probs, dim=1).item()
        pred_label = id2label[pred_id]
        confidence = probs[0][pred_id].item()
        emotion_text_with_emoji = emotion_emojis.get(pred_label, f"❓ {pred_label.capitalize()}")

        # ✅ Display Result
        st.markdown(f"""
            <div style='background-color:#E6F4EA; padding:20px; border-radius:10px; text-align:center;'>
                <h2 style='color:#2E8B57;'>{emotion_text_with_emoji}</h2>
                <p style='font-size: 16px;'>Confidence: {confidence:.2%}</p>
            </div>
        """, unsafe_allow_html=True)

        # 📊 Bar chart of all emotion scores
        score_dict = {id2label[i]: float(probs[0][i]) for i in range(len(id2label))}
        st.markdown("### 📊 Emotion Confidence Scores")
        st.bar_chart(score_dict)

