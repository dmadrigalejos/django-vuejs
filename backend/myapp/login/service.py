from .dao import LoginDAO
from myapp.user.models import User

class LoginService(object):



    def retrieveUser(self, username, password):
        loginDAO = LoginDAO()
        user = User()
        user = loginDAO.retrieveUser(username=username)
        if (len(user)<=0):
            return None

        if (password == user[0].userPassword):
            return user
        else:
            return None