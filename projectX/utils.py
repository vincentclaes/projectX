from datetime import datetime


def build_s3_key(user, type_):
    _now = datetime.now()
    return 'twitter/' + user + '/' + type_ + '/' + str(_now.date()) + '/' + str(_now) + '.json'
