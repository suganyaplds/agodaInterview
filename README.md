# agodaInterview

User needs to pass 2 parameters to changepassword function.
    1. oldPassword
    2. newPassword
    
Password can be changed successfully only when it satisfies all the requirements below. 

  1. Old password should match with system
  2. New password should match all the below conditions. 
        a. At least 18 alphanumeric characters and list of special chars !@#$&*
        b. At least 1 Upper case, 1 lower case ,least 1 numeric, 1 special character
        c. No duplicate repeat characters more than 4
        d. No more than 4 special characters
        e. 50 % of password should not be a number
  3. Password is not similar to old password, < 80% match.

Note: The user for whom this change password method is called is currently hardcoded in line no 51 of ChangePassword.py which will be extended later for all users. 
