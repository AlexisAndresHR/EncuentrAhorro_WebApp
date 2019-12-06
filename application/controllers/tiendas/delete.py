import config
import hashlib
import app

class Delete:
    
    def __init__(self):
        pass

    '''
    def GET(self, id_tienda, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_DELETE(id_tienda) # call GET_DELETE function
            elif privsession_privilegeilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    def POST(self, id_tienda, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege
            if session_privilege == 0: # admin user
                return self.POST_DELETE(id_tienda) # call POST_DELETE function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    @staticmethod
    def GET_DELETE(id_tienda, **k):

    @staticmethod
    def POST_DELETE(id_tienda, **k):
    '''

    def GET(self, id_tienda, **k):
        message = None # Error message
        id_tienda = config.check_secure_val(str(id_tienda)) # HMAC id_tienda validate
        result = config.model.get_tiendas(int(id_tienda)) # search  id_tienda
        result.id_tienda = config.make_secure_val(str(result.id_tienda)) # apply HMAC for id_tienda
        return config.render.delete(result, message) # render delete.html with user data

    def POST(self, id_tienda, **k):
        form = config.web.input() # get form data
        form['id_tienda'] = config.check_secure_val(str(form['id_tienda'])) # HMAC id_tienda validate
        result = config.model.delete_tiendas(form['id_tienda']) # get tiendas data
        if result is None: # delete error
            message = "El registro no se puede borrar" # Error messate
            id_tienda = config.check_secure_val(str(id_tienda))  # HMAC user validate
            id_tienda = config.check_secure_val(str(id_tienda))  # HMAC user validate
            result = config.model.get_tiendas(int(id_tienda)) # get id_tienda data
            result.id_tienda = config.make_secure_val(str(result.id_tienda)) # apply HMAC to id_tienda
            return config.render.delete(result, message) # render delete.html again
        else:
            raise config.web.seeother('/tiendas') # render tiendas delete.html 
