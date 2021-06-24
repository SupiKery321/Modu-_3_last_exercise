print("Zadanie 1")
Lista_zakupow = {
    "piekarnia": ["chleb", "bułki", "pączek"],
    "warzywniak": ["marchew", "seler", "rukola"]
}


ile = 0
for key in Lista_zakupow:
  lista = [a.capitalize() for a in Lista_zakupow[key]]
  print("Idę do", key.capitalize(), "i kupuję tam", lista)
  ile = ile + len(Lista_zakupow[key])
print("W sumie kupuję", ile , "produktów")

print("Zadanie 2")
for number in range(0,101):
    if number % 5 == 0:
        print(number**3)

print("supi_learns_branch")