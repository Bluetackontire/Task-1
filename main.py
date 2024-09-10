from functions import login, rsong, save, correct, wrong, guess
#brings in the functions from a seperate file

login()
rsong()

guess.num = 0

while guess.num != rsong.song_namef:  #prints the artist and first letter of song
    guess()
    while guess.song_guess.title() == rsong.song_namef or guess.song_guess == rsong.song_namef:  #if the guess is correct
        correct()
        rsong()
        guess()
        song_guess = 0  #brings back to first while loop
    else:  #if they get it wrong
        wrong()
        if wrong.tries == 0:  #prints if out of tries (2 tries)
            print("You are out of tries\033[1;37;0m")
            print("Your score is " + str(correct.score))  #prints their score
            break  #ends while loop if user is out of tries

save()  #saves the score in an external file

#https://ozzmaker.com/add-colour-to-text-in-python/
