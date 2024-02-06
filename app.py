from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import yaml

app = Flask(__name__)
db_config = yaml.load(open('database.yaml'), Loader=yaml.FullLoader)
app.config['SQLALCHEMY_DATABASE_URI'] = db_config['uri']
db = SQLAlchemy(app)
CORS(app)

# Define SQLAlchemy models for the 'students' table
class Student(db.Model):
    __tablename__ = "students"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    email = db.Column(db.String(255))
    attendance_average = db.Column(db.Float)
    assignment_completion = db.Column(db.Float)
    ranking = db.Column(db.Integer)
    cohort = db.Column(db.String(255))

    def __init__(self, name, email, attendance_average, assignment_completion, ranking, cohort):
        self.name = name
        self.email = email
        self.attendance_average = attendance_average
        self.assignment_completion = assignment_completion
        self.ranking = ranking
        self.cohort = cohort

    def __repr__(self):
        return '<Student %r>' % self.name

# Define SQLAlchemy models for the 'weekly_attendance' table
class WeeklyAttendance(db.Model):
    __tablename__ = "weekly_attendance"
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('students.id'))
    week = db.Column(db.Integer)
    present = db.Column(db.Boolean)
    absent = db.Column(db.Boolean)

    def __init__(self, student_id, week, present, absent):
        self.student_id = student_id
        self.week = week
        self.present = present
        self.absent = absent

    def __repr__(self):
        return '<WeeklyAttendance %r>' % self.week

# Route to render index.html template
@app.route('/')
def index():
    # Fetch data for display
    students = Student.query.all()

    # Calculate total number of students
    total_students = len(students)

    # Calculate average attendance and assignment completion
    if total_students > 0:
        attendance_sum = sum(student.attendance_average for student in students)
        assignment_sum = sum(student.assignment_completion for student in students)
        average_attendance = attendance_sum / total_students
        average_assignment_completion = assignment_sum / total_students
    else:
        average_attendance = 0
        average_assignment_completion = 0

    return render_template('index.html', average_attendance=average_attendance, average_assignment_completion=average_assignment_completion, total_students=total_students)

# CRUD operations for 'students' table
@app.route('/students', methods=['POST'])
def create_student():
    body = request.json
    name = body['name']
    email = body['email']
    attendance_average = body['attendance_average']
    assignment_completion = body['assignment_completion']
    ranking = body['ranking']
    cohort = body['cohort']

    student = Student(name, email, attendance_average, assignment_completion, ranking, cohort)
    db.session.add(student)
    db.session.commit()

    return jsonify({'status': 'Student created successfully'})

@app.route('/students/<int:id>', methods=['GET'])
def get_student(id):
    student = Student.query.get(id)
    if student:
        return jsonify({'id': student.id, 'name': student.name, 'email': student.email, 'attendance_average': student.attendance_average, 'assignment_completion': student.assignment_completion, 'ranking': student.ranking, 'cohort': student.cohort})
    else:
        return jsonify({'error': 'Student not found'}), 404

@app.route('/students/<int:id>', methods=['PUT'])
def update_student(id):
    body = request.json
    student = Student.query.get(id)
    if student:
        student.name = body.get('name', student.name)
        student.email = body.get('email', student.email)
        student.attendance_average = body.get('attendance_average', student.attendance_average)
        student.assignment_completion = body.get('assignment_completion', student.assignment_completion)
        student.ranking = body.get('ranking', student.ranking)
        student.cohort = body.get('cohort', student.cohort)

        db.session.commit()
        return jsonify({'status': 'Student updated successfully'})
    else:
        return jsonify({'error': 'Student not found'}), 404

@app.route('/students/<int:id>', methods=['DELETE'])
def delete_student(id):
    student = Student.query.get(id)
    if student:
        db.session.delete(student)
        db.session.commit()
        return jsonify({'status': 'Student deleted successfully'})
    else:
        return jsonify({'error': 'Student not found'}), 404

# CRUD operations for 'weekly_attendance' table (existing code)

if __name__ == '__main__':
    app.run(debug=True)
