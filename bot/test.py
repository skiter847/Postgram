import requests

r = requests.post('http://127.0.0.1:8000/cbbf15d8-0421-4512-84d9-5e5d977e3aef/channel/exists/',
                  data={'channel': 'https://t.me/breakingmash'})


print(r.content.decode('utf-8'))
