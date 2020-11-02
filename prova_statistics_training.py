######################################################
# Program to collect and analyse data from trainings #
######################################################
import numpy as np

######################TEST CODE######################
exer = "4x15w10.0"

for symbol in exer:
	if symbol == "w":
		print("\nL'esercizio è stato eseguito con pesi!\n")
		series_n = exer[0]
		rep_n    = exer[2:4]
		weight   = exer[-4:]
print(f"Sono state eseguite {series_n} serie da {rep_n} ripetizioni,\nutilizzando un peso da {weight} kg.\n")
#####################################################