# -*- coding: utf-8 -*-
"""

Created on Mon May  6 15:47:35 2024

@author: IAN CARTER KULANI
Phone:+265(0)988061969
E-mail:iancarterkulani@gmail.com
Purpose: The software prompts the user to enter total number of published centers,total 
number of registered  voters, total number of null and void votes, total number of valid votes and total valid votes for each candidate. Afterward,it determines the candidate with the majority of votes 
and displays the results on the screen.
#NOTE:For a candidate to be a majority winner of an election, the candidate total valid votes should 
be greater than majority votes, which is Fifty plus one. 

"""
print("=========================================SOUTH AFRICA 2014 PRESIDENTIAL ELECTION=========================================\n\n")

percent=100
#Get total number of published centers
Totalpublishedcenters=int(input("Enter Total published centers:"))
#Get the total number of registered votes
TotalRegisteredvotes=int(input("Enter Total Registered Voters/Turnout:"))
Totalvotescast=int(input("Enter Total Votes Cast /Total Votes:"))
#Get total number of Null_&_Void votes
Nullandvoid=int(input("Enter Total Null_&_Void Votes / Invalid Votes:"))
#Get Total Valid Votes
Totalvalidvotes=int(input("Enter Total Valid Votes:"))
#Get Total Valid Votes for National Party
Totalvalidvotesfor_African_National_Congress=int(input("Enter Total Valid Votes for African National Congress:"))
#Get Total Valid Votes for  Democratic Alliance	
Totalvalidvotesfor_Democratic_Alliance=int(input("Enter Total Valid Votes for Democratic Alliance:"))
#Get Total Valid Votes for Economic Freedom Fighters
Totalvalidvotesfor_Economic_Freedom_Fighters=int(input("Enter Total Valid Votes for Economic Freedom Fighters:"))
#Get Total Valid Votes for Inkatha Freedom Party
Totalvalidvotesfor_Inkatha_Freedom_Party=int(input("Enter Total Valid Votes for Inkatha Freedom Party:"))	
#Get Total Valid Votes for National Freedom Party
Totalvalidvotesfor_National_Freedom_Party=int(input("Enter Total Valid Votes for National Freedom Party:"))
#Get Total Valid Votes for United Democratic Movement	
Totalvalidvotesfor_United_Democratic_Movement=int(input("Enter Total Valid Votes for United Democratic Movement:"))
#Get Total Valid Votes for Freedom Front Plus	
Totalvalidvotesfor_Freedom_Front_Plus=int(input("Enter Total Valid Votes for Freedom Front Plus:"))
#Get Total Valid Votes for Congress of the People
Totalvalidvotesfor_Congress_of_the_People=int(input("Enter Total Valid Votes for Congress of the People:"))
#Get Total Valid Votes forAfrican Christian Democratic Party
Totalvalidvotesfor_African_Christian_Democratic_Party=int(input("Enter Total Valid Votes for African Christian Democratic Party:"))
#Get Total Valid Votes for African Independent Congress
Totalvalidvotesfor_African_Independent_Congress=int(input("Enter Total Valid Votes for African Independent Congress:"))
#Get Total Valid Votes for Agang South Africa
Totalvalidvotesfor_Agang_South_Africa=int(input("Enter Total Valid Votes for A gang South Africa:"))
#Get Total Valid Votes for Pan Africanist Congress	
Totalvalidvotesfor_Pan_Africanist_Congress=int(input("Enter Total Valid Votes for Pan Africanist Congress:"))
#Get Total Valid Votes for African Peoples Convention	
Totalvalidvotesfor_African_Peoples_Convention=int(input("Enter Total Valid Votes for African Peoples Convention:"))
#Get Total Valid Votes for Al Jama ah	
Totalvalidvotesfor_Al_Jama_ah=int(input("Enter Total Valid Votes for Al Jama ah:"))
#Get Total Valid Votes for Minority Front
Totalvalidvotesfor_Minority_Front=int(input("Enter Total Valid Votes for Minority Front:"))
#Get Total Valid Votes for United Christian Democratic Party
Totalvalidvotesfor_United_Christian_Democratic_Party=int(input("Enter Total Valid Votes for United Christian Democratic Party:"))
#Get Total Valid Votes for Azanian Peoples Organisation	
Totalvalidvotesfor_Azanian_Peoples_Organisation=int(input("Enter Total Valid Votes for Azanian Peoples Organisation:"))
#Get Total Valid Votes for Bushbuckridge Residents Association
Totalvalidvotesfor_Bushbuckridge_Residents_Association=int(input("Enter Total Valid Votes for Bushbuckridge Residents Association:"))
#Get Total Valid Votes for Independent Civic Organisation	
Totalvalidvotesfor_Independent_Civic_Organisation=int(input("Enter Total Valid Votes for Independent Civic Organisation:"))
#Get Total Valid Votes for Patriotic Alliance
Totalvalidvotesfor_Patriotic_Alliance=int(input("Enter Total Valid Votes for Patriotic Alliance:"))
#Get Total Valid Votes for Workers and Socialist Party
Totalvalidvotesfor_Workers_and_Socialist_Party=int(input("Enter Total Valid Votes for Workers and Socialist Party:"))
#Get Total Valid Votes for Ubuntu Party
Totalvalidvotesfor_Ubuntu_Party=int(input("Enter Total Valid Votes for Ubuntu Party:"))
#Get Total Valid Votes for Kingdom Governance Movement	
Totalvalidvotesfor_Kingdom_Governance_Movement=int(input("Enter Total Valid Votes for Kingdom Governance Movement:"))
#Get Total Valid Votes for Front National
Totalvalidvotesfor_Front_National=int(input("Enter Total Valid Votes for Front National:"))
#Get Total Valid Votes for Keep It Straight and Simple Party
Totalvalidvotesfor_Keep_It_Straight_and_Simple_Party=int(input("Enter Total Valid Votes for Keep It Straight and Simple Party:"))
#Get Total Valid Votes for Pan Africanist Movement
Totalvalidvotesfor_Pan_Africanist_Movement=int(input("Enter Total Valid Votes for Pan Africanist Movement:"))
#Get Total Vald Votes for First Nation Liberation Alliance 
Totalvalidvotesfor_First_Nation_Liberation_Alliance=int(input("Enter Total Valid Votes for First Nation Liberation Alliance:"))
#Get Total Valid Votes for United Congress
Totalvalidvotesfor_United_Congress=int(input("Enter Total Valid Votes for United Congress:"))
#Get Total Valid Votes for Peoples Alliance
Totalvalidvotesfor_Peoples_Alliance=int(input("Enter Total Valid Votes for People's Alliance:"))
#Decision Making

