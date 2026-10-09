# Final Project Submission Guide — Emotion Detector

All local code, tests, static analysis, and screenshots are complete. Before
submitting, publish the project to a **public** GitHub repository named
`emotion-detection`. The expected links for the connected GitHub account are:

- README: `https://github.com/atharvagundu-9/emotion-detection/blob/main/README.md`
- Package initializer: `https://github.com/atharvagundu-9/emotion-detection/blob/main/EmotionDetection/__init__.py`

These URLs will work only after the repository has been created and the project
has been pushed to its `main` branch.

## Task 1 — GitHub repository URL

Submit:

```text
https://github.com/atharvagundu-9/emotion-detection/blob/main/README.md
```

## Task 2 — Create the emotion detection application

### Activity 1: application function

Submit the following from `EmotionDetection/emotion_detection.py`:

```python
def emotion_detector(text_to_analyze):
    """Return emotion scores and the dominant emotion for the supplied text.

    A request rejected by the Watson service with HTTP status 400 is represented
    by a dictionary whose values are all ``None``. The Flask layer uses that
    response to show the assignment's required blank-input error message.
    """
    payload = {"raw_document": {"text": text_to_analyze}}
    response = requests.post(
        WATSON_EMOTION_URL,
        json=payload,
        headers=WATSON_HEADERS,
        timeout=30,
    )

    if response.status_code == 400:
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None,
        }

    response.raise_for_status()
    formatted_response = json.loads(response.text)
    emotion_scores = formatted_response["emotionPredictions"][0]["emotion"]
    dominant_emotion = max(emotion_scores, key=emotion_scores.get)

    return {
        "anger": emotion_scores["anger"],
        "disgust": emotion_scores["disgust"],
        "fear": emotion_scores["fear"],
        "joy": emotion_scores["joy"],
        "sadness": emotion_scores["sadness"],
        "dominant_emotion": dominant_emotion,
    }
```

### Activity 2: import and test output

Upload or paste `evidence/2b_application_test.txt`.

## Task 3 — Format the output

### Activity 1: formatted return value

Submit the final return block from the function:

```python
return {
    "anger": emotion_scores["anger"],
    "disgust": emotion_scores["disgust"],
    "fear": emotion_scores["fear"],
    "joy": emotion_scores["joy"],
    "sadness": emotion_scores["sadness"],
    "dominant_emotion": dominant_emotion,
}
```

### Activity 2: formatted terminal output

Upload or paste `evidence/3b_formatted_output.txt`.

## Task 4 — Validate the EmotionDetection package

### Activity 1: public URL for `__init__.py`

Submit:

```text
https://github.com/atharvagundu-9/emotion-detection/blob/main/EmotionDetection/__init__.py
```

### Activity 2: package validation output

Upload or paste `evidence/4b_package_validation.txt`.

## Task 5 — Run unit tests

### Activity 1: unit-test code

Submit the contents of `test_emotion_detection.py`. It includes tests for joy,
anger, disgust, sadness, fear, and HTTP 400 invalid-input behavior.

### Activity 2: passing test output

Upload or paste `evidence/5b_unit_tests.txt`. It reports six passing tests and
ends with `OK`.

## Task 6 — Flask web deployment

### Activity 1: Flask code

Submit the contents of `server.py`:

```python
"""Flask web server for the Emotion Detection application."""

from flask import Flask, render_template, request
from EmotionDetection import emotion_detector

app = Flask(__name__)


@app.route("/")
def render_index_page():
    """Render the application's home page."""
    return render_template("index.html")


@app.route("/emotionDetector")
def detect_emotion():
    """Analyze the text supplied in the textToAnalyze query parameter."""
    text_to_analyze = request.args.get("textToAnalyze", "")
    response = emotion_detector(text_to_analyze)

    if response["dominant_emotion"] is None:
        return "Invalid text! Please try again!"

    return (
        "For the given statement, the system response is "
        f"'anger': {response['anger']}, "
        f"'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, "
        f"'joy': {response['joy']}, "
        f"'sadness': {response['sadness']}. "
        f"The dominant emotion is {response['dominant_emotion']}."
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
```

### Activity 2: deployment screenshot

Upload `6b_deployment_test.png`.

## Task 7 — Error handling

### Activity 1: status code 400

Submit this block from `emotion_detection.py`:

```python
if response.status_code == 400:
    return {
        "anger": None,
        "disgust": None,
        "fear": None,
        "joy": None,
        "sadness": None,
        "dominant_emotion": None,
    }
```

### Activity 2: blank-input handling

Submit this block from `server.py`:

```python
if response["dominant_emotion"] is None:
    return "Invalid text! Please try again!"
```

### Activity 3: error screenshot

Upload `7c_error_handling_interface.png`.

## Task 8 — Static code analysis

### Activity 1: analyzed code

Submit the contents of `server.py` from Task 6.

### Activity 2: perfect score

Upload or paste `evidence/8b_static_analysis.txt`. It reports:

```text
Your code has been rated at 10.00/10
```

## Final checklist

- Publish the supplied source as a public GitHub repository.
- Confirm both GitHub URLs above open without signing in.
- Upload the two PNG screenshots with their existing filenames.
- Use the matching text evidence for Tasks 2, 3, 4, 5, and 8.
- Submit all activities only after checking the previews.
