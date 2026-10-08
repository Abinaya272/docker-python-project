from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>PEP Cloud App</h1>
    <h2>Hello from Docker!</h2>
    <p>Successfully deployed on AWS EC2 using Terraform and GHCR.</p>
    """

app.run(host="0.0.0.0", port=80)