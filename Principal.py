from modelo.App import AutomataApp

import tkinter as tk

if __name__ == "__main__":
    ventana_principal = tk.Tk()
    app = AutomataApp(ventana_principal)
    ventana_principal.mainloop()

