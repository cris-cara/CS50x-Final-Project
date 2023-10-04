import datetime
import random
from cs50 import SQL
from flask import Flask, redirect, request, session
from flask_session import Session
from helpers import *

# Create an instance of the Flask app
app = Flask(__name__)

# Define constants for the game's result
WINNER = "Winner"
LOSER = "Loser"

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///hangman.db")
# Create table
db.execute("CREATE TABLE IF NOT EXISTS history ("
           "id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, "
           "name TEXT NOT NULL, "
           "start_time DATETIME NOT NULL UNIQUE, "
           "secret_word TEXT NOT NULL, "
           "level TEXT NOT NULL, "
           "result INTEGER NOT NULL)")

# Add a global function to the Jinja environment for using "strptime" in template history.html
app.jinja_env.globals.update(strptime=datetime.datetime.strptime)

# Extract a list of words from the text file
with open("static/txt/words.txt") as file:
    words = [row.strip().lower() for row in file.readlines()]


@app.after_request
def after_request(response):
    """ Ensure responses aren't cached """
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route('/', methods=["GET", "POST"])
def index():
    """ Define the root route ('/') for the homepage, supporting both GET and POST methods """
    if request.method == "POST":
        # Retrieve form data
        name = request.form.get("name").strip().title()
        level = request.form.get("level")
        time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Check for input errors
        if not name:
            return error("Please type a valid a name")

        if not level:
            return error("Please choose a difficulty level")

        # Begin a session and store user data
        session["name"] = name
        session["level"] = level.title()
        session["start_time"] = time

        return redirect("/game")
    else:
        return render_template("homepage.html")


@app.route('/history')
def scoreboard():
    """ Define a route ('/history') to display the game history """
    return render_template("history.html", games=db.execute("SELECT * FROM history"))


@app.route('/game')
def game():
    """ Define a route ('/game') to start a new game """

    # Initialize game session variables
    session["secret_word"] = random.choice(words)
    session["result"] = LOSER
    session["life_points"] = 6
    session["guessed_letters"] = set()
    session["letters_typed"] = set()

    # If the player chose easy level, the game gives a letter as a clue
    if session["level"] == "Easy":
        session["hint"] = random.choice(session["secret_word"])

    # Generate a string to display with underscores for not guessed letters and actual letters for guessed letters.
    todisplay = "_ " * len(session["secret_word"])

    return render_template("game.html", session=session, todisplay=todisplay,
                           img="/static/img/hangman%d.png" % (6 - session["life_points"]))


@app.route('/submit_letter', methods=["POST"])
def submit_letter():
    """ Define a route ('/submit_letter') to handle letter submissions during the game """

    # Check if the player has remaining life points
    if session["life_points"] > 0:
        # Retrieve the submitted letter from the form and convert it to lowercase
        typed = request.form.get('letter').lower()
        # Add the typed letter to the set of all letters typed by the player
        session["letters_typed"].add(typed)

        if typed in session["secret_word"]:
            # If the typed letter is in the secret word, add it to the set of guessed letters
            session["guessed_letters"].add(typed)
        else:
            # Otherwise, decrement the player's remaining life points
            session["life_points"] -= 1

        # If the player has guessed all the letters in the secret word, set the result to WINNER and display a
        # winning message.
        if set(session["guessed_letters"]) == set(session["secret_word"]):
            session["result"] = WINNER
            return render_template("endgame.html",
                                   message=f"🏆 You won! You guessed the secret word!")

        # If the player has no remaining life points, display a losing message and reveal the secret word.
        if session["life_points"] == 0:
            return render_template("endgame.html",
                                   message=f"💔 You lost! The secret word was {session['secret_word'].upper()}")

        # Render the game template with updated game session data and the hangman image based on remaining life points
        return render_template("game.html", session=session, todisplay=update_todisplay(session),
                               img="/static/img/hangman%d.png" % (6 - session["life_points"]))

    else:
        # If the player has no remaining life points from the start, display a losing message and reveal the secret word
        return render_template("endgame.html",
                               message=f"💔 You lost! The secret word was {session['secret_word'].upper()}")


@app.route('/quit')
def quit():
    """ Define a route ('/quit') to handle quitting the game """

    # Insert the game record into the database
    db.execute("INSERT INTO history (name, start_time, secret_word, level, result) VALUES (?, ?, ?, ?, ?)",
               session["name"], session["start_time"], session["secret_word"].upper(), session["level"],
               session["result"])

    # Clear the session
    session.clear()

    return redirect('/')


# Run the Flask app if this script is executed directly
if __name__ == '__main__':
    app.run(debug=True)
    