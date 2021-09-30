import pandas as pd
import csv 
import sqlite3

def check(s,a):
	if s == "Netherlands":
		a[0]+=1
	elif s == "Kingdom":
		a[1]+=1
	elif s =="Spain":
		a[2]+=1
	elif s=="France":
		a[3]+=1
	elif s == "Austria":
		a[4]+=1
	elif s == "Italy":
		a[5]+=1

	return a
def print_out(a):
	print("Netherlands: ", a[0])
	print("United Kingdom: ", a[1])
	print("Spain: ",a[2])
	print("France: ",a[3])
	print("Austria: ",a[4])
	print("Italy: ",a[5])


file = 'Data.csv'
df = pd.read_csv(file)

#Question1:
print(df.info())
print()

#Question2:
print(df[['Hotel_Address','Average_Score']].head(10))

print()

#Question3:
df['Rec']=""
df['Rec'] = df['Negative_Review'] != "No Negative Review"
print(df['Rec'].tail(5))

print()

#Question4:
l = []
a = [0,0,0,0,0,0] 

Uk=[] 
Sp= [] 
Ne = []
Fr = [] 
Au = []
Ita= []


for i in range(len(df)):
	# s.append("")
	s1 = df.loc[i,'Hotel_Address']
	if s1 not in l:
		l.append(s1)
		j = len(s1)-1
		s2 = ""
		while True:
			if s1[j] == " ":
				break 
			s2 = s1[j] + s2
			j = j - 1
		a = check(s2,a)
		
		#For Ques3
		if s2 == "Kingdom":
			Uk.append(s1)
		elif s2 == "Spain":
			Sp.append(s1)
		elif s2 == "France":
			Fr.append(s1)
		elif s2 == "Austria":
			Au.append(s1)
		elif s2 == "Italy":
			Ita.append(s1)
		elif s2 == "Netherlands":
			Ne.append(s1)

	# break
print_out(a)

print()


# #Question5:
s = str(input("Country that you choose : "))

if s == "United Kingdom":
	print(Uk)
elif s == "Spain":
	print(Sp)
elif s == "France":
	print(Fr)
elif s == "Austria":
	print(Au)
elif s == "Italy":
	print(Ita)
elif s == "Netherlands":
	print(Ne)

print()

#Question6:
chuoi = []
chuoi = df['Average_Score']
t = 0
t = max(chuoi)
print("Highest point: ", t)
best_hotels = df[df['Average_Score']==t]
print("Best hotels :")
best_hotels.reset_index(inplace = True)
print(best_hotels.loc[0,'Hotel_Name'])
for i in range (1,len(best_hotels)):
	if best_hotels.loc[i,'Hotel_Name'] != best_hotels.loc[i-1,'Hotel_Name']:
		print(best_hotels.loc[i,'Hotel_Name'])
print()

t = min(chuoi)
print("Lowesst point: ",t)
worst_hotels = df[df['Average_Score']==t]
print("Worst hotels: ")
worst_hotels.reset_index(inplace = True)
print(worst_hotels.loc[0,'Hotel_Name'])
for i in range (1,len(worst_hotels)):
	if worst_hotels.loc[i,'Hotel_Name'] != worst_hotels.loc[i-1,'Hotel_Name']:
		print(worst_hotels.loc[i,'Hotel_Name'])
print()

#Question7:
num = float(input("Type in the score that you think would fit you the best: "))
find_hotels = df[df['Average_Score']==num]
print("The hotels you are looking for: ")
find_hotels.reset_index(inplace= True)
print(find_hotels.loc[0,'Hotel_Name'])
for i in range(1,len(find_hotels)):
	if find_hotels.loc[i,'Hotel_Name'] != find_hotels.loc[i-1,'Hotel_Name']:
		print(find_hotels.loc[i,'Hotel_Name'])

print()

#Question8:
print("Before sort: ")
chuoi = df[['Hotel_Name','Average_Score']]
print(chuoi)
sorted_chuoi = chuoi.sort_values(by=['Average_Score'],ascending=False)
print("After sort: ")
sorted_chuoi.reset_index(inplace=True)
print(sorted_chuoi)

print()

#Question9:
sorted_chuoi.to_csv("HotelsPointbySteven.csv")

#Question10:
chunksize = 260000
i = 0
for chunk in pd.read_csv(file, chunksize=chunksize):
    # process(chunk)
    i += 1
    chunk.reset_index(inplace=True)
    if i == 1 :
    	chunk.to_csv('Data1.csv')
    else:
    	chunk.to_csv('Data2.csv')