import numpy as np
import matplotlib.pyplot as plt

vector = np.zeros(7)

tiempo = []
medianas = []

with open("T_exp_LM35.txt", "r") as archivo:
    for linea in archivo:
        valores = [float(valor) for valor in linea.strip().split('\t')]
        
        nuevo_valor = valores[1]
        
        vector = np.roll(vector, -1)
        vector[-1] = nuevo_valor
        
        mediana_actual = np.median(vector)
        
        tiempo.append(valores[0]) 
        medianas.append(mediana_actual)
        
        print(f"Mediana actual: {mediana_actual}")
        plt.plot(tiempo, medianas, marker='o')
        plt.xlabel('Tiempo')
        plt.ylabel('Mediana')
        plt.title('Evolución de la mediana a lo largo del tiempo')
        plt.pause(0.1)
        plt.clf()

plt.show()