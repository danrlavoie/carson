import os.path
import datetime as dt
from datetime import datetime
def checkForResponse(request):
	'''Returns true if it has been more than 30 minutes since the request was run'''
	filename = 'var\\' + request + '.json'
	if (os.path.isfile(filename)):
		t = os.path.getmtime(filename)
		mod_time = datetime.fromtimestamp(t)
		if (not(datetime.now() - mod_time > dt.timedelta(minutes=15))):
			return False
	return True
def storeResponse(request, response):
	filename = 'var\\' + request + '.json'
	with open(filename, 'w') as fp:
	    json.dump(response, fp)

