from unittest import result
import requests

base_url ="https://rickandmortyapi.com/api/"

lista_personajes = []
lista_especies = []
  

for i in range(1,827):
    c = f"https://rickandmortyapi.com/api/character/{i}"
    r = requests.get(c)
    ans = r.json()
    specie = ans["species"] 
    if specie not in lista_especies:
        lista_especies.append(specie)

print(len(lista_especies))