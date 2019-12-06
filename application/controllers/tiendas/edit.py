import config
import hashlib
import app

class Edit:
    
    def __init__(self):
        pass

    '''
    def GET(self, id_tienda, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_EDIT(id_tienda) # call GET_EDIT function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    def POST(self, id_tienda, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.POST_EDIT(id_tienda) # call POST_EDIT function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    @staticmethod
    def GET_EDIT(id_tienda, **k):

    @staticmethod
    def POST_EDIT(id_tienda, **k):
        
    '''

    def GET(self, id_tienda, **k):
        message = None # Error message
        id_tienda = config.check_secure_val(str(id_tienda)) # HMAC id_tienda validate
        result = config.model.get_tiendas(int(id_tienda)) # search for the id_tienda
        result.id_tienda = config.make_secure_val(str(result.id_tienda)) # apply HMAC for id_tienda
        return config.render.edit(result, message) # render tiendas edit.html

    def POST(self, id_tienda, **k):
        form = config.web.input()  # get form data
        form['id_tienda'] = config.check_secure_val(str(form['id_tienda'])) # HMAC id_tienda validate
        # edit user with new data
        result = config.model.edit_tiendas(
            form['id_tienda'],form['nombre_tienda'],form['nom_acceso_tienda'],form['contrasena_tienda'],form['fotografia_tienda'],form['promedio_evaluaciones'],
        )
        if result == None: # Error on udpate data
            id_tienda = config.check_secure_val(str(id_tienda)) # validate HMAC id_tienda
            result = config.model.get_tiendas(int(id_tienda)) # search for id_tienda data
            result.id_tienda = config.make_secure_val(str(result.id_tienda)) # apply HMAC to id_tienda
            message = "Error al editar el registro" # Error message
            return config.render.edit(result, message) # render edit.html again
        else: # update user data succefully
            raise config.web.seeother('/tiendas') # render tiendas index.html
