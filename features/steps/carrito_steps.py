from behave import given, when, then
from app.carrito import Carrito
from app.descuentos import calcular_descuento

@given('tengo un carrito vacío')
def step_carrito_vacio(context):
    context.carrito = Carrito()

@when('agrego el producto "{nombre}" con precio {precio:d} y cantidad {cantidad:d}')
def step_agregar_producto(context, nombre, precio, cantidad):
    for _ in range(cantidad):
        context.carrito.agregar(nombre, float(precio))

@then('el carrito tiene {cantidad:d} artículo')
@then('el carrito tiene {cantidad:d} artículos')
def step_verificar_cantidad(context, cantidad):
    assert context.carrito.cantidad() == cantidad

@then('el total del carrito es {total:d}')
def step_verificar_total(context, total):
    assert context.carrito.total() == float(total)

@when('vacío el carrito')
def step_vaciar_carrito(context):
    context.carrito.vaciar()

@when('aplico el código de descuento "{codigo}"')
def step_aplicar_descuento(context, codigo):
    context.codigo_descuento = codigo

@then('el total con descuento es {total_final:d}')
def step_verificar_descuento(context, total_final):
    total_actual = context.carrito.total()
    total_calculado = calcular_descuento(total_actual, context.codigo_descuento)
    assert total_calculado == float(total_final)