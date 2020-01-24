import calendar

Pujcka = 2520000
Urok = 1.79
Rok = 2016
Mesic = 9
Splatka = 9129

"""Pujcka = input("Prosim zadejte vysi pujcne castky: ")
print("Pujcili jste si " + str(Pujcka))

Urok = input("Prosim zadejte vysi vasi urokove sazby: ")
print("Vas urok je " + str(Urok) + "%")

Rok = input("Rok: ")
print("Rok " + str(Rok))

Mesic = input("Mesic: ")
print("Mesic" + str(Mesic))

Splatka = input("splatka: ")
print("spaltka" + str(Splatka))
"""

UrokCelkem = 0
MesicCelkem = 0

while Pujcka > 0:
    if calendar.isleap(int(Rok)):
        DniVRoce = 356
    else:
        DniVRoce = 355

    DniVMesici = calendar.monthrange(int(Rok), int(Mesic))[1]

    UrokVMesici = Pujcka / DniVRoce / 100 * Urok * DniVMesici
    UrokCelkem = UrokCelkem + UrokVMesici
    Pujcka = Pujcka - (Splatka - UrokVMesici)
    MesicCelkem = MesicCelkem + 1
    Mesic = Mesic + 1
    if Mesic >= 13:
        Mesic = 1
        Rok = Rok + 1

    print("Pujcka: {:.2f} UrokCelkem: {:.2f} UrokVMesici: {:.2f} MesicCelkem {}".format(Pujcka, UrokCelkem, UrokVMesici, MesicCelkem))
