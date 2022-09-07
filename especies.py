from unittest import result
import requests

base_url ="https://rickandmortyapi.com/api/"


lista_nombre_episodios = []
cont = 40
while(True):
    c = f"https://rickandmortyapi.com/api/episode/{cont}"
    r = requests.get(c)
    ans = r.json()
    if r.status_code == 404:
        break
    lista_nombre_episodios.append(ans["name"])

    cont+=1


print(lista_nombre_episodios)