if Totalvalidvotesfor_African_National_Congress>Totalvalidvotes/2+1 :
    print("Congratulations to the African National Congress For Winning 2014 Election\n\n")
elif Totalvalidvotesfor_Democratic_Alliance>Totalvalidvotes/2+1: 
    print("Congratulations to the  Democratic Alliance For Winning 2014 Election\n\n")
elif Totalvalidvotesfor_Economic_Freedom_Fighters>Totalvalidvotes/2+1: 
    print("Congratulations to the Economic Freedom Fighters For Winning 2014 Election\n\n")
elif Totalvalidvotesfor_Inkatha_Freedom_Party>Totalvalidvotes/2+1: 
    print("Congratulations to the Inkatha Freedom Party For Winning 2014 Election\n\n")
elif Totalvalidvotesfor_National_Freedom_Party>Totalvalidvotes/2+1 :
        print("Congratulations to the National Freedom Party For Winning 2014 Election\n\n")
elif Totalvalidvotesfor_United_Democratic_Movement>Totalvalidvotes/2+1: 
    print("Congratulations to the United Democratic Movement For Winning 2014 Election\n\n")
elif Totalvalidvotesfor_Freedom_Front_Plus>Totalvalidvotes/2+1: 
    print("Congratulations to the Freedom Front Plus For Winning 2014 Election\n\n")
