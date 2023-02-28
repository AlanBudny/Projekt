from random import randint
from classpokemony import Mystats,Enemystats
killcount = 0
iloscatak1 = 20 
iloscatak2 = 20 
iloscatak3 = 20 
iloscatak4 = 20 
leczmale = int(0)
leczsrednie = int(0)
leczduze = int(0)
    # MOJE POKI
def bulbasaur():
    Mystats.name = 'bulbasaur'
    Mystats.hpmoje = 100
    Mystats.atak1 = 20
    Mystats.atak2 = 10
    Mystats.atak3 = 1
    Mystats.atak4 = 15
def charmander():
    Mystats.name = 'charmander'
    Mystats.hpmoje = 120
    Mystats.atak1 = 40
    Mystats.atak2 = 15
    Mystats.atak3 = 20
    Mystats.atak4 = 10
def squirtle():
    Mystats.name = 'squirtle'
    Mystats.hpmoje = 90
    Mystats.atak1 = 20
    Mystats.atak2 = 5
    Mystats.atak3 = 15
    Mystats.atak4 = 10
def pikachu():
    Mystats.name = 'pikachu'
    Mystats.hpmoje = 150
    Mystats.atak1 = 50
    Mystats.atak2 = 40
    Mystats.atak3 = 30
    Mystats.atak4 = 35
def ratata():
    Mystats.name = 'rattata'
    Mystats.hpmoje = 50
    Mystats.atak1 = 10
    Mystats.atak2 = 15
    Mystats.atak3 = 7
    Mystats.atak4 = 3
def pidgey():
    Mystats.name = 'pidgey'
    Mystats.hpmoje = 65
    Mystats.atak1 = 20
    Mystats.atak2 = 15
    Mystats.atak3 = 10
    Mystats.atak4 = 8
def growlite():
    Mystats.name = 'growlite'
    Mystats.hpmoje = 200
    Mystats.atak1 = 80
    Mystats.atak2 = 60
    Mystats.atak3 = 40
    Mystats.atak4 = 20
    # PRZECIWNIK POKI
def bulbasaurenemy():
    Enemystats.nameenemy = 'bulbasaur'
    Enemystats.hpenemy = 100
    Enemystats.atakenemy = 20
def charmanderenemy():
    Enemystats.nameenemy = 'charmander'
    Enemystats.hpenemy = 120
    Enemystats.atakenemy = 40
def squirtleenemy():
    Enemystats.nameenemy = 'squirtle'
    Enemystats.hpenemy = 90
    Enemystats.atakenemy = 20
def pikachuenemy():
    Enemystats.nameenemy = 'pikachu'
    Enemystats.hpenemy = 150
    Enemystats.atakenemy = 50
def ratataenemy():
    Enemystats.nameenemy = 'rattata'
    Enemystats.hpenemy = 50
    Enemystats.atakenemy = 10
def pidgeyenemy():
    Enemystats.nameenemy = 'pidgey'
    Enemystats.hpenemy = 65
    Enemystats.atakenemy = 20
def growliteenemy():
    Enemystats.nameenemy = 'growlite'
    Enemystats.hpenemy = 200
    Enemystats.atakenemy = 5
# WYBOR POKEMONA--------------------------------------------------------------------------------------------
def wybor():
    global mojlevel,money
    money = 0
    argbh = input('Witaj miszczu pokemon,')
    argbh = input('To ja Profesor DĄB')
    argbh = input('Wybierz pokemona startowego')
    argbh = input('Masz do wyboru:')
    argbh = input('1-Bulbasaur')
    argbh = input('2-Charmander')
    argbh = input('3-Squirtle')
    inp = float(input('Co wybierasz? ').lower())
    if inp == 1:
        bulbasaur()
    elif inp == 2:
        charmander()
    elif inp == 3:
        squirtle()
    else:
        argbh = input('eee')
        argbh = input('nie chcesz żadnych z tych?')
        argbh = input('czekaj mam pomysł')
        argbh = input('nie wiedziałem, że jesteś analfabetą')
        argbh = input('nie ważne jak nie chcesz żadnych z tamtych to dostaniesz:')
        argbh = input('prądownice z amazona za 15 centów')
        pikachu()
    mojlevel = 1
    print('\n')
