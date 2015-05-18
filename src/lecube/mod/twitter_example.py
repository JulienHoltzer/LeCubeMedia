# -*- coding: utf-8 -*-

import tweepy


def get_api(cfg):
	auth = tweepy.OAuthHandler(cfg['CONSUMER_KEY'], cfg['CONSUMER_SECRET'])
	auth.set_access_token(cfg['OAUTH_TOKEN'], cfg['OAUTH_TOKEN_SECRET'])
	return tweepy.API(auth)

def main():

	cfg = {
		"CONSUMER_KEY": "value",
		"CONSUMER_SECRET": "valuee",
		"OAUTH_TOKEN": "valueee",
		"OAUTH_TOKEN_SECRET": "valueeee"
	}

	api = get_api(cfg)
	tweet = "TEST TEST Hello, world!"
	status = api.update_status(status=tweet)

if __name__ == "__main__":
	main()

