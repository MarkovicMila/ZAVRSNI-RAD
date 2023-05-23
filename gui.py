from tkinter import *
from klasa import *


root=Tk()
root.title("Turisticka agencija")

def export():
    t=Toplevel(root)

    csv_button=Button(t,text="CSV",command=lambda:a.export('csv')).grid(row=0,column=0)
    excel_button=Button(t,text="Excel",command=lambda:a.export('excel')).grid(row=0,column=1)

def izbor_broja_lezajeva(destinacija):
    t=Toplevel(root)
    
    var1 = IntVar(t) 
    var1.set("dvokrevetna") 
    r1=Radiobutton(t, text="dvokrevetna", variable=var1, value=2)
    r2=Radiobutton(t, text="trokrevetna", variable=var1, value=3)

    r1.grid(row=0,column=0)
    r2.grid(row=1,column=0)

    b_broj_lezajeva=Button(t,text="Izbor broja lezajeva",command=lambda:a.destinacija_broj_lezajeva(destinacija,var1.get()))
    b_broj_lezajeva.grid(row=2,column=0)

def izaberi_agenciju():
    t=Toplevel(root)
    
    var1 = StringVar(t) 
    var1.set("Balkan Fun") 
    r1=Radiobutton(t, text="Balkan Fun", variable=var1, value="Balkan Fun")
    r2=Radiobutton(t, text="Puzzle Group", variable=var1, value="Puzzle Group")
    r3=Radiobutton(t, text="Go2 Travelling", variable=var1, value="Go2 Travelling")
    r4=Radiobutton(t, text="Rapsody Travel", variable=var1, value="Rapsody Travel")
    

    r1.grid(row=0,column=0)
    r2.grid(row=1,column=0)
    r3.grid(row=2,column=0)
    r4.grid(row=3,column=0)


    b_agencija=Button(t,text="Izaberi agenciju",command=lambda:a.export_agencija(var1.get()))
    b_agencija.grid(row=4,column=0)


destinacija=a.listbox()
listbox=Listbox(root)
for i in range(len(destinacija)):
    listbox.insert(i,destinacija[i])

listbox.grid(row=0,column=0)

listbox.config(height=listbox.size())

b_destinacije=Button(root,text="Izbor destinacije",command=lambda:izbor_broja_lezajeva(listbox.get(listbox.curselection())))
b_destinacije.grid(row=listbox.size(),column=0)


b_agencija=Button(root,text="Pogledaj podatke za agenciju",height=3,command=lambda:izaberi_agenciju())
b_agencija.grid(row=1,column=1)


b_export=Button(root,text="Export",command=lambda:export())
b_export.grid(row=0,column=1)


mainloop()