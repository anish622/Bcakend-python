from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "please add a number to the url,like/5 or /10"
@app.route("/<int:number>")
def prime(number):
    primes = []
    for i in range(2, number + 1):
        for n in range(2, int(i ** 0.5) + 1):
            if i % n == 0:
                break
        else:
            primes.append(str(i))
    return ','.join(primes)


if __name__=="__main__":
    app.run(debug=True)