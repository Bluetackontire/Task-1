from song_file import song  #imports dictionary from seperate file


def rsong():
    import random
    rsong.random = random.choice(list(song.items()))
    rsong.writer = rsong.random[0]  #the artist
    rsong.song_namel = rsong.random[1][0]  #the first letter of the song
    rsong.song_namef = rsong.random[1]  #the full song name
    rsong.sguess = rsong.writer + ": " + rsong.song_namel


def save():    #saves the score in a seperate file
    f = open("scores.txt", "a")  #opens a save file
    f.write(login.name + " : " + str(correct.score) + "\n")
    f.close()
    score_file = "scores.txt"
    score = []
    with open(score_file) as f:
        for line in f:
            score.append(line.strip())
    score.sort(key=lambda x: int(x.split(" : ")[-1]), reverse=True)
    print(score[:5])  #prints the top 5 scores from the list


#previous problem was that it printed latest score if under the same name but that is currently fixed


def login():
    while True:
        login.name = input("Please enter your name: ").strip().capitalize()
        if login.name != "":  #makes sure user enters a name
            break


def correct():
    correct.score += 1
    print("\033[1;32;40mYou got it correct!\033[0;37;0m"
          )  #uses ASCII to colour text
    print("Your score is " + str(correct.score))


correct.score = 0  #starts the score at 0
#previous problem was that score kept return to 0 within function but that has currently been fixed


def wrong():
    wrong.wrong -= 1
    wrong.tries = 2 + wrong.wrong
    print("\033[1;31;40mYou got it wrong. You have " + str(wrong.tries) +
          " tries remaining.\033[1;37;0m")


wrong.wrong = 0
#previous problem was that the wrong counter kept return to 0 within function but that has currently been fixed
#previous problem was that the wrong counter kept going past '0 tries' (e.g. negative numbers) but that has currently been fixed


def guess():
    guess.num = 0
    print(rsong.sguess)  #uses another function to let user guess the song
    print("Please guess the song name: ")
    guess.song_guess = input()
