
# imports
from datetime import datetime
import requests
from json import loads

class MODULE(object):
	def __init__(self, handler):

		# Handler is the passed in engine object
		self.handler = handler

		# Name of Module
		self.name = 'ExampleModule'

		# Type is only for organizational purposes, not needed
		self.type = 'Example'

		# Module HTML API methods
		self.methods = ['POST']

		# Module Description
		self.description = 'This is an example module'

		# Add module inputs
		self.all_kwargs = [
			{
				"name" : "ids",
				"type" : "list",
				"desc" : "list of incoming invoice ticket"
			},
			{
				"name" : "clean",
				"type" : "bool",
				"desc" : "Deletes all dot information notes on ticket"
			},
			{
				"name" : "fedex",
				"type" : "bool",
				"desc" : "Adds Fedex status to dot information note"
			},
			{
				"name" : "note",
				"type" : "bool",
				"desc" : "Adds dot note to ticket"
			}
		]


	def run(self, unique_id=None, **kwargs):

		#Modify Thread 
		self.handler.modify_thread(unique_id, 'health', 'Healthy')

		# Add a log with the required fields
		self.handler.add_log({'data' : f'Updated {count} tickets', 'module' : self.name, 'status' : 1, 'errors' : [], 'date' : datetime.now()})

		# Execute whatever you want here
		print('Do some cool stuff!')

		# Return this object
		return {"status" : "success", "data" : ""} 
