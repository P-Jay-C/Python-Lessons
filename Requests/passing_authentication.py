import requests

r = requests.get('https://httpbin.org/basic-auth/P.Jay/Password', auth = ('P.Jay', 'Password'))

print(r.text)
