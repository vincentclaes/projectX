from __future__ import print_function

import boto3
import json

from projectX.twitter.scraper import get_tweets
from projectX.utils import build_s3_key


def get_tweets_for_user(user, pages, bucket = 'sonarsic-lz', function_ = 'tweets'):
    s3client = boto3.client('s3')
    ret_val = []
    for tweet in get_tweets(user, pages=pages):
        ret_val.append(tweet)
    file_object = {'statuses': ret_val}
    s3_key = build_s3_key(user, function_)
    s3client.put_object(Bucket=bucket, Key=s3_key, Body=json.dumps(file_object, default=str))


if __name__ == '__main__':
    get_tweets_for_user('binance', 1)