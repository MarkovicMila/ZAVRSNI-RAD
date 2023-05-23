import psycopg2 as pg
import openpyxl as op
import pandas as pd
import matplotlib as plt

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
            self.aranzmani_df.to_csv('Aramnzmani.csv',index=False)
            return 'File succesfully exported'
        else:
            self.aranzmani_df.to_excel('Aranzmani.xlsx',index=False)
            return 'File succesfully exported'
        
    def export_agencija(self,agencija):
        self.aranzmani_df=pd.read_sql_query('''
        SELECT AR.ID_ARANZMANA, AR.DESTINACIJA, AR.BROJ_KREVETA, AR.CENA
        FROM AGENCIJE AG, ARANZMANI AR
        WHERE AG.PIB_AGENCIJE=AR.PIB_AGENCIJE AND AG.NAZIV_AGENCIJE='{}' '''.format(agencija),self.con)
        self.aranzmani_df.to_excel('''Aranzmani za agenciju {}.xlsx'''.format(agencija),index=False)
    
        
    def destinacija_broj_lezajeva(self,destinacija,broj_lezajeva):
        pass


a=Aranzmani()
# p.export_excel()
# p.export_csv()
# p.dodaj_posiljku('Petar Petrovic','Marko Markovic')
# print(p.listbox())
# print(a.listbox())
# print(a.export_agencija('Rapsody Travel'))