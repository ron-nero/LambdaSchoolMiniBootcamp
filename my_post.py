import requests
 
url = 'http://lambdaschool.com/contact-form'
comment = {
 	'name' : 'Ron',
    'lastname' : 'N',
    'message': 'Hi, this is the Purge.',
    'email': 'ronstoppable107@gmail.com'
}

r = requests.post(url, json = comment)

print (r.status_code)
