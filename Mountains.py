# Mount Everest,8848,Himalayas,
# K2,8611,Karakoram,
# Kangchenjunga,8586,Himalayas,
# Lhotse,8516,Himalayas,
# Makalu,8485,Himalayas,
# Cho Oyu,8201,Himalayas,
# Dhaulagiri,8167,Himalayas,
# Manaslu,8163,Himalayas,
# Nanga Parbat,8126,Himalayas,
# Annapurna,8091,Himalayas,
# Gasherbrum I,8080,Karakoram,
# Broad Peak,8051,Karakoram,
# Gasherbrum II,8035,Karakoram,
# Shishapangma,8027,Himalayas,

# Now the problem is we have to convert this details in a dictionary and the key is only “Himalayas” and “Karakoram”

# So let start,
# Step 1:
# First of all the file type is csv and it is in notepad format so we have to import csv file.

import csv

# Step 2:
# We want output in dictionary so we have to take a blank dictionary “Himalayas” to store the items of ‘Himalayas”.“Karakoram” to store the items of “Karakoram”. “Mountains” to store the items of “Himalayas” and a list. List is use for store the items of “Himalayas” and “Karakoram”

Himalayas={}
Karakoram={}
Mountains={}
x=[]

# Step 3:
# Now open our mountains csv file in a read mode.

with open('mountains.csv', 'r') as file:
    reader = csv.reader(file)

# Step 4:
# Now  we use the “row” variable to read the file of reader, In addition we are using the if and elif condition to check the words “Himalays” and”Karakoram” is in the row or not if the words “Himalayas” and “Karakoram” is present in the row than make dictionary of “Himalayas” and “Karakoram”. Than we append the dictionary in the list which name is “X”

for row in reader:
    
        if 'Himalayas' in row:
            a=row[2]
            Himalayas[a]=row[0:2]
            print(Himalayas)
            x.append(Himalayas)
   
        elif 'Karakoram' in row:
            a=row[2]
            Karakoram[a]=row[0:2]
            print(Karakoram)
            x.append(Karakoram)

# Step 5:
# Next one is we read the list which is stored in “x” through the “i” than we read the keys of “ i” with the help of “k”. If k.keys() is in “k” so we append it in “k”

for i in x:
    for k in i:
        if k in Mountains.keys():
            Mountains[k].append(i[k])
            
        else:
            Mountains[k]=[]
            Mountains[k].append(i[k])

print(mountains)



