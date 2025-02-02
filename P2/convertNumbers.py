# pylint: disable=invalid-name
"""Ejercicio de Convert_Numbers"""

import sys
import time

def complemento_a_dos(numero, bits=32):
    """Convierte un número negativo en complemento a dos con el número de bits especificado."""
    if numero >= 0:
        return bin(numero)[2:].zfill(bits)  # Para números positivos
    # Para números negativos:
    numero_abs = abs(numero)
    binario = bin(numero_abs)[2:].zfill(bits)  # Representación binaria del valor absoluto
    binario_invertido = ''.join('1' if bit == '0' else '0' for bit in binario)  # Invertir los bits
    complemento_dos = bin(int(binario_invertido, 2) + 1)[2:].zfill(bits)  # Sumar uno
    return complemento_dos

def convertir_a_binario(numero):
    """Convierte un número a binario (usando complemento a dos para números negativos)."""
    if isinstance(numero, (int, float)):  # Verifica que el número sea válido
        return '0b' + complemento_a_dos(numero, 32).lstrip('0') or '0b0'
    return "#VALUE!"  # Si no es un número válido, devuelve #VALUE!

def convertir_a_hexadecimal(numero):
    """Convierte un número a hexadecimal (usando complemento a dos para números negativos)."""
    if isinstance(numero, (int, float)):  # Verifica que el número sea válido
        if numero >= 0:
            hex_val = hex(numero)[2:].upper().zfill(8)  # Para números positivos
        else:
            # Para negativos
            hex_complemento_dos = hex(int(complemento_a_dos(numero, 32), 2))[2:].upper().zfill(8)
            hex_val = hex_complemento_dos
        return '0x' + hex_val.lstrip('0') or '0x0'
    return "#VALUE!"  # Si no es un número válido, devuelve #VALUE!

def leer_archivo(archivo_entrada):
    """Lee el archivo de entrada y maneja los errores de datos no válidos."""
    numeros = []
    errores = []
    with open(archivo_entrada, 'r', encoding='utf-8') as archivo:
        lineas = archivo.readlines()
        for linea in lineas:
            numero = linea.strip()
            if not numero:  # Si está vacío, lo ignoramos
                continue
            try:
                # Intentamos convertir a número, si no se puede lanzará una excepción
                numero_float = float(numero)
                if numero_float.is_integer():  # Si es entero
                    numeros.append(int(numero_float))
                else:  # Si es decimal
                    numeros.append(numero_float)
            except ValueError:
                # Si no es un número, lo agregamos tal cual y guardamos la advertencia
                numeros.append(numero)
                errores.append(f"Advertencia: '{numero}' no es un número válido y será ignorado.")
    return numeros, errores

def imprimir_resultados(numeros, errores, tiempo_ejecucion, archivo_salida):
    """Imprime los resultados en consola y guarda los resultados en un archivo."""
    with open(archivo_salida, 'w', encoding='utf-8') as archivo:
        archivo.write("Resultados de Conversión\n")
        archivo.write("=========================\n")
        for numero in numeros:
            if isinstance(numero, (int, float)):  # Solo convertimos los números válidos
                binario = convertir_a_binario(numero)
                hexadecimal = convertir_a_hexadecimal(numero)
                archivo.write(f"{numero} en binario: {binario} en hexadecimal: {hexadecimal}\n")
                print(f"{numero} en binario: {binario} en hexadecimal: {hexadecimal}")
            else:
                # Si es inválido, lo marcamos como #VALUE!
                binario = "#VALUE!"
                hexadecimal = "#VALUE!"
                archivo.write(f"{numero} en binario: {binario} en hexadecimal: {hexadecimal}\n")
                print(f"{numero} en binario: {binario} en hexadecimal: {hexadecimal}")
        # Imprimir los errores si existen
        if errores:
            archivo.write("\nErrores:\n")
            for error in errores:
                archivo.write(f"{error}\n")
                print(error)
        archivo.write(f"\nTiempo de ejecución: {tiempo_ejecucion} segundos\n")
        print(f"\nTiempo de ejecución: {tiempo_ejecucion} segundos")

def main():
    """Función principal para gestionar la entrada de datos, conversión y mostrar los resultados."""
    if len(sys.argv) != 2:
        print("Uso incorrecto. El formato es: python convertNumbers.py fileWithData.txt")
        sys.exit(1)
    archivo_entrada = sys.argv[1]
    archivo_salida = 'ConvertionResults.txt'

    # Iniciar el cronómetro
    inicio = time.time()

    # Leer datos del archivo
    numeros, errores = leer_archivo(archivo_entrada)

    # Medir el tiempo de ejecución
    fin = time.time()
    tiempo_ejecucion = fin - inicio

    # Imprimir resultados y escribir en archivo
    imprimir_resultados(numeros, errores, tiempo_ejecucion, archivo_salida)

if __name__ == "__main__":
    main()
