#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Sistema de Citas (pruebas backend en local, sin BD)
- Captura por consola
- Almacenamiento en listas (simulación)
- El ciudadano ingresa el tiempo estimado (validado dentro de un rango)
- Manejo de prioridad especial
- Ordenamiento: prioritarios primero y, dentro de cada grupo, por menor tiempo (SJF)
- Cálculo de métricas (tiempo total y promedio de espera)
"""

from datetime import datetime

MIN_TIEMPO = 20   # minutos
MAX_TIEMPO = 120  # minutos
MAX_NOMBRE = 100  # longitud máxima razonable

# ----------------------------
# Utilidades de validación
# ----------------------------

def leer_entero_positivo(msg: str) -> int:
    while True:
        texto = input(msg).strip()
        if not texto.isdigit():
            print("✗ Error: ingresa un número entero positivo.")
            continue
        n = int(texto)
        if n <= 0:
            print("✗ Error: debe ser mayor que 0.")
            continue
        return n

def leer_nombre(msg: str) -> str:
    while True:
        nombre = input(msg).strip()
        if not nombre:
            print("✗ Error: el nombre no puede estar vacío.")
            continue
        if len(nombre) > MAX_NOMBRE:
            print(f"✗ Error: el nombre no puede exceder {MAX_NOMBRE} caracteres.")
            continue
        return nombre

def leer_tiempo_estimado(msg: str) -> int:
    while True:
        texto = input(msg).strip()
        if not texto.isdigit():
            print("✗ Error: ingresa un número entero de minutos.")
            continue
        t = int(texto)
        if t < MIN_TIEMPO or t > MAX_TIEMPO:
            print(f"✗ Error: el tiempo debe estar entre {MIN_TIEMPO} y {MAX_TIEMPO} minutos.")
            continue
        return t

def leer_prioridad(msg: str = "¿Tiene prioridad especial? (si/no): ") -> bool:
    while True:
        v = input(msg).strip().lower()
        if v in ("si", "sí", "s", "true", "1"):
            return True
        if v in ("no", "n", "false", "0"):
            return False
        print("✗ Error: responde 'si' o 'no'.")

def generar_turno(prefijo_fecha: str, consecutivo: int) -> str:
    # Ejemplo: 2025-08-14-0001
    return f"{prefijo_fecha}-{consecutivo:04d}"

# ----------------------------
# Lógica principal
# ----------------------------

def capturar_solicitudes() -> list:
    """Captura por consola y devuelve una lista de dicts con las solicitudes."""
    solicitudes = []
    hoy = datetime.now().strftime("%Y-%m-%d")
    total = leer_entero_positivo("¿Cuántos ciudadanos serán atendidos? ")

    for i in range(1, total + 1):
        print(f"\n--- Captura del ciudadano #{i} ---")
        nombre = leer_nombre("Nombre: ")
        tiempo = leer_tiempo_estimado(
            f"Tiempo estimado en minutos (entre {MIN_TIEMPO} y {MAX_TIEMPO}): "
        )
        prioridad = leer_prioridad()

        solicitud = {
            "turno": generar_turno(hoy, i),
            "nombre": nombre,
            "tiempo": tiempo,
            "prioridad": prioridad,
            "orden_llegada": i,  # para estabilidad del orden
        }
        solicitudes.append(solicitud)

    return solicitudes

def ordenar_solicitudes(solicitudes: list) -> list:
    """
    Ordena:
    1) Prioritarios primero (True > False)
    2) Menor tiempo estimado
    3) Orden de llegada (estable para empates)
    """
    # En Python, True > False, pero para "primero los prioritarios"
    # ordenamos por (-prioridad) o invertimos el booleano:
    # Usamos "not prioridad" para que True vaya primero (False ordena antes).
    return sorted(
        solicitudes,
        key=lambda s: (not s["prioridad"], s["tiempo"], s["orden_llegada"])
    )

def planificar_atencion(solicitudes_ordenadas: list) -> list:
    """
    Genera el plan con inicio, espera y fin para cada solicitud.
    Retorna una lista de dicts con los datos listos para mostrar.
    """
    plan = []
    tiempo_acumulado = 0
    for s in solicitudes_ordenadas:
        inicio = tiempo_acumulado
        espera = inicio
        fin = inicio + s["tiempo"]

        plan.append({
            "turno": s["turno"],
            "nombre": s["nombre"],
            "tiempo": s["tiempo"],
            "prioridad": "Sí" if s["prioridad"] else "No",
            "inicio_min": inicio,
            "espera_min": espera,
            "fin_min": fin,
        })

        tiempo_acumulado = fin

    return plan

def calcular_metricas(plan: list) -> dict:
    total_atencion = sum(item["tiempo"] for item in plan)
    n = len(plan)
    suma_espera = sum(item["espera_min"] for item in plan)
    promedio_espera = (suma_espera / n) if n > 0 else 0.0
    return {
        "total_atencion": total_atencion,
        "promedio_espera": promedio_espera
    }

def mostrar_resultados(plan: list, metricas: dict) -> None:
    print("\n================= LISTA FINAL DE ATENCIÓN =================")
    print(f"{'Turno':<14} {'Nombre':<25} {'Tiempo(min)':>11} {'Prioridad':>10} {'Inicio':>8} {'Espera':>8} {'Fin':>6}")
    print("-" * 90)
    for item in plan:
        print(f"{item['turno']:<14} "
              f"{item['nombre']:<25} "
              f"{item['tiempo']:>11} "
              f"{item['prioridad']:>10} "
              f"{item['inicio_min']:>8} "
              f"{item['espera_min']:>8} "
              f"{item['fin_min']:>6}")
    print("-" * 90)
    print(f"Tiempo total de atención: {metricas['total_atencion']} min")
    print(f"Tiempo promedio de espera: {metricas['promedio_espera']:.2f} min\n")

# ----------------------------
# Punto de entrada
# ----------------------------

def main():
    print("=== Sistema de Citas (pruebas locales) ===")
    print(f"Reglas: el ciudadano ingresa su tiempo; rango permitido: {MIN_TIEMPO}-{MAX_TIEMPO} min.")
    solicitudes = capturar_solicitudes()

    if not solicitudes:
        print("No se capturaron solicitudes.")
        return

    # Simulación de "guardado" en listas (solicitudes originales)
    repositorio_simulado = {
        "solicitudes": solicitudes[:]  # copia superficial
    }

    # Ordenamiento y planificación
    solicitudes_ordenadas = ordenar_solicitudes(repositorio_simulado["solicitudes"])
    plan = planificar_atencion(solicitudes_ordenadas)
    metricas = calcular_metricas(plan)

    # Mostrar resultados
    mostrar_resultados(plan, metricas)

    # Dejar accesible en la "simulación"
    repositorio_simulado["plan"] = plan
    repositorio_simulado["metricas"] = metricas

    # (Opcional) Mostrar el contenido simulado
    # print(repositorio_simulado)

if __name__ == "__main__":
    main()
