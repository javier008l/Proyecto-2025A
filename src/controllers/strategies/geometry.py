import itertools as it
import time
import numpy as np
import pandas as pd
from src.funcs.base import (
    ABECEDARY,
    dec2bin,
    emd_efecto,
    lil_endian,
    count_bits,
    seleccionar_subestado,
)
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

from src.testing.path import HCPath


class Geometry(SIA):
    """Class Phi is used as base for other strategies, bruteforce with pyphi."""

    def __init__(self, gestor: Manager) -> None:
        super().__init__(gestor)
        profiler_manager.start_session(
            f"{NET_LABEL}{len(gestor.estado_inicial)}{gestor.pagina}"
        )
        self.logger = SafeLogger(PYPHI_STRAREGY_TAG)

    @profile(context={TYPE_TAG: PYPHI_ANALYSIS_TAG})
    def aplicar_estrategia(
        self,
        condiciones: str,
        alcance: str,
        mecanismo: str,
    ):
        self.sia_preparar_subsistema(condiciones, alcance, mecanismo)
        print(self.sia_subsistema)

        i_state = tuple(
            bit
            for i, bit in enumerate(self.sia_subsistema.estado_inicial)
            if i in self.sia_subsistema.indices_ncubos
        )
        print(i_state, self.sia_subsistema.estado_inicial)

        return

        # initial_state_dec = int("".join(map(str, initial_state_bin)), 2)

        sistema = self.sia_subsistema

        cubos = sistema.ncubos
        promedios = [1 - x.data.mean() for x in cubos]

        print(promedios)

        return

        m, n = sistema.dims_ncubos.size, sistema.indices_ncubos.size

        sistema_t = tuple(
            np.zeros(
                (2,) * m,
                dtype=np.float32,
            )
            for _ in range(n)
        )

        ejes = [(0,) * n] * m
        ejes = [
            tuple((1 if i == j else 0) for i, _ in enumerate(ejes))
            for j, _ in enumerate(ejes)
        ]

        print(ejes)

        # vistos = { (0,0,0) }
        # (0,0,0) ° (1,0,0) = recorrer_adyacentes((1,0,0)) if (1,0,0) is not in vistos
        # (0,0,0) ° (0,1,0) = recorrer_adyacentes((0,1,0)) if (0,1,0) is not in vistos
        # (0,0,0) ° (0,0,1) = recorrer_adyacentes((0,0,1)) if (0,0,1) is not in vistos

        for tcube, ncube in zip(sistema_t, sistema.ncubos):
            print()
            estado_inicial = ncube.data[i_state]

            print(f"{estado_inicial=}")

            for estado_actual in np.nditer(ncube.data):
                diferencia = abs(estado_inicial - estado_actual)

                # hamming entre estado inicial y actual

                # guardar en tabla t la diferencia mas lo que digans los llamados recursivos POR el gamma

            break

    def generar_adyacentes_validos(self, estado: int):
        # Generar todos los adyacentes válidos de un estado
        ...

    def visualizar_resultados(self, tabla_t):
        print(tabla_t, "\n")
        ultima_fila = tabla_t.iloc[-1]  # última fila
        indice_minimo = ultima_fila.idxmin()
        valor_minimo = ultima_fila.min()

        # Encontrado el índice (columna) del valor mínimo
        print(f"Índice del mínimo en última fila: {indice_minimo}")
        print(f"Valor mínimo en última fila: {valor_minimo}")

        print("Partición base:")
        primal = self.sia_subsistema

        futuro = np.array([indice_minimo], dtype=np.int8)
        presente = np.array([], dtype=np.int8)
        bipartito = primal.bipartir(futuro, presente)
        emd_primal = emd_efecto(
            bipartito.distribucion_marginal(), self.sia_dists_marginales
        )
        print(f"emd_primal: {emd_primal}")

        # generar una bipartición para validar:
        for index in self.sia_subsistema.indices_ncubos:
            partito = self.sia_subsistema
            futuro = np.array([index], dtype=np.int8)
            presente = np.array([], dtype=np.int8)

            bipartito = partito.bipartir(futuro, presente)
            vector_marginal = bipartito.distribucion_marginal()
            emd_resultante = emd_efecto(vector_marginal, self.sia_dists_marginales)

            print(f"index: {index}, emd: {emd_resultante}")
        # print(bipartito)

        return
        Solution(
            "Geometrica",
            DUMMY_EMD,
            self.sia_dists_marginales,
            np.ndarray(DUMMY_ARR),
            DUMMY_PARTITION,
        )

    ...
    ...

    def aplicar_estrategia_old(self, condiciones: str, alcance: str, mecanismo: str):
        self.sia_preparar_subsistema(condiciones, alcance, mecanismo)

        # print(self.sia_subsistema)

        # return

        initial_state_bin = tuple(
            canal
            for i, canal in enumerate(self.sia_subsistema.estado_inicial)
            if i in self.sia_subsistema.indices_ncubos
        )
        initial_state_dec = int("".join(map(str, initial_state_bin)), 2)

        sistema = self.sia_subsistema
        m, n = sistema.dims_ncubos.size, sistema.indices_ncubos.size

        cubos = sistema.ncubos
        filas_base = lil_endian(m)
        reindexado = lil_endian(m)
        # filas_base = range(1 << m)
        # print(f"{filas_base=}")
        # print(f"{reindexado=}")

        # potencias para ejes
        ejes_potencia = np.array([1 << i for i in range(m)])
        # porque es lil-endian!
        # print(f"{ejes_potencia=}")

        # combinatoria de ejes_potencia
        # camino = HCPath()
        # factores_estado = list(camino.get_predecessors(m))
        # factores_estado = [
        #     list(it.combinations(ejes_potencia, i)) for i in range(m + 1)
        # ]
        # factores_estado = [lista for lista in factores_estado for lista in lista]
        # factores_estado = sorted(factores_estado, key=sum)
        # factores_estado = np.array(factores_estado, dtype=object)
        # print("Factores estado:", factores_estado)

        # Creamos un mapeo de índices usando filas_base
        # mapeo_indices = {valor: idx for idx, valor in enumerate(filas_base)}

        # Función para calcular el valor decimal de una tupla
        # def tupla_a_decimal(t):
        #     return sum(t) if len(t) > 0 else 0

        # Reordenamos factores_estado según el mapeo
        # factores_estado = sorted(
        #     factores_estado, key=lambda x: mapeo_indices[tupla_a_decimal(x)]
        # )
        # factores_estado = np.array(factores_estado, dtype=object)
        # Sólo iterar hasta la mitad para no intercambiar dos veces
        # half_length = len(filas_base) // 2
        # for i, j in zip(
        #     filas_base[:half_length],
        #     reindexado[:half_length],
        # ):
        #     factores_estado[i], factores_estado[j] = (
        #         factores_estado[j],
        #         factores_estado[i],
        #     )

        # print("Factores estado reordenado:", factores_estado)

        # return

        # print(f"{initial_state_bin=}")
        # print(f"{initial_state_dec=}")

        filas_iniciadas = [initial_state_dec ^ clave for clave in filas_base]
        tabla_t = pd.DataFrame(
            0.0, index=filas_iniciadas, columns=sistema.indices_ncubos, dtype=np.float64
        )

        # print(tabla_t)
        # print(cubos)

        # working_cubes = {1}

        for cubo in cubos:
            # if cubo.indice not in working_cubes:
            #     continue

            # print()
            # valor_inicial = cubo.data[seleccionar_subestado(initial_state_bin)]
            print(f"{cubo.indice=}")

            valor_inicial = cubo.data[initial_state_bin]
            # print(f"    valor_inicial: {valor_inicial}")

            for fila_tabla, factores_eje, valor_destino in zip(
                filas_iniciadas,
                # factores_estado,
                np.nditer(cubo.data),
            ):
                # print(
                #     f"{fila_tabla=}\t{factores_eje=}\t{valor_destino=}",
                # )

                if not factores_eje:
                    # print()
                    continue

                # print(f"    valor_destino: {valor_destino}")

                gamma = 1 / (1 << count_bits(fila_tabla ^ initial_state_dec))
                tabla_t.loc[fila_tabla, cubo.indice] = gamma * abs(
                    valor_destino - valor_inicial
                )
                for eje in factores_eje:
                    # eje_destino = fila_tabla ^ eje
                    # print(f"    +coste en {eje}: {tabla_t.loc[eje, cubo.indice]}")
                    tabla_t.loc[fila_tabla, cubo.indice] += tabla_t.loc[
                        eje, cubo.indice
                    ]
                    # print(
                    #     f"      {valor_destino} - {tabla_t.loc[eje, cubo.indice]} = {valor_destino - tabla_t.loc[eje, cubo.indice]}",
                    # )

                # print(f"  coste total: {tabla_t.loc[fila_tabla, cubo.indice]}")
                # print(f"  *= {gamma} = {gamma * tabla_t.loc[fila_tabla, cubo.indice]}")

                # tabla_t.loc[fila_tabla, cubo.indice] *= gamma

                # print(tabla_t, "\n")

        return self.visualizar_resultados(tabla_t)


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
