def test_agregar_producto_incrementa_cantidad(carrito_vacio):
    # a) agrega 1 producto y verifica que cantidad() == 1
    carrito_vacio.agregar("Mouse", 25)
    assert carrito_vacio.cantidad() == 1

def test_carrito_vacio_al_iniciar(carrito_vacio):
    # b) verifica que un carrito recién creado tiene 0 items
    assert carrito_vacio.cantidad() == 0

def test_total_suma_precios_correctamente(carrito_vacio):
    # c) agrega 2 productos y verifica que total() retorna la suma correcta
    carrito_vacio.agregar("Libro", 15)
    carrito_vacio.agregar("Cuaderno", 5)
    assert carrito_vacio.total() == 20

def test_agregar_producto_duplicado_incrementa_cantidad(carrito_vacio):
    # d) agrega el mismo producto dos veces y verifica cantidad == 2
    carrito_vacio.agregar("Lápiz", 2)
    carrito_vacio.agregar("Lápiz", 2)
    assert carrito_vacio.cantidad() == 2

def test_vaciar_deja_carrito_en_cero(carrito_vacio):
    # e) agrega productos, llama vaciar() y verifica que cantidad() == 0
    carrito_vacio.agregar("Mochila", 30)
    carrito_vacio.vaciar()
    assert carrito_vacio.cantidad() == 0