elif Totalvalidvotesfor_African_Christian_Democratic_Party>Totalvalidvotes/2+1 :
        print("Congratulations to the African Christian Democratic Party For Winning 2014 Election\n\n")
elif Totalvalidvotesfor_African_Independent_Congress>Totalvalidvotes/2+1: 
    print("Congratulations to the African Independent Congress For Winning 2014 Election\n\n")
elif Totalvalidvotesfor_Agang_South_Africa>Totalvalidvotes/2+1: 
    print("Congratulations to the Agang South Africa For Winning 2014 Election\n\n")
elif Totalvalidvotesfor_Pan_Africanist_Congress>Totalvalidvotes/2+1:
      print("Congratulations to the Pan Africanist Congress For Winning 2014 Election\n\n")
elif Totalvalidvotesfor_African_Peoples_Convention>Totalvalidvotes/2+1 :
        print("Congratulations to the African People's Convention For Winning 2014 Election\n\n")
elif Totalvalidvotesfor_Minority_Front>Totalvalidvotes/2+1: 
    print("Congratulations to the Minolity Party For Winning 2014 Election\n\n")
elif Totalvalidvotesfor_United_Christian_Democratic_Party>Totalvalidvotes/2+1: 
    print("Congratulations to the United Christian Democratic Party For Winning 2014 Election\n\n")
elif Totalvalidvotesfor_Azanian_Peoples_Organisation>Totalvalidvotes/2+1 :
        print("Congratulations to the Azanian Peoples Organisation For Winning 2014 Election\n\n")
elif Totalvalidvotesfor_Bushbuckridge_Residents_Association>Totalvalidvotes/2+1: 
    print("Congratulations to the Bushbuckridge Residents Association For Winning 2014 Election\n\n")
elif Totalvalidvotesfor_Independent_Civic_Organisation>Totalvalidvotes/2+1: 
    print("Congratulations to the Independent Civic Organisation For Winning 2014 Election\n\n")
elif Totalvalidvotesfor_Patriotic_Alliance>Totalvalidvotes/2+1 :
    print("Congratulations to the Patriotic Alliance For Winning 2014 Election\n\n")
elif Totalvalidvotesfor_Workers_and_Socialist_Party>Totalvalidvotes/2+1: 
    print("Congratulations to the Workers and Socialist Party For Winning 2014 Election\n\n")
elif Totalvalidvotesfor_Ubuntu_Party>Totalvalidvotes/2+1: 
    print("Congratulations to the Ubuntu Party 2014\n\n")
elif Totalvalidvotesfor_Kingdom_Governance_Movement>Totalvalidvotes/2+1 :
      print("Congratulations to the Kingdom Governance Movement For Winning 2014 Election\n\n")
elif Totalvalidvotesfor_Front_National>Totalvalidvotes/2+1: 
    print("Congratulations to the Front National you're a winner of 2014 election\n\n")
elif Totalvalidvotesfor_Keep_It_Straight_and_Simple_Party>Totalvalidvotes/2+1: 
    print("Congratulations to the Keep It Straight and Simple Party For Winning 2014 Election\n\n")
elif Totalvalidvotesfor_Pan_Africanist_Movement>Totalvalidvotes/2+1: 
    print("Congratulations to the Pan Africanist Movement For Winning 1994 Election\n\n")
elif Totalvalidvotesfor_First_Nation_Liberation_Alliance>Totalvalidvotes/2+1 :
     print("Congratulations to the First Nation Liberation Alliance For Winning 2014 Election\n\n")
elif Totalvalidvotesfor_United_Congress>Totalvalidvotes/2+1: 
    print("Congratulations to the United Congress For Winning 2014 Election\n\n")
elif Totalvalidvotesfor_Peoples_Alliance>Totalvalidvotes/2+1: 
    print("Congratulations to the Peoples Alliance For Winning 2014 Election\n\n")
else:
    print("No majority winner was found RUNOFF may be required\n")


