from flask import Flask, render_template, request, make_response

import pdfkit  # Make sure wkhtmltopdf is installed

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/form')
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
    response.headers['Content-Disposition'] = 'attachment; filename=resume.pdf'
    return response

@app.route('/sample-resume')
def sample_resume():
    sample_data = {
        "name": "Ismail Kilicaslan",
        "email": "paradise@example.com",
        "phone": "123-456-7890",
        "summary": "Experienced software developer with a passion for building user-centric products. Proficient in Python and JavaScript.",
        "skills": "Python, Flask, JavaScript, SQL, HTML, CSS, Git, Docker, AWS, Agile methodologies, REST APIs, Microservices",
        "experience": "DevOps Engineer at ABC Corp\nJunior Dev at XYZ Inc",
        "education": "B.Sc in Mathematics from XYZ University"
    }
    return render_template('resume.html', data=sample_data)

if __name__ == '__main__':
    app.run(debug=True)
    #app.run(host='0.0.0.0', port=8081)  # Run the app on port 8081