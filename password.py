stored_password = "secret123"   # the password to check against
logged_in = False

counter = 0                      # counter <- 0

while True:
    password = input("Enter password: ")   # INPUT password

    if password == stored_password:        # if password = stored_password
        logged_in = True                   # logged_in <- TRUE
        print("Logged in")                 # OUTPUT "Logged in"
        break                              # go to End
    else:
        print("Password is wrong")         # OUTPUT "Password is wrong"
        counter = counter + 1              # counter = counter + 1

        if counter == 3:                   # counter = 3?
            print("supit hakr")            # OUTPUT "supit hakr"
            break                          # go to End
        # otherwise loop back to INPUT password