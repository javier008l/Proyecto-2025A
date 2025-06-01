from src.controllers.manager import Manager

from src.controllers.strategies.force import BruteForce
from src.controllers.strategies.basic import Basic


def iniciar():
    """Punto de entrada principal"""
    # ABCD #
    estado_inicial = "100"
    condiciones = "111"
    alcance = "111"
    mecanismo = "111"

    gestor_sistema = Manager(estado_inicial)

    ### Ejemplo de solución mediante módulo de fuerza bruta ###
    analizador_phi = Basic(gestor_sistema)
    analizador_bf = BruteForce(gestor_sistema)

    sia_cero = analizador_phi.aplicar_estrategia(
        condiciones,
        alcance,
        mecanismo,
    )

    sia_bf = analizador_bf.analizar_completamente_una_red()
    print(sia_cero)
    print(sia_bf)
