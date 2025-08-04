from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        with open('contacts.txt', 'a') as f:
            f.write(f"{name} | {email} | {message}\n")
    return render_template('contact.html')

@app.route('/certificates')
def certificates():
    return render_template('certificates.html')

@app.route('/experience')
def experience():
    return render_template('experience.html')
@app.route('/education')
def education():
    return render_template('education.html')

if __name__ == '__main__':
    app.run(debug=True)
