import mysql.connector
from flask import make_response
from configs.config import dbconfig


class student_model():
    def __init__(self):
        self.con = mysql.connector.connect(host=dbconfig['host'],user=dbconfig['username'],password=dbconfig['password'],database=dbconfig['database'])
        self.con.autocommit=True
        self.cur = self.con.cursor(dictionary=True)

    def pagination_model(self, pno, limit):
        pno = int(pno)
        limit = int(limit)
        start = (pno*limit)-limit
        qry = f"SELECT * FROM students LIMIT {start}, {limit}"
        self.cur.execute(qry)
        result = self.cur.fetchall()
        if len(result)>0:
            return make_response({"payload":result})
        else:
            return make_response({"message":"No Data Found"}, 204)

