# Your code here!!
song = ["let it be", "whisper words of wisdom", "there will be an answer"]

def sing():
    for i in range(1, 9):
        if i <= 4:
            print(song[0] + ",")
        elif i == 5:
            print(song[1] + ", " + song[0] + ", " + song[0] + ",")
        elif i > 5 and i <= 8:
            print(song[0] + ",")
        else:
            print(song[2] + ", " + song[1])
        

sing()




