import numpy as np
import matplotlib.pyplot as plt

vector = np.zeros(7)

tiempo = []
medias = []

with open("T_exp_LM35.txt", "r") as archivo:
    for linea in archivo:
        valores = [float(valor) for valor in linea.strip().split('\t')]

        nuevo_valor = valores[1]

        vector = np.roll(vector, -1)
        vector[-1] = nuevo_valor
        
        media_actual = np.mean(vector)
        
        tiempo.append(valores[0])
        medias.append(media_actual)
        
        print(f"Media actual: {media_actual}")
        plt.plot(tiempo, medias, marker='o')
        plt.xlabel('Tiempo')
        plt.ylabel('Media')
        plt.title('Evolución de la media a lo largo del tiempo')
        plt.pause(0.1)
        plt.clf()

plt.show()

