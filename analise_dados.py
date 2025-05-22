import matplotlib.pyplot as plt


# Dados das pessoas em centimetro
altura = [160,165,170,175,180,185]

#Dados das pessoa em kilo
peso = [50,60,65,70,75,80]

plt.scatter(altura,peso)
plt.xlabel('Altura (cm)')
plt.ylabel('Peso (kg)')
plt.title('Relação entre altura e peso')
plt.show()