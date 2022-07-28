# Open file
# read file into lines array
# find index for start of "28.6fps"
# find index for end of block
# delete lines between indexes


from os import remove

def delete28fps():
    if ctFile.writable() != True:
        print("Cannot open file")
        return

    else:

        lines = ctFile.readlines()
        print("Reading lines...")


    # lets itirate through these "lines"
    # idk why "line" is included in the 'for' loop statement,
    #       but here we are. It does not seem to itirate
    #       properly w/o it.
    # print statments in there just to see where the program is at from
    #   terminal.

    for i, line in enumerate(lines):
        
        print(lines[i])

        if "28.6fps" in lines[i]:
            print(lines[i])

            while lines[i] != "End Export\n":
                print(lines[i])
                # where file.removeLine() !?
                # Can't seem to find a fn that will "truncate"
                #   a single line from a file
                i += 1
            return    
        

        else:
            print("nothing to strip")
    
    
    ctFile.close()
    print("File Closed.")

# Open up file via user CLI input with w/r privilages
ctFile = open(input("Enter File name: "), 'r+')

# Really not needed, but add statment noting if file was found
#  and actually writeable
print("File Open and writeable: ", ctFile.writable())

# Call the fn that deletes code from script file for 28.6fps exporting
delete28fps()

# Close file after calling fn
ctFile.close()
print("File Closed.")