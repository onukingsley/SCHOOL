from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    pageInfo = {
        'title': 'Welcome',
    }
    return render_template('index.html', name="Welcome", pg=pageInfo)


@app.route('/about')
def about():
    pageInfo = {
        'title': 'about us',
        'sub': 'Your ward is important to us. Feel free to drop it and pick it up later'
    }
    return render_template('about.html', pg=pageInfo)


@app.route('/admission')
def admissions():
    pageInfo = {
        'title': 'admission',
        'sub': 'Admission is currently undergoing. Rush now before it is too late and stay one year at home'
    }
    return render_template('admissions.html', pg=pageInfo)


if __name__ == '__main__':
    app.run(debug=True)
