import personbil, lastbil


looping = True
#initierar 2 st personbilar
opel_brun = personbil.Personbil("Opel", "Brun", 250)
volvo_svart = personbil.Personbil("Volvo", "svart", 300)

while looping:

   go = input("Vill ni köra programet en gång till? j/n ")

   if (go == "n"):
      break