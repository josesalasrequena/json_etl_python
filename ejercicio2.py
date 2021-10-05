# JSON ETL [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

import json
import requests

import matplotlib.pyplot as plt

def titulos_completados(url):
    dic_usuarios = {}
    response = requests.get(url)
    data = response.json()
     
    for dicc in data:
        
        user = str(dicc.get("userId"))
        if f"User{user}" not in dic_usuarios.keys():
           dic_usuarios[f"User{user}"] = {}
           dic_usuarios[f"User{user}"]["cant_titulos"] = 0
           dic_usuarios[f"User{user}"]["titulos"] = []
        if dicc.get("completed") == True:
           dic_usuarios[f"User{user}"]["cant_titulos"] += 1
           dic_usuarios[f"User{user}"]["titulos"].append(dicc.get("title")) 
    return dic_usuarios


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    
    # Ejercicio de consumo de datos por API
    url = "https://jsonplaceholder.typicode.com/todos"

    # El primer paso es que copien esa URL en su explorador web
    # y analicen los datos en general:
    # 1) Observando la URL se puede ver que en total hay 200 entradas,
    # del id=1 al id=200
    # 2) Observando la URL se puede ver que en total hay 10 usuarios,
    # del userId=1 al userId=10
    # 3) En cada entrada se especifica si el usuario completó ese título,
    # mediante el campo "completed".
    
    dic_usuarios = titulos_completados(url)
    
    # Alumno, de cada usuario en el total de las 200 entradas
    # debe contar cuantos títulos completó cada usuario (de los 10 posibles)
    # y armar un gráfico de barras resumiendo la información.
    # gráfico en el eje "x" está cada uno de los 10 usuarios y en el eje
    # "y" la cantidad de títulos completados

    # Para poder ir haciendo esto debe ir almacenando la información
    # de cada usuario a medida que "itera" en un bucle los datos
    # del JSON recolectado. Al finalizar el bucle deberá tener la data
    # de los 10 usuarios con cuantos títulos completó cada uno.

    # Debe poder graficar dicha información en un gráfico de barras.
    # En caso de no poder hacer el gráfico comience por usar print
    # para imprimir cuantos títulos completó cada usuario
    # y verifique si los primeros usuarios (mirando la página a ojo)
    # los datos recolectados son correctos.
    
    usuarios = [x for x in dic_usuarios.keys()]
    cantidad_titulos = [valor.get("cant_titulos") for user,valor in dic_usuarios.items()]
    fig = plt.figure()
    fig.suptitle('Titulos por cada Usuario', fontsize=18)
    ax = fig.add_subplot()
    ax.bar(usuarios, cantidad_titulos, label='Usuarios',color='royalblue')
    ax.set_facecolor('bisque')
    ax.legend()
    plt.show()
    print("terminamos")

 