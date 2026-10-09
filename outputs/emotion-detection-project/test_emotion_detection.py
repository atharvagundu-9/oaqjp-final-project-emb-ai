"""Unit tests for the Watson NLP emotion detector."""

import unittest
from unittest.mock import Mock, patch

from EmotionDetection import emotion_detector


class TestEmotionDetector(unittest.TestCase):
    """Verify the dominant emotion returned for representative statements."""

    @staticmethod
    def _watson_response(**scores):
        response = Mock(status_code=200)
        response.text = '{"emotionPredictions": [{"emotion": ' + str(
            scores
        ).replace("'", '"') + "}]}"
        response.raise_for_status = Mock()
        return response

    @patch("EmotionDetection.emotion_detection.requests.post")
    def test_joy(self, mock_post):
        """A happy statement is dominated by joy."""
        mock_post.return_value = self._watson_response(
            anger=0.01, disgust=0.01, fear=0.01, joy=0.95, sadness=0.02
        )
        result = emotion_detector("I am glad this happened")
        self.assertEqual(result["dominant_emotion"], "joy")

    @patch("EmotionDetection.emotion_detection.requests.post")
    def test_anger(self, mock_post):
        """An angry statement is dominated by anger."""
        mock_post.return_value = self._watson_response(
            anger=0.92, disgust=0.03, fear=0.02, joy=0.01, sadness=0.02
        )
        result = emotion_detector("I am really mad about this")
        self.assertEqual(result["dominant_emotion"], "anger")

    @patch("EmotionDetection.emotion_detection.requests.post")
    def test_disgust(self, mock_post):
        """A disgusted statement is dominated by disgust."""
        mock_post.return_value = self._watson_response(
            anger=0.04, disgust=0.89, fear=0.03, joy=0.01, sadness=0.03
        )
        result = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(result["dominant_emotion"], "disgust")

    @patch("EmotionDetection.emotion_detection.requests.post")
    def test_sadness(self, mock_post):
        """A sad statement is dominated by sadness."""
        mock_post.return_value = self._watson_response(
            anger=0.01, disgust=0.01, fear=0.02, joy=0.01, sadness=0.95
        )
        result = emotion_detector("I am so sad about this")
        self.assertEqual(result["dominant_emotion"], "sadness")

    @patch("EmotionDetection.emotion_detection.requests.post")
    def test_fear(self, mock_post):
        """A fearful statement is dominated by fear."""
        mock_post.return_value = self._watson_response(
            anger=0.01, disgust=0.01, fear=0.94, joy=0.01, sadness=0.03
        )
        result = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(result["dominant_emotion"], "fear")

    @patch("EmotionDetection.emotion_detection.requests.post")
    def test_invalid_text(self, mock_post):
        """A service status of 400 produces the required empty result."""
        mock_post.return_value = Mock(status_code=400)
        result = emotion_detector("")
        self.assertIsNone(result["dominant_emotion"])


if __name__ == "__main__":
    unittest.main()

