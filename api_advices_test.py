import requests

r = requests.get('https://api.adviceslip.com/advice')

print(r)
print(r.status_code)
print(r.text)
print(r.json())
print(r.json()['slip'])
print(r.json()['slip']['id'])
print(r.json()['slip']['advice'])