# DOPASOWANIE Z LEVELEM-------------------------------------------------------------------------------------
def losowanko():
    global pok
    pok = randint(1,7)
    if pok == 1: bulbasaurenemy()
    if pok == 2: charmanderenemy()
    if pok == 3: squirtleenemy()
    if pok == 4: pikachuenemy()
    if pok == 5: ratataenemy()
    if pok == 6: pidgeyenemy()
    if pok == 7: growliteenemy()
def przeciwnik():
    global levelenemy,hpenemyend,atakenemyend,levelenemy

    levelenemy = int(mojlevel + randint(-5,5))
    if levelenemy <= 0:
        levelenemy = 1
    
    atakenemyend = Enemystats.atakenemy + (randint(-5,5)* levelenemy)
    if atakenemyend <= 0:
        atakenemyend = 1

    hpenemyend = Enemystats.hpenemy + 10 + levelenemy/2
    if killcount >= 1:
        hpenemyend /= 3
def mojpokemon():
    global hpmojeend,atak4end,atak3end,atak2end,atak1end
    hpmojeend = Mystats.hpmoje + mojlevel/2
    atak1end = Mystats.atak1 + mojlevel/2
    atak2end = Mystats.atak2 + mojlevel/2
    atak3end = Mystats.atak3 + mojlevel/2
    atak4end = Mystats.atak4 + mojlevel/2
# EWOLUCJE--------------------------------------------------------------------------------------------------
def evolucja():
    if Mystats.name == 'bulbasaur' and mojlevel == 16:
        print(f'Gratulacje!!! Twój pokemon ewoluował z {Mystats.name}')
        Mystats.name = 'ivysaur'
        print(f'do {Mystats.name}')
    if Mystats.name == 'ivysaur' and mojlevel == 32:
        print(f'Gratulacje!!! Twój pokemon ewoluował z {Mystats.name}')
        Mystats.name = 'venusaur'
        print(f'do {Mystats.name}')
    if Mystats.name == 'charmander' and mojlevel == 16:
        print(f'Gratulacje!!! Twój pokemon ewoluował z {Mystats.name}')
        Mystats.name = 'charmeleon'
        print(f'do {Mystats.name}')
    if Mystats.name == 'charmeleon' and mojlevel == 32:
        print(f'Gratulacje!!! Twój pokemon ewoluował  {Mystats.name}')
        Mystats.name = 'charizard'
        print(f'do {Mystats.name}')
    if Mystats.name == 'squirtle' and mojlevel == 16:
        print(f'Gratulacje!!! Twój pokemon ewoluował z {Mystats.name}')
        Mystats.name = 'wartortle'
        print(f'do {Mystats.name}')
    if Mystats.name == 'watrortle' and mojlevel == 32:
        print(f'Gratulacje!!! Twój pokemon ewoluował z {Mystats.name}')
        Mystats.name = 'blastoise'
        print(f'do {Mystats.name}')
    if Mystats.name == 'pidey' and mojlevel == 18:
        print(f'Gratulacje!!! Twój pokemon ewoluował z {Mystats.name}')
        Mystats.name = 'pidgeotto'
        print(f'do {Mystats.name}')
    if Mystats.name == 'pidgeotto' and mojlevel == 36:
        print(f'Gratulacje!!! Twój pokemon ewoluował z {Mystats.name}')
        Mystats.name = 'pidgeot'
        print(f'do {Mystats.name}')
    if Mystats.name == 'rattata' and mojlevel == 20:
        print(f'Gratulacje!!! Twój pokemon ewoluował z {Mystats.name}')
        Mystats.name = 'raticate'
        print(f'do {Mystats.name}')
    if Mystats.name == 'growlite' and mojlevel == 32:
        print(f'Gratulacje!!! Twój pokemon ewoluował z {Mystats.name}')
        Mystats.name = 'arcanine'
        print(f'do {Mystats.name}')
