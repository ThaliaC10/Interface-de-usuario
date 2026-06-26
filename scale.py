import tkinter as tk

janela = tk.Tk()
janela.title("Exemplo — Scale")
janela.geometry("380x280")
janela.configure(bg="#EBF5FB")
janela.resizable(False, False)

tk.Label(janela, text="Controle de Volume",
         font=("Arial", 14, "bold"), bg="#EBF5FB", fg="#1B4F72").pack(pady=20)

# ── Scale ────────────────────────────────────────────────────────────
# from_      → valor mínimo
# to         → valor máximo
# resolution → incremento de cada passo
# orient     → 'horizontal' ou 'vertical'
# .get()     → lê o valor atual
# .set(v)    → define o valor pelo código
var_volume = tk.DoubleVar(value=50)

scale = tk.Scale(
    janela,
    variable=var_volume,
    from_=0,
    to=100,
    resolution=1,
    orient="horizontal",
    length=280,
    label="Volume (%)",
    font=("Arial", 10),
    bg="#EBF5FB",
    fg="#1B4F72",
    troughcolor="#AED6F1",
    activebackground="#2E86C1"
)
scale.pack(pady=10)

def mostrar():
    valor = var_volume.get()
    if valor == 0:
        emoji = "🔇"
    elif valor < 40:
        emoji = "🔉"
    else:
        emoji = "🔊"
    label_resultado.config(text=f"{emoji}  Volume: {int(valor)}%")

label_resultado = tk.Label(janela, text="Volume: 50%",
                            font=("Arial", 12), bg="#EBF5FB", fg="#1B4F72")
label_resultado.pack(pady=10)

tk.Button(janela, text="Ver Volume", command=mostrar,
          bg="#1B4F72", fg="white", font=("Arial", 11, "bold"),
          width=16, relief="flat", cursor="hand2").pack(pady=8)

janela.mainloop()
