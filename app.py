from flask import Flask , render_template, request, jsonify
import psycopg2
import psycopg2.extras

app = Flask(__name__)
app.secret_key = "SkillChen_Secret_Key"

DB_HOST='localhost'
DB_PORT='5432'
DB_USER='postgres'
DB_PASS='dba'
DB_NAME='sampledb'

conn = psycopg2.connect(dbname=DB_NAME,user=DB_USER,password=DB_PASS,host=DB_HOST,port=DB_PORT)


@app.route("/")
def index():
  cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
  cur.execute("select * from employee order by id asc")
  employee = cur.fetchall()
  return render_template("index.html", employee=employee)

@app.route("/ajaxfile", methods=['POST','GET'])
def ajaxfile():
  cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
  if request.method == 'POST':
    userid = request.form['userid']
    cur.execute("select * from employee where id=%s",[userid])
    employeelist= cur.fetchall()
  return jsonify({'htmlresponse': render_template('response.html', employeelist=employeelist)})

if __name__ == '__main__':
  app.run(debug=True)
