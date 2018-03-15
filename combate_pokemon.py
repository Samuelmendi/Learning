
pokemon_elegido = input("Contra que pokemon quieres combatir? (Squirtle / Charmander / Bulbasour): ")

vida_pikachu = 100
vida_enemigo = 0
ataque_enemigo = 0

if pokemon_elegido == "Squirtle":
    vida_enemigo = 90
    ataque_enemigo = 8

elif pokemon_elegido == "Charmander":
    vida_enemigo = 80
    ataque_enemigo = 7

else:
    pokemon_elegido == "Bulbasour"
    vida_enemigo = 100
    ataque_enemigo = 10
while vida_pikachu > 0 and vida_enemigo > 0:
    ataque_elgido = input("Que ataque vamos a usar? (Chispazo / Bola voltio): ")

    if ataque_elgido == "Chispazo":
        print("Has atacado a {} con Chispazo (10 de daño)".format(pokemon_elegido))
        vida_enemigo -= 10

    if ataque_elgido == "Bola voltio":
        print("Has atacado a {} con Bola voltio (12 de daño)".format(pokemon_elegido))
        vida_enemigo -= 12

    print("La vida actual de {} es {}".format(pokemon_elegido,vida_enemigo))

    print("{} te hace un ataque de {} de daño".format(pokemon_elegido,ataque_enemigo))
    vida_pikachu -= ataque_enemigo

    print("Tu vida actual es de {}".format(vida_pikachu))

if vida_pikachu > 0:
    print("Has ganado")
else:
    print("Te han partido la madre bro.")


print("El combate ha terminado")


