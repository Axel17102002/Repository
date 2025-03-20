import random
import string
import sys

# Preguntas para el juego
questions = [
    "¿Qué función se usa para obtener la longitud de una cadena en Python?",
    "¿Cuál de las siguientes opciones es un número entero en Python?",
    "¿Cómo se solicita entrada del usuario en Python?",
    "¿Cuál de las siguientes expresiones es un comentario válido en Python?",
    "¿Cuál es el operador de comparación para verificar si dos valores son iguales?",
]

# Respuestas posibles para cada pregunta, en el mismo orden que las preguntas
answers = [
    ("size()", "len()", "length()", "count()"),
    ("3.14", "'42'", "10", "True"),
    ("input()", "scan()", "read()", "ask()"),
    ("// Esto es un comentario", "/* Esto es un comentario */", "-- Esto es un comentario", "# Esto es un comentario"),
    ("=", "==", "!=", "==="),
]

# Índice de la respuesta correcta para cada pregunta, en el mismo orden que las preguntas
correct_answers_index = [1, 2, 0, 3, 1]
score = 0
questions_to_ask = random.choices(list(zip(questions, answers, correct_answers_index)), k=3)

for i in range(3):
    print(questions_to_ask[i][0])  # Imprime la preguntagit 
    for a in range(len(questions_to_ask[i][1])):  # Calcula `la cantidad de respuestas a imprimir len()`
        print(f"{a + 1}. {questions_to_ask[i][1][a]}")  # Imprime respuestas numeradas
    
    # El usuario tiene 2 intentos para responder correctamente
    for intento in range(2):
        user_answer = input("Respuesta: ")
        if user_answer.isdigit(): #Verificamos que se este ingresando un numero
            user_answer = int(user_answer) - 1 # Convertimos a entero y ajustamos el índice
            if user_answer < 0 or user_answer >= len(questions_to_ask[i][1]): #Verifico que la respuesta este dentro del rango
                print("Respuesta no valida. ")
                sys.exit(1) # Terminamos el programa con exit status 1
        else:
            print("Respuesta no valida.")
            sys.exit(1) # Terminamos el programa con exit status 1
        # Se verifica si la respuesta es correcta
        if user_answer == questions_to_ask[i][2]:
            print("¡Correcto!")
            score += 1
            break
        else: 
            print("Respuesta incorrecta.")
            if score > 0:
                score -= 0.5
    else:
         # Si el usuario no responde correctamente después de 2 intentos,
         # se muestra la respuesta correcta
         print("Incorrecto. La respuesta correcta es:")
         print(questions_to_ask[i][1][questions_to_ask[i][2]])
    # Se imprime un blanco al final de la pregunta
    print()
#Se imprime el puntaje
print("El puntaje fue: ",score)