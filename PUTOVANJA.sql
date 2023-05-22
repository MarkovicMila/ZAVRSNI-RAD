CREATE TABLE AGENCIJE(
PIB_agencije INTEGER PRIMARY KEY,
naziv_agencije VARCHAR(30) NOT NULL,
adresa_agencije VARCHAR(40) NOT NULL,
broj_licence VARCHAR(12) NOT NULL);

DROP TABLE AGENCIJE

INSERT INTO AGENCIJE VALUES (106900792,'Balkan Fun','Balkanska 27','OTP 109/2021');
INSERT INTO AGENCIJE VALUES (107156256,'Puzzle Group','Resavska 16a','OTP 108/2021');
INSERT INTO AGENCIJE VALUES (106848247,'Go2 Travelling','Strahinica Bana 36','OTP 60/2021');
INSERT INTO AGENCIJE VALUES (103721228,'Rapsody Travel','Vojvode Supljikca 19','OTP 124/2021');

CREATE TABLE ARANZMANI(
id_aranzmana SERIAL,
destinacija VARCHAR(20) NOT NULL,
PIB_agencije INTEGER NOT NULL,
broj_kreveta INTEGER NOT NULL,
cena INTEGER NOT NULL,
PRIMARY KEY(id_aranzmana),
FOREIGN KEY(PIB_agencije) REFERENCES AGENCIJE(PIB_agencije));

