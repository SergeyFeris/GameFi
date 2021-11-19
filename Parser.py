import requests
import json


print('Выберите сервис 1 - Redkite, 2 - GameFi')
servise = int(input())
print('Введите номер дропа')
drop = str(input())


with open('adresses.txt','r', encoding="UTF-8" ) as readFile:
    bep20 = readFile.readlines()
if servise == 1:
    link = 'https://redkite-api.polkafoundry.com/user/winner-search/'
if servise == 2:
    link = 'https://hub.gamefi.org/api/v1/user/winner-search/'

for adress in bep20:
    try:
        response = requests.get(link+drop+'?page=1&limit=10&search='+adress)
        info = json.loads(response.text)
        if info['data']['total'] == '1':
            print(adress)
        else:
            print('не попал')
    except json.decoder.JSONDecodeError:
        print(response.text)
        print(response) 