time = int(input())

hours = time // 3600
minutes = (time % 3600) // 60
seconds = time % 60

print(str(hours) + " hours, " + str(minutes) + " minutes, " + str(seconds) + " seconds")
