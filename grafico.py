#GRAFICO 3D (ASSI X, Y, Z) X = eta, Y = altezza Z = peso
import matplotlib.pyplot as plt
import random 

plt.style.use('_mpl-gallery')

n = 100 

eta = [random.randint(18, 80) for _ in range(n)]        # Età tra 18 e 80 anni
altezza = [random.randint(140, 200) for _ in range(n)]  # Altezza tra 140 e 200 cm
peso = [random.randint(40, 120) for _ in range(n)]      # Peso tra 40 e 120 kg

fig, ax = plt.subplots(subplot_kw={"projection": "3d"}) # subplot_kw={"projection": "3d"} è un dizionario che indica che il grafico è 3D
ax.scatter(eta, altezza, peso) #è un metodo dell'oggetto ax (asse del grafico) che crea un grafico a dispersione dove ogni punto ha 3 coordinate (X, Y, Z)

# Etichette degli assi
ax.set_xlabel('Età (anni)')
ax.set_ylabel('Altezza (cm)')
ax.set_zlabel('Peso (kg)')

plt.show()