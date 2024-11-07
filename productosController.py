
from db import productos_collection
from bson.objectid import ObjectId


def crear_producto(nombre, categoria, precio, cantidad):
    nuevo_producto = {
        "nombre": nombre,
        "categoria": categoria,
        "precio": float(precio),
        "cantidad": int(cantidad)
    }
    productos_collection.insert_one(nuevo_producto)



def leer_productos(categoria=None):
    filtro = {}
    if categoria:
        filtro = {"categoria": categoria}
    return list(productos_collection.find(filtro))


def actualizar_producto(id_producto, nuevos_datos):
    productos_collection.update_one(
        {"_id": ObjectId(id_producto)},
        {"$set": nuevos_datos}
    )


def eliminar_producto(id_producto):
    productos_collection.delete_one({"_id": ObjectId(id_producto)})
