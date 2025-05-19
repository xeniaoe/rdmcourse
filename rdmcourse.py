import numpy as np
import matplotlib.pyplot as plt

# Liste der Dateinamen
file_names = ['data/XO004_Eu.txt']

# Dateninitialisierung
all_data = []

# Schleife über Dateien
for file_name in file_names:
    # Datei einlesen und Daten extrahieren
    data = np.genfromtxt(file_name, delimiter=',', skip_header=1)
    all_data.append(data)

# Plotten der Daten
plt.figure(figsize=(8, 6))

for data, file_name in zip(all_data, file_names):
    # Hier anpassen, je nachdem, wie deine Daten strukturiert sind
    x_values = data[:, 0]
    y_values = data[:, 1]

    # Plotten der Daten
    plt.plot(x_values, y_values, label=file_name)


# Legende und Achsentitel hinzufügen
plt.xlabel('was ich will')
plt.ylabel('wie viel ich krieg')
legend_labels = ['C1']
plt.legend(legend_labels)
#plt.xlim(370,620)
#plt.ylim(0,1000)
#plt.savefig('PyrenPEnormal.png', dpi=600, bbox_inches='tight')
# Diagramm anzeigen
plt.show()