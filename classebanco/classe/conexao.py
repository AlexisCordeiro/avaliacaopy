import mysql.connector
import os
import boto3
def conectar():
    mydb = mysql.connector.connect(
        host="172.31.1.248",
        user="root",
        password='r00t123',
        database="livro"
        )
    return mydb
        

    
