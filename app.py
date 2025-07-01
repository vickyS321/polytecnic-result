from flask import Flask, render_template, request, redirect

app = Flask(_name_)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        roll = request.form['roll']
        return redirect(f"https://result.bteupexam.in/ShowResult.aspx?RollNo={roll}")
    return render_template('index.html')

if _name_ == '_main_':
    app.run(debug=True)
