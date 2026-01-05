from flask import Flask, request

app = Flask(__name__)

# VULNERABILITY 1: Hardcoded AWS Secret (SAST/Secret Scanners should catch this)
# In a real app, this should be an environment variable.
AWS_ACCESS_KEY_ID = "AKIAIMYOURFATHER1234"
AWS_SECRET_ACCESS_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"

@app.route('/')
def home():
    return "<h1>The Gatekeeper App is Running!</h1>"

@app.route('/user')
def user():
    # VULNERABILITY 2: Cross-Site Scripting (XSS)
    # We are taking user input ('name') and returning it directly to the browser 
    # without sanitizing it. A hacker could pass Javascript here.
    username = request.args.get('name', 'Guest')
    return f"Hello, {username}! Your access key is hidden."

if __name__ == '__main__':
    # Running on 0.0.0.0 is required for Docker to expose the port later
    app.run(debug=True, host='0.0.0.0', port=5000)