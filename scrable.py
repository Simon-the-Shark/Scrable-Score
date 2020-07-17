import time

punkty = {
    "a": 1, "A": 5, "b": 3, "c": 2, "C": 5, "d": 2, "e": 1, "E": 5, "f": 5, "g": 3, "h": 3, "i": 1, "j": 3, "k": 2,
    "l": 2, "L": 3, "m": 2, "n": 1, "N": 7, "o": 1, "O": 5, "p": 2, "r": 1, "s": 1, "S": 5, "t": 2, "u": 3, "w": 1,
    "y": 2, "z": 1, "Z": 9, "X": 5
}


def score(w):
    sc = 0
    for l in w:
        if l not in punkty:
            print(" litera"),
            print(l)
            print("nie istnieje w indeksie")
            print
            return sc
    for l in w:
        sc += punkty[l]
    print(w),
    print(sc)
    print
    return sc


def player2(pp1, pp2):
    p1 = pp1
    p2 = pp2
    slw = ""
    gr = ""
    while slw != "stop!" or gr != "stop!":
        gr = input("który gracz?")
        slw = input("jakie slowo?")
        if slw == "wyniki!" or gr == "wyniki!":
            print("gracz1"),
            print(p1)
            print("gracz2"),
            print(p2)
            print
        elif slw == "stop!" or gr == "stop!":
            break
        elif gr == "gracz1":
            p1 = p1 + score(slw)
        elif gr == "gracz2":
            p2 = p2 + score(slw)
        else:
            print("nie ma takiego gracza")
            print
            player2(p1, p2)
    print
    print("GRACZ PIERWSZY UZYSKAŁ:")
    print(p1),
    print("PUNKTÓW")
    print
    print("GRACZ DRUGI UZYSKAŁ:")
    print(p2),
    print("PUNKTÓW")
    print
    for i in range(9999):
        time.sleep(999)


def x22(p1, p2):
    print("w pytaniu o nazwe gracza proszę podawac tylko gracz1 lub gracz2.")
    print(
        "aby wyswietlić wyniki w pytaniu o gracza lub pytaniu o slowo nalezy wpisac wyniki!. Aby zakończyc grę i wyświetlic wyniki nalezy w pytaniu(dowolnym) wpisac stop!")
    print
    print("(nacisnij enter aby rozpoczac gre)")
    gagak = input("|~>")
    print
    player2(p1, p2)


def x33(p1, p2, p3):
    print("W pytaniu o nazwę gracza proszę podawac jedynie gracz1, gracz2 lub gracz3.")
    print(
        "aby wyswietlić wyniki w pytaniu o gracza lub pytaniu o slowo nalezy wpisac wyniki!. Aby zakończyc grę i wyświetlic wyniki nalezy w pytaniu(dowolnym) wpisac stop!")
    print
    print("(nacisnij enter aby rozpoczac gre)")
    gahsksjsjjj = input("|~>")
    print
    player3(p1, p2, p3)


def player3(pp1, pp2, pp3):
    p1 = pp1
    p2 = pp2
    p3 = pp3
    slw = ""
    gr = ""
    while slw != "stop!" or gr != "stop!":
        gr = input("który gracz?")
        slw = input("jakie slowo?")
        if slw == "wyniki!" or gr == "wyniki!":
            print("gracz1"),
            print(p1)
            print("gracz2"),
            print(p2)
            print
        elif slw == "stop!" or gr == "stop!":
            break
        elif gr == "gracz1":
            p1 = p1 + score(slw)
        elif gr == "gracz2":
            p2 = p2 + score(slw)
        elif gr == "gracz3":
            p3 = p3 + score(slw)
        else:
            print("nie ma takiego gracza")
            print
            player3(p1, p2, p3)
    print
    print("GRACZ PIERWSZY UZYSKAŁ:")
    print(p1),
    print("PUNKTÓW")
    print
    print("GRACZ DRUGI UZYSKAŁ:")
    print(p2),
    print("PUNKTÓW")
    print
    print(" GRACZ TRZECI UZYSKAL:")
    print(p3),
    print("PUNKTOW")
    for i in range(9999):
        time.sleep(999)


