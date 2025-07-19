def rho_profile(r, rs):
    """Static vacuum solution: structural density profile."""
    return 1 - rs / r

def friedmann_modified(a, rho, drho_dt, Omega_m):
    """
    Modified Friedmann equation for ρ(t)-modulated spacetime.
    
    Parameters:
        a : float
            Scale factor a(t)
        rho : float
            Structural field ρ(t)
        drho_dt : float
            Time derivative of ρ(t)
        Omega_m : float
            Matter density parameter
        
    Returns:
        H_squared : float
            Square of the Hubble parameter
    """
    H_squared = (Omega_m / rho - (a * drho_dt)**2) / (3 * a**2)
    return H_squared
