#!/usr/bin/python
""" 1) Go to dev.twitter.com creaate an application and genenrate tokens
    2) Setup your tokens below
"""

from twitter import Twitter, OAuth


TOKEN = ''
TOKEN_KEY = ''
CON_SECRET = ''
CON_SECRET_KEY = ''

t = Twitter(auth=OAuth(TOKEN, TOKEN_KEY, CON_SECRET, CON_SECRET_KEY))


def mute(screen_name):
    """ Mute a user friend """
    t.mute.users.create(screen_name=screen_name)


def get_tweets(screen_name):
    tweet_ids = []
    tweets = t.statuses.user_timeline(screen_name=screen_name, count=200)
    for tweet in tweets:
        tweet_ids.append(tweet['id'])
    
    return tweet_ids


def get_friends(screen_name):
    """ Get all friends belonging to a user """
    all_friends = []
    next_cursor = None
    while True:
        kwargs = {"screename": screen_name}
        if next_cursor:
            kwargs.update({"cursor": next_cursor})

        friends = t.friends.list(**kwargs)
        all_friends.extend(friends['users'])
        if friends['next_cursor'] > 0:
            next_cursor = friends['next_cursor']
        else:
            return all_friends


def delete_tweets(tweet_ids):
    if len(tweet_ids) > 0:
        for id in tweet_ids:
            try:
                t.statuses.destroy(id=id)
            except:
                pass

        return True
    else:
        return False
