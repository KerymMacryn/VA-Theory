# En codigo/quark_potential.py
import numpy as np
import matplotlib.pyplot as plt
import os

def plot_quark_potential():
    # Crear carpeta si no existe
    output_folder = '../figuras'
    os.makedirs(output_folder, exist_ok=True)

    r = np.linspace(0.1, 2.0, 100)  # Distancia en fermis
    V = 0.1 * r  # Potencial lineal (σ = 0.1 GeV/fm)

    plt.figure(figsize=(10, 6))
    plt.plot(r, V, 'r-', linewidth=2, label='Potencial VA-Quark')
    plt.xlabel('Distancia (fm)', fontsize=12)
    plt.ylabel('Energía (GeV)', fontsize=12)
    plt.title('Confinamiento desde el VA', fontsize=14)
    plt.legend()
    plt.grid(True)

    output_file = os.path.join(output_folder, 'quark_potential.png')
    plt.savefig(output_file, dpi=300)
    print(f"[✓] Imagen guardada en: {output_file}")

plot_quark_potential()
