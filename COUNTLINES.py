def COUNTLINES():
    file = open('STORY.TXT', 'r')
    lines = file.readlines()
    count = 0

    for w in lines:
        if w != "" and (w[0] == 'A' or w[0] == 'a'):
            count += 1

    print("Total lines started with 'A' or 'a':", count)
    file.close()

COUNTLINES()
