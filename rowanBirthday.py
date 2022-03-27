import os
os.system('')
message = "non binary flag moment"
ratio = 1/((300/200)*2)
lines = int(len(message)*ratio)
if lines < 4:
    lines = 4
while lines%4!=0:
    lines = lines -1

colourHeight = int(lines/4)
colours = ['\33[103m', '\33[107m', '\33[45;97m', '\33[40;97m']

for colour in colours:
    for y in range(colourHeight):
        print("")
        for x in range(len(message)):
            print(colour + message[x] + '\33[0m', end = "")
print()
