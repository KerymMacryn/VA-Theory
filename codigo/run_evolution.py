# run_evolution.py
import numpy as np
import matplotlib.pyplot as plt
from numerical_solvers import solve_rho_evolution

# Parámetros del modelo
params = {'m_rho_sq': 1.0}

# Dominio espacial
x = np.linspace(-10, 10, 500)
dx = x[1] - x[0]

# Condición inicial: pico gaussiano sobre fondo uniforme
rho0 = 1.0 + 0.2 * np.exp(-x**2)

# Intervalo de tiempo para la evolución
t_span = (0, 10)  # desde t=0 hasta t=10

# Resolver la evolución
solution = solve_rho_evolution(rho0, t_span, dx, params)

# Evaluar la solución en diferentes tiempos
times = np.linspace(t_span[0], t_span[1], 5)
sols = [solution.sol(t) for t in times]

# Graficar la evolución
import matplotlib.pyplot as plt
plt.figure(figsize=(10, 6))

for i, rho_t in enumerate(sols):
    plt.plot(x, rho_t, label=f't = {times[i]:.1f}')

plt.title("Evolución del campo estructural ρ(x, t)")
plt.xlabel("x")
plt.ylabel("ρ(x, t)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
