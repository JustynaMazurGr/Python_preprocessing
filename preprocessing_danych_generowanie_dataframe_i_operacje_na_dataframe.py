# -*- coding: utf-8 -*-
"""Preprocessing danych - generowanie DataFrame i operacje na DataFrame.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1HyzoeIoSTzPygeWbx7OKh8S5Pq20N9n3

Wygeneruj DataFrame zawierający dane studentów z dwóch różnych
grup. Tabela powinna zawierać następujące atrybuty: Imię, Numer
albumu (5 losowych cyfr – niekoniecznie unikalnych), numer grupy
zapisany jako: I lub II oraz trzy kolumny oznaczone kolejno: Kolokwium I,
Kolokwium II oraz Projekt – zawierające oceny z przedziału ⟨2, 5⟩.
Zakładamy, że w każdej z grup zapisanych jest po 30 osób. Następnie:
podaj, ile osób zdobyło maksymalną ocenę;
ile osób nie zaliczyło kolokwium II;
jaka była średnia ocen w każdej z grup z kolokwium I;
jaka była korelacja pomiędzy średnią ocen dla grupy I i grupy II;
jaka była mediana ocen w grupie II.

Zapisz do pliku csv dane.
Zapisz do pliku JSON dane, gdzie kolumny przechowywane są w odwrotnej kolejności.
"""

import pandas
import random
import numpy

imie = []                                
numer_albumu = []                       
numer_grupy = []                         
kolokwium1 = []                          
kolokwium2 = []                         
projekt = []                             

licznik = 0
for i in range(60):                         
    imie.append(random.choice(['Ala', 'Kasia','Bartek', 'Łukasz', 'Michał']))   
    numer_albumu.append(random.randint(10000,99999))    
    if licznik < 30:                        
        numer_grupy.append('I')             
        licznik += 1
    else:
        numer_grupy.append('II')            
    kolokwium1.append(random.randint(2,5))  
    kolokwium2.append(random.randint(2,5)) 
    projekt.append(random.randint(2,5))    
    
data = pandas.DataFrame(imie)  #TABELA DATAFRAME o nazwie data

data.set_axis(['Imię'], axis = 1, inplace = True)   #moją kolumnę o nazwie 0 teraz nazywam Imię.
                                                    
data['Numer albumu'] = numer_albumu
data['numer grupy'] = numer_grupy
data['Kolokwium I'] = kolokwium1    #liście kolokwium1 nadaję nazwę Kolokwium I i dodaję do tabeli
data['Kolokwium II'] = kolokwium2
data['Projekt'] = projekt

nr_alb = data['Numer albumu']       #zmiennej "nr_alb" przypisz listę "Numer albumu" z tabeli "data" i ten nr_alb będzie serią
nr_gr = data['numer grupy']         
ocena_kol1 = data['Kolokwium I']   
ocena_kol2 = data['Kolokwium II']   
ocena_proj = data['Projekt']        


#ile osób zdobyło maksymalną ocenę
zlicz_ocena_max = list(ocena_kol1).count(5) + list(ocena_kol2).count(5) + list(ocena_proj).count(5)   
print("liczba osób, które zdobyły maksymalną ocenę: ",zlicz_ocena_max)

#ile osób nie zaliczyło kolokwium II
zlicz_niez_kol2 = list(ocena_kol2).count(2)     #INT
print("liczba osób, które nie zaliczyło kolokwium2: ", zlicz_niez_kol2)

#jaka była średnia ocen w każdej z grup z kolokwium I

srednia_kol1_gr1 = data[data['numer grupy'] == 'I']['Kolokwium I'].mean()
srednia_kol1_gr2 = data[data['numer grupy'] == 'II']['Kolokwium I'].mean()
print("średnia ocen grupa 1:", srednia_kol1_gr1)
print("średnia ocen grupa 2:", srednia_kol1_gr2)

#_________________________________________________________________________________________________________
# jaka była korelacja pomiędzy średnią ocen dla grupy I i grupy II

# Obliczamy średnią ocenę dla grupy I i grupy II z kol 1, kol 2 i projektu
srednie_oc_gr1 = data[data['numer grupy']=='I'][['Kolokwium I','Kolokwium II','Projekt']].mean(axis=1)
srednie_oc_gr2 = data[data['numer grupy']=='II'][['Kolokwium I','Kolokwium II','Projekt']].mean(axis=1)

lista_gr1 = srednie_oc_gr1.head(30).tolist()  #tworzę listę średnich ocen (liczone po wierszach dla danej osoby) 30 od góry (bo pierwsza w tabeli jest grupa 1) 
lista_gr2 = srednie_oc_gr2.tail(30).tolist()    ##tworzę listę średnich ocen (liczone po wierszach dla danej osoby) 30 od dołu (bo druga w tabeli jest grupa 2) 

