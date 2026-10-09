
import tkinter as tk

ventana = tk.Tk()
ventana.title("Calculadora")
ventana.geometry("320x440")
ventana.resizable(False, False)
ventana.configure(bg="#F4F6FA")

operacion = ""

def presionar(valor):
    global operacion
    operacion += str(valor)
    pantalla.set(operacion)

def borrar():
    global operacion
    operacion = ""
    pantalla.set("0")

def retroceder():
    global operacion
    operacion = operacion[:-1]
    pantalla.set(operacion if operacion else "0")

def calcular():
    global operacion
    try:
        resultado = eval(
            operacion,
            {"__builtins__": {}},
            {}
        )
        if not isinstance(resultado, (int, float)):
            raise ValueError
        operacion = str(resultado)
        pantalla.set(operacion)
    except (SyntaxError, ZeroDivisionError,
            ValueError, TypeError, NameError):
        pantalla.set("Error")
        operacion = ""

pantalla = tk.StringVar(value="0")

entrada = tk.Entry(
    ventana,
    textvariable=pantalla,
    font=("Arial", 26),
    bg="white",
    fg="#1F2937",
    bd=0,
    justify="right",
    state="readonly",
    readonlybackground="white"
)
entrada.pack(fill="x", padx=15, pady=20, ipady=15)

marco = tk.Frame(ventana, bg="#F4F6FA")
marco.pack(expand=True, fill="both", padx=12, pady=5)

botones = [
    ["C", "⌫", "/", "*"],
    ["7", "8", "9", "-"],
    ["4", "5", "6", "+"],
    ["1", "2", "3", "="],
    ["0", "."]
]

for fila, valores in enumerate(botones):
    for columna, texto in enumerate(valores):

        if texto == "C":
            comando = borrar
        elif texto == "⌫":
            comando = retroceder
        elif texto == "=":
            comando = calcular
        else:
            comando = lambda x=texto: presionar(x)

        color = "#E5E9F0"
        letra = "#1F2937"

        if texto in ["+", "-", "*", "/"]:
            color = "#D8E7FF"
            letra = "#2563EB"
        elif texto == "=":
            color = "#2563EB"
            letra = "white"
        elif texto == "C":
            color = "#FEE2E2"
            letra = "#DC2626"

        boton = tk.Button(
            marco,
            text=texto,
            font=("Arial", 18, "bold"),
            bg=color,
            fg=letra,
            activebackground="#BFDBFE",
            bd=0,
            cursor="hand2",
            command=comando
        )

        boton.grid(
            row=fila,
            column=columna,
            padx=4,
            pady=4,
            sticky="nsew"
        )

for i in range(5):
    marco.rowconfigure(i, weight=1)

for i in range(4):
    marco.columnconfigure(i, weight=1)

ventana.mainloop()
