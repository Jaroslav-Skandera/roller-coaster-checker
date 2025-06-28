print("=======================")
print("Vítejte na horské dráze")
print("========================")

value = 0

# výška zákazníka
while True:
    try:
        height = int(input("Zadej výšku v cm:\n"))
        break
    except ValueError:
        print("Zadali jste neplatný vstup. Zadejte prosím číslo.")

if height >= 87:
    print("Super výška je ok")

    # věk
    while True:
        try:
            age = int(input("Mohu se zeptat, kolik je Vám let?\n"))
            break
        except ValueError:
            print("Zadali jste neplatný vstup. Zadejte prosím číslo.")

    if age <= 14:
        value += 100
        print("Váš lístek bude stát 100 Kč.")
    elif age <= 17:
        value += 150
        print("Váš lístek bude stát 150 Kč.")
    else:
        value += 200
        print("Váš lístek bude stát 200 Kč.")

    # Photo
    photo = input("Chci se zeptat, máte zájem o fotku během jízdy? Stojí 30 Kč (Ano / Ne)\n").lower()
    if photo == "ano":
        value += 30
        print("Super, snad se vám bude líbit.")
    else:
        print("Nevadí.")

    # Finální odpověď
    print(f"Super! Doufáme, že se vám bude líbit naše atrakce a že si jízdu užijete. Celková cena je {value} Kč.")

    #konec
    konec = input("Zmáčkněte libovolnou klavesu....")
    exit()



else:
    print("Bohužel nesplňujete výšku, zkuste to až povyrostete.")
    #konec
    konec = input("Zmáčkněte libovolnou klavesu....")
    exit()