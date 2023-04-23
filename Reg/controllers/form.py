def form():
    students = db.executesql("SELECT * FROM students", as_dict=True)
    return dict(students=students)

def index():
    courses = db.executesql("select * from courses" , as_dict=True)
    return (dict(courses=courses)
 	