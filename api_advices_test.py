import requests
from loguru import logger
arquivo = []

r = requests.get('https://api.adviceslip.com/advice')
try:
    print(r)
    print(r.status_code)
    print(r.text)
    print(r.json())
    print(r.json()['slip'])
    print(r.json()['slip']['id'])
    print(r.json()['slip']['advice'])
except Exception as error:
    logger.exception(f'Error: {error}')

with open('arquivo.txt', 'w', encoding='UTF-8') as arquivo:
    arquivo.write(r.text)

