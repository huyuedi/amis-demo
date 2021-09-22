from flask import Flask, render_template, request, redirect, session, url_for, jsonify
app = Flask(__name__)
app.debug=True

@app.route('/')
def parent():
     return render_template('parent.html')

@app.route('/child')
def child():
    return render_template('child.html')

if __name__ == '__main__':
    app.run()