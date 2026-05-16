import ctypes
import gc
# Utilizamos el módulo ctypes para acceder a los objetos inaccesibles mediante su dirección de memoria.
class PyObject(ctypes.Structure):
    _fields_ = [("refcnt", ctypes.c_long)]
gc.disable()  # Desactiva el Garbage Collector generacional (gc)
lst = []
lst.append(lst)
# Guarda la dirección de lista 
lst_address = id(lst)
# Destruye la referencia lst
del lst
object_1 = {}
object_2 = {}
object_1['obj2'] = object_2
object_2['obj1'] = object_1
obj_address = id(object_1)
del object_1, object_2 # destruye las referencias
# Quitar comentario para ver resultados de llamar manualmente al recolector de basura
#gc.collect()
# Ver reference count de las direcciones de objetos
print('Dirección: ',hex(obj_address), 'Referencias: ',PyObject.from_address(obj_address).refcnt)
print('Dirección: ',hex(lst_address), 'Referencias: ',PyObject.from_address(lst_address).refcnt)