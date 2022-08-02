class Usuario():

    def __init__(self,idd,nombre,password):

        self.id_usuario = idd
        self.nombre =nombre 
        self.password =password


class Tarea():

    def __init__(self,idd,nombre,desc,estado):
        
        self.id_tarea = idd
        self.nombre = nombre
        self.descripcion = desc
        self.estado = estado