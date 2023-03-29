import random
import string
import os
from pathlib import Path
from time import sleep
from timeit import repeat

dir_path = Path('C:\TempPath')
color_name = 'existColor.txt'
animal_name = 'existAnimal.txt'
number_name = 'existNum.txt'
color_path = dir_path.joinpath(color_name)
animal_path = dir_path.joinpath(animal_name)
number_path = dir_path.joinpath(number_name)

color=['Blue','Red','Yellow','Orange', 'Teal', 'Silver', 'Lime','Green','Gray']
#color=['Red','Blue']
animal=['bird','wolf','dog','cat','fish','lion','ferret'
        ,'snake','bee', 'fox', 'owl', 'goat', 'frog', 'bat', 'zebra', 'mouse', 'sheep', 'lamb', 'bear', 'deer', 'puma', 'orca', 'seal']
#animal=['bird','wolf']

def randomPassword(color, animal):
    if not os.path.exists("C:\TempPath\existColor.txt"):
        createFiles()

    color_file = open("C:\TempPath\existColor.txt", 'w+')
    animal_file = open("C:\TempPath\existAnimal.txt", 'w+')

    randomcolor=random.choice(color)
    color_file.write(randomcolor)
    color_file.flush()
    color_file = open("C:\TempPath\existColor.txt", 'r+')
    
    
    randomanimal=random.choice(animal)
    animal_file.write(randomanimal)
    animal_file.flush()
    animal_file = open("C:\TempPath\existAnimal.txt", 'r+')
    
    
    randomnum1=random.choice(string.digits)
    randomnum2=random.choice(string.digits)
    
    genPass = randomcolor+randomanimal+randomnum1+randomnum2
    
    if len(genPass) <=11:
        randomnumadd=random.choice(string.digits)
        genPass+= randomnumadd
        if len(genPass) <=11:
            randomnumadd=random.choice(string.digits)
            genPass+= randomnumadd
            if len(genPass) <=11:
                randomnumadd=random.choice(string.digits)
                genPass+= randomnumadd
                if len(genPass) <=11:
                    randomnumadd=random.choice(string.digits)
                    genPass+= randomnumadd
    
    print("Password is:",genPass)

    anotherPassword(color_file,animal_file)
    
    
    
def repeatPassword(color, animal,color_file,animal_file):
    randomcolor=random.choice(color)
    while True:
        color_file = open("C:\TempPath\existColor.txt", 'r+')
        file_data = color_file.read()
        if randomcolor==file_data:
            randomcolor=random.choice(color)
        
        if randomcolor!=file_data:
            color_file = open("C:\TempPath\existColor.txt", 'w+')
            color_file.write(randomcolor)
            color_file.close()
            color_file = open("C:\TempPath\existColor.txt", 'r+')
            break

            
    randomanimal=random.choice(animal)
    while True:
        animal_file = open("C:\TempPath\existAnimal.txt", 'r+')
        file_data = animal_file.read()
        if randomanimal==file_data:
            randomanimal=random.choice(animal)
            
        
        else:
            animal_file = open("C:\TempPath\existAnimal.txt", 'r+')
            animal_file.write(randomanimal)
            animal_file.close()
            animal_file = open("C:\TempPath\existAnimal.txt", 'r+')
            break    
        
    randomnum1=random.choice(string.digits)
    randomnum2=random.choice(string.digits)
    
    genPass = randomcolor+randomanimal+randomnum1+randomnum2
    
    if len(genPass) <=11:
        randomnumadd=random.choice(string.digits)
        genPass+= randomnumadd
        if len(genPass) <=11:
            randomnumadd=random.choice(string.digits)
            genPass+= randomnumadd
            if len(genPass) <=11:
                randomnumadd=random.choice(string.digits)
                genPass+= randomnumadd
                if len(genPass) <=11:
                    randomnumadd=random.choice(string.digits)
                    genPass+= randomnumadd
    
    print("Password is:",genPass)
    anotherPassword(color_file,animal_file)
    
def anotherPassword(color_file,animal_file):
    yorn=input('Do you need another password? \n')
    yorn=yorn.lower()
    if yorn=='y' or yorn=='yes':
        color_file.close()
        animal_file.close()
        repeatPassword(color,animal,color_file,animal_file)
    else:
        color_file.close()
        os.remove("C:\TempPath\existColor.txt")
        print("Removed color file.")
        animal_file.close()
        os.remove("C:\TempPath\existAnimal.txt")
        print("Removed animal file.")
        pass
    
def createFiles():
    if dir_path.is_dir():
        if color_path.is_file():
            print('Color text exists.')
        else:
            with open (dir_path.joinpath(color_name),'w') as f:
                print("Color File was created.")
                
    if dir_path.is_dir():
        if animal_path.is_file():
            print("Animal file exists")
        else:
            with open (dir_path.joinpath(animal_name),'w') as f:
                print("Animal File was created")

randomPassword(color,animal)

