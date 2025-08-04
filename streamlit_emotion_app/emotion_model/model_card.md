---
license: mit
tags:
- emotion-detection
- bert
- text-classification
- transformers
- huggingface
- crowdflower
datasets:
- crowdflower
language: en
widget:
- text: "I am feeling loved and joyful today!"
---

# 🧠 Emotion Detection Model (BERT-based)

This is a **BERT-based emotion classification model** fine-tuned on the **Crowdflower Emotion Dataset**. The model can classify English text into one of **six emotion categories**:

- 😢 sadness  
- 😀 joy  
- ❤️ love  
- 😠 anger  
- 😨 fear  
- 😲 surprise

---

## 📌 Use Cases

This model is best suited for:

- Emotion analysis in text messages
- Chatbot mood understanding
- Social media sentiment/emotion classification
- Customer feedback analysis

---

## 🧪 Model Details

| Detail               | Value                         |
|----------------------|-------------------------------|
| Base Model           | `bert-base-uncased`           |
| Model Type           | Text Classification (6 classes) |
| Framework            | 🤗 Transformers                |
| Tokenizer            | AutoTokenizer (`bert-base-uncased`) |
| Training Method      | Hugging Face Trainer API      |
| Dataset              | Crowdflower Emotion Dataset   |
| Training Epochs      | 3                             |

---

## 💬 Example

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

model_id = "sickboi25/emotion-detector"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForSequenceClassification.from_pretrained(model_id)

text = "I am so happy and full of love!"
inputs = tokenizer(text, return_tensors="pt")
outputs = model(**inputs)
predicted_class = torch.argmax(outputs.logits).item()

emotion_labels = ['sadness', 'joy', 'love', 'anger', 'fear', 'surprise']
print("Predicted Emotion:", emotion_labels[predicted_class])
📂 Dataset
Name: Crowdflower Emotion Dataset

Size: ~40,000 labeled English tweets

Labels: sadness, joy, love, anger, fear, surprise

Link: Crowdflower on Kaggle

🧠 Performance
Metric	Score
Accuracy	~90%
Loss	Low after 3 epochs
F1-Score	High on all classes

📜 License
This model is released under the MIT License.

👤 Author
Name: Ahsaan Ullah

Hugging Face Profile: @sickboi25

🔗 Model Page: https://huggingface.co/sickboi25/emotion-detector