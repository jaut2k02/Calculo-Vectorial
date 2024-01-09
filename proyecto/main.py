import tkinter as tk
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

def f(x, y, z):
    return 1 / ((((x ** 2) + (y ** 2) + (z ** 2)) + 1) ** 2)

def calcular_integral():
    try:
        x_superior = float(limites.get())
        n_intervalos = int(intervalos.get())

        x_inferior = -x_superior
        y_inferior = x_inferior
        y_superior = x_superior
        z_inferior = x_inferior
        z_superior = x_superior

        dx = (x_superior - x_inferior) / n_intervalos
        dy = (y_superior - y_inferior) / n_intervalos
        dz = (z_superior - z_inferior) / n_intervalos

        riemann_sum = 0

        for i in range(n_intervalos):
            for j in range(n_intervalos):
                for k in range(n_intervalos):
                    x = x_inferior + (i + 0.5) * dx
                    y = y_inferior + (j + 0.5) * dy
                    z = z_inferior + (k + 0.5) * dz
                    riemann_sum += f(x, y, z) * dx * dy * dz

        resultado_label.config(text=f"Resultado de la suma de Riemann: {riemann_sum}")

        # Crear la visualización 3D de la función
        x_vals = np.linspace(x_inferior, x_superior, n_intervalos)
        y_vals = np.linspace(y_inferior, y_superior, n_intervalos)
        z_vals = np.linspace(z_inferior, z_superior, n_intervalos)

        X, Y, Z = np.meshgrid(x_vals, y_vals, z_vals)
        function_values = f(X, Y, Z)

        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        scatter = ax.scatter(X, Y, Z, c=function_values, cmap='viridis')
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z') #type:ignore
        ax.set_title('Función a integrar: '+'\n'+
                     '1 /((x² + y² + z²) + 1)²)')

        # Añadir la barra de color
        fig.colorbar(scatter)

        canvas = FigureCanvasTkAgg(fig, master=root)
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.grid(row=5, column=0, columnspan=2)

    except ValueError:
        resultado_label.config(text="Por favor, ingrese valores válidos.")

def limpiar():
    limites.delete(0, tk.END)
    intervalos.delete(0, tk.END)
    resultado_label.config(text="Resultado de la suma de Riemann: ")

# Crear la interfaz gráfica
root = tk.Tk()
root.title("Proyecto Vectorial")

# Etiquetas y cuadros de texto
lblimites = tk.Label(root, text="Límites (a):", font=("Helvetica", 12), padx=5, pady=5)
limites = tk.Entry(root, font=("Helvetica", 12))

lbintervalos = tk.Label(root, text="Número de Intervalos:", font=("Helvetica", 12), padx=5, pady=5)
intervalos = tk.Entry(root, font=("Helvetica", 12))

# Botones
btn_calcular = tk.Button(root, text="Calcular Integral", command=calcular_integral, font=("Helvetica", 12), padx=10, pady=10, cursor="hand2")
btn_limpiar = tk.Button(root, text="Limpiar", command=limpiar, font=("Helvetica", 12), padx=10, pady=10, cursor="hand2")

# Etiqueta para mostrar el resultado
resultado_label = tk.Label(root, text="Resultado de la suma de Riemann: ", font=("Helvetica", 12), padx=5, pady=5)

# Ubicación en la interfaz
lblimites.grid(row=0, column=0, padx=10, pady=5, sticky="E")
limites.grid(row=0, column=1, padx=10, pady=5)

lbintervalos.grid(row=1, column=0, padx=10, pady=5, sticky="E")
intervalos.grid(row=1, column=1, padx=10, pady=5)

resultado_label.grid(row=2, column=0, columnspan=2, pady=10)

btn_calcular.grid(row=3, column=0, columnspan=2, pady=10)
btn_limpiar.grid(row=4, column=0, columnspan=2, pady=5)

# Iniciar la interfaz
root.mainloop()