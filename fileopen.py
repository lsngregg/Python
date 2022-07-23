# Open file
# read file into lines array
# find index for start of "28.6fps"
# find index for end of block
# delete lines between indexes

def delete28fps():
    lines = ctFile.readlines()


    # lets itirate through these "lines"
    for i, lines in enumerate(lines):
        if "28.6fps" in lines[i]:
            while lines[i] != "End Export":
                list.remove(lines)   

        else:
            print("nothing to strip")
            break

    ctFile.close()


ctFile = open(input("Enter File name: "), 'r+')

delete28fps