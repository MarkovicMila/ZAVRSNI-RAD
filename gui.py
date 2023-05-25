from tkinter import *
from klasa import *


root=Tk()
root.title("Turisticka agencija")
root.geometry('251x450')
icon=PhotoImage(file='autobus.png')
root.iconphoto(True,icon)
def quit(text):
    pyauto.alert(text)
    return root.quit()
def export():
    t=Toplevel(root)

    csv_button=Button(t,text="CSV",command=lambda:[a.export('csv'),quit('Formiran je csv file sa svim aranzmanima! Ok za izlazak')])
    csv_button.grid(row=0,column=0)
    csv_button.config(width=7)
    

    excel_button=Button(t,text="Excel",command=lambda:[a.export('excel'),quit('Formiran je excel file sa svim aranzmanima! Ok za izlazak')])
    excel_button.grid(row=0,column=1)
    excel_button.config(width=7)


def izbor_broja_lezajeva_dodatnih_opcija(destinacija):
    t=Toplevel(root)

    var1 = StringVar(t) 
    var1.set("dvokrevetna") 
    r1=Radiobutton(t, text="dvokrevetna", variable=var1, value='dvokrevetna')
    r2=Radiobutton(t, text="trokrevetna", variable=var1, value='trokrevetna')

    r1.grid(row=0,column=0)
    r1.config(anchor=W)
    r2.grid(row=1,column=0)
    r2.config(anchor=W)

    var2 = StringVar(t) 
    var2.set("Organizovani polazak") 
    r3=Radiobutton(t, text="Organizovani polazak", variable=var2, value='Organizovani polazak')
    r4=Radiobutton(t, text="Individualni polazak", variable=var2, value='Individualni polazak')

    r3.grid(row=2,column=0)
    r3.config(anchor=W)
    r4.grid(row=3,column=0)
    r4.config(anchor=W)


    x=IntVar()
    y=IntVar() 
    z=IntVar()
    fakultativni_izleti=Checkbutton(t,text='Fakultativni izleti',variable=x)
    fakultativni_izleti.grid(row=0,column=1)
    fakultativni_izleti.config(anchor=W)

    Turisticki_vodic=Checkbutton(t,text='Turisticki vodic',variable=y)
    Turisticki_vodic.grid(row=1,column=1)
    Turisticki_vodic.config(anchor=W)

    Putno_osiguranje=Checkbutton(t,text='Putno osiguranje',variable=z)
    Putno_osiguranje.grid(row=2,column=1)
    Putno_osiguranje.config(anchor=W)

    b_opcije=Button(t,text="Izbor",command=lambda:[a.opcije(destinacija,var1.get(),var2.get(),x,y,z),quit('Formiran je excel file za izabranu lokaciju! Ok za izlazak')])
    b_opcije.grid(row=4,column=1)




def izaberi_agenciju():
    t=Toplevel(root)

    var1 = StringVar(t) 
    var1.set("Balkan Fun") 
    r1=Radiobutton(t, text="Balkan Fun", variable=var1, value="Balkan Fun")
    r2=Radiobutton(t, text="Puzzle Group", variable=var1, value="Puzzle Group")
    r3=Radiobutton(t, text="Go2 Travelling", variable=var1, value="Go2 Travelling")
    r4=Radiobutton(t, text="Rapsody Travel", variable=var1, value="Rapsody Travel")
    

    r1.pack()
    r2.pack()
    r3.pack()
    r4.pack()


    b_agencija=Button(t,text="Izaberi agenciju",command=lambda:[a.export_agencija(var1.get()),quit('Formiran je excel file za izabranu agenciju! Ok za izlazak')])
    b_agencija.pack()

b_export=Button(root,text="Pogledajte sve aranzmane",command=lambda:export())
b_export.grid(row=2)
b_export.config(width=30,height=3)
b_agencija=Button(root,text="Pogledaj aranzmane za agenciju",command=lambda:izaberi_agenciju())
b_agencija.grid(row=3)
b_agencija.config(width=30,height=3)

destinacija=a.listbox()
listbox=Listbox(root)
for i in range(len(destinacija)):
    listbox.insert(i,destinacija[i])

listbox.grid(row=0)

listbox.config(height=listbox.size(),width=30)

b_destinacije=Button(root,text="Izbor destinacije",command=lambda:izbor_broja_lezajeva_dodatnih_opcija(listbox.get(listbox.curselection())))
b_destinacije.grid(row=1)
b_destinacije.config(width=30,height=3)


mainloop()