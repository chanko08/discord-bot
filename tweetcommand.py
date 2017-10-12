import logging
import sys
import discordbot
import tweepy

log = logging.getLogger(__name__)

class TweetCommand(discordbot.DiscordBotCommand):
	def __init__(self,
		consumer_key,
		consumer_secret,
		access_token,
		access_secret,
		name = 'tweets',
		max_tweets_to_retrieve = 5
	):
		super().__init__(name)
		self.consumer_key = consumer_key
		self.consumer_secret = consumer_secret
		self.access_token = access_token
		self.access_secret = access_secret
		self.max_tweets_to_retrieve = max_tweets_to_retrieve

	def start(self):
		twitter_auth = tweepy.OAuthHandler(
			self.consumer_key,
			self.consumer_secret
		)

		twitter_auth.set_access_token(
			self.access_token,
			self.access_secret
		)

		self.twitter = tweepy.API(twitter_auth)
		log.info('Finished authenticating with Twitter')

	async def run(self, args, bot, message):
		if len(args) != 1:
			return

		screen_name = args[0]


		tweets = self.twitter.user_timeline(
			screen_name = screen_name,
			count = self.max_tweets_to_retrieve,
			include_rts = True
		)

		log.info('Retrieved tweets from screen_name="{0}'.format(screen_name))

		resp = '\n'.join([tweet.text for tweet in tweets])
		await bot.send_message(message.channel, resp)