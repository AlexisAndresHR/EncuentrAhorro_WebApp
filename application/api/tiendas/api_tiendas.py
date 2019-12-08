import web
import config
import json


class Api_tiendas:
    def get(self, id_tienda, nombre_tienda):
        try:
            # http://0.0.0.0:8080/api_tiendas?user_hash=dc243fdf1a24cbced74db81708b30788&action=get
            if id_tienda is None and nombre_tienda is None:
                result = config.model.get_all_tiendas()
                tiendas_json = []
                for row in result:
                    tmp = dict(row)
                    tiendas_json.append(tmp)
                web.header('Content-Type', 'application/json')
                return json.dumps(tiendas_json)
            # http://0.0.0.0:8080/api_tiendas?user_hash=12345&action=get&id_tienda=1
            elif id_tienda is not None and nombre_tienda is None:
                result = config.model.get_tiendas(int(id_tienda))
                tiendas_json = []
                tiendas_json.append(dict(result))
                web.header('Content-Type', 'application/json')
                return json.dumps(tiendas_json)
            # http://0.0.0.0:8080/api_tiendas?user_hash=12345&action=get&nombre_tienda=SeA
            elif id_tienda is None and nombre_tienda is not None:
                result = config.model.get_infotienda_xnombre(str(nombre_tienda))
                tiendas_json = []
                tiendas_json.append(dict(result))
                web.header('Content-Type', 'application/json')
                return json.dumps(tiendas_json)
        
        except Exception as e:
            print "GET Error {}".format(e.args)
            tiendas_json = '[]'
            web.header('Content-Type', 'application/json')
            return json.dumps(tiendas_json)


# http://0.0.0.0:8080/api_tiendas?user_hash=12345&action=put&id_tienda=1&product=nuevo&description=nueva&stock=10&purchase_price=1&price_sale=3&product_image=0
    def put(self, nombre_tienda,nom_acceso_tienda,contrasena_tienda,fotografia_tienda,promedio_evaluaciones):
        try:
            config.model.insert_tiendas(nombre_tienda,nom_acceso_tienda,contrasena_tienda,fotografia_tienda,promedio_evaluaciones)
            tiendas_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(tiendas_json)
        except Exception as e:
            print "PUT Error {}".format(e.args)
            return None

# http://0.0.0.0:8080/api_tiendas?user_hash=12345&action=delete&id_tienda=1
    def delete(self, id_tienda):
        try:
            config.model.delete_tiendas(id_tienda)
            tiendas_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(tiendas_json)
        except Exception as e:
            print "DELETE Error {}".format(e.args)
            return None

# http://0.0.0.0:8080/api_tiendas?user_hash=12345&action=update&id_tienda=1&product=nuevo&description=nueva&stock=10&purchase_price=1&price_sale=3&product_image=default.jpg
    def update(self, id_tienda, nombre_tienda,nom_acceso_tienda,contrasena_tienda,fotografia_tienda,promedio_evaluaciones):
        try:
            config.model.edit_tiendas(id_tienda,nombre_tienda,nom_acceso_tienda,contrasena_tienda,fotografia_tienda,promedio_evaluaciones)
            tiendas_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(tiendas_json)
        except Exception as e:
            print "GET Error {}".format(e.args)
            tiendas_json = '[]'
            web.header('Content-Type', 'application/json')
            return json.dumps(tiendas_json)

    def GET(self):
        user_data = web.input(
            user_hash=None,
            action=None,
            id_tienda=None,
            nombre_tienda=None,
            nom_acceso_tienda=None,
            contrasena_tienda=None,
            fotografia_tienda=None,
            promedio_evaluaciones=None,
        )
        try:
            user_hash = user_data.user_hash  # user validation
            action = user_data.action  # action GET, PUT, DELETE, UPDATE
            id_tienda=user_data.id_tienda
            nombre_tienda=user_data.nombre_tienda
            nom_acceso_tienda=user_data.nom_acceso_tienda
            contrasena_tienda=user_data.contrasena_tienda
            fotografia_tienda=user_data.fotografia_tienda
            promedio_evaluaciones=user_data.promedio_evaluaciones
            # user_hash
            if user_hash == 'dc243fdf1a24cbced74db81708b30788':
                if action is None:
                    raise web.seeother('/404')
                elif action == 'get':
                    return self.get(id_tienda, nombre_tienda)
                elif action == 'put':
                    return self.put(nombre_tienda,nom_acceso_tienda,contrasena_tienda,fotografia_tienda,promedio_evaluaciones)
                elif action == 'delete':
                    return self.delete(id_tienda)
                elif action == 'update':
                    return self.update(id_tienda, nombre_tienda,nom_acceso_tienda,contrasena_tienda,fotografia_tienda,promedio_evaluaciones)
            else:
                raise web.seeother('/404')
        except Exception as e:
            print "WEBSERVICE Error {}".format(e.args)
            raise web.seeother('/404')
