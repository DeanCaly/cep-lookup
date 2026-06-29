import requests


cep = input('Digite o CEP desejado: ')
url = f"https://viacep.com.br/ws/{cep}/json/"


response = requests.get(url)
data = response.json()

info = f"Cep: {data['cep']}\n"\
       f"Logradouro: {data['logradouro']}\n"\
       f"Bairro: {data['bairro']}\n"\
       f"Local: {data['localidade']}\n"\
       f"Estado: {data['uf']}"

print(info)