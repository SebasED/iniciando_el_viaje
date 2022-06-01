"""
A  partir  del  ejercicio  anterior,  crea  un  programa  para  calcular  la  nota  final  de  un 
estudiante  universitario.  Para  ello,  el  usuario  debe  ingresar  3  notas  y  el  valor 
porcentual de cada nota, realiza y devuelve la media por pantalla.
"""

# Code for saving the scores and percentages in variables
score_1 = float(input("Type the score 1: \n"))
percentage_1 = float(input("Type the percentage for score 1: \n"))
score_2 = float(input("Type the score 2: \n"))
percentage_2 = float(input("Type the percentage for score 2: \n"))
score_3 = float(input("Type the score 3: \n"))
percentage_3 = float(input("Type the percentage for score 3: \n"))

# Calculate the stundent's final score
final_score = (score_1 * (percentage_1/100)) + (score_2 * (percentage_2/100)) + (score_3 * (percentage_3/100))

# Print result
print(f"The final score is: {final_score}")