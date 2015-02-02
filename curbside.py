import urllib
import urllib.request
import json 

#search the tree to find greatest depth secrets
#refresh session token, timed out after 10 requests, 404 error 
#could have used requests library as well
def search(s, depth):
	# refresh session id
	#message = '' 
	session = urllib.request.urlopen('http://challenge.shopcurbside.com/get-session').read().decode('utf-8')
	opensession = urllib.request.Request('http://challenge.shopcurbside.com/%s' % s, headers={'Session':session})	
	try:
		a = urllib.request.urlopen(opensession)
		b = a.read()
		a.close()
	except: #error checking since it was failing, discovered the next: isn't always a list of strings 
		print('error: %s' % b)
		return 
	secret = json.loads(b.decode('utf-8').lower())
	#normalize to all lowercase, incase of stuff like neXT NeXT...
	#iterate through the keys in 'next:'
	if 'next' in secret:
		#check to see if next key is list or single string
		if isinstance(secret['next'], str):
			search(secret['next'], depth+1)
		else: #if not a string iterate through the list
			for i in secret['next']:
				search(i, depth+1)	 #omg recursion 
	else:
		#message = message + secret['secret']
		print(secret['secret'])
		#return message

#probably better to pop each secret into a string and then print string at the end
#this method isn't very fast, O(n)?... wonder if there is a faster way
search('start', 0)