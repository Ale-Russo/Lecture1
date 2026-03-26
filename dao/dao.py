import mysql.connector

from dao.dbConnect import DBConnect
from gestionale.core.cliente import ClienteRecord
from gestionale.core.prodotto import ProdottoRecord
from gestionale.provaCollections import cliente


class DAO:

    def getAllProdotti(self):
        cnx=DBConnect.getConnection()
        #cnx = mysql.connector.connect(
        #    user = "root",
        #    password = "1234",
        #    host = "127.0.0.1",
        #    database = "sw_gestionale"
        #)


        cursor = cnx.cursor(dictionary=True)
        cursor.execute("Select * from prodotti")
        row = cursor.fetchall()
        res=[]
        for p in row:
            res.append(ProdottoRecord(p["nome"],p["prezzo"]))

        cursor.close()
        cnx.close()
        return res

    def getAllClienti(self):
        cnx = DBConnect.getConnection()
        #cnx = mysql.connector.connect(
        #    user = "root",
        #    password = "1234",
        #    host = "127.0.0.1",
        #    database = "sw_gestionale"
        #)


        cursor = cnx.cursor(dictionary=True)
        cursor.execute("Select * from clienti")
        row = cursor.fetchall()
        res=[]
        for c in row:
            res.append(ClienteRecord(c["nome"],c["mail"],c["categoria"]))

        cursor.close()
        cnx.close()
        return res

    def addProdotto(self,prodotto):
        cnx = DBConnect.getConnection()
        #cnx = mysql.connector.connect(
        #    user="root",
        #    password="1234",
        #    host="127.0.0.1",
        #    database="sw_gestionale"
        #)

        cursor = cnx.cursor()
        query="""insert into prodotti (nome,prezzo) values (%s,%s)"""
        cursor.execute(query,(prodotto.name,prodotto.prezzo_unitario))

        cnx.commit()
        cursor.close()
        cnx.close()
        return

    def addCliente(self,cliente):
        cnx = DBConnect.getConnection()
        #cnx = mysql.connector.connect(
        #    user="root",
        #    password="1234",
        #    host="127.0.0.1",
        #    database="sw_gestionale"
        #)

        cursor = cnx.cursor()
        query="""insert into clienti (nome,mail,categoria) values (%s,%s,%s)"""
        cursor.execute(query,(cliente.nome,cliente.mail,cliente.categoria))

        cnx.commit()
        cursor.close()
        cnx.close()
        return

    def hasProdotto(self,prodotto):
        cnx = DBConnect.getConnection()
        #cnx = mysql.connector.connect(
        #    user="root",
        #    password="1234",
        #    host="127.0.0.1",
        #    database="sw_gestionale"
        #)

        cursor = cnx.cursor(dictionary=True)
        query="Select * from prodotti where nome=%s"
        cursor.execute(query,(prodotto.name,))
        row = cursor.fetchall()
        cursor.close()
        cnx.close()
        return len(row)>0

    def hasCliente(self,cliente):
        cnx = DBConnect.getConnection()
        #cnx = mysql.connector.connect(
        #    user="root",
        #    password="1234",
        #    host="127.0.0.1",
        #    database="sw_gestionale"
        #)

        cursor = cnx.cursor(dictionary=True)
        query="Select * from clienti where mail=%s"
        cursor.execute(query,(cliente.mail,))
        row = cursor.fetchall()
        cursor.close()
        cnx.close()
        return len(row)>0

if __name__ == "__main__":
    mydao = DAO()
    mydao.getAllProdotti()