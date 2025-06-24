from flask import Flask 
app = Flask(__name__)




if __name__ == '__main__':
     app.run(host= '0.0.0.0', port=8081) # for ec2 instance
     # app.run(debug=True) # for localhost
     