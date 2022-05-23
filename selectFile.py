from csv import reader
import csv
import os

# Carpeta contenedora de los archivo .csv a procesar
path = r'C:\Users\cesar\OneDrive\Escritorio\Processing\CSV'
pathResultado = r'C:\Users\cesar\OneDrive\Escritorio\Processing\NewCSV'
oldMails = []
newMails = []

# Verificar si el directorio esta vacio
if len(os.listdir(path)) == 0:
	print("Directorio vacio")

# Muestra los archivos .csv encontrados
else:
	print("Archivos encontrados:")
	contenido = os.listdir(path)
	i = 0
	for rowfiles in contenido:
		#Para mostrar solo archivos que terminen en .csv y enumerarlos si aplica.
		if os.path.isfile(os.path.join(path, rowfiles)) and rowfiles.endswith('.csv'):
			i+=1
			print(str(i) + ". " + rowfiles)

	# Selecciona un archivo .csv a procesar
	j = int(input("Cual archivo deseas procesar?: ")) - 1
	answer = False
	while (answer == False):
		if(j < i and j >= 0):
			path = path + '\\' + contenido[j]
			with open(path, "r") as csv_file:
				csv_reader = reader(csv_file, delimiter=';')
				list_of_rows = list(csv_reader)

				for row in list_of_rows:
					oldMails.append(row[1])
				print(oldMails)

				domain = input("Dominio solicitado: ")

				for mails in oldMails:
					if mails.endswith(domain):
						newMails.append(mails)
				print(newMails)

			answer = True
		else:
			print("No has seleccionado ningun archivo")
			if (i == 1):
		 		j = int(input("Debes colocar el numero 1: ".format(i))) - 1
			else:
		 		j = int(input("Debes colocar un numero entre 1 y {0}: ".format(i))) - 1


nombrecsv = input("Nombre del nuevo archivo .csv: ") + '.csv'


with open(pathResultado+ "\\" +nombrecsv, 'w') as newcsv:
	fieldnames = ['New Mails']
	writer = csv.DictWriter(newcsv, fieldnames=fieldnames)

	for x in newMails:
		writer.writerow({'New Mails' : x})

print("Proceso realizado correctamente!")