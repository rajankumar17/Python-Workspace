def game():
    return 5555

score = game()
with open("hiscore.txt") as f:
    hiScoreStr = f.read()
    
if hiScoreStr=='':
    with open("hiscore.txt", "w") as f:
        f.write(str(score))

elif int(hiScoreStr)<score :
    with open("hiscore.txt", "w") as f:
        f.write(str(score))

with open("hiscore.txt","r") as f:
    print(f.readlines())