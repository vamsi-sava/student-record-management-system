from flask import Flask, render_template, request, redirect, url_for, session, flash, Response
import student
import io

app = Flask(__name__)
app.secret_key = 'vamsi_secret_key'

ADMIN_USER = 'Admin@1431'
ADMIN_PASS = 'Vamsi@1431'

@app.route('/', methods=['GET', 'POST'])
def login():
    if session.get('logged_in'):
        return redirect(url_for('dashboard', view='home'))
        
    if request.method == 'POST':
        user_name = request.form['username']
        password = request.form['password']
        if user_name == ADMIN_USER and password == ADMIN_PASS:
            session['logged_in'] = True
            return redirect(url_for('dashboard', view='home'))
        else:
            flash('Invalid Username or Password', 'danger')
            
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
        
    # Determine which step/module to show on the right side
    current_view = request.args.get('view', 'home')
    search_id = request.args.get('search_id')
    edit_id = request.args.get('edit_id')
    
    students_list = []
    edit_student_data = None
    
    if current_view == 'view_all':
        students_list = student.view_all_students()
    elif current_view == 'search' and search_id:
        res = student.search_student_by_id(search_id)
        if res:
            students_list = [res]
        else:
            flash('Student not found', 'warning')
    elif current_view == 'edit' and edit_id:
        edit_student_data = student.search_student_by_id(edit_id)
        
    return render_template('index.html', view=current_view, students=students_list, edit_student=edit_student_data)

@app.route('/add', methods=['POST'])
def add():
    data = {
        'id': int(request.form['id']), 'name': request.form['name'], 'dept': request.form['dept'],
        'year': int(request.form['year']), 'sem': int(request.form['sem']),
        'sub1': int(request.form['sub1']), 'sub2': int(request.form['sub2']),
        'sub3': int(request.form['sub3']), 'sub4': int(request.form['sub4']), 'sub5': int(request.form['sub5'])
    }
    try:
        student.add_student_record(data)
        flash('Student Added Successfully', 'success')
    except:
        flash('Error: Student ID already exists!', 'danger')
    return redirect(url_for('dashboard', view='view_all'))

@app.route('/update/<int:sid>', methods=['POST'])
def update(sid):
    data = {
        'name': request.form['name'], 'dept': request.form['dept'],
        'year': int(request.form['year']), 'sem': int(request.form['sem']),
        'sub1': int(request.form['sub1']), 'sub2': int(request.form['sub2']),
        'sub3': int(request.form['sub3']), 'sub4': int(request.form['sub4']), 'sub5': int(request.form['sub5'])
    }
    student.update_student_record(sid, data)
    flash('Student Updated Successfully', 'success')
    return redirect(url_for('dashboard', view='view_all'))

@app.route('/delete/<int:sid>')
def delete(sid):
    student.delete_student_record(sid)
    flash('Deleted successfully', 'success')
    return redirect(url_for('dashboard', view='view_all'))

@app.route('/export')
def export_report():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    records = student.view_all_students()
    
    csv_data = "ID,Name,Department,Year,Semester,Total,Percentage,Grade\n"
    for s in records:
        csv_data += f"{s['Student_ID']},{s['Name']},{s['Department']},{s['Year']},{s['Semester']},{s['Total']},{s['Perecentage']},{s['Grade']}\n"
        
    return Response(
        csv_data,
        mimetype="text/csv",
        headers={"Content-disposition": "attachment; filename=student_report.csv"}
    )

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)