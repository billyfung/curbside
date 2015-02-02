import urllib
import urllib.request
import json 

#search the tree to find greatest depth secrets
#session needs to be re-done every time
def search(s, depth, session):
	# refresh session id 
	opensession = urllib.request.Request('http://challenge.shopcurbside.com/%s' % s, headers={'Session':session})
	session = urllib.request.urlopen('http://challenge.shopcurbside.com/get-session').read().decode('utf-8')
	try:
		abc = urllib.request.urlopen(opensession)
		f = abc.read()
		abc.close()
	except:
		print('error: %s' % f)
		return 
	secret = json.loads(s.decode('utf-8').lower())
	#need to parse to be all lowercase
	if 'message' in secret:
		print(secret['message'])
	if 'next' in secret:
		#check to see if list or single string
		if isinstance(secret['next'], str):
			search(secret['next'], depth+1, session)
		else: #if not a string iterate through the list
			for i in secret['next']:
				search(i, depth+1, session)	 #omg recursion 
	else:
		print(secret['secret'])

session = urllib.request.urlopen('http://challenge.shopcurbside.com/get-session').read().decode('utf-8')
search('start', 0, session)