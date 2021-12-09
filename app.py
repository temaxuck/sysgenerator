from flask import Flask, render_template, request, url_for, redirect
from modules.Generator import GenSLU

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        if request.form.get('method') == 'Метод Гаусса':
            method = "Gauss"
        elif request.form.get('method') == 'Метод Крамера':
            method = "Cramer"
        elif request.form.get('method') == 'LU-метод':
            method = "LU"

        # might be needed later...
        # if request.form.get('AboutGauss'):
        #     return redirect("https://ru.wikipedia.org/wiki/%D0%9C%D0%B5%D1%82%D0%BE%D0%B4_%D0%93%D0%B0%D1%83%D1%81%D1%81%D0%B0")
        # elif request.form.get('AboutCramer'):
        #     print("About Cramer")
        # elif request.form.get('AboutLU'):
        #     print("About LU")
        
        return redirect(url_for("user_input", method=method))

    return render_template('home.html')
    
@app.route('/input<method>', methods=['POST', 'GET'])
def user_input(method, wrong=0):
    if request.method == 'POST':
        dim = request.form.get('dimension')
        return redirect(url_for("generator", dim=dim, method=method))
	
    return render_template("input.html", wrong=wrong, method=method)

@app.route('/generator<method><dim>', methods=['POST', 'GET'])
def generator(dim, method):
    try:
        dim = int(dim)
    except ValueError:
        return redirect(url_for("user_input", wrong=1, method=method))
    matrix, answer = GenSLU(dim)
    print(matrix, answer)

    return render_template('generator.html', matrix = matrix, solvec= answer, dimension = dim, method=method)

if __name__ == '__main__':
    app.run(debug=True)