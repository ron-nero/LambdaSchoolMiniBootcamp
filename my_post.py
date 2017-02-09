import requests
 
url = 'https://LambdaSchool.com/contact'
comment = {
 	'email' : 'ronstoppable107@gmail.com',
    'lastname' : 'N',
    'message': 'Hi, this is the Purge.',
    'firstname': 'Ron'
}

r = requests.post(url, json = comment)

print (r.status_code)