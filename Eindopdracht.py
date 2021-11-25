print("Hallo en welkom bij mijn gameshop The Dungeon!")

name= input("Wat is uw naam?\n")

print ("\n Hallo " + name +", Dankuwel dat u mijn gameshop heeft gekozen.\n")

menu_games= "Valorant,League Of Legends,Fifa,Clash Royale,Pubg,Csgo,Rainbow Six Siege"

print (name +" Welke games wilt u halen?\nVan uit deze games kunt u kiezen.\n" + menu_games)

order= input()

if order == "Valorant" or order =="League Of Legends" or order =="Fifa" or order =="Clash Royale" or order =="Pubg" or order =="Csgo" or order =="Rainbow Six Siege"  :

  print ("\nJij hebt echt smaak voor games! " + name +", Ik heb het genoteerd ik kom zo bij u terug." +"\n nog even geduld moet achterin gaan kijken.\n")
  print ("Dankuwel voor het wachten hier is uw "+ order)

elif order !=menu_games:
    print ("Sorry maar" + order +"\nhebben wij helaas niet")
    
print ("Fijne dag nog verder!")