from flask import Flask, request, render_template
import calc

app = Flask(__name__)

def calc_exe(input_str: str):
    """
    It takes a string, converts it to a list, and then calls the calc function on that list

    :param input_str: The string to be converted to a list and then calculated
    :type input_str: str
    :return: The result of the calculation.
    """
    input_list = calc.to_list(input_str)
    return round(calc.calc(input_list), 3)


@app.route('/', methods=['POST', 'GET'])
def calculate():
    result = " "
    error = " "
    if request.method == 'POST':
        try:
            result = calc_exe(input_str=request.form.get('user_input'))
        except Exception as err:
            error = err

    return render_template('tamplate.html', RESULT=result, ERROR=error)


if __name__ == "__main__":
    app.run(host='localhost', port=5000)