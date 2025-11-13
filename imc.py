import tkinter as tk
from tkinter import messagebox

def calcular_imc():
    try:
        altura_cm = float(entry_altura.get())
        peso = float(entry_peso.get())
        altura_m = altura_cm / 100

        imc = peso / (altura_m ** 2)
        imc_formatado = f"{imc:.2f}"

        # Classificação segundo IMC
        if imc < 18.5:
            status = "Abaixo do peso"
        elif 18.5 <= imc < 24.9:
            status = "Peso normal"
        elif 25 <= imc < 29.9:
            status = "Sobrepeso"
        elif 30 <= imc < 34.9:
            status = "Obesidade Grau I"
        elif 35 <= imc < 39.9:
            status = "Obesidade Grau II"
        else:
            status = "Obesidade Grau III"

        resultado_texto = (
            f"Nome: {entry_nome.get()}\n"
            f"Endereço: {entry_endereco.get()}\n"
            f"IMC: {imc_formatado}\n"
            f"Classificação: {status}"
        )

        text_resultado.delete(1.0, tk.END)
        text_resultado.insert(tk.END, resultado_texto)

    except ValueError:
        messagebox.showerror("Erro", "Digite valores numéricos válidos para altura e peso!")

def reiniciar():
    entry_nome.delete(0, tk.END)
    entry_endereco.delete(0, tk.END)
    entry_altura.delete(0, tk.END)
    entry_peso.delete(0, tk.END)
    text_resultado.delete(1.0, tk.END)

def sair():
    root.destroy()


# ------------------- INTERFACE -------------------

root = tk.Tk()
root.title("Cálculo do IMC - Índice de Massa Corporal")
root.geometry("600x350")

# Nome
tk.Label(root, text="Nome do Paciente:").place(x=10, y=20)
entry_nome = tk.Entry(root, width=70)
entry_nome.place(x=150, y=20)

# Endereço
tk.Label(root, text="Endereço Completo:").place(x=10, y=60)
entry_endereco = tk.Entry(root, width=70)
entry_endereco.place(x=150, y=60)

# Altura
tk.Label(root, text="Altura (cm)").place(x=10, y=110)
entry_altura = tk.Entry(root, width=20)
entry_altura.place(x=90, y=110)

# Peso
tk.Label(root, text="Peso (Kg)").place(x=10, y=150)
entry_peso = tk.Entry(root, width=20)
entry_peso.place(x=90, y=150)

# Caixa de Resultado
text_resultado = tk.Text(root, width=35, height=10, borderwidth=2, relief="solid")
text_resultado.place(x=280, y=100)

# Botões
btn_calcular = tk.Button(root, text="Calcular", width=15, command=calcular_imc)
btn_calcular.place(x=100, y=250)

btn_reiniciar = tk.Button(root, text="Reiniciar", width=15, command=reiniciar)
btn_reiniciar.place(x=250, y=250)

btn_sair = tk.Button(root, text="Sair", width=15, command=sair)
btn_sair.place(x=400, y=250)

root.mainloop()