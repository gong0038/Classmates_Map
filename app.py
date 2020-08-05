from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from forms import inputForm
import sqlite3
import base64
import webbrowser

app = Flask(__name__)
app.config['SECRET_KEY'] = '123456789'


@app.route('/')
def home():
    return render_template('index.html', the_title="Homepage")


@app.route('/findStudent', methods=['post', 'get'])
def find_student():
    form = inputForm()
    con = sqlite3.connect('week10.db')
    c = con.cursor()
    query = "select id, student from lab10 where student is not null order by student"
    c.execute(query)
    theseStudents = list(c.fetchall())
    nameList = theseStudents
    form.lstNames.choices = nameList

    if request.method == "POST":
        Name = form.lstNames.data
        c1 = con.cursor()
        query = "select id, link from lab10 where id={}".format(int(Name))
        c1.execute(query)
        oneRecord = c1.fetchone()
        thisUrl = base64.urlsafe_b64decode(oneRecord[1]).decode("utf-8")
        webbrowser.open(thisUrl, new=2)
        c1.close()
    c.close()
    return render_template("inputForm.html", form=form, the_title="Find the student")


@app.route('/displayAll', methods=['post', 'get'])
def display_all():
    con1 = sqlite3.connect("week10.db")
    c1 = con1.cursor()
    query = "select student, city, country,link from lab10 order by student asc"
    c1.execute(query)
    thoseStudents = c1.fetchall()
    newList = []
    urlList = []
    for row in thoseStudents:
        newList.append(row)
        url = base64.urlsafe_b64decode(row[3]).decode('utf-8')
        urlList.append(url)
    lst = zip(newList, urlList)
    return render_template("displayAll.html", lst=lst, the_title="Display all students")


if __name__ == '__main__':
    app.run(debug=True)
