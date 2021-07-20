import collections
from difflib import SequenceMatcher

#function to check whether the password doesn't have more than 4 repeat characters/numbers
def countChars(newPwd):
    newPwd = newPwd.lower()
    d = collections.defaultdict(int)
    for c in newPwd:
        d[c] += 1
    for c in d:
        #print(c, d[c])
        if(d[c] > 4):
            return False
    return True

#function to check new password
def checkNewPwd(s):
    print("Checking new password")
    #print("new Password is "+s)
    upper=0
    lower=0
    number=0
    specialchars=['!','@','#','$','&','*'] 
    spChar=0
    slen = len(s)
    #checking whether password satisfies below req
    # atleast 1 upper, 1 lower, 1 number, 1 special char
    # no more than 4 special characters
    # 50% password is not number
    if(slen>=18):
        for c in s:
            if(c.isalnum()):
                if c.isupper() and upper==0:
                    upper=1
                elif c.islower() and lower==0:
                    lower=1
                elif c.isnumeric():
                    number=number+1
                    if(number>=slen/2):
                        print("New password is invalid")
                        return False
            elif c in specialchars:
                spChar=spChar+1
                if(spChar>4):
                    print("New password is invalid")
                    return False
            else:
                print("New password is invalid")
                return False
        
        #checking for not having more than 4 repeated characters
        chars_count = countChars(s)
        if(not(chars_count)):
            print("New password is invalid")
            return False

        if(upper!=0 and lower!=0 and number!=0 and spChar!=0):
            return True
        else:
            print("New password is invalid")
            return False

    else:
        print("New password should have atleast 18 alphanumeric characters")
        return False

#function to check whether the old password matches with the system
def checkOldPwd(oldPwd, user):
    #print("old Password is "+oldPwd)
    username=user.lower()
    passwordsDB_dict={
        "suganya" : "VolkswagenBeetle2021!",
        "choachana" : "Choapassword1234!@#$",
        "rachata" : "Rachatapassword12!@",
        "natcha" : "NatchaPassword123!@"
    }
    print("Checking old password")
    if(passwordsDB_dict[username] == oldPwd):
        return True
    else:
        return False

#function to change the oldpassword to newpassword
def ChangePassword(oldPassword, newPassword):
    if(checkOldPwd(oldPassword, "suganya")):
        #print("Old password is matching")
        similarity = SequenceMatcher(None, oldPassword, newPassword).ratio()
        #print(similarity)
        if(similarity>=0.8):
            print("New Password is invalid")
            return False
        elif(checkNewPwd(newPassword)):
            print("New Password is valid")
            print("Can change old password to New password")
            return True
        else:
            print("Password cannot be changed")
            return False
    else:
        print("Old password is invalid")
        return False

#ChangePassword("password1","Bwertrerww123456!@#$w")
ChangePassword("password1","Bwertrerww123456!@#$ww")

