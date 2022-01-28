def func(line): #funkcijas izveide
  count = 0 #skaitītājs
  for i in line: #vērtības piešķiršana
    if i == '_':
      count += 1 #simbolu skaita noteikšana
  print("Apakšējo līniju skaits tekstā ir", count, ".") #teksta izvade uz ekrāna
  line = line.replace("_", " ") #aizstāšana ar space
  print("Jūsu rezultāts ir" +line) #rezultāta izvade uz ekrāna

line = input("Ievadiet tekstu!") #iespēja ievadīt tekstu
func(line) #funkcijas izsaukšana