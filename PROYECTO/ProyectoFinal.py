import tkinter as tt
from tkinter import messagebox


nombre = {
    "pam1": "Pantalon 1",
    "pam2": "Pantalon 2",
    "pam3": "Pantalon 3",
    "cam1": "Camisa 1",
    "cam2": "Camisa 2",
    "cam3": "Camisa 3",
    "pat1": "Pantaloneta 1",
    "pat2": "Pantaloneta 2",
    "pat3": "Pantaloneta 3"
}
cantidad = {
    "pam1": 10,
    "pam2": 30,
    "pam3": 22,
    "cam1": 55,
    "cam2": 42,
    "cam3": 14,
    "pat1": 44,
    "pat2": 36,
    "pat3": 10
}
color = {
    "pam1": "Azul",
    "pam2": "Negro",
    "pam3": "Verde",
    "cam1": "Azul",
    "cam2": "Negro",
    "cam3": "Verde",
    "pat1": "Azul",
    "pat2": "Negro",
    "pat3": "Verde"
}
talla = {
    "pam1": "S",
    "pam2": "M",
    "pam3": "L",
    "cam1": "S",
    "cam2": "M",
    "cam3": "L",
    "pat1": "S",
    "pat2": "M",
    "pat3": "L"
}
precio = {
    "pam1": 5000,
    "pam2": 6000,
    "pam3": 8000,
    "cam1": 3000,
    "cam2": 6000,
    "cam3": 7000,
    "pat1": 3000,
    "pat2": 4500,
    "pat3": 5650
}

usuarios = {'123': '123'}
intentos = {}
productos_en_factura = {}

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
            ventana.destroy()
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
    global ventana_menu
    ventana_menu = tt.Tk()
    ventana_menu.title("Ventana Menú")
    ventana_menu.geometry("300x600")

    tt.Label(ventana_menu, text=f"Bienvenido, {usuario_ingresado}!").pack()
    tt.Label(ventana_menu).pack()
    tt.Button(ventana_menu, text="Buscar Producto", command=ventana_buscar_producto).pack()
    tt.Label(ventana_menu).pack()
    tt.Button(ventana_menu, text="agregar producto", command=ventana_nuevop).pack()
    tt.Label(ventana_menu).pack()
    tt.Button(ventana_menu, text="agregar a factura", command=agregar_producto).pack()
    tt.Label(ventana_menu).pack()
    tt.Button(ventana_menu, text="realizar venta", command=calcular_total).pack()
    tt.Label(ventana_menu).pack()
    tt.Button(ventana_menu, text="Salir", command=ventana_menu.destroy).pack()
     
def calcular_total():
    total = 0
    factura_texto = "Detalles de la Factura:\n\n"
    
    for clave, cantidad in productos_en_factura.items():
        if clave in precio and cantidad > 0:
            subtotal = precio[clave] * cantidad
            factura_texto += f"Código: {clave}\n"
            factura_texto += f"Cantidad: {cantidad}\n"
            factura_texto += f"Subtotal: {subtotal} pesos\n\n"
            total += subtotal
    
    if total > 0:
        factura_texto += f"Total de la Factura: {total} pesos."
        messagebox.showinfo("Detalles de la Factura", factura_texto)
    else:
        messagebox.showinfo("Detalles de la Factura", "La factura está vacía.")

def agregar_producto():
    ventana_agregar = tt.Toplevel(ventana_menu)
    ventana_agregar.title("Agregar Producto")
    ventana_agregar.geometry("300x200")
    global entrada_clave_agregar
    global entrada_cantidad_agregar
    tt.Label(ventana_agregar, text="Ingrese la clave del producto a agregar:").pack()
    entrada_clave_agregar = tt.Entry(ventana_agregar)
    entrada_clave_agregar.pack()

    tt.Label(ventana_agregar, text="Ingrese la cantidad a agregar:").pack()
    entrada_cantidad_agregar = tt.Entry(ventana_agregar)
    entrada_cantidad_agregar.pack()
    
    tt.Button(ventana_agregar, text="Agregar", command=agregar_a_factura_con_argumentos).pack()

