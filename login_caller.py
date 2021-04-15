# page 1 - login and signup

import user_class

def user_login(email1,password1):
    user = user_class.User(email = email1,password=password1)
    ans = user.login()

    if(ans==True):
        return user

    else:
        return False

'''
ans=user_login("dhanya@gmail.com","dhans123")

print(ans)
'''
