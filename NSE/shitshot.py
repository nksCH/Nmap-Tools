from selenium import webdriver
from optparse import OptionParser



if __name__=="__main__":
	parser = OptionParser()	
	parser.add_option("-f", "--file", dest="filename",
                  help="save screenshot to filename", metavar="FILE")
	parser.add_option("-p", "--prefix",
                  dest="prefix",
                  help="prefix, either HTTP or HTTPS")
	parser.add_option("-t", "--host",
                  dest="host_ip",
                  help="ip or hostname of the target")
	parser.add_option("-l", "--port",
                  dest="port",
                  help="port of the app")
	options, remainder = parser.parse_args()


	phantomjs = webdriver.PhantomJS(service_args=['--ignore-ssl-errors=true'])
	browser = phantomjs
	url =  ""+str(options.prefix)+"://"+str(options.host_ip)+":"+str(options.port)+""
	print url
	browser.get(url)
	browser.save_screenshot(options.filename)
	browser.quit()
