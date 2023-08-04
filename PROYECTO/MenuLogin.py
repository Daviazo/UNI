import tkinter as tt
from tkinter import messagebox

from BuscarProductos import *

usuarios = {'123': '123'}
intentos = {}

def inicio():
    global ventana
    ventana = tt.Tk()

    ventana.title("Ventana de Inicio")
    ventana.geometry("500x200")

    tt.Label(ventana, text="Escoja una opción", bg="gray", width="100").pack()
    tt.Label(ventana).pack()
    tt.Button(ventana, text="Iniciar sesión", width="30", height="3", bg="white", command=iniciar_sesion).pack()
    tt.Label(ventana).pack()
    tt.Button(ventana, text="Registrar nuevo usuario", width="30", height="3", bg="white", command=registrar_usuario).pack()

    ventana.mainloop()

def iniciar_sesion():
    ventana_Login = tt.Toplevel(ventana)
    ventana_Login.title("Ventana Login")
    ventana_Login.geometry("200x200")

    tt.Label(ventana_Login, text="Por favor digite los datos").pack()

    global usuario
    usuario = tt.StringVar()
    global clave
    clave = tt.StringVar()

    tt.Label(ventana_Login, text="Digite su usuario").pack()
    tt.Entry(ventana_Login, textvariable=usuario).pack()
    tt.Label(ventana_Login, text="Digite su Clave").pack()
    tt.Entry(ventana_Login, textvariable=clave, show="*").pack()
    tt.Button(ventana_Login, text="Iniciar sesión", command=verificar_usuario).pack()

    global mensaje_login
    mensaje_login = tt.Label(ventana_Login, text="", fg="green")
    mensaje_login.pack()

def verificar_usuario():
    global usuario_ingresado
    usuario_ingresado = usuario.get()
    clave_ingresada = clave.get()

    if usuario_ingresado in usuarios and usuarios[usuario_ingresado] == clave_ingresada:
        mensaje_login.config(text="Acceso concedido")
        abrir_ventana_menu()
        ventana.destroy()
    else:
        if usuario_ingresado not in intentos:
            intentos[usuario_ingresado] = 1
        else:
            intentos[usuario_ingresado] += 1

        if intentos[usuario_ingresado] >= 3:
            mensaje_login.config(text="Acceso denegado. Demasiados intentos.")
            messagebox.showerror("Error", "Acceso denegado. Demasiados intentos.")
        else:
            mensaje_login.config(text=f"Acceso denegado. Intento {intentos[usuario_ingresado]} de 3.")
            messagebox.showerror("Error", f"Acceso denegado. Intento {intentos[usuario_ingresado]} de 3.")

def registrar_usuario():
    ventana_Registro = tt.Toplevel(ventana)
    ventana_Registro.title("Ventana Registro")
    ventana_Registro.geometry("200x200")

    tt.Label(ventana_Registro, text="Digite los datos para registrar un nuevo usuario").pack()

    global nuevo_usuario
    nuevo_usuario = tt.StringVar()
    global nueva_clave
    nueva_clave = tt.StringVar()

    tt.Label(ventana_Registro, text="Digite el nombre de usuario").pack()
    tt.Entry(ventana_Registro, textvariable=nuevo_usuario).pack()

    tt.Label(ventana_Registro, text="Digite la contraseña").pack()
    tt.Entry(ventana_Registro, textvariable=nueva_clave, show="*").pack()

    tt.Button(ventana_Registro, text="Registrar", command=registrar_usuario_funcion).pack()

    global mensaje_registro
    mensaje_registro = tt.Label(ventana_Registro, text="", fg="green")
    mensaje_registro.pack()

def registrar_usuario_funcion():
    nuevo_usuario_ingresado = nuevo_usuario.get()
    nueva_clave_ingresada = nueva_clave.get()

    if nuevo_usuario_ingresado in usuarios:
        mensaje_registro.config(text="ERROR: Ya existe ese usuario. Por favor, inicie sesión.")
        messagebox.showerror("Error", "Ya existe ese usuario. Por favor, inicie sesión.")
    else:
        usuarios[nuevo_usuario_ingresado] = nueva_clave_ingresada
        mensaje_registro.config(text="Usuario registrado con éxito.")
        messagebox.showinfo("Registro Exitoso", "Usuario registrado con éxito.")

def abrir_ventana_menu():
    ventana_menu = tt.Tk()
    ventana_menu.title("Ventana Menú")
    ventana_menu.geometry("300x200")

    tt.Label(ventana_menu, text=f"Bienvenido, {usuario_ingresado}!").pack()
    tt.Button(ventana_menu, text="Buscar Producto", command=buscar_producto_por_clave).pack()
    tt.Button(ventana_menu, text="Salir", command=ventana_menu.destroy).pack()

inicio()
