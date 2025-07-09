# En codigo/va_animation.py
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import os

def animate_va():
    # Crear carpeta de salida si no existe
    output_folder = '../figuras/animaciones'
    os.makedirs(output_folder, exist_ok=True)

    fig, ax = plt.subplots(figsize=(10, 6))
    x = np.linspace(0, 10, 100)
    line, = ax.plot([], [], 'b-', lw=2)
    
    def init():
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 250)
        return line,
    
    def update(frame):
        y = 246 * (1 - np.exp(-0.1 * frame * x))
        line.set_data(x, y)
        ax.set_title(f'Transición VA: t = {frame:.1f}')
        return line,
    
    anim = FuncAnimation(fig, update, frames=np.linspace(0, 10, 50),
                         init_func=init, blit=True)
    
    output_file = os.path.join(output_folder, 'va_evolution.gif')
    anim.save(output_file, writer='pillow', fps=10)
    print(f"[✓] Animación guardada en: {output_file}")

animate_va()
