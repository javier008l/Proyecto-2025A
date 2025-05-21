from src.controllers.manager import Manager

from src.controllers.strategies.geometry import Geometry
from src.controllers.strategies.q_nodes import QNodes
from src.controllers.strategies.phi import Phi


def iniciar():
    """Punto de entrada principal"""
    # ABCDEFGHIJ #
    estado_inicial = "0000"
    condiciones =    "1111"
    alcance =        "1111"
    mecanismo =      "1111"

    gestor_sistema = Manager(estado_inicial)

    ### Ejemplo de solución mediante módulo de fuerza bruta ###
    analizador_geo = Geometry(gestor_sistema)
    analizador_qn = QNodes(gestor_sistema)
    analizador_phi = Phi(gestor_sistema)

    sia_cero = analizador_geo.aplicar_estrategia(
        condiciones,
        alcance,
        mecanismo,
    )
    # sia_uno = analizador_qn.aplicar_estrategia(
    #     condiciones,
    #     alcance,
    #     mecanismo,
    # )
    # sia_dos = analizador_phi.aplicar_estrategia(
    #     condiciones,
    #     alcance,
    #     mecanismo,
    # )
    # print(sia_uno, sia_dos, sia_cero)
