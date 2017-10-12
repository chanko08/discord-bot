import os
import sys
import logging

import argparse
import functools

import discordbot
import tweetcommand

class EnvDefault(argparse._StoreAction):
    def __init__(self, env_var=None, required=False, default=None, **kwargs):

        #override default value if the environment variable exists
        real_default = default
        env_val = os.environ.get(env_var, None)

        #to use the env_val we need to unset required to pass it through
        if required and env_val:
            required = False

        default = env_val if env_val else real_default

        super(EnvDefault, self).__init__(default=default, required=required, 
                                     **kwargs)

    def __call__(self, parser, namespace, values, option_string=None):
        setattr(namespace, self.dest, values)

def main():
    program_args = argparse.ArgumentParser(description='Way of the White Arrow Discord bot')
    program_args.add_argument(
       '--log-level',
       default='INFO',
       help='Log level to output to the log file. Defaults to "INFO"',
       env_var='LOG_LEVEL',
       action=EnvDefault
    )
    program_args.add_argument(
       '--log-output',
       type=argparse.FileType('r'),
       default=sys.stdout,  
       help='Log file to output logs to. Defaults to "STDOUT"',
       env_var='LOG_OUTPUT',
       action=EnvDefault
    )
    program_args.add_argument(
       '--command-prefix',
       default='!',
       help='Prefix to use to specify Discord bot commands. Defaults to "!"',
       env_var='COMMAND_PREFIX',
       action=EnvDefault
    )

    required_args = program_args.add_argument_group('Required Arguments')
    required_args.add_argument(
        '--discord-token',
        required=True,
        help='Discord token to use for the bot.',
        env_var='DISCORD_TOKEN',
        action=EnvDefault
    )
    required_args.add_argument(
        '--twitter-consumer-key',
        required=True,
        help='Twitter Consumer Key to use for Twitter-based commands',
        env_var='TWITTER_CONSUMER_KEY',
        action=EnvDefault
    )
    required_args.add_argument(
        '--twitter-consumer-secret',
        required=True,
        help='Twitter Consumer Secret to use for Twitter-based commands',
        env_var='TWITTER_CONSUMER_SECRET',
        action=EnvDefault
    )
    required_args.add_argument(
        '--twitter-access-token',
        required=True,
        help='Twitter Access Token to use for Twitter-based commands',
        env_var='TWITTER_ACCESS_TOKEN',
        action=EnvDefault
    )
    required_args.add_argument(
        '--twitter-access-secret',
        required=True,
        help='Twitter Access Secret to use for Twitter-based commands',
        env_var='TWITTER_ACCESS_SECRET',
        action=EnvDefault
    )

    args = program_args.parse_args()
    print(args)

    
    log = logging.getLogger(__name__)
    log.setLevel(args.log_level)
    ch = logging.StreamHandler()
    ch.setLevel(args.log_level)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    log.addHandler(ch)

    bot = discordbot.DiscordBot(
        token=args.discord_token,
        commands=[
            tweetcommand.TweetCommand(
                consumer_key = args.twitter_consumer_key,
                consumer_secret = args.twitter_consumer_secret,
                access_token = args.twitter_access_token,
                access_secret = args.twitter_access_secret
            )
        ]
    )


    bot.run()
    

if __name__ == '__main__':
    main()