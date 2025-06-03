import tkinter as tk

def setup_after_idle():
    print("Setup finalizado quando tkinter ficou inativo")

root = tk.Tk()
root.title("Exemplo com after_idle")

# Executa o setup assim que a aplicação ficar inativa
root.after_idle(setup_after_idle)

label = tk.Label(root, text="Bem-vindo ao aplicativo!")
label.pack(pady=20)

root.mainloop()


