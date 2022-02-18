import requests

#get correct url

# payload = {'page':2, 'count': 25}

# r = requests.get('https://httpbin.org/get', params=payload)
# print(r.url)

# #posting
payload = {'username':'corey', 'password':'testing'}
r = requests.post('https://httpbin.org/post', data=payload)

r_dict = r.json()
print(r_dict['form'])



