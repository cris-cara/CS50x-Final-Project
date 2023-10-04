# Hangman

### Video Demo: https://youtu.be/nwLfoyH0RkA

### Intro

Welcome to the popular and classic game of **Hangman**. Are you ready to start this adventure where words hang in the
balance, and your vocabulary is your only weapon?

As you surely already know, the goal is to guess the secret word before the hangman dies. Be extremely careful, every
letter counts!

## Table of Contents

- [Description](#description)
- [Dependencies](#dependencies)
- [How to Play](#how-to-play)
- [Folder and files](#folder-and-files)

## Description

Hangman is crafted as a **Web Application** powered by the Python **Flask** framework, in addition to **HTML**, **CSS**
and **JavaScript**

In this delightful challenge, you'll encounter a virtual keyboard where you can carefully pick the letters you want to
test in order to unravel the enigmatic word. You have a maximum of 6 attempts to decipher the secret word.

Moreover, you have the choice between two levels of difficulty:

- **Easy**: you'll receive a helpful **hint** in the form of one letter.
- **Hard**: no hints here; it's just you against the word itself.

## Dependencies

- `datetime`
- `random`
- `cs50`
- `Flask`
- `Flask-Session`

The required modules which not comes with Python itself can be installed using the
following command:

```shell
pip install cs50 Flask Flask-Session
```

## How to play

To play the game, follow these steps:

1. **Run** the script
2. **Open** your browser and go to _**127.0.0.1:5000/**_
3. **Type** your **name** and **choose** the **difficulty level**
4. Press **Play!**

## Folder and files

### /static

* This folder is used to store static files, such as **CSS** style sheets, images, **JavaScript** and a text file
  containing a dictionary of English words

### /templates

* This folder is used to store **HTML** template files that define the structure and content of web pages dynamically
  generated by the application

### app.py

* This file is a **Python** script that implements the Hangman game using the Flask web framework. It includes the
  following features:

    - Creation of a Flask web application
    - Configuration of session management for user data
    - Integration with a SQLite database for storing game history
    - Definition of routes for the game's homepage, game history, and gameplay
    - Initialization of game variables like the secret word, life points, guessed letters, and more
    - Handling of user input for guessing letters and displaying game outcomes
    - Displaying game images based on the player's progress
    - Recording and displaying game history, including player names, start times, secret words, difficulty levels, and
      results

### helpers.py

* This file contains auxiliary functions useful to the script app.py

### hangman.db

* Main database containing the history of matches

### requirements.txt

* This file reports the command lines that must be run from the terminal in order to install, via **pip**, the modules
  necessary for Hangman to work.