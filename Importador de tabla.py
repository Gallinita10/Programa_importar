import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from tkinter import filedialog as fd
import pandas as pd
import pyodbc
import openpyxl

# root window
root = tk.Tk()
root.geometry('300x200')
root.resizable(False, False)
root.title('Importador de datos')

def select_file():
    
    filetypes = (
        ('excel files','*.csv'),
        ('excel files','*.xlsx'),
        ('text files', '*.txt'),
        ('All files', '*.*')
    )

    #abre explorador de archivos
    filename = fd.askopenfilename(
        title='Open a file',
        initialdir='/',
        filetypes=filetypes)

    #mensajito de archivo seleccionado
    showinfo(
        title='Selected File',
        message=filename
    )
    return filename

# download button
def download_clicked():
    
    arch = select_file()


    # Importar excel/CSV
    data = pd.read_excel (arch)   
    df = pd.DataFrame(data)
    #crea boton que al apretarlo ejecute todo este script siguiente
    # Connectar a SQL Server
    conn = pyodbc.connect('Driver={SQL Server};'
                          'Server=DESKTOP-JCF2VOL\SQLEXPRESS;'
                          'Database=Alumnos;'
                          'Trusted_Connection=yes;')
    cursor = conn.cursor()
    # Crea la Tabla
    cursor.execute('''
                    CREATE TABLE fichas (
                            DNI nvarchar(255) primary key,
                            Nombre_Alumno nvarchar(255),
                            Celular nvarchar(255),
                Mail nvarchar(255),
                Fecha_de_Nacimiento nvarchar(255),
                Ciudad_de_Residencia nvarchar(255),
                Provincia_de_Residencia nvarchar(255),
                Pais_de_Residencia nvarchar(255),
                Ciudad_de_Nacimiento nvarchar(255),
                Provincia_de_Nacimiento nvarchar(255),
                Pais_de_Nacimiento nvarchar(255),
                Estado_Civil nvarchar(255),
                Trabaja nvarchar(255),
                Obra_Social nvarchar(255),
                Nombre_Obra_Social nvarchar(255)
                            )
                '''
            )
    # Arma un dataframe con lo que haya en el excel y lo inserta a la tabla
    for row in df.itertuples():
        cursor.execute('''
                        INSERT INTO fichas (DNI, Nombre_Alumno, Celular, Mail, Fecha_de_Nacimiento, Ciudad_de_Residencia, Provincia_de_Residencia, Pais_de_Residencia, Ciudad_de_Nacimiento, Provincia_de_Nacimiento, Pais_de_Nacimiento, Estado_Civil, Trabaja, Obra_Social, Nombre_Obra_Social)
                        VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
                        ''',
                        row.DNI, 
                        row.Nombre_Alumno,
                        row.Celular,
                        row.Mail,
                        row.Fecha_de_Nacimiento,
                        row.Ciudad_de_Residencia,
                        row.Provincia_de_Residencia,
                        row.Pais_de_Residencia,
                        row.Ciudad_de_Nacimiento,
                        row.Provincia_de_Nacimiento,
                        row.Pais_de_Nacimiento,
                        row.Estado_Civil,
                        row.Trabaja,
                        row.Obra_Social,
                        row.Nombre_Obra_Social
                    )
    conn.commit()

    
    showinfo(
        title='Information',
        message='TRANSFERENCIA EXITOSA'
    )


# al apretar
download_button = ttk.Button(
    root,
    command=download_clicked
)
download_button.config(text="Importar archivo")

#posicion y tamano
download_button.pack(
    ipadx=5,
    ipady=5,
    expand=True
)

#inicio
root.mainloop()
