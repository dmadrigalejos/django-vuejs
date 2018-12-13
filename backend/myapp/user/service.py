from .dao import UserDAO

class UserService(object):

    def createUser(self, user):
        # json_object = {
        #     "username": user.username,
        #     "userPassword": user.userPassword,
        #     "userLastname": user.userLastname,
        #     "userFirstname": user.userFirstname
        # }

        userDAO = UserDAO()
        userDAO.createUser(json_user=user)

    def updateUser(self, user, userId):
        json_object = {
            "userId" : userId,
            "username" : user['username'],
            "userPassword" : user['userPassword'],
            "userFirstname" : user['userFirstname'],
            "userLastname" : user['userLastname']
        }
        userDAO = UserDAO()
        return userDAO.updateUser(json_update=json_object)

    def retrieveUsers(self):
        userDAO = UserDAO()
        return  userDAO.retrieveAllUsers()

    def retrieveOneUser(self, userId):
        userDAO = UserDAO()
        return userDAO.retrieveUser(userId)