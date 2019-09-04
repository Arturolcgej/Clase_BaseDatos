# Bioinformática
# Arturo García Cerrillo


# Programa de transcripción de una secuencia de DNA a RNA y posterior traducción a un polipéptido

# Translation.py

import sys # Uso del modulo sys para pasar la secuencia como parametro



Seq_User = sys.argv[1]	# Funcion para pasar las secuencias por parametro desde shell

Seq_User = Seq_User.upper() # Pasando a mayusculas

Length = len(Seq_User)		# Almacena longitud de cadena

Traduce = 1

if Length < 3:

	print("\nSu secuencia debe tener al menos 3 nucleotidos.\n")

	Traduce = 0

Seq_Program = ""  #Inicializamos con un vacio la variable que almacenara el string

print("\nLa secuencia introducida tiene ", Length," nucleotidos.\n")


# Analisis de la secuencia introducida

Contador_cadena = 0

# Paso a RNA si necesario

for Contador_cadena in range(0, Length):

	Seq_Program += Seq_User[Contador_cadena]

	if Seq_User[Contador_cadena] == "T":

		Seq_Program = Seq_Program[:-1]

		Seq_Program += "U"

	#print(Seq_Program[Contador_cadena])

	# Esta parte del codigo sirve para verificar que no haya otras letras distintas a A, C, T, G y U
	# (en desarrollo)

	#elif Seq_User[Contador_cadena] != "A":

	#	 if Seq_User[Contador_cadena] != "T":

	#	 	 if Seq_User[Contador_cadena] != "C":

	#	 	 	if Seq_User[Contador_cadena] != "G":

	#	 	 		if Seq_User[Contador_cadena] != "U":

	#					print("\n ERROR. La secuencia solo debe contener las bases A,T,C,G,U")

	#					Contador_cadena = -2

	#					break


