__author__ = 'nelson'

class Sesion():

    def creada(self,user):
        if user.is_authenticated():
            return True
        else:
            return False
