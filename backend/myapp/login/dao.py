from myapp.user.models import User
from django.db import connection

class LoginDAO(object):

    def retrieveUser(self, username):
        with connection.cursor() as cursor:
            cursor.execute("SELECT userid"
                           "        ,username "
                           "        ,userPassword "
                           "        ,userFirstname "
                           "        ,userLastname"
                           "  FROM user "
                           " WHERE username = %s", [username])
            result_set = cursor.fetchall()

        users = []

        for row in result_set:
            user = User()
            user.userId = row[0]
            user.username = row[1]
            user.userPassword = row[2]
            user.userFirstname = row[3]
            user.userLastname = row[4]

            users.append(user)

        return users