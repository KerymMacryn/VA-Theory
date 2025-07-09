import os
import numpy as np
import matplotlib.pyplot as plt

def plot_higgs_transition():
    # Crear carpeta si no existe
    output_folder = '../figuras'
    os.makedirs(output_folder, exist_ok=True)

    # Datos
    t = np.linspace(0, 10, 1000)
    rho_VA = np.exp(-t**2)
    phi = 246 * np.sqrt(1 - np.exp(-(0.5 * rho_VA)**2))

    # Plot
    plt.figure(figsize=(10, 6))
    plt.plot(t, phi, 'b-', linewidth=2, label='Campo de Higgs (Φ)')
    plt.xlabel('Tiempo (adimensional)', fontsize=12)
    plt.ylabel('Φ (GeV)', fontsize=12)
    plt.title('Transición VA → Espacio-Tiempo', fontsize=14)
    plt.legend()
    plt.grid(True)

    # Guardar imagen
    output_file = os.path.join(output_folder, 'higgs_va.png')
    plt.savefig(output_file, dpi=300, bbox_inches='tight')
    print(f"[✓] Imagen guardada correctamente en: {output_file}")

plot_higgs_transition()
