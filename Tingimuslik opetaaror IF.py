from datetime import date
#1
nimi=input("Kas sinu nimi on Juku?(vastused:jah/ei): ")
if nimi=="jah":
    print("Lähme kinno, Juku!")
    vanus=int(input("Kui vana sa oled?: "))
    if vanus<=6 and vanus>=1:
        print("Sinu pilet on tasuta")
    elif vanus>=6 and vanus<=14:
        print("Sinu pilet on lastepilet")
    elif vanus>=15 and vanus<=65:
        print("Sinu pilet on täispilet")
    elif vanus>=65 and vanus<=99:
        print("Sinu pilet on sooduspilet")
    else:
        print("Viga andmetega")
else:
    print("Head aega.")




#2
inimene1=input("Number 1, mis on teie nimi?: ")
inimene2=input("Number 2, aga teie nimi?: ")
if inimene1=="Mart" and inimene2=="Mari":
    print("Te olete pinginaabrid!")
else:
    print("Kahjuks, te ei ole pinginaabrid.")




#3
a=float(input("Mis on esimene seina pikkus?: "))
b=float(input("Mis on teine seina pikkus?: "))
if a>0 and b>0:
    ruut1=a*b
    print("Põranda pindala on: {0}".format(ruut1))
else:
    print("Vale andmet!")



#4
hind=float(input("Kas te tahate remondi? Sisestage ruutmetri hind: "))
if hind>0:
    hind1=ruut1*hind
    print("Ruutmeetri hind on: {0}".format(hind1))
    if hind1>700:
        soodustus=(hind1/100)*70
        print("Teie täis hind soodustusega 30% on: {0}".format(soodustus))
else: 
    print("Vale andmed")


#5
temperatuur=float(input("Praegu temperatuur: "))
if 40>temperatuur>18:
    print("See on rohkem kui 18. Tee vähem.")

else:
    print("Viga")
    




#6
pikkus=int(input("Mis on teie pikkus?: "))
if pikkus>=120 and pikkus<=149:
    print("Te olete lühike.")
elif pikkus>=150 and pikkus<=179:
    print("Te olete keskmine.")
elif pikkus>=180:
    print("Te olete pikk.")
else:
    print("Viga")


#7
pikkus=int(input("Mis on teie pikkus?: "))
sugu=input("mees/naine?(m/n): ")
if sugu=="m":
    sugu="mees"
else:
    sugu="naine"
if pikkus>=120 and pikkus<=149:
    print("Te olete lühike {0}.".format(sugu))
elif pikkus>=150 and pikkus<=179:
    print("Te olete keskmine {0}.".format(sugu))
elif pikkus>=180:
    print("Te olete pikk {0}.".format(sugu))
else:
    print("viga")

#8


#9
külje1=int(input("Esimene külje: "))
külje2=int(input("Teine külje: "))
if külje1==külje2:
    print("See on ruut.")
else:
    print("See ei ole ruut.")

#10
try:
    a=float(input("Esimene arv:"))
    try:
        b=float(input("Teine arv:"))
        t=input("Tehe(+,-,/,*):")
        if t in ['+','-','/','*']: 
            if t=='+':
                v=a+b
            elif t=='-':
                v=a-b
            elif t=='*':
                v=a*b
            elif t=='/':
                if b==0:
                    v="DIV/0"
                else:
                    v=a/b
            print("{0}{1}{2}={3}".format(a,t,b,v))
        else:
            print("Tundmatu märk")
    except:
        print("Vale b arvu andmetüüp")

except:
    print("vale a arvu andmetüüp")

#11
sp=date(int(input("Sünniaasta: ")),int(input("Sünnikuu: ")), int(input("Sünnipäev: ")))
praegu=date.today().year #2023

if (praegu-sp.year)%5==0:#sp>date(2000,1,1):
    print("Juubel")
else:
    print("----")

#12


#13


#14


