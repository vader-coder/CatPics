from flask import Flask, render_template
from flask import request, redirect 

app = Flask(__name__)
email_addresses = set()

#app should route '/' to hello world
@app.route('/')
def hello_world():
    author = "vader-coder"
    return render_template('index.html', author=author)

#use signup() when browser requests /signup
@app.route('/signup', methods = ['POST'])
def signup():
    email = request.form['email']#name = 'email'
    if email not in email_addresses:
        email_addresses.add(email)
    #print("The email address is \"" + email + "\"")
    return redirect('/')

@app.route('/emails')
def emails():
    return render_template('emails.html', email_addresses=email_addresses)

#if this module is one being run, run the app. 
if __name__ == '__main__':
    app.run()

    