data_srednie = pandas.DataFrame(lista_gr1)  #nowa TABELA DATAFRAME ze średnimi ocenami z grupy 1 i grupy 2 
data_srednie.set_axis(['Średnie oceny gr I'], axis = 1, inplace = True)  
data_srednie['Średnie oceny gr II'] = lista_gr2

# Obliczamy korelację pomiędzy średnią oceną dla grupy I i grupy II
korelacja = data_srednie['Średnie oceny gr I'].corr(data_srednie['Średnie oceny gr II'])
print("Korelacja pomiędzy średnią oceną dla grupy I i grupy II: ",korelacja)

#___________________________________________________________________________________________________________
#jaka była mediana ocen w grupie II z kol 1, kol 2 i proj.

#Policzona mediana dla każdego sprawdzianu osobno (da 3 wartości)
medianaGrII = data[data['numer grupy'] == 'II'][['Kolokwium I','Kolokwium II', 'Projekt']].median()
print("mediana ocen w grupie II: ",medianaGrII)

#Policzona mediana dla wszystkich sprawdzianów razem (da jedna wartość)
scalone_oc_gr2kol12 = data[data['numer grupy'] == 'II']['Kolokwium I'].append(data[data['numer grupy'] == 'II']['Kolokwium II']) #scala dwie kolumny (nie dodaje jak add 2+3)
scalone_oc_gr2 = scalone_oc_gr2kol12.append(data[data['numer grupy'] == 'II']['Projekt'])
medianaGr2 = scalone_oc_gr2.median()    
print("mediana ocen w grupie II: ",medianaGr2)

#Zapisuję do pliku csv dane
data.to_csv("/content/drive/MyDrive/DO ĆWICZEŃ/data.csv") #zapisze plik na google drive

#Zapisuję do pliku JSON dane, gdzie kolumny przechowywane są w odwrotnej kolejności
data[::-1].to_json("/content/drive/MyDrive/DO ĆWICZEŃ/data.json")    #zapisało kolumny w odwrotnej kolejności jak kazano w zadaniu

"""Wymień się plikiem z danymi z sąsiadem, a następnie wczytaj jej/jego dane do DataFrame;

przygotuj trzecią DataFrame, która powstanie przez wyznaczenie różnicy pomiędzy danymi – tj. od wartości pierwszego obiektu i pierwszego atrybutu w pierwszym DataFrame odejmij odpowiadające pole drugim DataFrame. W wyniku powstanie nowy DataFrame zawierający różnicę dwóch DataFrame;

wyznacz średnią wartość każdej kolumny z DataFrame utworzonego jako różnica dwóch DataFrame.
"""

import pandas

#Wczytanie mojego pliku
mojplik = pandas.read_csv("/content/drive/MyDrive/DO ĆWICZEŃ/data.csv")

#Wczytanie pliku sąsiada
pliksasiad = pandas.read_csv("/content/drive/MyDrive/DO ĆWICZEŃ/datasasiad.csv")

#przygotuj trzecią DataFrame, która powstanie przez wyznaczenie różnicy pomiędzy danymi – tj. 
#od wartości pierwszego obiektu i pierwszego atrybutu w pierwszym DataFrame odejmij odpowiadające pole drugim DataFrame. 
#W wyniku powstanie nowy DataFrame zawierający różnicę dwóch DataFrame

#używam sub, przechodzę po każdej z kolumn
roznicaKol1 = mojplik["Kolokwium I"].sub(pliksasiad["Kolokwium I"])
roznicaKol2 = mojplik["Kolokwium II"].sub(pliksasiad["Kolokwium II"])
roznicaProj = mojplik["Projekt"].sub(pliksasiad["Projekt"])

#tworzę nowy DataFrame zawierający różnicę dwóch DataFrame
trzecidata = pandas.DataFrame(mojplik["Imię"])
trzecidata['Numer albumu'] = mojplik['Numer albumu']
trzecidata['Numer grupy'] = mojplik['numer grupy']
trzecidata['różnica Kol1'] = roznicaKol1
trzecidata['różnica Kol2'] = roznicaKol2
trzecidata['różnica Proj'] = roznicaProj

#wyznacz średnią wartość każdej kolumny z DataFrame utworzonego jako różnica dwóch DataFrame.
srednia1 = roznicaKol1.mean()
srednia2 = roznicaKol2.mean()
srednia3 = roznicaProj.mean()

print(f"Średnia dla kolumny 1: {srednia1:.2f}\nŚrednia dla kolumny 2: {srednia2:.2f}\nŚrednia dla kolumny 3: {srednia3:.2f}\n")