import os
import discord
import logging
log = logging.getLogger(__name__)

class DiscordBot(discord.Client):
	def __init__(self, token, commands, command_prefix="!"):
		super().__init__()
		self.token = token
		self.command_prefix = command_prefix
		self.commands = commands or []


	async def on_message(self, message):
		log.info('Recieved message from discord')
		if not message.content.startswith(self.command_prefix) or message.content == self.command_prefix:
			log.info('Message recieved did not match with command_prefix="{0}"'.format(self.command_prefix))
			return

		cmd_msg = message.content.split()
		cmd_name = cmd_msg.pop(0)
		cmd_args = cmd_msg

		log.info('command="{0}", args={1}'.format(cmd_name, cmd_args))

		for command in self.commands:
			if cmd_name == self.command_prefix + command.name:
				log.info('Message matched command="{0}"'.format(command.name))
				await command.run(cmd_args, self, message)

	def run(self):
		log.info('starting commands')
		for command in self.commands:
			if hasattr(command, 'start'):
				command.start()

		log.info('starting main loop')
		super().run(self.token)

		log.info('ending commands')
		for command in self.commands:
			if hasattr(command, 'end'):
				command.end()

class DiscordBotCommand:
	def __init__(self, name='DiscordBotCommand'):
		self.name = name

	def start(self):
		pass

	async def run(self, bot, message):
		pass

	def stop(self):
		pass

	def match(self, message):
		pass