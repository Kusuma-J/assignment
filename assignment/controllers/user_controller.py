from app import app
from models.student_model import student_model
from flask import render_template
obj = student_model()

@app.route("/students/page/<pno>/limit/<limit>", methods=["get"])
def pagination(pno, limit):
    return obj.pagination_model(pno, limit)

# @app.route('/student/page/<pno>/limit/<limit>',methods=["get"])
# def paginate_students(pno, limit):
#     return render_template('students.html', students=obj.pagination_model(pno, limit))
