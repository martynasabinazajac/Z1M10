from flask import Flask, render_template

app=Flask(__name__)

#1.zachowanie aplikacji po wejściu na stronę główną

@app.route('/')
def homepage():
    movies = ["1","2", "3", "4", "5"]
    return render_template("homepage.html", movies=movies)

if __name__ == '__main__':
    app.run(debug=True)