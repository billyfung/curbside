import urllib
import urllib.request
import json 

#search the tree to find greatest depth secrets
#session needs to be re-done every time
def search(start, depth, session):
	opensession = urllib.request.Request('http://challenge.shopcurbside.com/%s' % start, headers={'Session':session})
	try:
		abc = urllib.request.urlopen(opensession)
		a = abc.read()
		abc.close()
		session = urllib.request.urlopen('http://challenge.shopcurbside.com/get-session').read().decode('utf-8')
	except:
		print('Error: depth %d %s' %(depth,a))
		return
	secret = json.loads(a.decode('utf-8'))
	if 'message' in secret:
		print(secret['message'])
	if 'next' in secret:
		for i in secret['next']:
			search(i, depth+1, session)
	else:
		print(secret)

session = urllib.request.urlopen('http://challenge.shopcurbside.com/get-session').read().decode('utf-8')
search('start', 0, session)