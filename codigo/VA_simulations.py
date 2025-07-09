import numpy as np
import matplotlib.pyplot as plt

def simulate_va_transition(kappa=0.5, rho_Planck=5e96):
    """Simula la transición VA → Espacio-Tiempo."""
    t = np.linspace(0, 10, 1000)
    rho_ET = rho_Planck * np.exp(-t**2)
    phi = 246e9 * np.sqrt(1 - np.exp(-(rho_ET/rho_Planck)**2))  # Higgs en eV
    
    plt.figure(figsize=(10, 6))
    plt.plot(t, phi, 'b-', label='Campo de Higgs (Φ)')
    plt.xlabel('Tiempo (adimensional)')
    plt.ylabel('Φ (eV)')
    plt.legend()
    plt.savefig('../figuras/higgs_va.png')

if __name__ == "__main__":
    simulate_va_transition()