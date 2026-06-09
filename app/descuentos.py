# app/descuentos.py — BUG INTENCIONAL
CODIGOS_DESCUENTO = {
    "PROMO10": 0.10,
    "PROMO20": 0.20,
}
def calcular_descuento(total: float, codigo: str) -> float:
    """
    Calcula el total con descuento aplicado.
    Raises ValueError si total es negativo.
    """
    # BUG 1: Falta validación de total negativo
    if total < 0:
        raise ValueError("El total no puede ser negativo")
    porcentaje = CODIGOS_DESCUENTO.get(codigo, 0)
    # BUG 2: La fórmula es incorrecta (multiplica en vez de restar)
    return total - (total * porcentaje)