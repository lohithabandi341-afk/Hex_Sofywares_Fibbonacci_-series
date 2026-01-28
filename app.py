from flask import Flask, render_template, request

app = Flask(__name__)

def fibonacci(n):
    series = []
    a, b = 0, 1
    for _ in range(n):
        series.append(a)
        a, b = b, a + b
    return series

@app.route('/', methods=['GET', 'POST'])
def index():
    fib_series = []
    if request.method == 'POST':
        num = int(request.form['number'])
        fib_series = fibonacci(num)
    return render_template('index.html', result=fib_series)

if __name__ == '__main__':
    app.run(debug=True)
