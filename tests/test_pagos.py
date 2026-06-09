# Respuestas a preguntas teóricas:
# f) ¿Por qué es incorrecto usar la PasarelaPago real en los tests automáticos?
# Es incorrecto porque los tests automáticos deben ser predecibles y no tener efectos secundarios. 
# Usar la pasarela real implicaría realizar cobros de dinero reales cada vez que se ejecuta la suite.

# g) ¿Qué diferencia existe entre un Stub y un Mock? ¿Cuál de los dos usaste?
# Un Stub devuelve respuestas predefinidas, mientras que un Mock adicionalmente permite verificar 
# que fue llamado con los argumentos correctos. En el test test_pago_exitoso_retorna_txn_id 
# la herramienta actuó como un Stub.


import pytest
from unittest.mock import MagicMock
from app.pagos import ProcesadorPago

@pytest.fixture
def procesador_con_mock():
    """Fixture que provee ProcesadorPago con pasarela mockeada."""
    mock_pasarela = MagicMock()
    mock_pasarela.cobrar.return_value = {"estado": "ok", "txn_id": "TXN-TEST-001"}
    return ProcesadorPago(pasarela=mock_pasarela), mock_pasarela

def test_pago_exitoso_retorna_txn_id(procesador_con_mock):
    procesador, mock_pasarela = procesador_con_mock
    resultado = procesador.procesar(monto=150.0, cliente="ana@mail.com")
    assert resultado["txn_id"] == "TXN-TEST-001"
    assert resultado["estado"] == "ok"

def test_pago_llama_pasarela_con_monto_correcto(procesador_con_mock):
    procesador, mock_pasarela = procesador_con_mock
    procesador.procesar(monto=250.0, cliente="ana@mail.com")
    mock_pasarela.cobrar.assert_called_once_with(monto=250.0)

def test_pago_sin_duplicados(procesador_con_mock):
    """Verifica que no se realizan cobros duplicados."""
    procesador, mock_pasarela = procesador_con_mock
    procesador.procesar(monto=100.0, cliente="juan@mail.com")
    assert mock_pasarela.cobrar.call_count == 1

def test_pago_falla_cuando_pasarela_lanza_excepcion():
    mock_pasarela = MagicMock()
    mock_pasarela.cobrar.side_effect = ConnectionError("Pasarela no disponible")
    procesador = ProcesadorPago(pasarela=mock_pasarela)
    with pytest.raises(ConnectionError):
        procesador.procesar(monto=50.0, cliente="luis@mail.com")