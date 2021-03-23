def number_of_bottles():
    bottle = 99
    count = 99
    song = ""

    for i in range(99):
        if bottle == 1:
            song += str(bottle) + " bottles of milk on the wall, " + str(bottle) + " bottle of milk. " \
                    "\nTake one down and pass it around, no more bottles of milk on the wall. " \
                    "\n" + "\nNo more bottles of milk on the wall, no more bottles of milk. " \
                    "\nGo to the store and buy some more, 99 bottles of milk on the wall."

        elif bottle >= 2:
            count -= 1
            song += str(bottle) + " bottles of milk on the wall, " + str(bottle) + " bottles of milk. " \
                "\nTake one down and pass it around, " + str(count) + " bottles of milk on the wall.\n" + "\n"

        bottle -= 1
    print(song)


number_of_bottles()