# POKEBALLE-------------------------------------------------------------------------------------------------
def pokeball():
    global pokebal,masterbal,ultrabal,greatbal
    pokebal = 100
    greatbal = 50
    ultrabal = 30
    masterbal = 1
def lapanie():
    global pokebal,masterbal,ultrabal,greatbal
    print(f'Masz do wyboru: pokekule ({pokebal}), świetnąkule ({greatbal}), ultrakulę ({ultrabal}), mistzrowskąkulę ({masterbal})')
    inp2 = input('Który ball? ').lower()
    if inp2 == 'pokekula':
        pokebal -= 1
        losuj = randint(1,1000000)
        if losuj == 2456:
            print(f'Gratulacje!!! Złapałeś {Enemystats.nameenemy}')
            złapany = True
    elif inp2 == 'świetnakula':
        greatbal -= 1
        losuj = randint(1,10000)
        if losuj == 1356:
            print(f'Gratulacje!!! Złapałeś {Enemystats.nameenemy}')
            złapany = True
    elif inp2 == 'ultrakula':
        ultrabal -= 1
        losuj = randint(1,100)
        if losuj == 58:
            print(f'Gratulacje!!! Złapałeś {Enemystats.nameenemy}')
            złapany = True
    elif inp2 == 'mistrzowskakula':
        masterbal -= 1
        print(f'Gratulacje!!! Złapałeś {Enemystats.nameenemy}')
        złapany = True
    else: 
        złapany = False
        argbh = input('pokemon uciekł z pokeballa')
    if złapany == True:
        if Enemystats.nameenemy == 'bulbasaur':
            bulbasaur()
        elif Enemystats.nameenemy == 'charmander':
            charmander()
        elif Enemystats.nameenemy == 'squirtle':
            squirtle()
        elif Enemystats.nameenemy == 'rattata':
            ratata()
        elif Enemystats.nameenemy == 'pidgey':
            pidgey()
        elif Enemystats.nameenemy == 'growlite':
            growlite()
# SKLEP-----------------------------------------------------------------------------------------------------
def sklep():
    global pokebal,money,iloscatak4,iloscatak3,iloscatak2,iloscatak1,leczduze,leczsrednie,leczmale,masterbal,ultrabal,greatbal
    aopauhwdpa = input('Witaj!')
    aopauhwdpa = input('Jesteś w sklepie')
    aopauhwdpa = input('Chcesz zobaczyć moje towary? ')
    aopauhwdpa = input('eh, i tak nie obchodzi mnie twoje zdanie')
    aopauhwdpa = input('Możesz kupić: 1-KULE, 2-Leczenia dla pokemona, 3-Odnowienie ataków')
    inp = float(input('Co bierzesz? '))
    if inp == 1:
        print(f'Masz {money} Boliwarów Wenezuelskich')
        inp2 = float(input('jakie kule? Masz do wyboru: 1-POKEKULA za 1000 boliwarów, 2-SWIETNAKULA za 2000 boliwarów, 3-ULTRAKULA za 5000 boliwarów i 4-MISTRZOWSKAKULA za 100000 '))
    elif inp == 2:
        print(f'Masz {money} Boliwarów Wenezuelskich')
        inp2 = float(input('jakie leczenie? Masz do wyboru: 1-MALE za 1000 boliwarów, 2-SREDNIE za 3000 boliwarów i 3-DUZE za 5000 '))
    elif inp == 3:
        print(f'Masz {money} Boliwarów Wenezuelskich')
        inp2 = float(input('Na który atak? Masz do wyboru: ATAK 1 ,  ATAK 2 , ATAK 3 i ATAK 4 każdy za 3000 boliwarów '))         
    else:
        uohdawd = input('NIE mam cię dosyć wywalaj ze sklepu ')
        wyjdz = True
    if wyjdz == False:
        
        ilosc = int(input('ile chcesz? '))

        if inp2 == 1 and money*ilosc > 1000:
            pokebal += ilosc
            money -= 1000*ilosc
        elif inp2 == 2 and money*ilosc > 2000:
            greatbal += ilosc
            money -= 2000*ilosc
        elif inp2 == 3 and money*ilosc > 5000:
            ultrabal += ilosc
            money -= 5000*ilosc
        elif inp2 == 4 and money*ilosc > 100000:
            masterbal += ilosc
            money -= 100000*ilosc
        elif inp2 == 1 and money*ilosc > 1000:
            leczmale += ilosc
            money -= 1000*ilosc
        elif inp2 == 2 and money*ilosc > 3000:
            leczsrednie += ilosc
            money -= 3000*ilosc
        elif inp2 == 3 and money*ilosc > 5000:
            leczduze += ilosc
            money -= 5000*ilosc
        elif inp2 == 1 and money*ilosc > 3000:
            iloscatak1 += ilosc
            money -= 3000*ilosc
        elif inp2 == 2 and money*ilosc > 3000:
            iloscatak2 += ilosc
            money -= 3000*ilosc
        elif inp2 == 3 and money*ilosc > 3000:
            iloscatak3 += ilosc
            money -= 3000*ilosc
        elif inp2 == 4 and money*ilosc > 3000:
            iloscatak4 += ilosc
            money -= 3000*ilosc
        aopauhwdpa = input('Idź i nigdy więcej nie wracaj!')
    if money < 0:
        exit()
