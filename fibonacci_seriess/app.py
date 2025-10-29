from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "enter a mumber to print fibonacci series utill that /5 /10"

@app.route("/<int:number>")
def fibo(number):
    fibs = "first" +  str(number) + "fibonacci numbers are"
    
    fib1,fib2=0,1
    
    for i in range(number):
        fibs+=str(fib1) + ","
        fib1,fib2 = fib2,fib1+fib2
    return fibs

if __name__=="__main__":
    app.run(debug=True)
    