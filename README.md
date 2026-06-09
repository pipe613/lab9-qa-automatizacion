# Laboratorio 9: Automatización de Pruebas y Gestión de Defectos (Dejo las respuestas f y g igual por si acaso aqui pero igual las deje en test_pagos)

## Módulo de Pagos (Mocking)

**f) ¿Por qué es incorrecto usar la PasarelaPago real en los tests automáticos?**
Es incorrecto porque los tests automáticos deben ser predecibles y no tener efectos secundarios. Usar la pasarela real implicaría realizar cobros de dinero reales cada vez que se ejecuta la suite de pruebas. Además, los tests dependerían de la conexión a internet y de la disponibilidad del servicio externo, lo que impediría controlar fácilmente escenarios de fallo.

**g) ¿Qué diferencia existe entre un Stub y un Mock? ¿Cuál de los dos usaste en test_pago_exitoso_retorna_txn_id?**
Un Stub simplemente devuelve respuestas predefinidas, mientras que un Mock hace eso y adicionalmente permite verificar que fue llamado con los argumentos correctos. En el test `test_pago_exitoso_retorna_txn_id`, la herramienta actuó específicamente como un Stub, ya que solo se configuró su valor de retorno y no se verificó con qué argumentos fue llamado.

## Cobertura de Código

**k) ¿Qué líneas quedaron sin cubrir al ejecutar el primer reporte? ¿Por qué?**
Quedaron sin cubrir las líneas 9 de `carrito.py` y 19 de `pagos.py`. Estas líneas corresponden a las validaciones de error (los bloques `if precio < 0:` y `if monto <= 0:` que lanzan un `ValueError`). Como en nuestros tests unitarios solo enviamos precios y montos positivos, el flujo del código nunca entró a esos condicionales para ejecutar la instrucción `raise ValueError`.

**l) ¿Significa cobertura 100% que el software no tiene bugs? Justifica con un ejemplo concreto del laboratorio.**
No, una cobertura del 100% no garantiza la ausencia de bugs; solo asegura que todas las líneas de código fueron ejecutadas al menos una vez durante las pruebas. Por ejemplo, en el módulo `descuentos.py`, antes de que corrigiéramos el código, la fórmula del descuento era incorrecta (`return total`), pero si hubiéramos medido la cobertura en ese momento, habría marcado 100% porque esa línea de retorno sí se ejecutaba, a pesar de que el resultado lógico que producía estaba mal.

## Gestión de Defectos

**o) ¿Cuál fue la severidad que asignaste a cada bug? Justifica tu decisión.**
Al bug de la fórmula matemática le asigné severidad HIGH. Aunque no hace que el sistema colapse (no es CRITICAL), afecta directamente la lógica de negocio central (el cobro a los clientes), generando un impacto económico importante si se cobra un monto incorrecto. Al bug de la falta de validación de números negativos le asignaría una severidad MEDIUM, ya que es un caso borde menos común pero que permite corromper el estado de los datos.

**p) ¿En qué se diferencia la severidad de la prioridad? Da un ejemplo donde ambas sean distintas.**
La severidad mide el impacto técnico que tiene el defecto sobre el sistema (qué tan roto está), mientras que la prioridad mide la urgencia de negocio para resolverlo (qué tan rápido se necesita). Ejemplo: Un error ortográfico en los Términos y Condiciones de la página web tiene una severidad LOW (no afecta la funcionalidad), pero si el departamento legal exige cambiarlo inmediatamente por riesgo de demanda, su prioridad será P1 (urgente).