from flask import render_template


def error(message, code=400):
    """Render message as an apology to user."""

    def escape(s):
        """
        Escape special characters.

        https://github.com/jacebrowning/memegen#special-characters
        """
        for old, new in [("-", "--"), (" ", "-"), ("_", "__"), ("?", "~q"),
                         ("%", "~p"), ("#", "~h"), ("/", "~s"), ("\"", "''")]:
            s = s.replace(old, new)
        return s

    return render_template("error.html", top=code, bottom=escape(message)), code


def update_todisplay(session):
    """ Update the displayed string to reveal guessed letters and show underscores for not guessed letters
    in the secret word """
    todisplay = ""
    for letter in session["secret_word"]:
        if letter in session["guessed_letters"]:
            todisplay += letter
        else:
            todisplay += "_ "

    return todisplay
