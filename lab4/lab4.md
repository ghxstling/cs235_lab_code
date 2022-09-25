# **COMPSCI 235 - LAB 4**
###### Name: Dylan Choy
###### UPI: dcho282

## **Notes**

Basic HTML Page
```html
<!DOCTYPE html>
<html>
    <head>
        <title>Page Title</title>
    </head>
    <body>
        <!-- Write your comments here -->
        <h1>This is a heading.</h1>
        <p>This is a paragraph.</p>
    </body>
</html>
```

HTML with external CSS

In the HTML file:
```html
<!-- index.html -->
<!DOCTYPE html>
<html>
    <head>
        <link rel="stylesheet" href="styles.css">
        <!-- This is a link tag to the CSS file -->
    </head>
    <body>
        <h1>This is a heading.</h1>
        <p class="mytext">This is a paragraph.</p>
    </body>
</html>
```
In the CSS file:
```css
/* styles.css */
h1 {
    color: darkblue;
}

.mytext {
    color: cornflowerblue;
}
```

Minimal Flask App
```py
# main.py
from flask import Flask

app = Flask(__name__)

# '/' is the router path
@app.route('/')
def hello_world():
    return "<h1>Hello World!</h1>"

if __name__ == '__main__':
    app.run(debug=True, port=8000)
    # debug = enables the debugger
    # port = specifies the port number
```
- Environment Variable: On Windows Command Prompt, you need to set the FLASK_APP environment variable to the name of the application (the python file name) if you don't call the app.run() function

Project Layout
- Flask expects a project to be organised in a specific structure
    - This is due to security reasons, as a user should not be allowed access to view the source code of a file
- All Flask apps serve files found under the 'static' directory

Directory Structure Example:
```
├── static
│   └── css
│       └── styles.css
├── templates
│   └── index.html
├── main.py
│
└──.gitignore
```

Read variables from URL
```py
# main.py
from markupsafe import escape
from flask import Flask, render_template

app = Flask(__name__)

# <username> is a variable in the URL
@app.route('/user/<username>')
def show_user_profile(username):
    return f'Hello, {escape(username)}'

# <input_val> is a variable in the URL of type int
@app.route('/factorial/<int: input_val>')
def show_factorial(input_val):
    # Function from Lab 1
    factorial = compute_factorial(input_val)
    return render_template('index.html',
        input=input_val,
        factorial=factorial)

if __name__ == '__main__':
    app.run()
```
```html
<!-- factorial.html -->
<h1>This tool computes factorial (n!)</h1>
<p>{{ input }}! = {{ factorial }}</p>
<!-- Texts in double curly brackets are rendered as variables -->
```

## **Hands-on Lab Activity:**

### Questions

**1.** Whatʼs the terminal command for starting a Flask server?
> To start a Flask server in terminal, you use the `flask run` command or `python -m flask run` command.

**2.** Why do we want to enable debug mode during development?
> By enabling debugging mode, the Flask server will automatically detect any code changes in the web application and reload itself. This is convenient for developers as they ultimately don't need to restart the server every time they change their source code.\ Additionally, the server browser will display an interactive debugger if any error occurs.

**3.** If you put a python file under `./static/` directory, can you access it from the browser?
> Yes, you can.

**4.** What is URL encoding and why does it exist?
> URL encoding converts characters from the ASCII character-set into a format that is compatible with the Internet for transmission. Because URLs typically only contain ASCII characters, any non-ASCII character found in the URL must be converted in order for them to be sent over the Internet successfully, which is done by URL encoding. Such characters are replaced with a % followed by a string of hexadecimal digits. Additionally, any spaces found in the URL are replaced with either a + sign or "%20".
