from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        text = request.form['text']
        # Підрахунок кількості рядків у введеному тексті
        lines = text.split('\n')
        line_count = len(lines)
        return render_template('index.html', line_count=line_count)
    return render_template('index.html', line_count=None)

if __name__ == '__main__':
    app.run(debug=True)
