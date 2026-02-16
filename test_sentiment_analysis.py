from SentimentAnalysis.sentiment_analysis import sentiment_analyzer
import unittest

class TestSentimentAnalyzer(unittest.TestCase):
    def test_sentiment_analyzer(self):
        # Test for a positive response
        response1 = sentiment_analyzer("I love working with Python")
        self.assertEqual(response1['label'], 'SENT_POSITIVE')

        # Test for negative response
        response2 = sentiment_analyzer("I hate working with Python")
        self.assertEqual(response2['label'], 'SENT_NEGATIVE')

        # Test for neutral response
        response3 = sentiment_analyzer("I am neutral on working with Python")
        self.assertEqual(response3['label'], 'SENT_NEUTRAL')

unittest.main()