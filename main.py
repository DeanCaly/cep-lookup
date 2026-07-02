import requests

def validate_cep():
      while True:
              cep = input('Digite o CEP desejado: ')
              cep = cep.replace('-', '').strip()                
              if len(cep) != 8 or not cep.isdigit():
                     print('Cep inválido! O cep deve ter 8 digitos e ser composto apenas por números')
              else:
                     return cep


cep = validate_cep()
url = f"https://viacep.com.br/ws/{cep}/json/"
response = requests.get(url)
data = response.json()

info = f"Cep: {data['cep']}\n"\
       f"Logradouro: {data['logradouro']}\n"\
       f"Bairro: {data['bairro']}\n"\
       f"Local: {data['localidade']}\n"\
       f"Estado: {data['uf']}"


print(info)