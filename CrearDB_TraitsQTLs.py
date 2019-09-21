# Generación de la base de datos TaitsQTLs_Genetica
# en MySQL con uso de python y un archivo .csv
# Arturo Garcia Cerrillo

import mysql.connector
import pandas as pd
import math

#Conexión con MySQL
mydb = mysql.connector.connect(
	host="localhost",
	user="root",
	passwd="genoma123",
	port = '3306',
	database = "TraitsQTLs_Genetica"
	)

mycursor = mydb.cursor()

#Creacion de tablas en la base de datos TraitsQTLs_Genetica
sqlDatosGenerales = "CREATE TABLE DatosGenerales ( \
    persona_id INT AUTO_INCREMENT PRIMARY KEY, \
	nombre VARCHAR(255), \
	sexo CHAR(1),\
	edad INT(2), \
	estado  VARCHAR(10)\
	)"
sqlMediciones = "CREATE TABLE Mediciones ( \
	medicion_id INT AUTO_INCREMENT PRIMARY KEY, \
	tipo VARCHAR(20), \
	medida FLOAT, \
	persona_id INT, \
	CONSTRAINT persona_fk \
	FOREIGN KEY (persona_id) \
	REFERENCES DatosGenerales(persona_id) \
	)"

mycursor.execute(sqlDatosGenerales)
mycursor.execute(sqlMediciones)
mycursor.execute("SHOW TABLES")
for x in mycursor:
		print(x)

#Almacenamiento del archivo .csv con el uso de pandas
data = pd.read_csv('Mediciones2.csv')
d = data.iloc[:,:]
val = []
sql = "INSERT INTO DatosGenerales (Nombre, Sexo, Edad, Estado) VALUES (%s, %s, %s, %s)"
sqlmed ="INSERT INTO Mediciones (tipo,medida,persona_id) VALUES (%s, %s, %s)"

for row in d.iterrows():

	# Variable para ingresar datos en la tabla de MySQL
	val_cus = list(row[1][0:4])
	mycursor.execute(sql, val_cus)

	# Valor de la altura para cada individuo
	altura = row[1][4]
	val = [["altura",altura,row[0]+1]]

	# Valores del calzado para cada individuo
	calzado = row[1][17]
	val.append(["calzado",calzado,row[0]+1])

	# Valores de presión sistólica para cada individuo
	Sistole = row[1][18]
	val.append(["Presion_sistole",Sistole,row[0]+1])

	# Valores de presión diastólica para cada individuo
	Diastole = row[1][19]
	val.append(["Presion_diastole",Diastole,row[0]+1])

	# Valores de la frente para cada individuo
	medic_frente = list(row[1][5:10])

	for i in medic_frente:
		if math.isnan(i):
			print ("No hay medicion de frente")
		else:
			val.append(["frente",i,row[0]+1])

	# Valores del brazo para cada individuo
	medic_brazo = list(row[1][11:16])

	for ii in medic_brazo:
	    if math.isnan(ii):
	        print ("No hay medicion de brazo")
	    else:
	        val.append(["brazo",ii,row[0]+1])

	mycursor.executemany(sqlmed, val)


#Commit para llevar a cabo los cambios
mydb.commit()
print(mycursor.rowcount, "record inserted.")

# Fin del codigo