print("__________________________________________________________ELECTION STATISTICS__________________________________________________________\n")
#calculating percentage 
#Calculating percentage for total votes cast
Percentage=round(Totalvalidvotes*percent/Totalvalidvotes, 2);
print("Total Votes Cast in percentage=",Percentage)
#Calculating percentage for total valid votes for all canidates
Percentage=round(Totalvalidvotes*percent/Totalvotescast, 2);
print("Total Valid Votes for all candidtes in percentage=",Percentage)
#Calculating percentage for null_&_void votes
Percentage=round(Nullandvoid*percent/Totalvalidvotes, 2);
print("Total Null_&_Void votes in percentage=",Percentage)
#Calculating percentage for Total Registered voters/turnout
Percentage=round(Totalvotescast*percent/TotalRegisteredvotes, 2);
print("Total Registered voters/turnout in percentage=",Percentage)
#Calculating percentage for African National Congress
Percentage=round(Totalvalidvotesfor_African_National_Congress*percent/Totalvalidvotes, 2);
print("Total Valid Votes for African National Congress in Percentage=",Percentage)
#Calculating percentage for Democratic Alliance
Percentage=round(Totalvalidvotesfor_Democratic_Alliance*percent/Totalvalidvotes, 2);
print("Total Valid Votes for Democratic Alliance in percentage=",Percentage)
#Calculating percentage for Economic Freedom Fighters
Percentage=round(Totalvalidvotesfor_Economic_Freedom_Fighters*percent/Totalvalidvotes, 2);
print("Total Valid Votes forEconomic Freedom Fighters in percentage=",Percentage) 
#Calculating percentage for Inkatha Freedom Party
Percentage=round(Totalvalidvotesfor_Inkatha_Freedom_Party*percent/Totalvalidvotes, 2);
print("Total Valid Votes for Inkatha Freedom Party  in percentage=",Percentage) 
#Calculating percentage for National Freedom Party
Percentage=round(Totalvalidvotesfor_National_Freedom_Party*percent/Totalvalidvotes, 2);
print("Total Valid Votes for National Freedom Party in Percentage=",Percentage)
#Calculating percentage for United Democratic Movement
Percentage=round(Totalvalidvotesfor_United_Democratic_Movement*percent/Totalvalidvotes, 2);
print("Total Valid Votes for United Democratic Movement in percentage=",Percentage)
#Calculating percentage for Freedom_Front_Plus
Percentage=round(Totalvalidvotesfor_Freedom_Front_Plus*percent/Totalvalidvotes, 2);
print("Total Valid Votes for Freedom Front Plus in percentage=",Percentage) 
#Calculating percentage for Congress of the People
Percentage=round(Totalvalidvotesfor_Congress_of_the_People*percent/Totalvalidvotes, 2);
print("Total Valid Votes for Congress of the People in Percentage=",Percentage)
#Calculating percentage for African Christian Democratic Party
Percentage=round(Totalvalidvotesfor_African_Christian_Democratic_Party*percent/Totalvalidvotes, 2);
print("Total Valid Votes for African Christian Democratic Party in percentage=",Percentage)
#Calculating percentage for African Independent Congress
Percentage=round(Totalvalidvotesfor_African_Independent_Congress*percent/Totalvalidvotes, 2);
print("Total Valid Votes for African Independent Congress in Percentage=",Percentage)
#Calculating percentage for Agang South Africa
Percentage=round(Totalvalidvotesfor_Agang_South_Africa*percent/Totalvalidvotes, 2);
print("Total Valid Votes for A gang South Africa in percentage=",Percentage)
#Calculating percentage for Pan Africanist Congress
Percentage=round(Totalvalidvotesfor_Pan_Africanist_Congress*percent/Totalvalidvotes, 2);
print("Total Valid Votes for Pan Africanist Congress in percentage=",Percentage)
#Calculating percentage for African People's Convention
Percentage=round(Totalvalidvotesfor_African_Peoples_Convention*percent/Totalvalidvotes, 2);
print("Total Valid Votes for African People's Convention in percentage=",Percentage) 
#Calculating percentage for Al_Jama ah
Percentage=round(Totalvalidvotesfor_Al_Jama_ah*percent/Totalvalidvotes, 2);
print("Total Valid Votes for Al_Jama ah in percentage=",Percentage) 
#Calculating percentage  for Minority Front
Percentage=round(Totalvalidvotesfor_Minority_Front*percent/Totalvalidvotes, 2);
print("Total Valid Votes for Minority Front in Percentage=",Percentage)
#Calculating percentage for United Christian Democratic Party 
Percentage=round(Totalvalidvotesfor_United_Christian_Democratic_Party*percent/Totalvalidvotes, 2);
print("Total Valid Votes for United Christian Democratic Party in percentage=",Percentage)
#Calculating percentage for Azanian Peoples Organisation
Percentage=round(Totalvalidvotesfor_Azanian_Peoples_Organisation*percent/Totalvalidvotes, 2);
print("Total Valid Votes for Azanian People's Organisation in percentage=",Percentage) 
#Calculating percentage for Bushbuckridge Residents Association
Percentage=round(Totalvalidvotesfor_Bushbuckridge_Residents_Association*percent/Totalvalidvotes, 2);
print("Total Valid Votes for Bushbuckridge Residents Association in Percentage=",Percentage)
#Calculating percentage for Independent Civic Organisation
Percentage=round(Totalvalidvotesfor_Independent_Civic_Organisation*percent/Totalvalidvotes, 2);
print("Total Valid Votes for Independent Civic Organisation in percentage=",Percentage)
#Calculating percentage for Patriotic Alliance
Percentage=round(Totalvalidvotesfor_Patriotic_Alliance*percent/Totalvalidvotes, 2);
print("Total Valid Votes for Patriotic Alliance in percentage=",Percentage)
#Calculating percentage for Workers and Socialist Party
Percentage=round(Totalvalidvotesfor_Workers_and_Socialist_Party*percent/Totalvalidvotes, 2);
print("Total Valid Votes for Workers and Socialist Party in percentage=",Percentage)
#Calculating percentage for Ubuntu Party
Percentage=round(Totalvalidvotesfor_Ubuntu_Party*percent/Totalvalidvotes, 2);
print("Total Valid Votes for Ubuntu Party in percentage=",Percentage)
#Calculating percentage for Kingdom Governance Movement
Percentage=round(Totalvalidvotesfor_Kingdom_Governance_Movement*percent/Totalvalidvotes, 2);
print("Total Valid Votes for Kingdom Governance Movement in percentage=",Percentage) 
#Calculating percentage for Front National
Percentage=round(Totalvalidvotesfor_Front_National*percent/Totalvalidvotes, 2);
print("Total Valid Votes for Front National in percentage=",Percentage)
#Calculating percentage for Keep It Straight and Simple Party
Percentage=round(Totalvalidvotesfor_Keep_It_Straight_and_Simple_Party*percent/Totalvalidvotes, 2);
print("Total Valid Votes for Keep It Straight and Simple Party in percentage=",Percentage) 
#Calculating percentage for Pan Africanist Movement
Percentage=round(Totalvalidvotesfor_Pan_Africanist_Movement*percent/Totalvalidvotes, 2);
print("Total Valid Votes for Pan Africanist Movement in percentage=",Percentage)
#Calculating percentage for First Nation Liberation Alliance
Percentage=round(Totalvalidvotesfor_First_Nation_Liberation_Alliance*percent/Totalvalidvotes, 2);
print("Total Valid Votes for First Nation Liberation Alliance  in percentage=",Percentage) 
#Calculating percentage for United Congress
Percentage=round(Totalvalidvotesfor_United_Congress*percent/Totalvalidvotes, 2);
print("Total Valid Votes for United Congress in percentage=",Percentage) 
#Calculating percentage for People's Alliance
Percentage=round(Totalvalidvotesfor_Peoples_Alliance*percent/Totalvalidvotes, 2);
print("Total Valid Votes for People's Alliance in percentage=",Percentage)


print("=========================================================================================================================\n")















