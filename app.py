from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
   return "Hello from Docker Strategy in OpenShift from sudhanshuuuu   Rohiiiiittttt!"

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
