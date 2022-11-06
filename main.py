from easygui import fileopenbox
from os import system
from time import sleep

def main():
    
    system("title Text file splitter")
    output = open("output.txt", "w")
    char = input("Enter the character to split the lines with: ")
    system("cls")

    part = input("""
    Do you want to keep the first part or the second part:
    1. First part
    2. Second part
    """)
    if part == "1":
        part = 0
    if part == "2":
        part = 1
    else:
        print("Invalid input")
        input()
        main()
    system("cls")

    print("Press enter to open the file: ")
    input()
    f = fileopenbox()

    file = open(f, "r", encoding = "utf-8")
    for x in file:
        l = x.split(char)[part]
        output.write(l)

    print("Done.")
    print("Output file: output.txt")
    sleep(5)
    input()
    main()

main()
