# pylint: disable=invalid-name
"""Ejercicio de Word_Count"""

import sys
import time

def read_file(file_name):
    """Lee el archivo y devuelve el contenido como una lista de palabras"""
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            content = file.read()
            words = content.split()  # Dividir el contenido en palabras
            return words
    except FileNotFoundError:
        print(f"Error: El archivo '{file_name}' no se encontró.")
        sys.exit(1)
    except IOError as e:
        print(f"Error de I/O al leer el archivo: {e}")
        sys.exit(1)
    except ValueError as e:
        print(f"Error al procesar los datos del archivo: {e}")
        sys.exit(1)

def count_words(words):
    """Cuenta la frecuencia de cada palabra en la lista de palabras"""
    word_count = {}
    for word in words:
        word = word.lower()  # Convertir a minúsculas por si hay mayúsculas
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count

def write_results(word_count, total_words, elapsed_time):
    """Escribe los resultados en la pantalla y en un archivo"""
    total_unique_words = len(word_count)  # Número total de palabras distintas
    # Ordenar las palabras por frecuencia (de mayor a menor)
    sorted_word_count = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
    # Escribir los resultados en el archivo
    with open('WordCountResults.txt', 'w', encoding='utf-8') as file:
        file.write("Palabra - Frecuencia\n")
        for word, count in sorted_word_count:
            file.write(f"{word} - {count}\n")
        # Escribir el total de palabras diferentes y cantidad de palabras leídas
        file.write(f"\nTotal de palabras leídas: {total_words}\n")
        file.write(f"Total de palabras diferentes: {total_unique_words}\n")
        file.write(f"Tiempo de ejecución: {elapsed_time} segundos\n")
    # Imprimir resultados en la pantalla
    print("Palabra - Frecuencia")
    for word, count in sorted_word_count:
        print(f"{word} - {count}")
    # Imprimir el total de palabras leídas y el total de palabras diferentes
    print(f"\nTotal de palabras leídas: {total_words}")
    print(f"Total de palabras diferentes: {total_unique_words}")
    print(f"Tiempo de ejecución: {elapsed_time} segundos")

def main():
    """Función principal que ejecuta el programa."""
    if len(sys.argv) != 2:
        print("Uso: python wordCount.py <archivo>")
        sys.exit(1)

    file_name = sys.argv[1]

    # Medir el tiempo de ejecución
    start_time = time.time()

    # Leer el archivo
    words = read_file(file_name)
    total_words = len(words)  # Total de palabras leídas

    # Contar las palabras
    word_count = count_words(words)

    # Calcular el tiempo transcurrido
    elapsed_time = time.time() - start_time

    # Escribir los resultados
    write_results(word_count, total_words, elapsed_time)

if __name__ == "__main__":
    main()
