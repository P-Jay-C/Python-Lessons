import json
from urllib.request import urlopen

with urlopen("https://www.yahoo.com/?err=404&err_url=https%3a%2f%2ffinance.yahoo.com%2fwebservice%2fv1%2fsymbols%2fallcurrencies%2fquote%3fformat%3djson") as response:
    source = response.read() 

data = json.loads(source)

print(json.dumps(data,indent=2))
