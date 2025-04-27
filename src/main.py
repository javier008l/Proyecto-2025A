from src.controllers.manager import Manager

from src.controllers.strategies.phi import Phi
from src.controllers.strategies.q_nodes import QNodes


def iniciar():
    """Punto de entrada principal"""
                    # ABCDEFGHIJ #
    estado_inicial = "1000000000"
    condiciones =    "1111111111"
    alcance =        "1111111111"
    mecanismo =      "1111111111"

    gestor_sistema = Manager(estado_inicial)

    ### Ejemplo de solución mediante módulo de fuerza bruta ###
    analizador_phi = Phi(gestor_sistema)
    analizador_fb = QNodes(gestor_sistema)

    sia_uno = analizador_fb.aplicar_estrategia(
        condiciones,
        alcance,
        mecanismo,
    )
    sia_dos = analizador_phi.aplicar_estrategia(
        condiciones,
        alcance,
        mecanismo,
    )

    print(sia_uno)
    print(sia_dos)
