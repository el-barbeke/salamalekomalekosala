import tkinter as tk

# Definir la lista de letras para el teclado de 26 letras
letras = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 
]

def on_key_press(letra):
    print(f'Tecla presionada: {letra}')

# Crear la ventana principal
root = tk.Tk()
root.title('Teclado de un show mas')

# Crear un frame para contener los botones del teclado
frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

# Organizar las teclas en 3 filas
filas = 3
teclas_por_fila = len(letras) // filas  # Cantidad de teclas por fila

# Colocar las teclas en el grid
for i, letra in enumerate(letras):
    fila = i // teclas_por_fila  # Calcular la fila
    columna = i % teclas_por_fila  # Calcular la columna
    btn = tk.Button(frame, text=letra, width=5, height=2, command=lambda l=letra: on_key_press(l))
    btn.grid(row=fila, column=columna, padx=5, pady=5)

# Ejecutar la aplicación
root.mainloop()
