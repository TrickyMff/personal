import discord
from random import *
import requests
from datetime import datetime


TOKEN = "MTM1NjkzMzI2NzU0MTk4NzM4OA.GGEJue.Jj3ESlaNErObFNiNH-5m0G7KqhvaMmOGsy02PE"
trigger_url = [
	"https://trigger.macrodroid.com/e0bf695c-2467-4c8d-a059-513d6870edd5/{trigger_that_fired}",
	"http://192.168.0.192:8080/{webhook_caller_ip}"
]

intents = discord.Intents.default()
client = discord.Client(intents=intents)

phrases = [
	'щас встану, подожди',
	'сейчас все будет :thumbsup:',
	'вибрация уже работает, ждёмссс',
	'все, сейчас встаю уже',
	'подожди моя, я встаю',
	'секунду...',
	'умница, сейчас буду',
	'если не встал, то еще напиши, больше вибраций будет'
]

last_index = 0

def currentTime():
	return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

@client.event
async def on_ready():
	print(f"{currentTime()} Successfully logged in as: {client.user}.")

@client.event
async def on_message(message):
	sender_id = message.author.id
	client_id = client.user.id
	channel = message.channel
	dm = discord.ChannelType.private
	
	if sender_id != client_id and channel.type == dm:
		response1 = requests.get(trigger_url[0]).status_code
		if response1 != 200:
			response2 = requests.get(trigger_url[1])
	
		print(f'{currentTime()} MESSAGE: {message.content}		RESPONSE: {response1}|{"—" if response1 == 200 else {response2}}')
		
		index = randrange( len(phrases) )
		global last_index
		while index == last_index: index = randrange( len(phrases) )
		
		last_index = index
		await channel.send( phrases[index] )
		
client.run(TOKEN)
