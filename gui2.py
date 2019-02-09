from tkinter import *
import googlemaps

def distance(event):
	region='RU'
	origins=[e1.get()]
	destinations=[e2.get()]
	gmaps = googlemaps.Client(key='AIzaSyBNtYP55CU8LGJ7Q1oXFToBOxHyPlV7vQw')
	distance_matrix_result = gmaps.distance_matrix(origins=[x+','+region for x in origins], destinations=[x+','+region for x in destinations], language='RU')
	for i in distance_matrix_result['rows']:
		for j in i['elements']:
			d.config(text=(j['distance']['text']))
	Tx.config(state=NORMAL)
	Tx.delete('1.0',END)
	Tx.insert('1.0', distance_matrix_result);
	Tx.config(state=DISABLED)

TT=Tk()
TT.title('Distance')
TT.bind('<Return>', distance)

left=Frame()
left.grid(row=1, column=1)
l1=Label(left, text="Пункт отправления:")
l1.config(font="Arial, 10")
l1.grid(row=1,column=1)
e1 = Entry(left)
e1.config(width=30, font="Arial, 10")
e1.grid(row=2, column=1)
e1.focus()
l2=Label(left, text="Пункт прибытия:")
l2.grid(row=3,column=1)
l2.config(font="Arial, 10")
e2 = Entry(left)
e2.grid(row=4, column=1)
e2.config(width=30, font="Arial, 10")
B=Button(left, text="Расчитать \n расстояние", command=distance)
B.config(font="Arial, 10")
B.grid(row=5, column=1)


right=Frame()
right.grid(row=1, column=2, columnspan=5)
l3=Label(right, text="Расстояние:")
l3.grid(row=1, column=2)
l3.config(font='Arial, 10')
d = Label(right)
d.grid(row=2,column=2)
d.config(font='Arial, 14')
l4=Label(right, text="Логи:")
l4.grid(row=3, column=2)
l4.config(font='Arial, 10')
Tx=Text(right, width=40, height=5, state=DISABLED)
Tx.grid(row=4, column=2)
Tx.config(font="Arial, 10")

mainloop()
