# run_simulation.py
import numpy as np
import matplotlib.pyplot as plt
from tsqvt_core import ricci_scalar, potential_V, potential_V_prime

# --- Parámetros y grilla ---
x = np.linspace(-10, 10, 1000)
dx = x[1] - x[0]

# Definir un perfil de rho(x) como ejemplo
rho = 1.0 + 0.2 * np.exp(-x**2)  # pico gaussiano alrededor de x=0

# --- Calcular escalar de Ricci ---
R = ricci_scalar(rho, dx)

# --- Calcular potencial estructural ---
params = {'m_rho_sq': 1.0}
V = potential_V(rho, params)
V_prime = potential_V_prime(rho, params)

# --- Mostrar resultados ---
print(f"Máximo de R(x): {np.max(R)}")
print(f"Integral de V(rho): {np.trapz(V, x)}")

# --- Graficar ---
plt.figure(figsize=(12, 6))

plt.subplot(1, 3, 1)
plt.plot(x, rho, label='ρ(x)')
plt.title("Campo estructural ρ(x)")
plt.grid(True)

plt.subplot(1, 3, 2)
plt.plot(x, R, label='R(x)', color='darkred')
plt.title("Escalar de Ricci R(x)")
plt.grid(True)

plt.subplot(1, 3, 3)
plt.plot(x, V, label='V(ρ)', color='green')
plt.title("Potencial estructural V(ρ)")
plt.grid(True)

plt.tight_layout()
plt.show()
# Guardar datos en archivo CSV
np.savetxt("../images/imagesresults_rho.csv", np.column_stack([x, rho, R, V]), 
           delimiter=",", header="x,rho(x),R(x),V(rho)", comments='')
