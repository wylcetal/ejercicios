""" Realizar una aplicación con interfaz gráfica y con conexión a base de datos con las siguientes características
1. Capacidad de crear la base de datos por medio de botones
2. Una interfaz gráfica con campos para rellenar 
3. Botones de CRUD. Create, Read, Update, Delete
4. Popups al momento de cerrar el programa
5. Sección "Acerca de" y "Ayuda"
6. Campos: ID, nombre, password, apellido, dirección y comentarios.
7. Botón borrar todos los campos
"""

from tkinter import *
from tkinter import messagebox
import sqlite3

global base

base = False

raiz = Tk()
raiz.title("Carga de usuarios")
raiz.geometry("270x350")

frame = Frame(raiz)
frame.pack()



#Funciones----------------------------------------------------------------------

def sql():
	conn = sqlite3.connect('Personas.db')
	cursor = conn.cursor()

def Exit():
	question = messagebox.askquestion("Salir", "Se perderan todos los cambios")
	if question == "yes":
		quit()

def Create_base():
	global base

	try:

		if base == False:
			conn = sqlite3.connect('Personas.db')
			cursor = conn.cursor()

			cursor.execute(""" 
				CREATE TABLE Personas (id INTEGER PRIMARY KEY AUTOINCREMENT, nombre VARCHAR(50),password VARCHAR(50)
				, apellido VARCHAR(50), direccion VARCHAR(100), comentarios VARCHAR(99))
				""")

			base = True
			messagebox.showinfo("Info", "Base de datos creada")
		else:
			messagebox.showinfo("Info", "La base de datos ya existe!")
	except:
		messagebox.showinfo("Info2", "La base de datos ya existe!")

def Insert_into():

	conn = sqlite3.connect('Personas.db')
	cursor = conn.cursor()

	ingreso = (campo_nombre.get(), campo_password.get(), campo_apellido.get(), campo_direccion.get(), text6.get("1.0", "end-1c"))
	print(ingreso)

	cursor.execute("INSERT INTO Personas VALUES (NULL,?,?,?,?,?)", ingreso)
	conn.commit()
	conn.close()

def Read():

	conn = sqlite3.connect('Personas.db')
	cursor = conn.cursor()

	cursor.execute("SELECT * FROM Personas WHERE id=?", (campo_ID.get(),))
	Datos = cursor.fetchall()
	Erase_all()
	entry1.insert(0, Datos[0][0])
	entry2.insert(0, Datos[0][1])
	entry3.insert(0, Datos[0][2])
	entry4.insert(0, Datos[0][3])
	entry5.insert(0, Datos[0][4])
	text6.insert("1.0", Datos[0][5])

def Update():

	conn = sqlite3.connect('Personas.db')
	cursor = conn.cursor()


	if campo_nombre.get() != "":
		cursor.execute("UPDATE Personas SET nombre=? WHERE id=?", (campo_nombre.get(), campo_ID.get()))
	if campo_password.get() != "":
		cursor.execute("UPDATE Personas SET password=? WHERE id=?", (campo_password.get(), campo_ID.get()))
	if campo_apellido.get() != "":
		cursor.execute("UPDATE Personas SET apellido=? WHERE id=?", (campo_apellido.get(), campo_ID.get()))
	if campo_direccion.get() != "":
		cursor.execute("UPDATE Personas SET direccion=? WHERE id=?", (campo_direccion.get(), campo_ID.get()))
	if text6.get("1.0", "end-1c") != "":
		cursor.execute("UPDATE Personas SET comentarios=? WHERE id=?", (text6.get("1.0", "end-1c"), campo_ID.get()))


	conn.commit()
	conn.close()

def Delete():
	if campo_ID != "":

		conn = sqlite3.connect('Personas.db')
		cursor = conn.cursor()

		cursor.execute("DELETE FROM Personas WHERE id=?", (campo_ID.get(),))

		campo_nombre.set("")
		campo_password.set("")
		campo_apellido.set("")
		campo_direccion.set("")
		text6.delete("1.0", "end-1c")

		conn.commit()
		conn.close()



