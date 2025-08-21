from tkinter import *
from tkinter import messagebox

# -------------------------
# Función para abrir ventana sin imagen
# -------------------------
def abrir_ventana(num):
    nueva_ventana = Toplevel()
    nueva_ventana.title(f"Ventana del Botón {num}")
    nueva_ventana.geometry("400x200")
    nueva_ventana.config(bg="white")

    # --- Si el botón es el 1, mostrar solo los datos pedidos ---
    if num == 1:
        extra1 = Label(
            nueva_ventana,
            text="Lugar de nacimiento: San Gil",
            font=("Helvetica", 14),
            bg="white",
            fg="black"
        )
        extra1.pack(pady=10)

        extra2 = Label(
            nueva_ventana,
            text="Fecha de nacimiento: 31 de marzo del 2008",
            font=("Helvetica", 14),
            bg="white",
            fg="black"
        )
        extra2.pack(pady=10)

# -----------------------------
# ventana principal de la app
# -----------------------------
ventana_principal = Tk()
ventana_principal.title("App de Botones con Imagen")
ventana_principal.geometry("800x500")
ventana_principal.resizable(False, False)
ventana_principal.config(bg="white")

# --------------------------------
# frame principal
# --------------------------------
frame_principal = Frame(ventana_principal)
frame_principal.config(bg="white", width=780, height=480)
frame_principal.place(x=9, y=9)

# --------------------------------
# etiqueta con el nombre
# --------------------------------
nombre = Label(frame_principal, text="Carlos Esteban Galvis Montaña")
nombre.config(bg="white", fg="blue", font=("Helvetica", 20, "bold"))
nombre.place(relx=0.3, rely=0.05)  

# Imagen de la persona 
try:
    panel_img = PhotoImage(file="img/panel.png")
    lbl_panel_img = Label(frame_principal, image=panel_img, bg="white")
    lbl_panel_img.image = panel_img
    lbl_panel_img.place(relx=0.5, rely=0.3)
except Exception as e:
    lbl_error = Label(frame_principal, text="No se encontró la imagen", bg="white", fg="red", font=("Helvetica", 14))
    lbl_error.place(relx=0.5, rely=0.3, anchor="center")

# --------------------------------
# frame lateral para botones
# --------------------------------
frame_botones = Frame(frame_principal)
frame_botones.config(bg="lightgray", width=200, height=480)
frame_botones.place(x=0, y=0)

# Crear los 8 botones
y_base = 20
for i in range(1, 9):
    boton = Button(
        frame_botones,
        text=f"Botón {i}",
        font=("Helvetica", 14),
        command=lambda n=i: abrir_ventana(n)
    )
    boton.place(x=30, y=y_base + (i-1)*50, width=140, height=40)

# --------------------------------
# iniciar la app
# --------------------------------
ventana_principal.mainloop()
