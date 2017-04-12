import os
import sys
from flask import (Flask,flash, make_response, render_template, 
		request, url_for, redirect, session, g)


app = Flask(__name__)
#app.config['SECRET_KEY'] = 'super secret key'
 

@app.route('/')
def index():
    return render_template('union_demo.html')



@app.route('/contact',methods=['POST'])
def contact():

    name = request.form['name']
    mail = request.form['mail']
    number = request.form['number']
    message = request.form['message']


    return render_template('index.html', name_1 = name)




"""
@app.route('/sim')
def index():
    return render_template('sim.html')
"""

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)


"""
import sys
if sys.argv[1].upper() == 'DEBUG':
   app.run(host='0.0.0.0', port=8001, debug=True)
elif sys.argv[1].upper() == 'RUNSERVER':
    app.run(host='0.0.0.0', port=80) 
"""
