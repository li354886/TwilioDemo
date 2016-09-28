import requests
from authy.api import AuthyApiClient
authy_api = AuthyApiClient('DN6yaD6GAN84LRMm1CJPtQshbzhIbAhv')

# r = requests.post('https://api.authy.com/protected/json/users/new?api_key=f45ec9af9dcb7419dc52b05889c858e9')
user = authy_api.users.create('new_user@email.com', '405-342-5699', 1)

if user.ok():
    print 'OK'
else:
    print user.errors()