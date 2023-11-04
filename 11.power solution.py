power = input("Has power? ")

if power == "yes":
    print("Seek other Help")
else:
    plug = input("Is plugged in? ")
    if plug != "yes":
        print("Pug the switch in")
    else:
        switch = input("Is the switch on? ")
        if switch != "yes":
            print("Turn on Switch")
        else:
            fuse = input("Is fuse OK? ")
            if fuse != "yes":
                print("Check Fuse")
            else:
                print("Sorry!, Seek other help")

# ctrl + alt + shift + j
