
class LoginException(Exception):

    def __int__(self):
        super().__int__()


Login_id = "Admin"
Password = "Admin"

try:
    if Login_id == 'Admi' and Password == 'Admin':
        print("Valid User")

    else:
         raise LoginException("Invalud User")

except LoginException as e:
    print('LoginException', e)