if (Traduce):

	Proteina = "Polipeptido: "  

	#Traduccion
	Contador_cadena = 0

	while Contador_cadena <= Length-3:


		# Codones con U

		if Seq_Program[Contador_cadena] == "U":

			if Seq_Program[Contador_cadena+1] == "U":

				if (Seq_Program[Contador_cadena+2] == "U") or (Seq_Program[Contador_cadena+2] == "C"):

					Proteina += "Phe-"

					Contador_cadena += 3

				elif (Seq_Program[Contador_cadena+2] == "A") or (Seq_Program[Contador_cadena+2] == "G"):

					Proteina += "Leu-"

					Contador_cadena += 3


			elif Seq_Program[Contador_cadena+1] == "C":

				if (Seq_Program[Contador_cadena+2] == "U") or (Seq_Program[Contador_cadena+2] == "C") or (Seq_Program[Contador_cadena+2] == "A") or (Seq_Program[Contador_cadena+2] == "G"):

					Proteina += "Ser-"

					Contador_cadena += 3

			elif Seq_Program[Contador_cadena+1] == "A":

				if (Seq_Program[Contador_cadena+2] == "U") or (Seq_Program[Contador_cadena+2] == "C"):
					
					Proteina += "Tyr-"

					Contador_cadena += 3

				elif (Seq_Program[Contador_cadena+2] == "A") or (Seq_Program[Contador_cadena+2] == "G"):

					Proteina += "STOP\n"

					Contador_cadena += 3

			elif Seq_Program[Contador_cadena+1] == "G":

				if (Seq_Program[Contador_cadena+2] == "U") or (Seq_Program[Contador_cadena+2] == "C"):
					
					Proteina += "Cys-"

					Contador_cadena += 3

				elif (Seq_Program[Contador_cadena+2] == "A"):

					Proteina += "STOP\n"

					Contador_cadena += 3

				elif (Seq_Program[Contador_cadena+2] == "G"):
					
					Proteina += "Trp-"

					Contador_cadena += 3


		# Codones con C

		elif Seq_Program[Contador_cadena] == "C":

			if Seq_Program[Contador_cadena+1] == "U":

				if (Seq_Program[Contador_cadena+2] == "U") or (Seq_Program[Contador_cadena+2] == "C") or (Seq_Program[Contador_cadena+2] == "A") or (Seq_Program[Contador_cadena+2] == "G"):

					Proteina += "Leu-"

					Contador_cadena += 3


			elif Seq_Program[Contador_cadena+1] == "C":

				if (Seq_Program[Contador_cadena+2] == "U") or (Seq_Program[Contador_cadena+2] == "C") or (Seq_Program[Contador_cadena+2] == "A") or (Seq_Program[Contador_cadena+2] == "G"):

					Proteina += "Pro-"

					Contador_cadena += 3

			elif Seq_Program[Contador_cadena+1] == "A":

				if (Seq_Program[Contador_cadena+2] == "U") or (Seq_Program[Contador_cadena+2] == "C"):
					
					Proteina += "His-"

					Contador_cadena += 3

				elif (Seq_Program[Contador_cadena+2] == "A") or (Seq_Program[Contador_cadena+2] == "G"):

					Proteina += "Gln-"

					Contador_cadena += 3

			elif SSeq_Program[Contador_cadena+1] == "G":

				if (Seq_Program[Contador_cadena+2] == "U") or (Seq_Program[Contador_cadena+2] == "C") or (Seq_Program[Contador_cadena+2] == "A") or (Seq_Program[Contador_cadena+2] == "G"):

					Proteina += "Arg-"

					Contador_cadena += 3


		# Codones con A

		elif Seq_Program[Contador_cadena] == "A":

			if Seq_Program[Contador_cadena+1] == "U":

				if (Seq_Program[Contador_cadena+2] == "U") or (Seq_Program[Contador_cadena+2] == "C") or (Seq_Program[Contador_cadena+2] == "A"):

					Proteina += "Ile-"

					Contador_cadena += 3

				elif (Seq_Program[Contador_cadena+2] == "G"):

					Proteina += "Met-"

					Contador_cadena += 3


			elif Seq_Program[Contador_cadena+1] == "C":

				if (Seq_Program[Contador_cadena+2] == "U") or (Seq_Program[Contador_cadena+2] == "C") or (Seq_Program[Contador_cadena+2] == "A") or (Seq_Program[Contador_cadena+2] == "G"):

					Proteina += "Thr-"

					Contador_cadena += 3

			elif Seq_Program[Contador_cadena+1] == "A":

				if (Seq_Program[Contador_cadena+2] == "U") or (Seq_Program[Contador_cadena+2] == "C"):
					
					Proteina += "Asn-"

					Contador_cadena += 3

				elif (Seq_Program[Contador_cadena+2] == "A") or (Seq_Program[Contador_cadena+2] == "G"):

					Proteina += "Lys-"

					Contador_cadena += 3

			elif Seq_Program[Contador_cadena+1] == "G":

				
				if (Seq_Program[Contador_cadena+2] == "U") or (Seq_Program[Contador_cadena+2] == "C"):
				
					Proteina += "Ser-"

					Contador_cadena += 3

				elif (Seq_Program[Contador_cadena+2] == "A") or (Seq_Program[Contador_cadena+2] == "G"):

					Proteina += "Arg-"

					Contador_cadena += 3


		# Codones con G

		elif Seq_Program[Contador_cadena] == "G":

			if Seq_Program[Contador_cadena+1] == "U":

				if (Seq_Program[Contador_cadena+2] == "U") or (Seq_Program[Contador_cadena+2] == "C") or (Seq_Program[Contador_cadena+2] == "A") or (Seq_Program[Contador_cadena+2] == "G"):

					Proteina += "Val-"

					Contador_cadena += 3


			elif Seq_Program[Contador_cadena+1] == "C":

				if (Seq_Program[Contador_cadena+2] == "U") or (Seq_Program[Contador_cadena+2] == "C") or (Seq_Program[Contador_cadena+2] == "A") or (Seq_Program[Contador_cadena+2] == "G"):

					Proteina += "Ala-"

					Contador_cadena += 3

			elif Seq_Program[Contador_cadena+1] == "A":

				if (Seq_Program[Contador_cadena+2] == "U") or (Seq_Program[Contador_cadena+2] == "C"):
					
					Proteina += "Asp-"

					Contador_cadena += 3

				elif (Seq_Program[Contador_cadena+2] == "A") or (Seq_Program[Contador_cadena+2] == "G"):

					Proteina += "Glu-"

					Contador_cadena += 3

			elif Seq_Program[Contador_cadena+1] == "G":

				if (Seq_Program[Contador_cadena+2] == "U") or (Seq_Program[Contador_cadena+2] == "C") or (Seq_Program[Contador_cadena+2] == "A") or (Seq_Program[Contador_cadena+2] == "G"):

					Proteina += "Gly-"

					Contador_cadena += 3


	# Impresion de resultados

	print("...RESULTADO...\n")

	print("Su secuencia codifica el siguiente polipeptido: \n\n", Proteina,"\n")



# FIN DEL PROGRAMA
