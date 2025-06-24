from flask import Flask, render_template, request, make_response
import pdfkit

app = Flask(__name__)

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/')
def form():
    return render_template('form.html')

@app.route('/resume', methods=['POST'])
def resume():
    data = request.form.to_dict()
    return render_template('resume.html', data=data)

@app.route('/download', methods=['POST'])
def download_resume():
    data = request.form.to_dict()
    rendered = render_template('resume.html', data=data)
    pdf = pdfkit.from_string(rendered, False)
    response = make_response(pdf)
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = 'attachment; filename=lebenslauf.pdf'
    return response

if __name__ == '__main__':
    app.run(debug=True)
    #app.run(host='0.0.0.0', port=8081)
    
