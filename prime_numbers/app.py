from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "please enter a number to print prime nummbers utill like /5 /10"

@app.route("/<int:number>")
def prime(number):
    primes = ","
    
    for i in range(2,number+1):
        for n in range(2,(i//2)+1):
            if (i%n)==0:
               break
        else:
                primes+=str(i)+ ","
    return primes

if __name__=="__main__":
    app.run(debug=True)