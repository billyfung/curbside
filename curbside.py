import urllib
import urllib.request
import json 

#search the tree to find greatest depth secrets
#session needs to be re-done every time
def search(s, depth, session):
	opensession = urllib.request.Request('http://challenge.shopcurbside.com/%s' % s, headers={'Session':session})
	try:
		abc = urllib.request.urlopen(opensession)
		s = abc.read()
		abc.close()
	except:
		print('Error: depth %d %s' %(depth,s))
		return
	secret = json.loads(s.decode('utf-8'))
	if 'message' in secret:
		print(secret['message'])
	if 'next' in secret:
		for i in secret['next']:
			session = sessionrefresh()
			search(i, depth+1, session)
	else:
		print(secret)

def sessionrefresh():
	session = urllib.request.urlopen('http://challenge.shopcurbside.com/get-session').read().decode('utf-8')
	return session

session = urllib.request.urlopen('http://challenge.shopcurbside.com/get-session').read().decode('utf-8')
search('start', 0, session)