from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "enter a mumber to print factorial that /5 /10"

@app.route("/<int:number>")
def factorial(number):
    fact = 1
    for i in range(1,number+1):
        fact=fact*i
    return f"factorial of {number} is {fact}"
if __name__=="__main__":
    app.run(debug=True)