def karczma():
    global money
    x = input("Witaj")
    x = input("jesteś w karczmie")
    x = input("co chcesz zrobić")
    x = input(f"masz {money} boliwarów wenezuelskich")
    x = input("1-Napij się za 5 boliwarów wenezuelskich")
    x = input("2-Prześpij się za 10 boliwarów wenezuelskich")
    x = input("3-załóż się o 20 boliwarów wenezuelskich")
    if money <= 0:
        print(" a no tak przecież ci nie stać biedaku")
        runda()
    xx = float(input())
    if xx == 1:
        if money >= 5:
            xxx = randint(1,10)
            if xxx == 1:
                Mystats.hpmoje =- 5
                print("zatrułeś się i straciłeś 5 zdrowia")
                runda()
                if hpmojeend <= 0:
                    print("zginąłęś")
                    print('\n killcount to: ',killcount) 
            else:
                Mystats.hpmoje =+ 10
                print("uleczyłeś 10 zdrowia")
                runda()
        else:
            print("nie stać cię")
            runda()
    if xx == 2:
        if money >= 10:
            xxxx = randint(1,5)
            if xxxx == 1:
                if money >= 10:
                    money =- 10
                    Mystats.hpmoje =+ 20
                    print("uleczyłeś 20 zdrowia ale cię okradziono")
                    runda()
                    
                else:
                    money = 0
                    Mystats.hpmoje =+ 20
                    print("uleczyłeś 20 zdrowia ale cię okradziono")
                    runda()
            else:
                Mystats.hpmoje =+ 20
                print("uleczyłeś 20 zdrowia")
                runda()
        else:
            print("nie stać cię")
            runda()
    if xx == 3:
        y = randint(1,3)
        zaklad = float(input("obstaw liczbę od 1-3"))
        if y == zaklad:
            money =+ 40
            runda()
        else:
            print("nie udało ci się zgadnąć")
            runda()            
# LECZENIE--------------------------------------------------------------------------------------------------
def leczenie():
    global hpmojeend,leczduze,leczsrednie,leczmale
    print(f'masz {leczmale} małych fiolek')
    print(f'masz {leczsrednie} średnich fiolek')
    print(f'masz {leczduze} dużych fiolek')
    inp = float(input('Które fiolki? 1 - małe, 2 - średnie, 3 - duże'))
    if inp == 1 and leczmale > 0:
        hpmojeend += leczmale
        leczmale -= 1
    if inp == 2 and leczsrednie > 0:
        hpmojeend += leczsrednie*5
        leczmale -= 1
    if inp == 3 and leczduze > 0:
        hpmojeend += leczduze*10
        leczmale -= 1
    else:
        print('sory nic nie uleczono')
