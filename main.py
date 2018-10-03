from flask import Flask, request, redirect, render_template

app = Flask(__name__)

app.config['DEBUG'] = True

@app.route('/', methods=['GET'])
def base():
    return render_template("forms.html")

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

#Error if user leaves any fields empty (besides email)
    if username == '':
        user_error = "Must enter a username"
    if password == '':
        pass_error = "Must enter a password"
    if verify == '':
        verify_error = "Must re-enter password"

#Error if username/pass isnt valid: contains space, <3 or >20 char
    if len(username) < 3 or len(username) > 20:
        user_error = "Username must be between 3 and 20 characters"
    if len(password) <3 or len(password) > 20:
        pass_error = "Password must be between 3 and 20 characters"
    if password.find(" ") != 0:
        pass_error = "Must contain no spaces"
    
#Error if passwords don't match
    if password != verify:
        verify_error = "Passwords do not match"

#Error if email isn't valid: single @, single ., no spaces, 3-20 char
    if len(email) <3 or len(email) > 20:
        email_error = "Email must be between 3 and 20 characters"
    if email.find(" ") != -1:
        email_error = "Must contain no spaces"
    if email.count('.') != 1:
        email_error = "Must contain only once period"
    if email.count('@') != 1:
        email_error = "Must contain only one @ symbol"

#If no errors, take user to Welcome page
    if not user_error and not pass_error and not verify_error and not email_error:
        return render_template('welcome.html', username=username)
    else:
        return render_template('forms.html', 
                                pass_error=pass_error, 
                                verify_error=verify_error, 
                                email_error=email_error)


app.run()