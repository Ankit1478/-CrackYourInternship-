#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Hello World</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            }
            h1 {
                color: white;
                font-size: 4em;
                text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
            }
        </style>
    </head>
    <body>
        <h1>Hello, World! 🌍</h1>
    </body>
    </html>
    '''

if __name__ == '__main__':
    # Run on all interfaces (0.0.0.0) to make it accessible externally
    app.run(host='0.0.0.0', port=5000, debug=True)
