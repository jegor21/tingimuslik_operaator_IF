#võileib
soov=input("Kas tahad süüa?:").lower()
if soov=="jah" or soov=="yes" or soov=="да":
    valik=int(input("1-juustuga võileib \n2-vorstiga võileib ==>"))
    if valik in [1,2]:
        if valik == 1:
            print("Palun juustuga võileib!")
        else:
            print("Palun voorstiga võileib!")
    else:
        print("Vale valik!")
else:
    print("Ei taha, siis ei taha")



#тодация

grupp=input("Rühma nimetus: ")
if grupp=="TARgv23":
    puudumised=int(input("Mitu puudumist sul on?: "))
    if puudumised<15:
        hinned=float(input("Mis on keskmine hinne?: "))
        if hinned>3.8:
            print("Toetust!")
        else:
            print("Liiga madal keskmine hind. Toetust ei ole!")
    else:
        print("Toetus ei määratakse")
else:
    print("Rühma nimetus ei sobi.")

grupp=input("Rühma nimetus: ")
puudumised=int(input("Mitu puudumist sul on?: "))
hinne=float(input("Mis on keskmine hind?: "))
if grupp=="TARgv23" and puudumised<15 and hinne>3.8:
    print("Toetus!")
else:
    print("Toetust ei ole!")

#m ja n
m=float(input("Kui palju kallub m?: "))
n=float(input("Kui palju kallub n?: "))
if m>n:
    v="m kallub rohkem kui n"
elif m<n:
    v="m kallub vähem kui n"
elif m==n:
    v="m=n"
print(v)




#kalkulaator
try:
    a=float(input("Esimene arv:"))
    try:
        b=float(input("Teine arv:"))
        t=input("Tehe:")
        if t in ['+','-','/','*','**','%','//']: #''="
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
            elif t=='**':
                v=a**b
            elif t=='%':
                v=a%b
            else:
                v=a//b
            print("{0}{1}{2}={3}".format(a,t,b,v))
        else:
            print("Tundmatu märk")
    except:
        print("Vale b arvu andmetüüp")

except:
    print("vale a arvu andmetüüp")



#kolmnurk
a=float(input("Alpha:"))
b=float(input("Betta:"))
c=float(input("Gamma:"))
if a>0 and b>0 and c>0:
    if a+b+c==180:
        print("Kolmnurk")
    else:
        print("Nurgad")
else:
    print("Andmed ei ole õiged")
