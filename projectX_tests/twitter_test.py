import unittest   # The test framework
import os
from projectX.twitter import twitter_get_tweets

class TwitterGetTweets(unittest.TestCase):
    def test_get_tweet(self):
        response = twitter_get_tweets.get_tweets_for_user('binance', 1)
        self.assertEqual(4, 4)

if __name__ == '__main__':
    unittest.main()