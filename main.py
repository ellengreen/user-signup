from flask import Flask, request, redirect, render_template

app = Flask(__name__)

app.config['DEBUG'] = True

@app.route('/', methods=['GET'])
def index():
    return render_template("forms.html")

#Requires form to be filled out
def blank(form):
    if form == "":
        return True
    else:
        return False

#Sets up length requirements
def valid_length(data):
    if len(data) <3 or len(data) >20:
        return False
    else:
        return True

#Checks for spaces
def spaces(data):
    if " " in data:
        return True
    else:
        return False

#Checks for special characters
#special_chars = ('[@_!#$%^&*()<>?/\|}{~:]')
#def special_char(data):


@app.route('/welcome', methods=['POST'])

def verify():
    username = request.form['username']
    password = request.form['password']
    verify = request.form['verify']
    email = request.form['email']

    user_error = ''
    pass_error = ''
    verify_error = ''
    email_error = ''

#Error if username, password, or email doesn't meet length requirements
    if not valid_length(username):
        user_error = "Username must be between 3 and 20 characters"
    if not valid_length(password):
        pass_error = "Password must be between 3 and 20 characters"
    if not valid_length(email):
        email_error = "Email must be between 3 and 20 characters"
    
#Error if passwords don't match
    if password != verify:
        verify_error = "Passwords do not match"

#Error if spaces in form
    if spaces(username):
        user_error = "Must not contain spaces"
    if spaces(password):
        pass_error = "Must not contain spaces"
    if spaces(email):
        email_error = "Must not contain spaces"

#Error if email contains multiple "@" or "."
    if email.count('@') != 1:
        email_error = "Must contain one @ symbol"
    if email.count('.') != 1:
        email_error = "Must contain one period"

#Error if special characters used
 

#Error if user leaves any fields empty (besides email)
    if blank(username):
        user_error = "Must enter a username"
    if blank(password):
        pass_error = "Must enter a password"
    if blank(verify):
        verify_error = "Must re-enter password"
    if blank(email):
        email_error = ''


#If no errors, take user to Welcome page
    if not user_error and not pass_error and not verify_error and not email_error:
        return render_template('welcome.html', username=username)
    else:
        return render_template('forms.html', 
                                user_error=user_error,
                                pass_error=pass_error, 
                                verify_error=verify_error, 
                                email_error=email_error)


app.run()