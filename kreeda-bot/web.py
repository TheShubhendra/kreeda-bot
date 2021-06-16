from flask import Flask, session, request, render_template
from telegram import bot
from uuid import uuid4
from decouple import config

TOKEN = config("TOKEN")
bot = bot.Bot(TOKEN)

app = Flask(__name__, template_folder="2d-run")
app.config["SECRET_KEY"] = config("SECRET_KEY")


@app.route("/")
def game():
    user_id = request.args.get("u")
    message_id = request.args.get("i")
    session["user_id"] = user_id
    session["message_id"] = message_id
    print(user_id, message_id)
    return render_template("index.html")


@app.route("/api/setScore", methods=["POST"])
def setScore():
    user_id = session["user_id"]
    message_id = session["message_id"]
    score = request.form
    print(user_id, message_id)
    print(int(score["score"]))
    return bot.set_game_score(user_id, score, inline_message_id=message_id, force=True)


@app.route("/api/getHighScore", methods=["POST"])
def getHighScore():
    user_id = session["user_id"]
    message_id = session["message_id"]
    try:
        high_score = bot.get_game_high_scores(user_id, inline_message_id=message_id)
    except:
        high_score = 0
    return high_score


if __name__ == "__main__":
    app.run(debug=True)
