import mysql.connector
from flask import Flask, render_template, request

app = Flask(__name__)

# Connect to MySQL database
db = mysql.connector.connect(
    host="covid.csjkhblwl2np.us-west-2.rds.amazonaws.com",
    user="admin",
    password="admin1234",
    database="covid"
)
cursor = db.cursor()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        uname = request.form['uname']
        email = request.form['email']
        phone_number = request.form['phone_number']
        num_vaccines = request.form['num_vaccines']
        
        # Insert form data into MySQL table
        cursor.execute("INSERT INTO form_submissions (uname, email, phone_number, num_vaccines) VALUES (%s, %s, %s, %s)",
                       (uname, email, phone_number, num_vaccines))
        db.commit()
        
        return render_template('result.html', uname=uname, email=email, phone_number=phone_number, num_vaccines=num_vaccines)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
