
import gradio as gr
import joblib
import re
import nltk
import os

from dotenv import load_dotenv
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

load_dotenv()

# Load trained model
MODEL_PATH = "labtherory/movie_genre_classifier.joblib"

saved_data = joblib.load(MODEL_PATH)

classifier = saved_data["classifier"]
vectorizer = saved_data["vectorizer"]
genre_mapper = saved_data["genre_mapper"]

reverse_mapper = {v: k for k, v in genre_mapper.items()}

# Initialize preprocessing
nltk.download("stopwords", quiet=True)

ps = PorterStemmer()
stop_words = set(stopwords.words("english"))


def preprocess_text(text):
    text = re.sub(r"[^a-zA-Z]", " ", text)
    text = text.lower()
    words = text.split()
    words = [word for word in words if word not in stop_words]
    words = [ps.stem(word) for word in words]
    return " ".join(words)


def predict_genre(script):
    if not script or not script.strip():
        return "Please enter a movie script.", ""

    processed = preprocess_text(script)
    features = vectorizer.transform([processed])

    prediction = classifier.predict(features)[0]
    genre = reverse_mapper[prediction]

    probabilities = ""
    if hasattr(classifier, "predict_proba"):
        probs = classifier.predict_proba(features)[0]
        classes = classifier.classes_

        probabilities = "\n".join(
            f"{reverse_mapper[c]}: {p * 100:.2f}%"
            for c, p in sorted(
                zip(classes, probs),
                key=lambda x: x[1],
                reverse=True
            )
        )

    return genre, probabilities


with gr.Blocks(title="Movie Genre Classifier") as demo:

    gr.Markdown("# 🎬 Movie Genre Classification")

    gr.Markdown(
        "Enter your movie script below to predict its genre."
    )

    script_input = gr.Textbox(
        lines=10,
        label="Movie Script",
        placeholder="Enter your movie script..."
    )

    predict_button = gr.Button("Predict Genre")

    genre_output = gr.Textbox(label="Predicted Genre")
    probability_output = gr.Textbox(label="Genre Probabilities")

    predict_button.click(
        predict_genre,
        inputs=script_input,
        outputs=[genre_output, probability_output]
    )


if __name__ == "__main__":
    demo.launch(share=False)
            