# page 1 - login and signup

import user_class

def user_signup(email1,password1,firstname1,lastname1,age1,phone1):
    user = user_class.User(email = email1,password=password1,firstName=firstname1,lastName=lastname1,age=age1,phoneNo=phone1)
    
    ans = user.signUp()
    
    return ans


