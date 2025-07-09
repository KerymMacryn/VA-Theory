import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import os

# --- Parámetros físicos ---
v = 246e9  # VEV del Higgs en eV
rho_Planck = 5e96  # Escala de densidad de Planck en kg/m³
xi = 0.1  # Acoplamiento a la curvatura escalar
R_curv = 1e-8  # Curvatura escalar fija en eV² (ajustable)

# Conversión de densidad: kg/m³ → eV⁴
kg_m3_to_ev4 = 5.6e-10

# --- Funciones físicas del modelo ---

# Densidad en función del tiempo
def rho_t(t):
    """Densidad efectiva en eV⁴ como función gaussiana en el tiempo."""
    return 1e30 * np.exp(-t**2) * kg_m3_to_ev4

# Masa efectiva del Higgs según la densidad VA
def m_H(rho):
    """Masa efectiva inducida por el VA (con saturación hiperbólica)."""
    return v * np.sqrt(1 - np.exp(-(rho / 1e21)**2))  # 1e21 eV⁴ ≈ escala crítica

# EDO para el campo Higgs con interacción VA
def higgs_va(y, t, kappa):
    phi, dphi_dt = y
    rho = rho_t(t)
    m_eff = m_H(rho)
    d2phi_dt2 = - (m_eff**2 + xi * R_curv + kappa * rho) * phi
    return [dphi_dt, d2phi_dt2]

# --- Simulación numérica ---

# Condiciones iniciales
phi0 = v
dphi_dt0 = 0.0
y0 = [phi0, dphi_dt0]
t = np.linspace(0, 10, 1000)  # Tiempo adimensional

# Valores de kappa a explorar
kappa_range = [0.1, 0.3, 0.6, 0.8, 1.0]

# Crear carpeta si no existe
os.makedirs("../figuras", exist_ok=True)

# Graficar resultados
plt.figure(figsize=(10, 6))
for kappa in kappa_range:
    sol = odeint(higgs_va, y0, t, args=(kappa,))
    plt.plot(t, sol[:, 0], label=f'κ = {kappa:.1f}')

plt.title("Evolución del campo de Higgs con interacción VA", fontsize=14)
plt.xlabel("Tiempo (adimensional)", fontsize=12)
plt.ylabel("Campo φ (eV)", fontsize=12)
plt.legend()
plt.grid(True)

# Guardar y mostrar
plt.savefig("../figuras/evolucion_higgs_va.png", dpi=300)
plt.show()
