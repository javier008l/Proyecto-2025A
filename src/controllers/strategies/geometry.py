import itertools as it
import time
import numpy as np
import pandas as pd
from src.funcs.base import ABECEDARY, dec2bin, lil_endian
from src.funcs.format import fmt_biparticion
from src.controllers.manager import Manager

import math

from pyphi import Network, Subsystem
from pyphi.labels import NodeLabels
from pyphi.models.cuts import Bipartition, Part

from src.middlewares.slogger import SafeLogger
from src.middlewares.profile import profiler_manager, profile

from src.models.base.sia import SIA
from src.models.core.solution import Solution
from src.models.enums.distance import MetricDistance
from src.models.base.application import aplicacion


from src.constants.base import (
    NET_LABEL,
    TYPE_TAG,
)
from src.constants.models import (
    DUMMY_ARR,
    DUMMY_EMD,
    DUMMY_PARTITION,
    PYPHI_STRAREGY_TAG,
    PYPHI_ANALYSIS_TAG,
)


class Geometry(SIA):
    """Class Phi is used as base for other strategies, bruteforce with pyphi."""

    def __init__(self, config: Manager) -> None:
        super().__init__(config)
        profiler_manager.start_session(
            f"{NET_LABEL}{len(config.estado_inicial)}{config.pagina}"
        )
        self.logger = SafeLogger(PYPHI_STRAREGY_TAG)

    @profile(context={TYPE_TAG: PYPHI_ANALYSIS_TAG})
    def aplicar_estrategia(self, condiciones: str, alcance: str, mecanismo: str):
        self.sia_preparar_subsistema(condiciones, alcance, mecanismo)

        sistema = self.sia_subsistema

        A, B, C, D, E, F = a, b, c, d, e, f = range(6)

        m, n = sistema.dims_ncubos.size, sistema.dims_ncubos.size

        cubos = sistema.ncubos
        # cadenas_lil_endian = lil_endian(m)
        cadenas_lil_endian = range(1 << m)

        # potencias para ejes
        ejes = np.array([1 << i for i in range(m)])
        print(f"{ejes=}")

        # combinatoria de ejes
        claves = [list(it.combinations(ejes, i)) for i in range(m + 1)]
        claves = [lista for lista in claves for lista in lista]

        # claves = np.ndarray(claves, dtype=object)[lil_endian(m)]
        claves = sorted(claves, key=sum)

        claves = np.array(claves, dtype=object)
        print(f"{claves=}")

        # nditer para selección de clave, accediendo según diccionario de combinatoria

        tabla_t = pd.DataFrame(
            0,
            index=cadenas_lil_endian,
            columns=range(n),
        )

        print(tabla_t)

        for indice, cubo in enumerate(cubos):
            print()
            # print("cubo::\n", cubo)
            for fila, x, coords in zip(
                cadenas_lil_endian, claves, np.nditer(cubo.data)
            ):
                print(indice, fila, x, coords)

                print(cubo)
                if coords:
                    for i in coords:
                        # x_inicial = x[estado_inicial]
                        # x_actual = x[coords[i]]
                        # coste_transicion = abs(x_inicial - x_actual)
                        # print(coste_transicion)
                        ...
                        # acá básicamente la idea es acceder al valor de las claves y ubcarlas correctamente en la clave real.

        # idealmente de aca en adelante

        # Tras tener soluciones prometedoras las evaluamos/bipartimos para hallar la pérdida real (max 5)

        return Solution(
            "Geometrica",
            DUMMY_EMD,
            self.sia_dists_marginales,
            np.ndarray(DUMMY_ARR),
            DUMMY_PARTITION,
        )


"""

000
001
010
011: 3=1,2
100
101: 5=1,4
110: 6=2,4
111: 7=1,2,4


[1,2,4]

"""
