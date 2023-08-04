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

ventana = tt.Tk()
ventana.title("Búsqueda de Productos")
ventana.geometry("300x200")

tt.Label(ventana, text="Ingrese la clave del producto a buscar:").pack()
entrada_clave = tt.Entry(ventana)
entrada_clave.pack()

tt.Button(ventana, text="Buscar", command=buscar_productos).pack()

ventana.mainloop()

