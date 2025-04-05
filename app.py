from flask import Flask, redirect

app = Flask(__name__)

@app.route('/')
def open_website():
    return redirect("https://example.com")  # change this to the site you want

if __name__ == '__main__':
    app.run(debug=True)
