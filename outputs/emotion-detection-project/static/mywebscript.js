function runEmotionAnalysis() {
  const textToAnalyze = document.getElementById("textToAnalyze").value;
  const responseElement = document.getElementById("system_response");
  const button = document.getElementById("analyzeButton");

  responseElement.textContent = "Analyzing…";
  button.disabled = true;

  fetch(`/emotionDetector?textToAnalyze=${encodeURIComponent(textToAnalyze)}`)
    .then((response) => response.text())
    .then((text) => {
      responseElement.textContent = text;
    })
    .catch(() => {
      responseElement.textContent = "The service could not be reached. Please try again.";
    })
    .finally(() => {
      button.disabled = false;
    });
}

