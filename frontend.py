"""
This is a program the store book information:
Title, Author, Year and ISBN

Features:
Users can amongst other things do the following;
1. Add entry 
2. Update records
3. Delete records
4. View all entries
"""
from tkinter import *
import backend

# global selected_tuple     

def get_selected_row(event):
    global selected_tuple  
    try:
        index = list1.curselection()[0]
        selected_tuple = list1.get(index)

        e1.delete(0, END)
        e1.insert(END, selected_tuple[1])
        e2.delete(0, END)
        e2.insert(END, selected_tuple[2])
        e3.delete(0, END)
        e3.insert(END, selected_tuple[3])
        e4.delete(0, END)
        e4.insert(END, selected_tuple[4])
    except IndexError:
        pass

def view_command():
    list1.delete(0, END)
    for row in backend.view():
        list1.insert(END, row)

def search_command():
    list1.delete(0, END)
    for row in backend.search(str_title.get(), str_author.get(), str_year.get(), str_isbn.get()):        
        list1.insert(END, row)

def add_command():
    backend.insert(str_title.get(), str_author.get(), str_year.get(), str_isbn.get())
    list1.delete(0, END)
    list1.insert(END, (str_title.get(), str_author.get(), str_year.get(), str_isbn.get()))

def delete_command():
    backend.delete(selected_tuple[0])

def update_command():
    print(selected_tuple)
    backend.update(selected_tuple[0],str_title.get(), str_author.get(), str_year.get(), str_isbn.get())


window=Tk()

window.wm_title("Sam Book Store")

l1 = Label(window, text="Title")
l1.grid(row=0, column=0)

l2 = Label(window, text="Author")
l2.grid(row=0, column=2)

l3 = Label(window, text="Year")
l3.grid(row=1, column=0)

l4 = Label(window, text="ISBN")
l4.grid(row=1, column=2)

str_title = StringVar()
e1 = Entry(window, textvariable=str_title)
e1.grid(row=0, column=1)

str_author = StringVar()
e2 = Entry(window, textvariable=str_author)
e2.grid(row=0, column=3)

str_year = StringVar()
e3 = Entry(window, textvariable=str_year)
e3.grid(row=1, column=1)

str_isbn = StringVar()
e4 = Entry(window, textvariable=str_isbn)
e4.grid(row=1, column=3)

list1= Listbox(window, height=10, width=35)
list1.grid(row=2, column=0, rowspan=6, columnspan=2)

scroll1 = Scrollbar(window)
scroll1.grid(row=2, column=2, rowspan=6)

list1.configure(yscrollcommand=scroll1.set)
scroll1.configure(command=list1.yview)

list1.bind('<<ListboxSelect>>', get_selected_row)

b1 = Button(window, text="View all", width=12, command=view_command)
b1.grid(row=2, column=3)

b2 = Button(window, text="search entry", width=12, command=search_command)
b2.grid(row=3, column=3)

b3 = Button(window, text="Add entry", width=12, command=add_command)
b3.grid(row=4, column=3)

b4 = Button(window, text="Update", width=12, command=update_command)
b4.grid(row=5, column=3)

b5 = Button(window, text="Delete", width=12, command=delete_command)
b5.grid(row=6, column=3)

b6 = Button(window, text="Close", width=12, command = window.destroy)
b6.grid(row=7, column=3)


window.mainloop()