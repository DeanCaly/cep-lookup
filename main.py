import requests
import requests.exceptions

def validate_cep():
      while True:
              cep = input('Digite o CEP desejado: ')
              cep = cep.replace('-', '').strip()                
              if len(cep) != 8 or not cep.isdigit():
                     print('Cep inválido! O cep deve ter 8 digitos e ser composto apenas por números')
              else:
                     return cep


def get_address(cep):
       url = f"https://viacep.com.br/ws/{cep}/json/"
       try:
              response = requests.get(url, timeout=5)
       except requests.exceptions.ConnectionError:
              print("Erro de conexão. Verifique sua internet e tente novamente.")
       except requests.exceptions.Timeout:
              print("Indisponível no momento! Tente conectar novamente em alguns minutos")
              
       data = response.json()
       
       if "erro" in data:
              print("cep não encontrado")
              return None
       return data
       
       
cep = validate_cep()

data = get_address(cep)


info = f"Cep: {data['cep']}\n"\
       f"Logradouro: {data['logradouro']}\n"\
       f"Bairro: {data['bairro']}\n"\
       f"Local: {data['localidade']}\n"\
       f"Estado: {data['uf']}"


print(info)
