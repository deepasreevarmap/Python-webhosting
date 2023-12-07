from flask import Flask,render_template,request
import mysql.connector
# Create the Flask application
app = Flask(__name__)
user_dict={'admin':'1234','user':'5678'}
connection = mysql.connector.connect(host='localhost',user='root',password='',database='ems')
mycursor = connection.cursor()
# Define a route and the corresponding view function
@app.route('/')
def hello():
    return render_template('first.html')
@app.route('/empl')
def about():
    return render_template('emp.html')
@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/login_home', methods=['POST'])
def login_home():
    
    username = request.form['username']
    pwd = request.form['password']
    if username not in user_dict:
        return render_template('/login.html',msg='Invalid username')
    elif user_dict[username] !=pwd:
        return render_template('/login.html',msg='invalid password')
    else:
        return render_template('/home.html')
    
@app.route('/view_all')
def view():
    query = "SELECT * FROM EMPLOYEE"
    mycursor.execute(query)
    data = mycursor.fetchall()
    return render_template('/view.html',sqldata=data)

@app.route('/search')
def search():
    return render_template('/search.html')

@app.route('/searchresult',methods=["POST"])
def searchresult():
    ename=request.form.get('emp_id')
    query = "SELECT * FROM EMPLOYEE WHERE EMP_ID="+ename
    mycursor.execute(query)
    data = mycursor.fetchall()
    return render_template('/view.html',sqldata=data)
@app.route('/add')
def search():
    return render_template('/add.html')
         

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)