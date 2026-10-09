# Emotion Detection Application

This final project is an AI-powered web application that detects the emotions
expressed in English text. It calls the Watson NLP EmotionPredict service,
returns scores for anger, disgust, fear, joy, and sadness, and identifies the
dominant emotion.

## Project structure

```text
EmotionDetection/
    __init__.py
    emotion_detection.py
static/
    mywebscript.js
    style.css
templates/
    index.html
server.py
test_emotion_detection.py
```

## Run locally

```bash
python -m pip install -r requirements.txt
python server.py
```

Open `http://localhost:5000` in a browser.

## Test and analyze

```bash
python -m unittest test_emotion_detection.py -v
pylint server.py
```

