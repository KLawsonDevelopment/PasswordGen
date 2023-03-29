## Imports

import random
import string
import os
from pathlib import Path
from time import sleep
from timeit import repeat

## Global Variables

dir_path = Path('C:\TempPath')
color_name = 'existColor.txt'
animal_name = 'existAnimal.txt'
number_name = 'existNum.txt'
color_path = dir_path.joinpath(color_name)
animal_path = dir_path.joinpath(animal_name)
number_path = dir_path.joinpath(number_name)

## Lists of colors and animals. Shorter lists are for testing.

color=['Blue','Red','Yellow','Orange', 'Teal', 'Silver', 'Lime','Green','Gray']
#color=['Red','Blue']
animal=['bird','wolf','dog','cat','fish','lion','ferret'
        ,'snake','bee', 'fox', 'owl', 'goat', 'frog', 'bat', 'zebra', 'mouse', 'sheep', 'lamb', 'bear', 'deer', 'puma', 'orca', 'seal']
#animal=['bird','wolf']

#Initial password generation.

def randomPassword(color, animal):

    # If file does not exist, call file creation.

    if not os.path.exists("C:\TempPath\existColor.txt"):
        createFiles()

    # Open files

    color_file = open("C:\TempPath\existColor.txt", 'w+')
    animal_file = open("C:\TempPath\existAnimal.txt", 'w+')

    # Create random color and write to file

    randomcolor=random.choice(color)
    color_file.write(randomcolor)
    color_file.flush()
    color_file = open("C:\TempPath\existColor.txt", 'r+')
    
    # Create random animal and write to file

    randomanimal=random.choice(animal)
    animal_file.write(randomanimal)
    animal_file.flush()
    animal_file = open("C:\TempPath\existAnimal.txt", 'r+')

    # Create random numbers    
    
    randomnum1=random.choice(string.digits)
    randomnum2=random.choice(string.digits)

    # Combine
    
    genPass = randomcolor+randomanimal+randomnum1+randomnum2

    # If password is under 12 characters, extend with numbers.
    
    while len(genPass) <=11:
        randomnumadd=random.choice(string.digits)
        genPass+=randomnumadd
    
    # Show password

    print("Password is:",genPass)

    #Call anotherPassword

    anotherPassword(color_file,animal_file)
    
# Checking to see if another password is needed.
    
def anotherPassword(color_file,animal_file):
    yorn=input('Do you need another password? \n')
    yorn=yorn.lower()

    # If yes, run repeat password.

    if yorn=='y' or yorn=='yes':
        color_file.close()
        animal_file.close()
        repeatPassword(color,animal,color_file,animal_file)

    # If no, close and delete files.

    else:
        color_file.close()
        os.remove("C:\TempPath\existColor.txt")
        print("Removed color file.")
        animal_file.close()
        os.remove("C:\TempPath\existAnimal.txt")
        print("Removed animal file.")
        pass

# Repeat password function.

def repeatPassword(color, animal,color_file,animal_file):

    # Make another random color

    randomcolor=random.choice(color)

    # Check randomcolor against color in file. If same, repeat. If different, pass.

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

    # Create random animal

    randomanimal=random.choice(animal)

    # Check randomanimal against animal in file. If same, repeat. If different, pass.

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
        
    # Create random numbers.

    randomnum1=random.choice(string.digits)
    randomnum2=random.choice(string.digits)

    #Combine.
    
    genPass = randomcolor+randomanimal+randomnum1+randomnum2

    # If password is less than 12 characters, add extra digits.

    while len(genPass) <=11:
        randomnumadd=random.choice(string.digits)
        genPass+=randomnumadd
    

    
    print("Password is:",genPass)
    anotherPassword(color_file,animal_file)
    

    
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

