import logging
import os
from clases import Cliente, ReservaSalas, AlquilerEquipos, AsesoriaEspecializada, Reserva, ReservaInvalidaError

# Configuración del archivo de logs [cite: 18, 31]
# Se asegura de que la carpeta logs exista
if not os.path.exists('logs'):
    os.makedirs('logs')

logging.basicConfig(
    filename='logs/sistema_software_fj.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def ejecutar_simulacion():
    """Simula 10 operaciones completas (válidas e inválidas)."""
    print("=== SOFTWARE FJ - SIMULACIÓN DE GESTIÓN ===\n")
    
    # Instancias de prueba
    juan = Cliente("Juan Perez", "1001")
    sala_a = ReservaSalas("Sala de Conferencias", 120)
    laptop = AlquilerEquipos("MacBook Air", 45)
    profe = AsesoriaEspecializada("Asesoría IA", 300)

    # Lista de 10 casos: (Cliente, Servicio, Duración)
    casos = [
        (juan, sala_a, 3),      # 1. Éxito
        (juan, sala_a, -5),     # 2. Fallo: Duración negativa
        (juan, laptop, 5),      # 3. Éxito
        (juan, laptop, 50),     # 4. Fallo: Excede 30 días
        (juan, profe, 2),       # 5. Éxito
        (None, sala_a, 2),      # 6. Fallo: Sin cliente
        (juan, profe, 0.5),     # 7. Fallo: Menos de 1 hora
        (juan, laptop, 10),     # 8. Éxito
        (juan, sala_a, 1),      # 9. Éxito
        (juan, profe, 4)        # 10. Éxito
    ]

    for i, (cli, serv, dur) in enumerate(casos, 1):
        print(f"--- Operación #{i} ---")
        try:
            if cli is None:
                raise ValueError("Referencia de cliente nula.")
            
            reserva_activa = Reserva(cli, serv, dur)
            reserva_activa.procesar()
        except (ReservaInvalidaError, ValueError) as e:
            # El sistema continúa funcionando ante errores graves 
            print(f"Resultado: Error controlado - {e}")
        except Exception as e:
            print(f"Resultado: Error inesperado del sistema.")

    print("=== SIMULACIÓN FINALIZADA - REVISE EL ARCHIVO DE LOGS ===")

if __name__ == "__main__":
    ejecutar_simulacion()