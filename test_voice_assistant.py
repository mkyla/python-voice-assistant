import unittest
from unittest.mock import patch, MagicMock
import voice_assistant

class TestVoiceAssistant(unittest.TestCase):

    @patch('voice_assistant.pyttsx3.init')
    def test_speak(self, mock_init):
        mock_engine = MagicMock()
        mock_init.return_value = mock_engine
        voice_assistant.speak("Hello")
        mock_engine.say.assert_called_with("Hello")
        mock_engine.runAndWait.assert_called_once()

    @patch('voice_assistant.sr.Recognizer')
    @patch('voice_assistant.sr.Microphone')
    def test_listen_success(self, mock_microphone, mock_recognizer_class):
        mock_recognizer = MagicMock()
        mock_recognizer_class.return_value = mock_recognizer
        mock_recognizer.recognize_google.return_value = "Hello world"
        result = voice_assistant.listen()
        self.assertEqual(result, "hello world")

    @patch('voice_assistant.requests.get')
    def test_get_weather(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.text = "Sunny +20°C"
        mock_get.return_value = mock_response
        result = voice_assistant.get_weather("London")
        self.assertEqual(result, "Sunny +20°C")

    def test_get_time(self):
        result = voice_assistant.get_time()
        # Just check it's a string in HH:MM format
        self.assertRegex(result, r'\d{2}:\d{2}')

if __name__ == '__main__':
    unittest.main()