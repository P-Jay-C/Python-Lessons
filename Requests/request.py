import requests

# r = requests.get('https://xkcd.com/353/')

r = requests.get('https://imgs.xkcd.com/comics/python.png')

print(r.headers)

# with open('comic.png', 'wb') as f:
#     f.write(r.content)


