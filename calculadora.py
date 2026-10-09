
import tkinter as tk

# Operaciones matematicas
def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        raise ValueError("No se puede dividir entre cero")
    return a / b


# Interfaz grafica
def main():
    ventana = tk.Tk()
    ventana.title("Calculadora")
    ventana.geometry("300x400")
    ventana.configure(bg="white")

    pantalla = tk.Entry(
        ventana,
        font=("Arial", 24),
        justify="right"
    )
    pantalla.pack(pady=20, padx=10, fill="x")

    def presionar(numero):
        pantalla.insert(tk.END, numero)

    def limpiar():
        pantalla.delete(0, tk.END)

    def calcular():
        try:
            resultado = eval(
                pantalla.get(),
                {"__builtins__": {}},
                {}
            )
            if type(resultado) not in (int, float):
                raise ValueError()
            limpiar()
            pantalla.insert(0, str(resultado))
        except Exception:
            limpiar()
            pantalla.insert(0, "Error")

    marco = tk.Frame(ventana, bg="white")
    marco.pack()

    botones = [
        ["7", "8", "9", "/"],
        ["4", "5", "6", "*"],
        ["1", "2", "3", "-"],
        ["C", "0", "=", "+"]
    ]

    for fila in range(4):
        for columna in range(4):
            texto = botones[fila][columna]

            if texto == "C":
                accion = limpiar
            elif texto == "=":
                accion = calcular
            else:
                accion = lambda x=texto: presionar(x)

            tk.Button(
                marco,
                text=texto,
                font=("Arial", 18),
                width=4,
                height=2,
                bg="#E5E7EB",
                fg="black",
                command=accion
            ).grid(
                row=fila,
                column=columna,
                padx=3,
                pady=3
            )

    ventana.mainloop()


if __name__ == "__main__":
    main()
