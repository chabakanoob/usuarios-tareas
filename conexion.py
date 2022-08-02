
import mysql.connector as msql
import clases as cl
import os

def limpiar_pantalla():

    limpiar = "clear"

    if os.name in ("nt","dos"):
        limpiar="cls"
    
    os.system(limpiar)

def conectar(hostname,username,passwduser,database_user):

    conexion = None

    try:
        conexion = msql.connect(
            database = database_user,
            host = hostname,
            user = username,
            passwd = passwduser
            )
        print("conexion establecida")
    except:
        print("algo saliio mal !")
    
    return conexion


miconexion = conectar("127.0.0.1","root","1234","work_ramen")


def insertar_usuario(conexion,usuario,passwd):

    try:

        cursor = conexion.cursor()

        cursor.execute("insert into usuario values (null,'{}','{}')".format(usuario,passwd))

        conexion.commit()

        cursor.close()

    except Exception as e:
        print("insercion fallida !",e)


def consultar_tabla(conexion,tabla,campos):

    try:

        cursor =conexion.cursor()

        cursor.execute("select {} from {}".format(campos,tabla))

        for row in cursor:

            print("usuario :",row[0]," |||| pass :",row[len(row)-1],end="\n\n")

    except Exception as e:
        print("consulta fallida !",e)

    cursor.close()

def consultar_usuario(conexion,usuario):

    cursor = conexion.cursor()
    try:
        cursor.execute("select * from usuario where nombre = '{}'".format(usuario))

        # iterador = cursor.__iter__()

        # primero = iterador.__next__()
        # print("primero",primero)


        for x in cursor:
            return x

        # print(iterador.__next__())
        # print(iterador.__next__())
        # print(iterador.__next__())
        # print(iterador.__next__())
        # print(iterador.__next__())

        cursor.close()
        
    except Exception as e:
        print("excepcion consluta",e)
        cursor.close()
        return False

def consultar_tarea(conexion,tarea,id_usuario):

    cursor = conexion.cursor()

    try:
        cursor.execute("select t.id_tarea,t.nombre,t.descripcion,t.estado from tareas t,usuario u where t.id_usuario=u.id_usuario and u.id_usuario={} and t.nombre like '{}%'".format(id_usuario,tarea))

        container_tareas = []

        for x in cursor:

            container_tareas.append(x)

        cursor.close()

        return container_tareas
    
    except Exception as e:
        print("excepcion consulta",e)





# insertar_usuario(miconexion,"arlequin","yyyy")

# consultar_tabla(miconexion,"usuario")


def log_user(username):  

    usuario_escogido = consultar_usuario(miconexion,username)

    if usuario_escogido == None:

        print("Este usuario no existe")

    else:

        print("usuario encontrado !\n\n")

        intentos = 3

        while True:

            pass_user = input("introduce la passwd : ")

            if pass_user == usuario_escogido[2]:

                print("Logeado con exito !")
                print(active_user)
                
                return True,usuario_escogido 
                
            else:
                print("error ! Intentos restantes {}".format(intentos))
                intentos -=1

            if intentos == 0:
                print("\nhas consumido tus intentos")
                
                return (False)

active_user = None

while True:


    try:

        action = int(input("\n\n1 --consultar usuarios \n\n 2 -- agregar usuarios \n\n 3 -- iniciar sesion"))

        if action == 0:
            print("bye !")
            break

        if action == 1:

            consultar_tabla(miconexion,"usuario","nombre,password")

        if action == 2:

            nomuser = input("Enter name : ")
            passwd_user = input("Enter passwd : ")

            insertar_usuario(miconexion,nomuser,passwd_user)
        


        if action == 3 and active_user == None:

            print(active_user)
            
            while True:

                action = input("[0] para salir \ \ \  introduce el nick : ")

                if action == "0":
                    break
                else:
                    succes  = log_user(action)

                    if succes[0]:

                        active_user = True

                        current_user = cl.Usuario(succes[1][0],succes[1][1],succes[1][2])

                        while True:

                            limpiar_pantalla()

                            print("\n\n    -----> usuario : {}".format(current_user.nombre))
                            
                            action_user = int(input("\n\n[0] para salir [1] consultar total de tareas [2] buscar tarea por nombre"))
                    
                            if action_user == 0:
                                break

                            if action_user == 1:
                                pass

                            if action_user == 2:

                                
                                tarea_usuario = input("nombre de la tarea ----- >  \n\n")

                                contenedor = consultar_tarea(miconexion,tarea_usuario,current_user.id_usuario)
                                
                                #creamos tantos objetos de tareas como coincidencias tengamos en la busqueda y agregamos a lista vacia
                                contenedor_tareas_obj = []

                                for x,tarea in enumerate(contenedor):

                                    contenedor_tareas_obj.append(cl.Tarea(contenedor[x][0],contenedor[x][1],contenedor[x][2],contenedor[x][3]))

                                for tarea in contenedor_tareas_obj:
                                    print("--------------------------------------------------------------------------------------")
                                    print("nombre tarea -- >",tarea.nombre)
                                    print("\ndecripcion -- >",tarea.descripcion)
                                    print("\nestado -- >",tarea.estado)
                                    print("--------------------------------------------------------------------------------------")

             

            

        
        else:
            print("ya estas logeado con ",active_user[1])


    except Exception as e:
        print("Fail (3) !",e)

















        # action = in(input cristiano es mejor que messi sin duda.)