INSERT INTO ARANZMANI (destinacija,PIB_agencije,broj_kreveta,cena) VALUES ('Lefkada',106900792,2,390);
INSERT INTO ARANZMANI (destinacija,PIB_agencije,broj_kreveta,cena) VALUES ('Lefkada',106900792,3,340);
INSERT INTO ARANZMANI (destinacija,PIB_agencije,broj_kreveta,cena) VALUES ('Zakintos',106900792,2,385);
INSERT INTO ARANZMANI (destinacija,PIB_agencije,broj_kreveta,cena) VALUES ('Zakintos',106900792,3,365);
INSERT INTO ARANZMANI (destinacija,PIB_agencije,broj_kreveta,cena) VALUES ('Sicilija',106900792,2,570);
INSERT INTO ARANZMANI (destinacija,PIB_agencije,broj_kreveta,cena) VALUES ('Sicilija',106900792,3,560);
INSERT INTO ARANZMANI (destinacija,PIB_agencije,broj_kreveta,cena) VALUES ('Kusadasi',106900792,3,205);
INSERT INTO ARANZMANI (destinacija,PIB_agencije,broj_kreveta,cena) VALUES ('Kusadasi',106900792,2,215);
INSERT INTO ARANZMANI (destinacija,PIB_agencije,broj_kreveta,cena) VALUES ('Kavos',106900792,3,385);
INSERT INTO ARANZMANI (destinacija,PIB_agencije,broj_kreveta,cena) VALUES ('Kavos',106900792,2,465);
INSERT INTO ARANZMANI (destinacija,PIB_agencije,broj_kreveta,cena) VALUES ('Kefalonija',106900792,3,320);
INSERT INTO ARANZMANI (destinacija,PIB_agencije,broj_kreveta,cena) VALUES ('Kefalonija',106900792,2,340);
INSERT INTO ARANZMANI (destinacija,PIB_agencije,broj_kreveta,cena) VALUES ('Evia',106900792,2,220);
INSERT INTO ARANZMANI (destinacija,PIB_agencije,broj_kreveta,cena) VALUES ('Evia',106900792,3,200);
INSERT INTO ARANZMANI (destinacija,PIB_agencije,broj_kreveta,cena) VALUES ('Zakintos',103721228,2,359);
INSERT INTO ARANZMANI (destinacija,PIB_agencije,broj_kreveta,cena) VALUES ('Zakintos',103721228,3,349);
INSERT INTO ARANZMANI (destinacija,PIB_agencije,broj_kreveta,cena) VALUES ('Kusadasi',103721228,2,279);
INSERT INTO ARANZMANI (destinacija,PIB_agencije,broj_kreveta,cena) VALUES ('Kusadasi',103721228,3,269);
INSERT INTO ARANZMANI (destinacija,PIB_agencije,broj_kreveta,cena) VALUES ('Kavos',103721228,2,289);
INSERT INTO ARANZMANI (destinacija,PIB_agencije,broj_kreveta,cena) VALUES ('Kavos',103721228,3,279);
INSERT INTO ARANZMANI (destinacija,PIB_agencije,broj_kreveta,cena) VALUES ('Lutraki',103721228,2,359);
INSERT INTO ARANZMANI (destinacija,PIB_agencije,broj_kreveta,cena) VALUES ('Lutraki',103721228,3,349);
INSERT INTO ARANZMANI (destinacija,PIB_agencije,broj_kreveta,cena) VALUES ('Lefkada',103721228,2,359);
INSERT INTO ARANZMANI (destinacija,PIB_agencije,broj_kreveta,cena) VALUES ('Lefkada',103721228,3,329);
INSERT INTO ARANZMANI (destinacija,PIB_agencije,broj_kreveta,cena) VALUES ('Evia',103721228,2,229);
INSERT INTO ARANZMANI (destinacija,PIB_agencije,broj_kreveta,cena) VALUES ('Evia',103721228,3,219);
INSERT INTO ARANZMANI (destinacija,PIB_agencije,broj_kreveta,cena) VALUES ('Budva',103721228,2,239);
INSERT INTO ARANZMANI (destinacija,PIB_agencije,broj_kreveta,cena) VALUES ('Budva',103721228,3,229);
INSERT INTO ARANZMANI (destinacija,PIB_agencije,broj_kreveta,cena) VALUES ('Marmaris',106848247,2,279);
INSERT INTO ARANZMANI (destinacija,PIB_agencije,broj_kreveta,cena) VALUES ('Marmaris',106848247,3,269);
INSERT INTO ARANZMANI (destinacija,PIB_agencije,broj_kreveta,cena) VALUES ('Kusadasi',106848247,3,169);
INSERT INTO ARANZMANI (destinacija,PIB_agencije,broj_kreveta,cena) VALUES ('Kusadasi',106848247,2,179);
INSERT INTO ARANZMANI (destinacija,PIB_agencije,broj_kreveta,cena) VALUES ('Lefkada',106848247,3,259);
INSERT INTO ARANZMANI (destinacija,PIB_agencije,broj_kreveta,cena) VALUES ('Lefkada',106848247,2,279);
INSERT INTO ARANZMANI (destinacija,PIB_agencije,broj_kreveta,cena) VALUES ('Zakintos',106848247,2,359);
INSERT INTO ARANZMANI (destinacija,PIB_agencije,broj_kreveta,cena) VALUES ('Zakintos',106848247,3,329);
INSERT INTO ARANZMANI (destinacija,PIB_agencije,broj_kreveta,cena) VALUES ('Kavos',106848247,3,269);
INSERT INTO ARANZMANI (destinacija,PIB_agencije,broj_kreveta,cena) VALUES ('Kavos',106848247,2,279);
INSERT INTO ARANZMANI (destinacija,PIB_agencije,broj_kreveta,cena) VALUES ('Lutraki',106848247,3,249);
INSERT INTO ARANZMANI (destinacija,PIB_agencije,broj_kreveta,cena) VALUES ('Lutraki',106848247,2,259);
INSERT INTO ARANZMANI (destinacija,PIB_agencije,broj_kreveta,cena) VALUES ('Evia',106848247,3,219);
INSERT INTO ARANZMANI (destinacija,PIB_agencije,broj_kreveta,cena) VALUES ('Evia',106848247,2,229);
INSERT INTO ARANZMANI (destinacija,PIB_agencije,broj_kreveta,cena) VALUES ('Budva',106848247,3,210);
INSERT INTO ARANZMANI (destinacija,PIB_agencije,broj_kreveta,cena) VALUES ('Budva',106848247,2,220);
INSERT INTO ARANZMANI (destinacija,PIB_agencije,broj_kreveta,cena) VALUES ('Kalitea',107156256,3,270);
INSERT INTO ARANZMANI (destinacija,PIB_agencije,broj_kreveta,cena) VALUES ('Kalitea',107156256,2,320);
INSERT INTO ARANZMANI (destinacija,PIB_agencije,broj_kreveta,cena) VALUES ('Zakintos',107156256,3,275);
INSERT INTO ARANZMANI (destinacija,PIB_agencije,broj_kreveta,cena) VALUES ('Zakintos',107156256,3,290);
INSERT INTO ARANZMANI (destinacija,PIB_agencije,broj_kreveta,cena) VALUES ('Kavos',107156256,2,275);
INSERT INTO ARANZMANI (destinacija,PIB_agencije,broj_kreveta,cena) VALUES ('Kavos',107156256,3,260);
INSERT INTO ARANZMANI (destinacija,PIB_agencije,broj_kreveta,cena) VALUES ('Kefalonija',107156256,3,195);
INSERT INTO ARANZMANI (destinacija,PIB_agencije,broj_kreveta,cena) VALUES ('Kefalonija',107156256,2,210);

SELECT * FROM AGENCIJE

SELECT * FROM ARANZMANI