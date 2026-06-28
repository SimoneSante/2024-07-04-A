from database.DB_connect import DBConnect
from model.state import State
from model.sighting import Sighting


class DAO():
    def __init__(self):
        pass

    @staticmethod
    def get_all_shape(c):
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Connessione fallita")
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """select distinct s.shape as forma
                        from sighting s
                        where year(s.datetime)=%s"""

            cursor.execute(query,(c,))

            for row in cursor:
                result.append(row["forma"])
            cursor.close()
            cnx.close()
        return result

    @staticmethod
    def get_all_sightings():
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Connessione fallita")
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """select * 
                    from sighting s 
                    order by `datetime` asc """
            cursor.execute(query)

            for row in cursor:
                result.append(Sighting(**row))
            cursor.close()
            cnx.close()
        return result

    @staticmethod
    def get_all_years():
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Connessione fallita")
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """select distinct year(s.datetime) as anno
                        from sighting s
                        order by anno  desc"""
            cursor.execute(query)

            for row in cursor:
                result.append(row["anno"])
            cursor.close()
            cnx.close()
        return result

    @staticmethod
    def get_nodi(c,b):
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Connessione fallita")
        else:
            cursor = cnx.cursor(dictionary=True)
            query = f"""select s.*
                        from sighting s
                        where year(s.datetime)=%s and s.shape="{b}" """
            params=(c,)
            cursor.execute(query,params)
            for row in cursor:
                result.append(Sighting(**row))
            cursor.close()
            cnx.close()
        return result

    @staticmethod
    def get_archi(c, b):
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Connessione fallita")
        else:
            cursor = cnx.cursor(dictionary=True)
            query = f"""with nodi as(select s.*
                        from sighting s
                        where year(s.datetime)=%s and s.shape="{b}")
    
                        select  n1.id as id, n2.id as id1
                        from nodi n1, nodi n2
                        where n1.state =n2.state and n1.datetime < n2.datetime  """
            params = (c,)
            cursor.execute(query, params)
            for row in cursor:
                result.append((row["id"],row["id1"]))
            cursor.close()
            cnx.close()
        return result

