import tweepy

def get_api(cfg):
	auth = tweepy.OAuthHandler(cfg['CONSUMER_KEY'], cfg['CONSUMER_SECRET'])
	auth.set_access_token(cfg['OAUTH_TOKEN'], cfg['OAUTH_TOKEN_SECRET'])
	return tweepy.API(auth)

def main():

	cfg = {
		"CONSUMER_KEY": "IUVGYfSZtIns5ZxF0RLiIsNbZ",
		"CONSUMER_SECRET": "XHdwHAFGAmnP3XfYDrIilrOu92rQbBhbs5psS2goW8Ewed2nxI",
		"OAUTH_TOKEN": "462977723-bJaDN93XW9XVPzNbTQjOjNwEnlZPcJhWYTX20SKr",
		"OAUTH_TOKEN_SECRET": "XGVISj0TvUWFnYnmZQfW9zFJj3ADyGZkKDB95b4H0pPbI"
	}

	api = get_api(cfg)
	tweet = "TESTTEST Hello, world!"
	status = api.update_status(status=tweet)

if __name__ == "__main__":
	main()