def x22(p1, p2):
    print("w pytaniu o nazwe gracza proszę podawac tylko gracz1 lub gracz2.")
    print(
        "aby wyswietlić wyniki w pytaniu o gracza lub pytaniu o slowo nalezy wpisac wyniki!. Aby zakończyc grę i wyświetlic wyniki nalezy w pytaniu(dowolnym) wpisac stop!")
    print
    print("(nacisnij enter aby rozpoczac gre)")
    gagak = input("|~>")
    print
    player2(p1, p2)


def player4(pp1, pp2, pp3, pp4):
    p1 = pp1
    p2 = pp2
    p3 = pp3
    p4 = pp4
    slw = ""
    gr = ""
    while slw != "stop!" or gr != "stop!":
        gr = input("który gracz?")
        slw = input("jakie slowo?")
        if slw == "wyniki!" or gr == "wyniki!":
            print("gracz1"),
            print(p1)
            print("gracz2"),
            print(p2)
            print("gracz3"),
            print(p3)
            print("gracz4"),
            print(p4)
            print
            
        elif slw == "stop!" or gr == "stop!":
            break
        elif gr == "gracz1":
            p1 = p1 + score(slw)
        elif gr == "gracz2":
            p2 = p2 + score(slw)
        elif gr == "gracz3":
            p3 = p3 + score(slw)
        elif gr == "gracz4":
            p4 = p4 + score(slw)
        else:
            print("nie ma takiego gracza")
            print
            player4(p1, p2, p3, p4)
    print
    print("GRACZ PIERWSZY UZYSKAŁ:")
    print(p1),
    print("PUNKTÓW")
    print
    print("GRACZ DRUGI UZYSKAŁ:")
    print(p2),
    print("PUNKTÓW")
    print
    print(" GRACZ TRZECI UZYSKAL:")
    print(p3),
    print("PUNKTOW")
    print
    print("GRACZ CZWARTY UZYSKAL:")
    print(p4),
    print("PUNKTOW")
    for i in range(9999):
        time.sleep(999)


def x44(p1, p2, p3, p4):
    print("W pytaniu o nazwę gracza proszę podawac jedynie gracz1, gracz2, gracz3 lub gracz4.")
    print(
        "aby wyswietlić wyniki w pytaniu o gracza lub pytaniu o slowo nalezy wpisac wyniki!. Aby zakończyc grę i wyświetlic wyniki nalezy w pytaniu(dowolnym) wpisac stop!")
    print
    print("(nacisnij enter aby rozpoczac gre)")
    gahsksjsjjj = input("|~>")
    print
    player4(p1, p2, p3, p4)


def start():
    print("witam w liczniku puktów w Scrable")
    print("aby dowiedziec sie o polskich znakach napisz pomoc aby zignorowac nacisnij enter")
    qwe = input("|~>")
    if qwe.lower() == "pomoc":
        pomoc()
    else:
        stt()


def pomoc():
    print("ten program niestety nie przyjmuje polskich znakow")
    print("ale to nie oznacza ze nie darady policzyć za nie punktow")
    print("aby policzyc punkty za znak polski nalezy napisac znak podobny do tego z WIELKIEJ LITERY.")
    print(" polskie znaki napisane alfabetycznie to:")
    print("A,C,E,L,N,O,S,Z,X")
    print("UWAGA: zwroc uwage ma litery pochodne od z")
    ddd = input("( aby wyswietlic caly dostepny alfabet i ilosc punktow  wpisz alf , a zeby pominac nacisnij enter)")
    if ddd == "alf":
        print(punkty)
    stt()


def stt():
    print
    print("ile jest uczestników???")
    rty = str(input(">"))
    if rty == "2":
        x22(0, 0)
    elif rty == "3":
        x33(0, 0, 0)
    elif rty == "4":
        x44(0, 0, 0, 0)
    else:
        print("niestety w scrable mozna grac tylko w 2,3 lub 4 osoby")
    stt()
start()
