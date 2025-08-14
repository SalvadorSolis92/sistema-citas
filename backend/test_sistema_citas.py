import unittest
from sistema_citas import ordenar_solicitudes, calcular_metricas

class TestSistemaCitas(unittest.TestCase):

    def test_ordenar_citas_prioridad(self):
        """Debe ordenar primero por prioridad y luego por menor tiempo."""
        ciudadanos = [
            {"nombre": "Ana", "tiempo": 25, "prioridad": False, "turno": 1, "orden_llegada": 1},
            {"nombre": "Luis", "tiempo": 40, "prioridad": True, "turno": 2, "orden_llegada": 2},
            {"nombre": "Juan", "tiempo": 30, "prioridad": True, "turno": 3, "orden_llegada": 3}
        ]
        resultado = ordenar_solicitudes(ciudadanos)
        self.assertEqual(resultado[0]["nombre"], "Juan")  # Prioridad y menor tiempo
        self.assertEqual(resultado[1]["nombre"], "Luis")
        self.assertEqual(resultado[2]["nombre"], "Ana")

    def test_calcular_metricas(self):
        """Debe calcular correctamente el tiempo total y promedio."""
        plan = [
            {"nombre": "Juan", "tiempo": 30, "espera_min": 0},
            {"nombre": "Luis", "tiempo": 40, "espera_min": 30},
            {"nombre": "Ana", "tiempo": 25, "espera_min": 70}
        ]
        metricas = calcular_metricas(plan)
        self.assertEqual(metricas["total_atencion"], 95)
        self.assertAlmostEqual(metricas["promedio_espera"], 33.33, places=2)


if __name__ == "__main__":
    unittest.main()
