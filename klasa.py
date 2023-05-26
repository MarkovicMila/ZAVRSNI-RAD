import psycopg2 as pg
import openpyxl as op
import pandas as pd
import matplotlib.pyplot as plt
import pyautogui as pyauto

class Aranzmani:
    def __init__(self):
        self.con=pg.connect(
            database='putovanja',
            password='itoip',
            user='postgres',
            host='localhost',
            port='5432'
        )
        self.aranzmani_df=None

    def import_from_sql(self):
        self.aranzmani_df=pd.read_sql('SELECT * FROM ARANZMANI',con=self.con)
        return self.aranzmani_df

    def listbox(self):
        pom=a.import_from_sql().iloc[:,1]
        destinacija=[]      
        for i in pom:
            if i not in destinacija:
                destinacija.append(i)
        return destinacija
    
    def close_connection(self):
        self.con.close()
    
    def export(self,lokacija):
        if lokacija=='csv':
            self.aranzmani_df.to_csv('Aranzmani.csv',index=False)
            return 'File succesfully exported'
        else:
            self.aranzmani_df.to_excel('Aranzmani.xlsx',index=False)
            return 'File succesfully exported'
        
    def export_agencija(self,agencija):
        self.aranzmani_df=pd.read_sql_query('''
        SELECT AR.ID_ARANZMANA, AR.DESTINACIJA, AR.BROJ_KREVETA, AR.CENA
        FROM AGENCIJE AG, ARANZMANI AR
        WHERE AG.PIB_AGENCIJE=AR.PIB_AGENCIJE AND AG.NAZIV_AGENCIJE='{}' 
        ORDER BY AR.CENA ASC'''.format(agencija),self.con)
        self.aranzmani_df.to_excel('''Aranzmani za agenciju {}.xlsx'''.format(agencija),index=False)

        pom=pd.read_sql_query('''
        SELECT AR.ID_ARANZMANA, AR.DESTINACIJA, AR.CENA
        FROM AGENCIJE AG, ARANZMANI AR
        WHERE AG.PIB_AGENCIJE=AR.PIB_AGENCIJE AND AG.NAZIV_AGENCIJE='{}' AND AR.BROJ_KREVETA=2
        ORDER BY AR.CENA ASC'''.format(agencija),self.con)
        cena=pom.iloc[:,2]
        destinacija=pom.iloc[:,1]

        plt.figure(figsize=(10,7))
        plt.subplot(2,1,1)
        plt.title('Cene za dvokrevetne sobe')
        plt.bar(destinacija,cena)

        pom=pd.read_sql_query('''
        SELECT AR.ID_ARANZMANA, AR.DESTINACIJA, AR.CENA
        FROM AGENCIJE AG, ARANZMANI AR
        WHERE AG.PIB_AGENCIJE=AR.PIB_AGENCIJE AND AG.NAZIV_AGENCIJE='{}' AND AR.BROJ_KREVETA=3
        ORDER BY AR.CENA ASC'''.format(agencija),self.con)
        cena=pom.iloc[:,2]
        destinacija=pom.iloc[:,1]
        plt.subplot(2,1,2)
        plt.title('Cene za trokrevetne sobe')
        plt.bar(destinacija,cena)

        plt.show()    
        
    def opcije(self,destinacija,broj_lezajeva,polazak,fakultativni_izleti,Turisticki_vodic,Putno_osiguranje,Party_narukvica):
        if broj_lezajeva=='dvokrevetna':
            broj_lezajeva=2
        elif broj_lezajeva=='trokrevetna':
            broj_lezajeva=3
        
        self.aranzmani_df=pd.read_sql_query('''
        SELECT AR.ID_ARANZMANA, AG.NAZIV_AGENCIJE, AG.PIB_AGENCIJE, AG.ADRESA_AGENCIJE, AG.BROJ_LICENCE, AR.CENA
        FROM AGENCIJE AG, ARANZMANI AR
        WHERE AG.PIB_AGENCIJE=AR.PIB_AGENCIJE AND AR.DESTINACIJA='{}' AND AR.BROJ_KREVETA={}
        ORDER BY AR.CENA ASC'''.format(destinacija,int(broj_lezajeva)),self.con)
        
        
        cena=self.aranzmani_df.iloc[:,5]
        if polazak=='Individualni polazak':
            cena-=50
        if fakultativni_izleti.get()==1:
            cena+=30
        if Turisticki_vodic.get()==1:
            cena+=10
        if Putno_osiguranje.get()==1:
            cena+=15
        if Party_narukvica.get()==1:
            cena+=20
            

        self.aranzmani_df.iloc[:,5]=cena
        self.aranzmani_df.to_excel('''Aranzmani za destinaciju {} i {} kreveta.xlsx'''.format(destinacija,broj_lezajeva),index=False)


        agencija=self.aranzmani_df.iloc[:,1]
        plt.bar(agencija,cena,color='red')
        plt.show()


a=Aranzmani()
# p.export_excel()
# p.export_csv()
# p.dodaj_posiljku('Petar Petrovic','Marko Markovic')
# print(p.listbox())
# print(a.listbox())
# print(a.export_agencija('Rapsody Travel'))