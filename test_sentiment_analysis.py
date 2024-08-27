import unittest
from SentimentAnalysis.sentiment_analysis import sentiment_analyzer

class TestEntimentAnalyzer(unittest.TestCase):
    def test_sentiment_analyzer(self):
        self.assertEqual(sentiment_analyzer('I love workin with Python').get('label'), 'SENT_POSITIVE')
        self.assertEqual(sentiment_analyzer('I hate workin with Python').get('label'), 'SENT_NEGATIVE')
        self.assertEqual(sentiment_analyzer('I am neutral on Python').get('label'), 'SENT_NEUTRAL')


unittest.main()