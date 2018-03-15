number_to_guess = 3

user_number = int(input("Adivina un numero: "))

if user_number == number_to_guess:
    print("Has ganado")
else:
    print ("Intenta otra vez")
    user_number = int(input("Adivina un numero: "))
    if user_number == number_to_guess:
        print("Has ganado")
    else:
        print("Intenta otra vez")
        user_number = int(input("Adivina un numero: "))
        if user_number == number_to_guess:
            print("Has ganado")
        else:
            print("Intenta otra vez")
            user_number = int(input("Adivina un numero: "))
            if user_number == number_to_guess:
                print("Has ganado")
            else:
                print("Intenta otra vez")
                user_number = int(input("Adivina un numero: "))
                if user_number == number_to_guess:
                    print("Has ganado")
                else:
                    print("Has perdido")