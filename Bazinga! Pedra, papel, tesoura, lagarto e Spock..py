from random import choice

lista = ['tesoura', 'papel', 'pedra', 'lagarto', 'spock']

p0 = 'EMPATE! Vamos de novo.'
p1 = 'Tesoura corta papel'
p2 = 'Papel cobre rocha'
p3 = 'Rocha esmaga lagarto'
p4 = 'Lagarto envenena Spock'
p5 = 'Spock esmaga tesouras'
p6 = 'Tesoura decapita lagarto'
p7 = 'Lagarto come papel'
p8 = 'Papel refuta Spock'
p9 = 'Spock vaporiza a rocha'
p10 = 'Rocha esmaga tesoura'

c = 'Bazinga! '
c1 = 'Raj, trapaceu. De novo! '



print('-'*50)
escolhido1 = choice(lista)
escolhido2 = choice(lista)
print('1. tesoura corta papel;\n2. papel cobre rocha;\n3. rocha esmaga lagarto;\n4. lagarto envenena Spock;\n5. Spock esmaga tesouras;\n6. tesoura decapita lagarto;\n7. lagarto come papel;\n8. papel refuta Spock;\n9. Spock vaporiza a rocha;\n10. pedra esmaga tesoura.')
print('-'*50)
choice1 = input("Sheldon, says: - Come on, Raj. You know that I will win! Ready?  [Y / N]")
if 'y' in choice1:
    if escolhido1 == 'tesoura':
        print("tesoura")
    elif escolhido1 == 'papel':
        print("papel")
    elif escolhido1 == 'pedra':
        print("Pedra")
    elif escolhido1 == 'lagarto':
        print("Lagarto")
    elif escolhido1 == 'spock':
        print("Spock")
else:
    print("De novo!")
    exit()

choice2 = input("Rajesh says: - 'Ready????'  [Y / N]")
if 'y' in choice2:
    if escolhido2 == 'tesoura':
        print("tesoura")
    elif escolhido2 == 'papel':
        print('papel')
    elif escolhido2 == 'pedra':
        print("Pedra")
    elif escolhido2 == 'lagarto':
        print("Lagarto")
    elif escolhido2 == 'spock':
        print("Spock")
else:
    print("De novo!")
    exit()
    print('')
if ('tesoura' in escolhido1 and 'tesoura' in escolhido2) or ('papel' in escolhido1 and 'papel' in escolhido2) or ('pedra' in escolhido1 and 'pedra' in escolhido2) or ('lagarto' in escolhido1 and 'lagarto' in escolhido2) or ('spock' in escolhido1 and 'spock' in escolhido2):
    print(p0)
elif 'tesoura' in escolhido1 and 'papel' in escolhido2:
    print(c + p1)
elif 'papel' in escolhido1 and 'pedra' in escolhido2:
    print(c + p2)
elif 'pedra' in escolhido1 and 'lagarto' in escolhido2:
    print(c + p3)
elif 'lagarto' in escolhido1 and 'spock' in escolhido2:
    print(c + p4)
elif 'spock' in escolhido1 and 'tesoura' in escolhido2:
    print(c + p5)
elif 'tesoura' in escolhido1 and 'lagarto' in escolhido2:
    print(c + p6)
elif 'lagarto' in escolhido1 and 'papel' in escolhido2:
    print(c + p7)
elif 'papel' in escolhido1 and 'spock' in escolhido2:
    print(c + p8)
elif 'spock' in escolhido1 and 'pedra' in escolhido2:
    print(c + p9)
elif 'pedra' in escolhido1 and 'tesoura' in escolhido2:
    print(c + p10)

elif 'tesoura' in escolhido2 and 'papel' in escolhido1:
    print(p1)
    print(c1)
elif 'papel' in escolhido2 and 'pedra' in escolhido1:
    print(p2)
    print(c1)
elif 'pedra' in escolhido2 and 'lagarto' in escolhido1:
    print(p3)
    print(c1)
elif 'lagarto' in escolhido2 and 'spock' in escolhido1:
    print(p4)
    print(c1)
elif 'spock' in escolhido2 and 'tesoura' in escolhido1:
    print(p5)
    print(c1)
elif 'tesoura' in escolhido2 and 'lagarto' in escolhido1:
    print(p6)
    print(c1)
elif 'lagarto' in escolhido2 and 'papel' in escolhido1:
    print(p7)
    print(c1)
elif 'papel' in escolhido2 and 'spock' in escolhido1:
    print(p8)
    print(c1)
elif 'spock' in escolhido2 and 'pedra' in escolhido1:
    print(p9)
    print(c1)
elif 'pedra' in escolhido2 and 'tesoura' in escolhido1:
    print(p10)
    print(c1)