def Erase_all():
	campo_ID.set("")
	campo_nombre.set("")
	campo_password.set("")
	campo_apellido.set("")
	campo_direccion.set("")
	text6.delete("1.0", "end-1c")





#Menú---------------------------------------------------------------------------
barra_menu = Menu(raiz)
raiz.config(menu=barra_menu)

bbdd_menu = Menu(barra_menu, tearoff=0)
barra_menu.add_cascade(label="BBDD", menu=bbdd_menu)
bbdd_menu.add_command(label="Conetar", command=lambda:Create_base())
bbdd_menu.add_command(label="Salir", command=lambda:Exit())

borrar_menu = Menu(barra_menu, tearoff=0)
barra_menu.add_cascade(label="Borrar", menu=borrar_menu)
borrar_menu.add_command(label="Borrar campos", command=lambda:Erase_all())

crud_menu = Menu(barra_menu, tearoff=0)
barra_menu.add_cascade(label="CRUD", menu=crud_menu)
crud_menu.add_command(label="Crear", command=lambda:Insert_into())
crud_menu.add_command(label="Leer", command=lambda:Read())
crud_menu.add_command(label="Actualizar", command=lambda:Update())
crud_menu.add_command(label="Borrar", command=lambda:Delete())

ayuda_menu = Menu(barra_menu, tearoff=0)
barra_menu.add_cascade(label="Ayuda", menu=ayuda_menu)
ayuda_menu.add_command(label="Licencia", command=lambda:messagebox.showinfo("Licencia", "Software libre para todos..."))
ayuda_menu.add_command(label="Acerca de...", command=lambda:messagebox.showinfo("Acerca de:", "Mini registro de usuarios V 0.1"))

#campo_ID-----------------------------------------------------------------------
campo_ID = StringVar()
label1= Label(frame, text="ID: ")
label1.grid(row=1, column=1)
entry1 = Entry(frame, textvariable=campo_ID)
entry1.grid(row=1, column=2, padx=10, pady=10, columnspan=3)
#campo_nombre-------------------------------------------------------------------
campo_nombre = StringVar()
label2= Label(frame, text="Nombre: ")
label2.grid(row=2, column=1)
entry2 = Entry(frame, textvariable=campo_nombre)
entry2.grid(row=2, column=2, padx=10, pady=10, columnspan=3)
#campo_password-----------------------------------------------------------------
campo_password = StringVar()
label3= Label(frame, text="Password: ")
label3.grid(row=3, column=1)
entry3 = Entry(frame, textvariable=campo_password)
entry3.grid(row=3, column=2, padx=10, pady=10, columnspan=3)
entry3.config(show="*")
#campo_apellido-----------------------------------------------------------------
campo_apellido = StringVar()
label4= Label(frame, text="Apellido: ")
label4.grid(row=4, column=1)
entry4 = Entry(frame, textvariable=campo_apellido)
entry4.grid(row=4, column=2, padx=10, pady=10, columnspan=3)
#campo_direccion----------------------------------------------------------------
campo_direccion = StringVar()
label5= Label(frame, text="Dirección: ")
label5.grid(row=5, column=1)
entry5 = Entry(frame, textvariable=campo_direccion)
entry5.grid(row=5, column=2, padx=10, pady=10, columnspan=3)
#campo_comentarios--------------------------------------------------------------
#campo_comentarios = StringVar()
label6= Label(frame, text="Comentarios: ")
label6.grid(row=6, column=1)
text6 = Text(frame, width=15, height=5)
text6.grid(row=6, column=2, padx=10, pady=10, columnspan=3)
scroll = Scrollbar(frame, command=text6.yview)
scroll.grid(row=6, column=4) #Arreglar el scrollbar



#Botones------------------------------------------------------------------------

button_create = Button(frame, text="Create", command=lambda:Insert_into())
button_create.grid(row=7, column=1)

button_read = Button(frame, text="Read", command=lambda:Read())
button_read.grid(row=7, column=2, padx=10, pady=10)

button_update = Button(frame, text="Update", command=lambda:Update())
button_update.grid(row=7, column=3, padx=10, pady=10)

button_delete = Button(frame, text="Delete", command=lambda:Delete())
button_delete.grid(row=7, column=4, padx=10, pady=10)



raiz.mainloop()
