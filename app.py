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
    str_in = ""
    result = ""
    error = ""
    if request.method == 'POST':
        try:
            str_in = request.form.get('user_input')
            result = str(calc_exe(str_in))
            str_in += " = "
        except Exception as err:
            error = err
    return render_template('template.html', INPUT=str_in, RESULT=result, ERROR=error)


if __name__ == "__main__":
    app.run(debug=True)