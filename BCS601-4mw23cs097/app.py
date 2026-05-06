from flask import Flask, render_template, request

app = Flask(__name__)

def hcf(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return (a * b) // hcf(a, b)

def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

@app.route('/', methods=['GET', 'POST'])
def index():
    result = {}

    if request.method == 'POST':
        num1 = int(request.form['num1'])
        num2 = int(request.form['num2'])
        string = request.form['string']

        result['hcf'] = hcf(num1, num2)
        result['lcm'] = lcm(num1, num2)
        result['reverse'] = string[::-1]

        fact_list = {}
        for i in range(4, 9):
            fact_list[i] = factorial(i)

        result['factorials'] = fact_list

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)