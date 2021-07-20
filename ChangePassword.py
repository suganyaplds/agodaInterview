def checkNewPwd(s):
    print("Checking new password")
    upper=0
    lower=0
    number=0
    specialchars=['!','@','#','$','&','*'] 
    spChar=0
    slen = len(s)
    
    if(slen>=18):
        for c in s:
            if(c.isalnum()):
                if c.isupper() and upper==0:
                    upper=1
                elif c.islower() and lower==0:
                    lower=1
                elif c.isnumeric():
                    number=number+1
            elif c in specialchars:
                spChar=spChar+1
            else:
                print("New password is invalid")
                return False

        if(upper!=0 and lower!=0 and number!=0 and number<slen/2 and spChar!=0 and spChar<=4):
            return True
        else:
            print("New password is invalid")
            return False

    else:
        print("New password should have atleast 18 alphanumeric characters")
        return False

def checkOldPwd(oldPwd, user):
    username=user.lower()
    passwordsDB_dict={
        "suganya" : "password1",
        "raja" : "password2",
        "ravi" : "password3"
    }
    print("Checking old password")
    if(passwordsDB_dict[username] == oldPwd):
        return True
    else:
        return False

def ChangePassword(oldPassword, newPassword):
    #print("old Password is "+oldPassword)
    #print("new Password is "+newPassword)
    if(checkOldPwd(oldPassword, "suganya")):
        #print("Old password is matching")
        if(checkNewPwd(newPassword)):
            print("New Password is valid")
            print("Can change old password to New password")
            return True
        else:
            print("Password cannot be changed")
            # print("It should contain at least 18 alphanumeric characters and list of special chars !@#$&*")
            # print("It should contain at least 1 Upper case, 1 lower case , 1 numeric, 1 special character")
            # print("It should not contain more than 4 special characters")
            # print("50% of password should not be a number")
            return False
    else:
        print("Old password is invalid")
        return False

ChangePassword("password1","Bwertrerww123456!@#$w")
#ChangePassword("password1","Bwertrerww123456!@#$^w")

