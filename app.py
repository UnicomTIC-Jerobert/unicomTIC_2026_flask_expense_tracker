from flask import Flask

app = Flask(__name__)

@app.get("/")
def home():
    return "HELLO FROM FLASK IN WINDOWS"

if __name__ == "__main__":
    app.run(debug=True)



