from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
  {
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Nepal, Nepal',
    'Salary': '1000000円'
  },
  {
    'id': 2,
    'title': 'Data Analyst',
    'location': 'yokohama, kanagawaken',
    'Salary': '1500000円'
  },
  {
    'id': 3,
    'title': 'Frontend Engineer',
    'location': 'Remote',
    'Salary': '1800000円'
  },
  {
    'id': 4,
    'title': 'Backend Engineer',
    'location': 'Shizuokaken',
    'Salary': '1800000円'
  },
]


@app.route("/")
def hello_world():
  return render_template('home.html', jobs=JOBS, company_name="Sudip")


@app.route("/api/job")
def list_jobs():
  return jsonify(JOBS)


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
