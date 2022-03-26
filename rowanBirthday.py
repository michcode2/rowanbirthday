message = "hello world"
ratio = 1/(300/200)
lines = int(len(message)*ratio)
for y in range(lines):
    print("")
    for x in range(len(message)):
        print(print('\x1b[6;30;42m' + 'h' + '\x1b[0m'), end = "")
