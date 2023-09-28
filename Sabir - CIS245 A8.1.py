def main():
    #Initialize file and iterators
    f = None
    mainLoop = True
    previousI = 0
    currentI = 0
    #Allows for consecutive editing of files
    while mainLoop == True:
        tempFileName = input("What is the name of the file?: ")
        #Adds txt to create a text file
        fileName = tempFileName+'.txt'
        name = input("What is your name?: ")
        streetAddress = input("What is your street address?: ")
        phoneNumber = input("What is your phone number? ")
        #First Try-Except block to check if phoneNumber is a number
        try:
            int(phoneNumber)
            #Second try-except block to make sure fileName name and streetAddress are text
            try:
                int(fileName)
                int(name)
                int(streetAddress)
            except ValueError:
                #Last try-except block to check if the file already exists and you're just trying to edit it
                try:
                    #The if statements are used to add a new line depending on if you're on the first edit or not, currentI will be larger than 0 for consecutive edits
                    if currentI > 0:
                        f = open(fileName, "x")
                        f = open(fileName, "a")
                        f.write('\n')
                        f.write(name + ',')
                        f.write(streetAddress + ',')
                        f.write(phoneNumber)
                        f.close()
                        #Increases currentI to add a new line for next edit
                        currentI+=1
                    else:
                        f = open(fileName, "x")
                        f = open(fileName, "a")
                        f.write(name + ',')
                        f.write(streetAddress + ',')
                        f.write(phoneNumber)
                        f.close()
                        currentI+=1
                except FileExistsError:
                    if previousI < currentI:
                        f = open(fileName, "a")
                        f.write('\n')
                        f.write(name + ',')
                        f.write(streetAddress + ',')
                        f.write(phoneNumber)
                        f.close()
                        currentI+=1
                    else:
                        f = open(fileName, "a")
                        f.write(name + ',')
                        f.write(streetAddress + ',')
                        f.write(phoneNumber)
                        f.close()
                        currentI+=1
        except ValueError:
            print("Please enter a valid number")
            
        f = open(fileName, "rt")
        print(f.read())
        
        
main()