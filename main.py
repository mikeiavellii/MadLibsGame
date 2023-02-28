import random
import replit
run = True

print(f"Welcome to MadLibs Version")

while run:
    version = random.randint(1, 2)
    print(f"#{version}\n")

    if (version == 1):
        color = input("Enter a color: ")
        plural_noun = input("Enter a plural noun: ")
        celebrity = input("Enter a celebrity: ")
        replit.clear()

        print(f"Roses are {color}")
        print(f"{plural_noun} are blue")
        print(f"I love {celebrity}")


    if (version == 2):
        Adjective = input("Enter an adjective: ")
        AnAmountofTime = input("Enter an amount of time: ")
        FemaleCelebrity = input("Enter a female celebrity: ")
        LastNameofaCelebrity = input("Enter a last name of a celebrity: ")
        Noun1 = input("Enter a noun: ")
        Noun2 = input("Enter a second noun: ")
        Noun3 = input("Enter a third noun: ")
        Noun4 = input("Enter a fourth noun: ")
        PartoftheBody = input("Enter a part of the body: ")
        PluralNoun1 = input("Enter a plural noun: ")
        PluralNoun2 = input("Enter a second plural noun: ")
        Profession = input("Enter a profession: ")
        TypeofBuilding = input("Enter a type of building: ")

        print(f"Every Wednesday, when I get home from school, I have a piano")
        print(f"lesson. My teacher is a very strict {Noun1}. Her name is")
        print(f"{FemaleCelebrity}. Our piano is a Steinway Concert {Noun2}")
        print(f"and it has 88 {PluralNoun1}. It also has a soft pedal and")
        print(f"a {Adjective} pedal. When I have a lesson, I sit down on the piano")
        print(f"{Noun3} and play for {AnAmountofTime}. I do scales to")
        print(f"exercise my {PluralNoun2}, and then I usually play a minuet by")
        print(f"Johann Sebastian {LastNameofaCelebrity}. Teacher says I am a natural")
        print(f"{Noun4} and have a good natural {PartoftheBody}. Perhaps")
        print(f"when I get better I will become a concert {Profession}.and give")
        print(f"a recital at Carnegie {TypeofBuilding}.")

    while (run):
        response = input("Would you like to try a another Mad Lib?\nType \"Yes\" to try another or \"No\" to exit\n")
        if (response.lower() == "yes"):
            break
            run = True

        elif (response.lower() == "no"):
            print("Thanks for playing.\nHave a good one!")
            run = False
            break




