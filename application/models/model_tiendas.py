import web
import config

db = config.db


def get_all_tiendas():
    try:
        return db.select('tiendas')
    except Exception as e:
        print "Model get all Error {}".format(e.args)
        print "Model get all Message {}".format(e.message)
        return None


def get_tiendas(id_tienda):
    try:
        return db.select('tiendas', where='id_tienda=$id_tienda', vars=locals())[0]
    except Exception as e:
        print "Model get Error {}".format(e.args)
        print "Model get Message {}".format(e.message)
        return None


def delete_tiendas(id_tienda):
    try:
        return db.delete('tiendas', where='id_tienda=$id_tienda', vars=locals())
    except Exception as e:
        print "Model delete Error {}".format(e.args)
        print "Model delete Message {}".format(e.message)
        return None


def insert_tiendas(nombre_tienda,nom_acceso_tienda,contrasena_tienda,fotografia_tienda,promedio_evaluaciones):
    try:
        return db.insert('tiendas',nombre_tienda=nombre_tienda,
nom_acceso_tienda=nom_acceso_tienda,
contrasena_tienda=contrasena_tienda,
fotografia_tienda=fotografia_tienda,
promedio_evaluaciones=promedio_evaluaciones)
    except Exception as e:
        print "Model insert Error {}".format(e.args)
        print "Model insert Message {}".format(e.message)
        return None


def edit_tiendas(id_tienda,nombre_tienda,nom_acceso_tienda,contrasena_tienda,fotografia_tienda,promedio_evaluaciones):
    try:
        return db.update('tiendas',id_tienda=id_tienda,
nombre_tienda=nombre_tienda,
nom_acceso_tienda=nom_acceso_tienda,
contrasena_tienda=contrasena_tienda,
fotografia_tienda=fotografia_tienda,
promedio_evaluaciones=promedio_evaluaciones,
                  where='id_tienda=$id_tienda',
                  vars=locals())
    except Exception as e:
        print "Model update Error {}".format(e.args)
        print "Model updateMessage {}".format(e.message)
        return None
