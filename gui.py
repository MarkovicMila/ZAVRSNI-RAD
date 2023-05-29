from tkinter import *
from klasa import *


root=Tk()
root.title("Turisticka agencija")
icon=PhotoImage(file='autobus.png')
root.iconphoto(True,icon)

def agencija():

    sifra=pyauto.password('Unesite sifru',default='',mask='*')
    if sifra=='Balkan_admin' or sifra=='Puzzle_admin' or sifra=='Go2_admin' or sifra=='Rapsody_admin':
        pyauto.alert('''            Uspesno ste se ulogovali! 
        Dobrodosni na stranicu za agencije.''')

        t=Toplevel(root)

        b_dodaj=Button(t,text='''Dodajte novu ponudu 
            za vasu agenciju''',command=lambda:dodaj_ponudu(sifra))
        b_dodaj.pack()
        b_dodaj.config(width=30)

        b_pogledaj=Button(t,text='''Pogledajte ponude 
        za drugu agenciju''',command=lambda:pogledaj_ponudu(sifra))
        b_pogledaj.pack()
        b_pogledaj.config(width=30)
    
    else:
        quit('Uneli ste losu sifru. Ok za izlazak')
    
def dodaj_ponudu(sifra):
    t=Toplevel(root)

    destinacija=Label(t,text='Destinacija:').pack()
    destinacija=Entry(t)
    destinacija.pack()

    broj_kreveta=Label(t,text='Broj kreveta:').pack()
    broj_kreveta=Entry(t)
    broj_kreveta.pack()

    cena=Label(t,text='Cena:').pack()
    cena=Entry(t)
    cena.pack()

    if sifra=='Balkan_admin':
        dodaj=Button(t,text="Dodaj",command=lambda:[a.nov_aranzman(destinacija.get(),106900792,broj_kreveta.get(),cena.get()),quit('Dodali ste novu ponudu.')])
        dodaj.pack()
    elif sifra=='Puzzle_admin':
        dodaj=Button(t,text="Dodaj",command=lambda:[a.nov_aranzman(destinacija.get(),107156256,broj_kreveta.get(),cena.get()),quit('Dodali ste novu ponudu.')])
        dodaj.pack()
    elif sifra=='Go2_admin':
        dodaj=Button(t,text="Dodaj",command=lambda:[a.nov_aranzman(destinacija.get(),106848247,broj_kreveta.get(),cena.get()),quit('Dodali ste novu ponudu.')])
        dodaj.pack()
    elif sifra=='Rapsody_admin':
        dodaj=Button(t,text="Dodaj",command=lambda:[a.nov_aranzman(destinacija.get(),103721228,broj_kreveta.get(),cena.get()),quit('Dodali ste novu ponudu.')])
        dodaj.pack()
    else:
        quit('Uneli ste losu sifru. Ok za izlazak')

def pogledaj_ponudu(sifra):

    if sifra=='Balkan_admin':
        t=Toplevel(root)

        var1 = StringVar(t) 
        var1.set("Puzzle Group") 
        r1=Radiobutton(t, text="Puzzle Group", variable=var1, value="Puzzle Group")
        r2=Radiobutton(t, text="Go2 Travelling", variable=var1, value="Go2 Travelling")
        r3=Radiobutton(t, text="Rapsody Travel", variable=var1, value="Rapsody Travel")
        
        r1.pack()
        r2.pack()
        r3.pack()
        
        b_ponude=Button(t,text="Izaberi agenciju",command=lambda:[a.export_agencija(var1.get()),quit('Formiran je excel file za izabranu agenciju! Ok za izlazak')])
        b_ponude.pack()
        
    elif sifra=='Puzzle_admin':
        t=Toplevel(root)

        var1 = StringVar(t) 
        var1.set("Balkan Fun") 
        r1=Radiobutton(t, text="Balkan Fun", variable=var1, value="Balkan Fun")
        r2=Radiobutton(t, text="Go2 Travelling", variable=var1, value="Go2 Travelling")
        r3=Radiobutton(t, text="Rapsody Travel", variable=var1, value="Rapsody Travel")
        
        r1.pack()
        r2.pack()
        r3.pack()
        
        b_ponude=Button(t,text="Izaberi agenciju",command=lambda:[a.export_agencija(var1.get()),quit('Formiran je excel file za izabranu agenciju! Ok za izlazak')])
        b_ponude.pack()
    elif sifra=='Go2_admin':
        t=Toplevel(root)

        var1 = StringVar(t) 
        var1.set("Go2 Travelling") 
        r1=Radiobutton(t, text="Balkan Fun", variable=var1, value="Balkan Fun")
        r2=Radiobutton(t, text="Puzzle Group", variable=var1, value="Puzzle Group")
        r3=Radiobutton(t, text="Rapsody Travel", variable=var1, value="Rapsody Travel")
        
        r1.pack()
        r2.pack()
        r3.pack()
        
        b_ponude=Button(t,text="Izaberi agenciju",command=lambda:[a.export_agencija(var1.get()),quit('Formiran je excel file za izabranu agenciju! Ok za izlazak')])
        b_ponude.pack()
    elif sifra=='Rapsody_admin':
        t=Toplevel(root)

        var1 = StringVar(t) 
        var1.set("Rapsody Travel") 
        r1=Radiobutton(t, text="Balkan Fun", variable=var1, value="Balkan Fun")
        r2=Radiobutton(t, text="Puzzle Group", variable=var1, value="Puzzle Group")
        r3=Radiobutton(t, text="Go2 Travelling", variable=var1, value="Go2 Travelling")
        
        r1.pack()
        r2.pack()
        r3.pack()
        
        b_ponude=Button(t,text="Izaberi agenciju",command=lambda:[a.export_agencija(var1.get()),quit('Formiran je excel file za izabranu agenciju! Ok za izlazak')])
        b_ponude.pack()
    else:
        quit('Uneli ste losu sifru. Ok za izlazak')
    
