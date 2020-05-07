import os, sys
#ha ha ha
path = "./test.hex"
buffer = ""
def xxdToClangHex(path):
    dump = open(path, 'r')

    for line in dump.readlines():
        for word in line.split(" "):
            if word.find('\n') > 0:
                splited_word = word.split("\n")
                word = splited_word[0]
                hexWord = "0x{}{}".format(word, ",\n")
            else:
                hexWord = "0x{}{}".format(word, ", ")
            buffer += hexWord



if __name__=="__main__":
    path = sys.argv[1]
