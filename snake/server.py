import os

import cherrypy
from snake import Snake

class Battlesnake(object):
	def __init__(self):
		self.snake = Snake()

	@cherrypy.expose
	@cherrypy.tools.json_out()
	def index(self):
		return {
			'apiversion': '1',
			'author': 'owenj',
			'color': '#906df9',
			'head': 'default',
			'tail': 'default'
		}

	@cherrypy.expose
	@cherrypy.tools.json_in()
	def start(self):
		data = cherrypy.request.json
		self.snake.start(data)

		print('START')
		return 'ok'

	@cherrypy.expose
	@cherrypy.tools.json_in()
	@cherrypy.tools.json_out()
	def move(self):
		data = cherrypy.request.json
		move = self.snake.move(data)

		print('MOVE:', move)
		return {'move': move}

	@cherrypy.expose
	@cherrypy.tools.json_in()
	def end(self):
		data = cherrypy.request.json
		self.snake.end(data)

		print('END')
		return 'ok'

if __name__ == '__main__':
	server = Battlesnake()
	cherrypy.config.update({'server.socket_host': '0.0.0.0'})
	cherrypy.config.update(
		{'server.socket_port': int(os.environ.get('PORT', '8080')),}
	)
	print('Starting Battlesnake Server...')
	cherrypy.quickstart(server)
