# Open file
# read file into lines array
# find index for start of "28.6fps"
# find index for end of block
# delete lines between indexes

def delete28fps():
    lines = ctFile.readlines()

    for line in lines:
        if "28.6fps" in line:
            n = line.index(n)

        elif "End Export" in line:
            x = line.index(x)

        else:
            print("nothing to strip")
            break


    for i in range(n,x):
        line.strip()
        print("Stripped " + line)

    ctFile.close()


ctFile = open(input("Enter File name: "), 'r+')

delete28fps