# EXP-------------------------------------------------------------------------------------------------------
def exp():
    global xp,mojlevel
    xp = 0
    xp += levelenemy/2
    if xp > mojlevel or xp == mojlevel:
        afgiayfgaifawikbgiakfbaifugbaifaogbaof = input('KOLEJNY LEVEL !')
        mojlevel += 1
        xp = 0
# KOLEJNOŚĆ RZECZY------------------------------------------------------------------------------------------
wybor()
pokeball()
przeciwnik()
mojpokemon()
def runda():
    global hpenemyend,money,iloscatak4,iloscatak3,iloscatak2,iloscatak1,killcount,hpmojeend
    losowanko()
    while True:
        print('Twój przeciwnik to:',Enemystats.nameenemy)
        print('HP przeciwnika to: ',round(hpenemyend,2))
        print('LVL przeciwnika to: ',levelenemy)
        print('\n')
        print('Twoj pokemon to: ',Mystats.name)
        print('Jego level to: ',mojlevel)
        print('Jego HP wynosi: ',int(hpmojeend))
        print('1 atak zadaje:',int(atak1end))
        print(f'masz {iloscatak1} ataków 1')
        print('2 atak zadaje:',int(atak2end))
        print(f'masz {iloscatak2} ataków 2')
        print('3 atak zadaje:',int(atak3end))
        print(f'masz {iloscatak3} ataków 3')
        print('4 atak zadaje:',int(atak4end))
        print(f'masz {iloscatak4} ataków 4')
        print('\n')
        inp = float(input('Który atak wybierasz, lub jeśli chcesz go złąpać napisz 5? '))
        if inp == 1 and iloscatak1 > 0:
            hpenemyend = int(hpenemyend - atak1end)
            iloscatak1 -= 1
            print(f'twoj pokemon użył: atak 1 i zadał {atak1end} damage a')
        elif inp == 2 and iloscatak2 > 0:
            hpenemyend = hpenemyend - atak2end
            iloscatak2 -= 1
            print(f'twoj pokemon użył: atak 2 i zadał {atak2end} damage a')
        elif inp == 3 and iloscatak3 > 0:
            hpenemyend = hpenemyend - atak3end
            iloscatak3 -= 1
            print(f'twoj pokemon użył: atak 3 i zadał {atak3end} damage a')
        elif inp == 4 and iloscatak4 > 0:
            hpenemyend = hpenemyend - atak4end
            iloscatak4 -= 1
            print(f'twoj pokemon użył: atak 4 i zadał {atak4end} damage a')
        elif inp == 5:
            lapanie()        
        else:
            aosfgbhuhofasbinfhoasihfaos=input('Twoj pokemon nie zrozumiał co gadałeś')
        if hpenemyend <= 0:
            afglbhuogaghuoavgbyifgbi = input('GRATULACJE ! Zabiłeś przeciwnika! Teraz nadchodzi kolejny!')
            print(f'Dostałeś {levelenemy/2} expa')
            money += levelenemy*5
            killcount += 1
            inp3 = float(input('jeśli chcesz się uleczyć wpisz 1 a jeśli nie wpisz 2'))
            if inp3 == 1:
                leczenie()
            los = randint(1,8)
            if los == 1:
                sklep()
            if los == 2:
                karczma()
            exp()
            przeciwnik()
            runda()
        else:
            print('Przeciwnik atakuje i zadaje: ',atakenemyend)
            hpmojeend = hpmojeend - atakenemyend
        print('\n'*3)
        if hpmojeend <= 0: 
            print('\n killcount to: ',killcount)
            break
runda()