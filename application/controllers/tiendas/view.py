import config
import hashlib
import app


class View:

    def __init__(self):
        pass

    '''
    def GET(self, id_tienda):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_VIEW(id_tienda) # call GET_VIEW() function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    @staticmethod
    def GET_VIEW(id_tienda):
    '''

    def GET(self, id_tienda):
        id_tienda = config.check_secure_val(str(id_tienda)) # HMAC id_tienda validate
        result = config.model.get_tiendas(id_tienda) # search for the id_tienda data
        return config.render.view(result) # render view.html with id_tienda data