def kupac():
    t=Toplevel(root)
    t.geometry('251x548')


    b_export=Button(t,text="Pogledajte sve aranzmane",command=lambda:export())
    b_export.grid(row=2)
    b_export.config(width=30,height=3)
    b_agencija=Button(t,text="Pogledaj aranzmane za agenciju",command=lambda:izaberi_agenciju())
    b_agencija.grid(row=3)
    b_agencija.config(width=30,height=3)

    destinacija=a.listbox()
    listbox=Listbox(t)
    for i in range(len(destinacija)):
        listbox.insert(i,destinacija[i])

    listbox.grid(row=0)

    listbox.config(height=15,width=30)

    b_destinacije=Button(t,text="Izbor destinacije",command=lambda:izbor_broja_lezajeva_dodatnih_opcija(listbox.get(listbox.curselection())))
    b_destinacije.grid(row=1)
    b_destinacije.config(width=30,height=3)

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

    br_kreveta=Label(t,text='Izaberite broj lezajeva:')
    br_kreveta.grid(row=0,column=0,columnspan=40)
    br_kreveta.config(anchor='w')

    var1 = StringVar(t) 
    var1.set("dvokrevetna") 
    r1=Radiobutton(t, text="dvokrevetna", variable=var1, value='dvokrevetna')
    r2=Radiobutton(t, text="trokrevetna", variable=var1, value='trokrevetna')

    r1.grid(row=1,column=0,columnspan=20)
    r1.config(anchor='w')
    r2.grid(row=1,column=21,columnspan=20)
    r2.config(anchor='w')

    tip_polaska=Label(t,text='Izaberite tip polaska:')
    tip_polaska.grid(row=2,column=0,columnspan=40)
    tip_polaska.config(anchor='w')

    var2 = StringVar(t) 
    var2.set("Organizovani polazak") 
    r3=Radiobutton(t, text="Organizovani polazak", variable=var2, value='Organizovani polazak')
    r4=Radiobutton(t, text="Individualni polazak", variable=var2, value='Individualni polazak')

    r3.grid(row=3,column=0,columnspan=20)
    r3.config(anchor='w')
    r4.grid(row=3,column=21,columnspan=20)
    r4.config(anchor='w')

    dodatne_opcije=Label(t,text='Izaberite dodatne opcije:')
    dodatne_opcije.grid(row=4,column=0,columnspan=40)
    dodatne_opcije.config(anchor='w')

    x=IntVar()
    y=IntVar() 
    z=IntVar()
    q=IntVar()

    fakultativni_izleti=Checkbutton(t,text='Fakultativni izleti',variable=x)
    fakultativni_izleti.grid(row=5,column=0,columnspan=20)
    fakultativni_izleti.config(anchor='w')

    Turisticki_vodic=Checkbutton(t,text='Turisticki vodic',variable=y)
    Turisticki_vodic.grid(row=5,column=21,columnspan=20)
    Turisticki_vodic.config(anchor='w')

    Putno_osiguranje=Checkbutton(t,text='Putno osiguranje',variable=z)
    Putno_osiguranje.grid(row=6,column=0,columnspan=20)
    Putno_osiguranje.config(anchor='w')

    Party_narukvica=Checkbutton(t,text='Party narukvica',variable=q)
    Party_narukvica.grid(row=6,column=21,columnspan=20)
    Party_narukvica.config(anchor='w')
    
    b_opcije=Button(t,text="Izbor",command=lambda:[a.opcije(destinacija,var1.get(),var2.get(),x,y,z,q),quit('Formiran je excel file za izabranu lokaciju! Ok za izlazak')])
    b_opcije.grid(row=7,column=0,columnspan=40)
    


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

label1=Label(root,text='''Izaberite da li pristupate aplikaciji
    kao agencija ili kao kupac:''')
label1.grid(row=1)
label1.config(width=30,height=3)
b_agencija=Button(root,text="Agencija",command=lambda:agencija())
b_agencija.grid(row=2)
b_agencija.config(width=30,height=3)
b_kupac=Button(root,text="Kupac",command=lambda:kupac())
b_kupac.grid(row=3)
b_kupac.config(width=30,height=3)

mainloop()