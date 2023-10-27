Var =["revo","motor","200cc","hitam",2]
Var.append ("Rp21jt"".""standar")
Var.insert (2,"honda")
print(Var[6])


pilihan = input("Masukan pilihan 1 untuk persegi, 2 untuk lingkaran, 3 untuk segitiga: ")
match pilihan:
    case "1":
        s = int(input("masukan sisi: "))
        persegi = s*s
        print('luas persegi', persegi)
    case "2":
        phi = 3.14
        r = int(input("masukkan jari: "))
        lingkaran = phi*r*r
        print('luas lingkaran', lingkaran)
    case "3":
        l = 1/2
        a = int(input("masukan alas: "))
        t =  int(input("masukan tinggi: "))
        segitiga = l*a*t
        print("luas segitiga", segitiga)
    case _:
       print("pilihan tidak tersedia")