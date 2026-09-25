import tkinter as tk
from tkinter import messagebox
import os

class Calculadora:
    def __init__(self, parent_root):
        self.window = tk.Toplevel(parent_root)
        self.window.title("🔢 Calculadora - otakOS")
        self.window.geometry("320x420")
        self.window.configure(bg="#1e1e2d")
        self.window.resizable(False, False)

        # Barra superior estándar con botón de cerrar
        frame_toolbar = tk.Frame(self.window, bg="#2a2a3d", height=40)
        frame_toolbar.pack(fill=tk.X, padx=0, pady=0)
        frame_toolbar.pack_propagate(False)

        self.btn_cerrar = tk.Button(
            frame_toolbar, 
            text="❌ Cerrar", 
            bg="#ff4d4d", 
            fg="white", 
            activebackground="#ff6666",
            relief=tk.FLAT,
            font=("Arial", 9, "bold"),
            command=self.window.destroy
        )
        self.btn_cerrar.pack(side=tk.RIGHT, padx=8, pady=6)

        # Pantalla / Display de la calculadora
        self.display_var = tk.StringVar(value="0")
        
        display_frame = tk.Frame(self.window, bg="#14141e", bd=0)
        display_frame.pack(fill=tk.X, padx=10, pady=10)

        self.display = tk.Label(
            display_frame,
            textvariable=self.display_var,
            anchor="e",
            bg="#14141e",
            fg="white",
            font=("Arial", 24, "bold"),
            padx=10,
            pady=15
        )
        self.display.pack(fill=tk.X)

        # Panel de botones
        buttons_frame = tk.Frame(self.window, bg="#1e1e2d")
        buttons_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

        # Configuración de la botonera (Texto, Fila, Columna)
        botones = [
            ('C', 0, 0), ('(', 0, 1), (')', 0, 2), ('/', 0, 3),
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('*', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('-', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('+', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2) # El '=' ocupará dos columnas o se ajusta
        ]

        # Configurar grid pesos para que se expandan bien
        for i in range(5):
            buttons_frame.rowconfigure(i, weight=1)
        for j in range(4):
            buttons_frame.columnconfigure(j, weight=1)

        # Crear e insertar botones dinámicamente
        for (texto, fila, col) in botones:
            # Color distintivo para operadores y acción de limpiar
            if texto in ('/', '*', '-', '+', '='):
                bg_color = "#ff69b4" if texto == '=' else "#3b3b4f"
                active_color = "#ff1493" if texto == '=' else "#4b4b6f"
            elif texto == 'C':
                bg_color = "#ff4d4d"
                active_color = "#ff6666"
            else:
                bg_color = "#2a2a3d"
                active_color = "#3a3a4d"

            # El botón '=' abarca 2 columnas si se desea, o lo dejamos estándar en su celda
            colspan = 2 if texto == '=' else 1

            btn = tk.Button(
                buttons_frame,
                text=texto,
                bg=bg_color,
                fg="white",
                activebackground=active_color,
                relief=tk.FLAT,
                font=("Arial", 14, "bold"),
                command=lambda t=texto: self.on_button_click(t)
            )
            btn.grid(row=fila, column=col, columnspan=colspan, sticky="nsew", padx=3, pady=3)

    def on_button_click(self, char):
        actual = self.display_var.get()

        if char == 'C':
            self.display_var.set("0")
        elif char == '=':
            try:
                # Reemplazar símbolos visuales si fuera necesario y evaluar de forma segura
                resultado = eval(actual.replace('x', '*'))
                self.display_var.set(str(resultado))
            except Exception:
                messagebox.showerror("Error", "Expresión matemática inválida", parent=self.window)
                self.display_var.set("0")
        else:
            if actual == "0" and char not in ('+', '-', '*', '/'):
                self.display_var.set(char)
            else:
                self.display_var.set(actual + char)

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()
    app = Calculadora(root)
    root.mainloop()
