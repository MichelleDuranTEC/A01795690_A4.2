# pylint: disable=invalid-name
"""Ejercicio de Compute_Statistics"""

import sys
import time

def leer_archivo(archivo):
    """Lee el archivo y retorna una lista de números, manejando errores de datos inválidos."""
    datos = []
    errores = 0  # Contador de los valores inválidos
    total_lineas = 0  # Contador total de líneas (válidas + inválidas)
    with open(archivo, 'r', encoding="utf-8") as file:
        for linea in file:
            total_lineas += 1  # Contamos todas las líneas (válidas e inválidas)
            try:
                # Intentamos convertir cada valor a float
                numero = float(linea.strip())
                datos.append(numero)
            except ValueError:
                # Si no se puede convertir a número, se muestra un mensaje
                print(f"Advertencia: '{linea.strip()}' no es un número válido y será ignorado.")
                errores += 1
    return datos, errores, total_lineas

def calcular_estadisticas(datos):
    """Calcula conteo, media, mediana, moda, desviación estándar y varianza muestral."""
    # Conteo (solo se cuenta el total de datos válidos)
    n = len(datos)
    if n == 0:
        return "No se puede calcular estadísticas para un conjunto vacío de datos."
    # Media
    media = sum(datos) / n
    # Mediana
    datos_ordenados = sorted(datos)
    if n % 2 == 0:
        mediana = (datos_ordenados[n//2 - 1] + datos_ordenados[n//2]) / 2
    else:
        mediana = datos_ordenados[n//2]
    # Moda
    frecuencia = {}
    for num in datos:
        if num in frecuencia:
            frecuencia[num] += 1
        else:
            frecuencia[num] = 1
    # Encontrar el número con mayor frecuencia
    max_frecuencia = max(frecuencia.values())
    moda = [num for num, freq in frecuencia.items() if freq == max_frecuencia]
    # Si no hay moda (todos los números tienen la misma frecuencia)
    if len(moda) == len(frecuencia):
        moda = "#N/A"  # No hay una moda
    else:
        # Tomamos solo el primer número con la máxima frecuencia
        moda = moda[0]

    # Desviación estándar
    varianza = sum((x - media) ** 2 for x in datos) / (n - 1)
    desviacion_estandar = varianza ** 0.5
    # Varianza muestral
    varianza_muestral = varianza

    return {
        'conteo': n,
        'media': media,
        'mediana': mediana,
        'moda': moda,
        'desviacion_estandar': desviacion_estandar,
        'varianza_muestral': varianza_muestral
    }

def imprimir_resultados(estadisticas, tiempo, archivo_salida, errores, total_lineas):
    """Imprime los resultados en pantalla y los guarda en el archivo de resultados."""
    resultados = f"""
    Estadísticas Descriptivas:
    Conteo: {total_lineas} (Incluyendo {errores} valores no válidos)
    Media: {estadisticas['media']}
    Mediana: {estadisticas['mediana']}
    Moda: {estadisticas['moda']}
    Desviación estándar: {estadisticas['desviacion_estandar']}
    Varianza muestral: {estadisticas['varianza_muestral']}
    
    Tiempo de ejecución: {tiempo} segundos
    """

    print(resultados)
    # Guardar resultados en el archivo de salida
    with open(archivo_salida, 'w', encoding="utf-8") as file:
        file.write(resultados)

def main():
    """Función principal que ejecuta el programa."""
    if len(sys.argv) != 2:
        print("Uso incorrecto. El formato es: python computeStatistics.py fileWithData.txt")
        sys.exit(1)

    archivo_entrada = sys.argv[1]
    archivo_salida = "StatisticsResults.txt"

    # Iniciar el cronómetro
    inicio = time.time()

    # Leer datos del archivo
    datos, errores, total_lineas = leer_archivo(archivo_entrada)

    # Calcular estadísticas
    estadisticas = calcular_estadisticas(datos)

    # Medir el tiempo transcurrido
    fin = time.time()
    tiempo_ejecucion = fin - inicio

    # Imprimir y guardar resultados
    imprimir_resultados(estadisticas, tiempo_ejecucion, archivo_salida, errores, total_lineas)

if __name__ == "__main__":
    main()
