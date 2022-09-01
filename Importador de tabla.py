import pandas as pd
import pyodbc
from tkinter import *

# Import CSV
data = pd.read_csv (r'C:\Users\Enzo\Desktop\Escuela\Tercer año\Gestión de base de datos\Programa importar\Ficha Alumnos.xlsx')   
df = pd.DataFrame(data)

# Connect to SQL Server
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-1PSC1H3\SQLEXPRESS;'
                      'Database=Alumnos;'
                      'Trusted_Connection=yes;')
cursor = conn.cursor()

# Create Table
cursor.execute('''
		CREATE TABLE fichas (
			DNI float primary key,
			Nombre_Alumno nvarchar(255),
			Celular float,
            Mail nvarchar(255),
            Fecha_de_nacimiento datetime,
            Ciudad_de_Residencia nvarchar(255),
            Provincia_de_Residencia nvarchar(255),
            Pais_de_Residencia nvarchar(255),
            Ciudad_de_nacimiento nvarchar(255),
            Provincia_de_nacimiento nvarchar(255),
            Pais_de_Nacimiento nvarchar(255),
            Estado_Civil nvarchar(255),
            Trabaja nvarchar(255),
            Obra_Social nvarchar(255),
            Nombre_Obra_Social nvarchar(255)

			)
               ''')

# Insert DataFrame to Table
for row in df.itertuples():
    cursor.execute('''
                INSERT INTO fichas (DNI, Nombre_Alumno, Celular, Mail, Fecha_de_nacimiento, Ciudad_de_Residencia, Provincia_de_Residencia, Pais_de_Residencia, Ciudad_de_nacimiento, Provincia_de_nacimiento, Pais_de_Nacimiento, Estado_Civil, Trabaja, Obra_Social, Nombre_Obra_Social)
                VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
                ''',
                row.DNI, 
                row.Nombre_Alumno,
                row.Celular,
                row.Mail,
                row.Fecha_de_nacimiento,
                row.Ciudad_de_Residencia,
                row.Provincia_de_Residencia,
                row.Pais_de_Residencia,
                row.Ciudad_de_nacimiento,
                row.Provincia_de_nacimiento,
                row.Pais_de_Nacimiento,
                row.Estado_Civil,
                row.Trabaja,
                row.Obra_Social,
                row.Nombre_Obra_Social

                )
conn.commit()