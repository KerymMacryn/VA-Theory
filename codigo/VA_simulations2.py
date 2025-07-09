import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

def higgs_va(y, t, kappa, R_curv):
    # Ejemplo sencillo del sistema diferencial
    phi, dphi_dt = y
    d2phi_dt2 = -kappa * phi + R_curv  # Solo ejemplo, adapta a tu modelo real
    return [dphi_dt, d2phi_dt2]

def plot_higgs_evolution():
    # Parámetros iniciales y rango de tiempo
    phi0 = 246  # Valor inicial del campo Higgs
    dphi_dt0 = 0  # Derivada inicial
    t = np.linspace(0, 10, 200)  # Tiempo adimensional
    kappa_range = np.linspace(0.1, 1.0, 5)  # Ejemplo de valores kappa

    plt.figure(figsize=(10, 6))
    for kappa in kappa_range:
        R_cur_
