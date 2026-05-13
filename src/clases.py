import abc
import logging

# --- EXCEPCIONES PERSONALIZADAS ---
# Requerimiento: Incorporar excepciones personalizadas [cite: 17]
class SoftwareFJError(Exception):
    """Clase base para excepciones del sistema."""
    pass

class ReservaInvalidaError(SoftwareFJError):
    """Se lanza cuando los parámetros de la reserva son incorrectos."""
    pass

class ServicioNoDisponibleError(SoftwareFJError):
    """Se lanza cuando el servicio no puede ser procesado."""
    pass

# --- CLASES BASE Y ABSTRACCIÓN ---
class EntidadSistema(abc.ABC):
    """Clase abstracta que representa entidades generales[cite: 21]."""
    @abc.abstractmethod
    def obtener_detalles(self):
        pass

class Servicio(abc.ABC):
    """Clase abstracta Servicio[cite: 23]."""
    def __init__(self, nombre, tarifa_base):
        self.nombre = nombre
        self.tarifa_base = tarifa_base

    @abc.abstractmethod
    def calcular_costo(self, duracion):
        """Método sobrescrito por clases derivadas[cite: 24]."""
        pass

    @abc.abstractmethod
    def validar_parametros(self, duracion):
        """Validaciones estrictas[cite: 12]."""
        pass

# --- CLASES DERIVADAS (POLIMORFISMO) ---
class ReservaSalas(Servicio):
    def calcular_costo(self, duracion):
        return self.tarifa_base * duracion

    def validar_parametros(self, duracion):
        if duracion <= 0:
            raise ServicioNoDisponibleError("La duración de la sala debe ser mayor a 0.")

class AlquilerEquipos(Servicio):
    # Requerimiento: Métodos sobrecargados (parámetros opcionales) [cite: 26, 27]
    def calcular_costo(self, duracion, seguro=True):
        costo = self.tarifa_base * duracion
        return costo + 50 if seguro else costo

    def validar_parametros(self, duracion):
        if duracion > 30:
            raise ServicioNoDisponibleError("El alquiler de equipos no puede exceder los 30 días.")

class AsesoriaEspecializada(Servicio):
    def calcular_costo(self, duracion):
        # Implementación con impuestos (19%)
        return (self.tarifa_base * duracion) * 1.19

    def validar_parametros(self, duracion):
        if duracion < 1:
            raise ServicioNoDisponibleError("Las asesorías requieren mínimo 1 hora.")

# --- ENCAPSULACIÓN: CLASE CLIENTE ---
class Cliente(EntidadSistema):
    def __init__(self, nombre, id_cliente):
        # Encapsulación de datos personales con atributos privados [cite: 22]
        self.__nombre = nombre 
        self.__id_cliente = id_cliente
        self.validar_datos()

    def validar_datos(self):
        if not self.__nombre or not self.__id_cliente:
            raise ValueError("Datos de cliente incompletos.")

    def obtener_detalles(self):
        return f"Cliente: {self.__nombre} (ID: {self.__id_cliente})"

# --- CLASE RESERVA ---
class Reserva:
    """Integra cliente, servicio, duración y estado[cite: 25]."""
    def __init__(self, cliente, servicio, duracion):
        self.cliente = cliente
        self.servicio = servicio
        self.duracion = duracion
        self.estado = "Pendiente"

    def procesar(self):
        # Bloque try/except/finally robusto [cite: 17]
        try:
            print(f"Procesando reserva para {self.cliente.obtener_detalles()}...")
            self.servicio.validar_parametros(self.duracion)
            costo = self.servicio.calcular_costo(self.duracion)
            self.estado = "Confirmada"
            # Registro en logs [cite: 18, 31]
            logging.info(f"EXITO: {self.cliente.obtener_detalles()} - Servicio: {self.servicio.nombre} - Costo: {costo}")
            print(f"Reserva exitosa. Costo: ${costo}")
        except ServicioNoDisponibleError as e:
            self.estado = "Fallida"
            logging.error(f"ERROR DE NEGOCIO: {str(e)}")
            # Encadenamiento de excepciones [cite: 17]
            raise ReservaInvalidaError("No se pudo completar la reserva.") from e
        except Exception as e:
            logging.critical(f"ERROR CRÍTICO: {str(e)}")
            raise
        finally:
            print(f"Estado de la operación: {self.estado}\n")