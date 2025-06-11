from src.middlewares.slogger import SafeLogger
from src.controllers.manager import Manager
from src.controllers.strategies.q_nodes import QNodes

from src.strategies.force import BruteForce


def iniciar():
    """Punto de entrada principal"""
    estado_inicial = "100000"
    condiciones =    "111111"
    
    # Lista de pruebas a realizar
    pruebas = [
    ('011111', '111111'),  # BCDEFt+1 | ABCDEFt
    ('101101', '111111'),  # ACDFt+1 | ABCDEFt
    ('101110', '111111'),  # ACDEt+1 | ABCDEFt
    ('101111', '011111'),  # ACDEFt+1 | BCDEFt
    ('101111', '101111'),  # ACDEFt+1 | ACDEFt
    ('101111', '110111'),  # ACDEFt+1 | ABDEFt
    ('101111', '111011'),  # ACDEFt+1 | ABCEFt
    ('101111', '111101'),  # ACDEFt+1 | ABCDFt
    ('101111', '111110'),  # ACDEFt+1 | ABCDEt
    ('110011', '111111'),  # ABEFt+1 | ABCDEFt
    ('110111', '111111'),  # ABDFt+1 | ABCDEFt
    ('110110', '111111'),  # ABDEt+1 | ABCDEFt
    ('110111', '011111'),  # ABDEFt+1 | BCDEFt
    ('110111', '101111'),  # ABDEFt+1 | ACDEFt
    ('110111', '110111'),  # ABDEFt+1 | ABDEFt
    ('110111', '111011'),  # ABDEFt+1 | ABCEFt
    ('110111', '111101'),  # ABDEFt+1 | ABCDFt
    ('110111', '111110'),  # ABDEFt+1 | ABCDEt
    ('111011', '111111'),  # ABCFt+1 | ABCDEFt
    ('111010', '111111'),  # ABCEt+1 | ABCDEFt
    ('111011', '011111'),  # ABCEFt+1 | BCDEFt
    ('111011', '101111'),  # ABCEFt+1 | ACDEFt
    ('101011', '111111'),  # ACEFt+1 | ABCDEFt 
    ('101110', '111111'),  # ADEFt+1 | ABCDEFt 
    ('111011', '111011'),  # ABCEFt+1 | ABCEFt
    ('111110', '111101'),  # BCDEFt+1 | ABCDFt
    ('111111', '011111'),  # ABCDEFt+1 | BCDEFt
    ('111111', '101111'),  # ABCDEFt+1 | ACDEFt
    ('111111', '101111'),  # ABCDEFt+1 | ACDEFt
    ('110111', '111111'),  # ABDEFt+1 | ABCDEFt
    ('111111', '111011'),  # ABCDEFt+1 | ABCEFt
    ('111110', '111111'),  # ABCDEt+1 | ABCDEFt
    ('111101', '111111'),  # ABCDFt+1 | ABCDEFt
    ('101111', '111111'),  # ACDEFt+1 | ABCDEFt
    ('110111', '111111'),  # ABDEFt+1 | ABCDEFt
    ('111011', '111111'),  # ABCEFt | ABCDEFt+1
    ('111110', '111111'),  # ABCDEt+1 | ABCDEFt
    ('011111', '111111'),  # BCDEFt+1 | ABCDEFt
    ('101111', '111111'),  # ACDEFt+1 | ABCDEFt
    ('101111', '111111'),  # ACDEFt+1 | ABCDEFt
    ('110111', '111111'),  # ABDEFt+1 | ABCDEFt
    ('111011', '111111'),  # ABCEFt+1 | ABCDEFt
    ('111110', '111111'),  # ABCDEt+1 | ABCDEFt
    ('111111', '111101'),  # ABCDEFt+1 | ABCDFt
    ('111111', '101111'),  # ABCDEFt+1 | ACDEFt
    ('111111', '110111'),  # ABCDEFt+1 | ABDEFt
    ('111111', '111011'),  # ABCDEFt+1 | ABCEFt
    ('111111', '111110'),  # ABCDEFt+1 | ABCDEt
    ('111111', '011111'),  # ABCDEFt+1 | BCDEFt
    ('111111', '111111'),  # ABCDEFt+1 | ABCDEFt
]


    logger = SafeLogger("PruebasQ6")

    gestor_sistema = Manager(estado_inicial)
    analizador_fb = QNodes(gestor_sistema)

    # Realizar todas las pruebas
    for i, (alcance, mecanismo) in enumerate(pruebas, 1):
        print(f"Prueba {i}: Alcance = {alcance}, Mecanismo = {mecanismo}")
        sia_uno = analizador_fb.aplicar_estrategia(condiciones, alcance, mecanismo)
        logger.critic(f"Resultado: {sia_uno}\n")



    ### Ejemplo de solución mediante módulo de fuerza bruta ###
    analizador_bf = BruteForce(gestor_sistema)

    sia_cero = analizador_bf.aplicar_estrategia(
        condiciones,
        alcance,
        mecanismo,
    )

    print(sia_cero)
