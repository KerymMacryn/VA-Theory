# tsqvt_core.py
# Módulo para las definiciones físicas fundamentales de la TSQVT.

import numpy as np

# --- Constantes Físicas ---
G_N = 6.67430e-11  # Constante gravitacional de Newton
C_LIGHT = 299792458  # Velocidad de la luz
H_BAR = 1.054571817e-34 # Constante de Planck reducida

# --- Parámetros del Modelo ---
# Parámetro de regularización para el límite rho -> 0
# Representa la escala de corte donde la EFT ya no es válida.
EPSILON_RHO = 1e-35 

def regularize(rho):
    """
    Aplica regularización para evitar singularidades en rho=0.
    Reemplaza 1/rho con una forma numéricamente estable.
    """
    return rho / (rho**2 + EPSILON_RHO)

def metric(rho):
    """
    Calcula la métrica emergente g_munu = rho * eta_munu.
    Devuelve la métrica en un punto o en una rejilla.
    Ref: [1], Ec. (43)
    """
    # En 1D espacial, la métrica es diag(-rho, 1/rho)
    # Aquí devolvemos rho, ya que es el factor determinante.
    return rho

def ricci_scalar(rho_grid, dx):
    """
    Calcula el escalar de Ricci para la métrica g_munu = rho * eta_munu.
    Utiliza diferencias finitas para las derivadas.
    Ref: [1], Ec. (32)
    """
    # Derivadas de rho usando diferencias finitas de segundo orden
    d_rho = np.gradient(rho_grid, dx)
    d2_rho = np.gradient(d_rho, dx)
    
    # Evitar división por cero con regularización
    rho_reg = np.maximum(rho_grid, EPSILON_RHO)
    
    term1 = 1.5 * (d_rho**2) / (rho_reg**2)
    term2 = -3.0 * d2_rho / rho_reg
    
    return term1 + term2

def potential_V(rho, params):
    """
    Potencial V(rho) para el campo estructural.
    Ejemplo: potencial de masa m^2 * (rho-1)^2
    Ref: [1], p. 30, Ec. (85)
    """
    m_rho_sq = params.get('m_rho_sq', 0.0)
    return 0.5 * m_rho_sq * (rho - 1.0)**2

def potential_V_prime(rho, params):
    """Derivada del potencial V(rho) con respecto a rho."""
    m_rho_sq = params.get('m_rho_sq', 0.0)
    return m_rho_sq * (rho - 1.0)