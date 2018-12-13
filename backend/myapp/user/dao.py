from django.db import connection
from myapp.user.models import User

class UserDAO(object):

    def createUser(self, json_user):
        with connection.cursor() as cursor:
            cursor.execute("INSERT INTO user ("
                           "     userId "
                           "    ,username "
                           "    ,userPassword "
                           "    ,userLastname "
                           "    ,userFirstname "
                           "    )"
                           "    VALUES ("
                           "     %(userId)s "
                           "    ,%(username)s "
                           "    ,%(userPassword)s "
                           "    ,%(userLastname)s "
                           "    ,%(userFirstname)s "
                           "    )", json_user)


    def updateUser(self, json_update):
        with connection.cursor() as cursor:
            affected_rows = cursor.execute("UPDATE user "
                                           "   SET   username = %(username)s "
                                           "        ,userPassword = %(userPassword)s "
                                           "        ,userLastname = %(userLastname)s "
                                           "        ,userFirstname = %(userFirstname)s "
                                           " WHERE userId = %(userId)s" , json_update)
        return  affected_rows

    def retrieveAllUsers(self):
        with connection.cursor() as cursor:
            cursor.execute("SELECT userid"
                           "        ,userName "
                           "        ,userPassword "
                           "        ,userFirstname "
                           "        ,userLastname"
                           "  FROM user ")
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


    def retrieveUser(self, userId):
        with connection.cursor() as cursor:
            cursor.execute("SELECT userid"
                           "        ,userName "
                           "        ,userPassword "
                           "        ,userFirstname "
                           "        ,userLastname"
                           "  FROM user "
                           " WHERE userid = %s", userId)
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