def agregar_a_factura_con_argumentos():
    codigo = entrada_clave_agregar.get()
    cantidad = int(entrada_cantidad_agregar.get())

    if codigo in nombre:
        productos_en_factura[codigo] = cantidad
        messagebox.showinfo("Producto Agregado", f"Se ha agregado {cantidad} unidades de '{nombre[codigo]}' a la factura.")
    else:
        messagebox.showerror("Error", "No se encontró ningún producto con la clave especificada.")

def buscar_producto_por_clave(clave_buscada):
    productos_encontrados = []
    if clave_buscada in nombre:
        producto = {
            "nombre": nombre[clave_buscada],
            "cantidad": cantidad[clave_buscada],
            "color": color[clave_buscada],
            "talla": talla[clave_buscada],
            "precio": precio[clave_buscada]
        }
        productos_encontrados.append(producto)
    return productos_encontrados

def buscar_productos():
    clave_buscada = entrada_clave.get()
    productos_encontrados = buscar_producto_por_clave(clave_buscada)

    if productos_encontrados:
        resultado_text = ""
        for producto in productos_encontrados:
            resultado_text += f"Nombre: {producto['nombre']}\n"
            resultado_text += f"Cantidad: {producto['cantidad']}\n"
            resultado_text += f"Color: {producto['color']}\n"
            resultado_text += f"Talla: {producto['talla']}\n"
            resultado_text += f"Precio: {producto['precio']} pesos\n"
            resultado_text += "\n"

        messagebox.showinfo("Resultados de la búsqueda", resultado_text)
    else:
        messagebox.showerror("Error", f"No se encontraron productos con la clave '{clave_buscada}'.")

def ventana_buscar_producto():
    global entrada_clave
    
    ventana = tt.Toplevel(ventana_menu)
    ventana.title("Búsqueda de Productos")
    ventana.geometry("300x200")
    
    tt.Label(ventana, text="Ingrese la clave del producto a buscar:").pack()
    entrada_clave = tt.Entry(ventana)
    entrada_clave.pack()

    tt.Button(ventana, text="Buscar", command=buscar_productos).pack()
  
def nuevo_producto():
    clave = entrada_clave.get()
    if clave in nombre:
        messagebox.showerror("Error", f"La clave '{clave}' ya existe en la base de datos.")
        return
    
    nombre_nuevo = entrada_nombre.get()
    cantidad_nueva = int(entrada_cantidad.get())
    color_nuevo = entrada_color.get()
    talla_nueva = entrada_talla.get()
    precio_nuevo = float(entrada_precio.get())
    
    nombre[clave] = nombre_nuevo
    cantidad[clave] = cantidad_nueva
    color[clave] = color_nuevo
    talla[clave] = talla_nueva
    precio[clave] = precio_nuevo
    
    messagebox.showinfo("Producto Agregado", "El producto ha sido agregado a la base de datos.")
    
    entrada_clave.delete(0, tt.END)
    entrada_nombre.delete(0, tt.END)
    entrada_cantidad.delete(0, tt.END)
    entrada_color.delete(0, tt.END)
    entrada_talla.delete(0, tt.END)
    entrada_precio.delete(0, tt.END)

def ventana_nuevop():
    global entrada_clave, entrada_nombre, entrada_cantidad, entrada_color, entrada_talla, entrada_precio
    
    ventananp = tt.Toplevel(ventana_menu)
    ventananp.title("Nuevo Producto")
    ventananp.geometry("400x300")
    
    tt.Label(ventananp, text="Clave del producto:").pack()
    entrada_clave = tt.Entry(ventananp)
    entrada_clave.pack()
    
    tt.Label(ventananp, text="Nombre del producto:").pack()
    entrada_nombre = tt.Entry(ventananp)
    entrada_nombre.pack()
    
    tt.Label(ventananp, text="Cantidad:").pack()
    entrada_cantidad = tt.Entry(ventananp)
    entrada_cantidad.pack()
    
    tt.Label(ventananp, text="Color:").pack()
    entrada_color = tt.Entry(ventananp)
    entrada_color.pack()
    
    tt.Label(ventananp, text="Talla:").pack()
    entrada_talla = tt.Entry(ventananp)
    entrada_talla.pack()
    
    tt.Label(ventananp, text="Precio:").pack()
    entrada_precio = tt.Entry(ventananp)
    entrada_precio.pack()
    
    tt.Button(ventananp, text="Nuevo Producto", command=nuevo_producto).pack()


inicio()