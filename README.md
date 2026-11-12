🎬 Advanced Movie Genre Classification & Story Generator

An AI-powered web application that analyzes movie scripts, predicts their genres using Machine Learning, generates creative stories, and improves existing stories using Cohere AI.

📌 Project Overview

The Advanced Movie Genre Classification & Story Generator combines Natural Language Processing (NLP), Machine Learning, and Generative AI to help users analyze movie scripts and create engaging stories.

The application uses a trained Multinomial Naive Bayes classifier with text vectorization to predict movie genres and Cohere AI for story generation and improvement.

✨ Features
1. Movie Genre Prediction
Accepts movie scripts as text input.
Preprocesses text using NLTK.
Removes stopwords and applies stemming.
Converts text into numerical features using TF-IDF or the saved vectorizer.
Predicts the movie genre using a trained Machine Learning model.
Displays genre prediction probabilities.
2. AI Story Generator
Generates creative stories using Cohere AI.
Supports multiple genres:
Action
Adventure
Comedy
Drama
Horror
Romance
Sci-Fi
Thriller
Other
Allows users to select story tone and complexity.
Generates complete stories based on user-provided concepts.
3. Story Improvement
Improves existing stories using Cohere AI.
Supports different improvement areas:
Character Development
Plot Complexity
Dialogue Quality
Narrative Flow
Emotional Depth
Thematic Consistency
🛠️ Technologies Used
Technology	Purpose
Python	Backend development
Gradio	Web application interface
Scikit-learn	Machine Learning classification
NLTK	Natural Language Processing
NumPy	Numerical operations
Pandas	Data processing
Joblib	Model loading
Cohere AI	Story generation and improvement
TF-IDF / Vectorizer	Text feature extraction
📂 Project Structure
text
movie-genre-classification/
│
├── app.py
├── README.md
├── requirements.txt
├── .env
├── .gitignore
│
├── labtherory/
│   ├── movie_genre_classifier.joblib
│   ├── tfidf_vectorizer.pkl
│   ├── kaggle_movie_train.csv
│   ├── kaggle_movie_test.csv
│   ├── test_predictions.csv
│   └── project.ipynb
│
└── venv/


Note: The venv/ and .env folders/files should not be uploaded to GitHub. The trained model must be available for genre prediction.

⚙️ Installation and Setup
Step 1: Clone the Repository
bash
git clone https://github.com/USERNAME/movie-genre-classification.git


Navigate into the project:

bash
cd movie-genre-classification

Step 2: Create a Virtual Environment
bash
python -m venv venv


Activate on Windows PowerShell:

powershell
.\venv\Scripts\Activate.ps1

Step 3: Install Dependencies
bash
pip install -r requirements.txt

Step 4: Configure Cohere API

Create a .env file in the project root directory.

Add your Cohere API key:

env
COHERE_API_KEY=your_cohere_api_key


Obtain your API key from:

https://dashboard.cohere.com/api-keys

Never share or upload your API key publicly.

Step 5: Run the Application
bash
python app.py


Open the following URL in your browser:

text
http://127.0.0.1:7860

🧠 Machine Learning Workflow

The genre prediction system follows these steps:

Collect movie script datasets.
Clean and preprocess text.
Remove unnecessary characters and stopwords.
Apply Porter Stemming.
Convert text into numerical features.
Train the Multinomial Naive Bayes classifier.
Save the trained model using Joblib.
Load the trained model into the Gradio application.
Predict the genre of new movie scripts.
🔐 Environment Variables

The application uses environment variables to protect sensitive credentials.

Example .env:

env
COHERE_API_KEY=your_api_key


Make sure .env is included in .gitignore.

🧪 Testing

Test the application using these steps:

Launch the Gradio application.
Enter a movie script in the Genre Prediction tab.
Click Predict Genre.
Check the predicted genre and probabilities.
Enter a story concept in the Story Generator tab.
Select a genre, tone, and complexity.
Generate a story.
Submit an existing story for improvement.
🚀 Future Enhancements
Improve genre classification accuracy.
Support additional movie genres.
Add multilingual script analysis.
Improve story generation quality.
Add downloadable generated stories.
Deploy the application online.
Enhance the user interface and experience.
👨‍💻 Author

Developed as a Machine Learning and Natural Language Processing project.

📜 License

This project is intended for educational and research purposes. Add an appropriate open-source license if you intend to distribute it publicly.