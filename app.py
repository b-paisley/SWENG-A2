from flask import Flask, request, render_template
import calc

app = Flask(__name__)
print(__name__)
@app.route('/', methods=['POST', 'GET'])
def calculate():
    result = " "
    error = " "
    if request.method == 'POST':
        try:
            result = calc.calc_exe(input_str=request.form.get('user_input'))
        except Exception as err:
            error = err

    print(result)
    return render_template('tamplate.html', RESULT=result, ERROR=error)

if __name__ == "__main__":
    print("running")
    app.run(host='localhost', port=5000)