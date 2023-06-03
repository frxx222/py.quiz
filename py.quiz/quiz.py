import time

print("Welcome to the number Quiz game!")
name = input("Please enter your name: ")

print("Hello, " + name + "!")
play_again = True

while play_again:
    answer = ["Lyra", "Scorpius", "Gemini", "Canis Major", "Aries", "Virgo", "Cancer", "Leo", "Pisces", "Taurus"]
    time_limit = 30
    points = 0

    print("1. The constellation is associated with the myth of the Greek musician and poet Orpheus.")
    start_time = time.time()
    user_answer = input("Answer: ")
    if time.time() - start_time >= time_limit:
        print("You're out of time!!")
    elif user_answer == answer[0]:
        points += 1
        print("Your answer is correct!")
    else:
        print("Incorrect!")

    print("2. It represents the scorpion and is associated with the story of Orion in Greek mythology.")
    start_time = time.time()
    user_answer = input("Answer: ")
    if time.time() - start_time >= time_limit:
        print("You're out of time!!")
    elif user_answer == answer[1]:
        points += 1
        print("Your answer is correct!")
    else:
        print("Incorrect!")

    print("3. It is located in the northern celestial hemisphere. Its name means “the twins” in Latin.")
    start_time = time.time()
    user_answer = input("Answer: ")
    if time.time() - start_time >= time_limit:
        print("You're out of time!!")
    elif user_answer == answer[2]:
        points += 1
        print("Your answer is correct!")
    else:
        print("Incorrect!")

    print("4. Its name means “the greater dog” in Latin, and represents the bigger dog following Orion, the hunter in Greek mythology.")
    start_time = time.time()
    user_answer = input("Answer: ")
    if time.time() - start_time >= time_limit:
        print("You're out of time!!")
    elif user_answer == answer[3]:
        points += 1
        print("Your answer is correct!")
    else:
        print("Incorrect!")

    print("5. It is usually associated with the story of the Golden Fleece in Greek mythology.")
    start_time = time.time()
    user_answer = input("Answer: ")
    if time.time() - start_time >= time_limit:
        print("You're out of time!!")
    elif user_answer == answer[4]:
        points += 1
        print("Your answer is correct!")
    else:
        print("Incorrect!")

    print("6. Its is a constellation lies in the southern sky. Its name means “virgin” in Latin.")
    start_time = time.time()
    user_answer = input("Answer: ")
    if time.time() - start_time >= time_limit:
        print("You're out of time!!")
    elif user_answer == answer[5]:
        points += 1
        print("Your answer is correct!")
    else:
        print("Incorrect!")

    print("7. Contains a number of famous deep sky objects, among them the open cluster Praesepe, also known as the Beehive Cluster")
    start_time = time.time()
    user_answer = input("Answer: ")
    if time.time() - start_time >= time_limit:
        print("You're out of time!!")
    elif user_answer == answer[6]:
        points += 1
        print("Your answer is correct!")
    else:
        print("Incorrect!")

    print("8. This constellation lies in the northern sky. It is one of the zodiac constellations and one of the largest constellations in the sky.")
    start_time = time.time()
    user_answer = input("Answer: ")
    if time.time() - start_time >= time_limit:
        print("You're out of time!!")
    elif user_answer == answer[7]:
        points += 1
        print("Your answer is correct!")
    else:
        print("Incorrect!")

    print("9. I lies between Aries constellation to the east and Aquarius to the west.")
    start_time = time.time()
    user_answer = input("Answer: ")
    if time.time() - start_time >= time_limit:
        print("You're out of time!!")
    elif user_answer == answer[8]:
        points += 1
        print("Your answer is correct!")
    else:
        print("Incorrect!")


    print("10. A large constellation in the northern sky. Its name means “bull” in Latin.")
    start_time = time.time()
    user_answer = input("Answer: ")
    if time.time() - start_time >= time_limit:
        print("You're out of time!!")
    elif user_answer == answer[9]:
        points += 1
        print("Your answer is correct!")
    else:
        print("Incorrect!")

    # Repeat the above code for the remaining questions (2-10)

    print("Your final points is " + str(points))
    if points >= 7:
        print("Congratulations, you passed!!")
    else:
        print("Sorry, you failed!!")

    user_input = input("Do you want to play again? (Y/N): ")
    if user_input.upper() != "Y":
        play_again = False

print("Thank you for playing!")
