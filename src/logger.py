import os.path
import logging
import pendulum
import datetime as dt
from datetime import datetime

class Logger:
	def __init__(self):
		self.current_time = pendulum.now().start_of('hour')
		logging.basicConfig(level=logging.INFO)
		self.logger = logging.getLogger(__name__)
		self.handler = logging.FileHandler('log/' + self.current_time.strftime('%F-%H') + '.log')
		self.handler.setLevel(logging.INFO)
		self.logger.addHandler(self.handler)

	def checkForResponse(self, request):
		'''Returns true if it has been more than 30 minutes since the request was run'''
		filename = 'var/' + request + '.json'
		if (os.path.isfile(filename)):
			t = os.path.getmtime(filename)
			mod_time = datetime.fromtimestamp(t)
			if (not(datetime.now() - mod_time > dt.timedelta(minutes=15))):
				return False
		return True


	def storeResponse(self, request, response):
		filename = 'var/' + request + '.json'
		with open(filename, 'w') as fp:
		    json.dump(response, fp)

	# Logs informational messages to the console and to a file.
	def logMessage(self, _class='Test', msg='test', level='info'):
		if (level == 'info'):
			self.logger.log(logging.INFO, _class + ': ' + msg)
		elif(level == 'error'):
			self.logger.log(logging.ERROR, _class + ': ' + msg)
		elif(level == 'warning'):
			self.logger.log(logging.WARNING, _class + ': ' + msg)

		if (pendulum.now().start_of('hour') > self.current_time):
			self.switch_file()

	# Switches files for logging so that the logfile doesn't get too bloated.
	def switchFile(self):
		self.logger.info('Switching to new log file.')
		self.logger.removeHandler(self.handler)
		del self.handler
		del self.current_time
		self.current_time = pendulum.now().start_of('hour')
		self.handler = logging.FileHandler('log/' + self.current_time.strftime('%F-%H') + '.log')
		self.logger.addHandler(self.handler)
		self.logger.info('File switching complete!')

	def main(self):
		self.logMessage()

if __name__ == '__main__':
    log = Logger()
    log.main()
