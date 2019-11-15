from flask import Flask, render_template, request
from twilio.rest import Client

app = Flask(__name__)


@app.route("/", methods=["get", "post"])
def main():

    if request.method == "POST":
        text = request.form["write"]
        text1 = request.form["to"]
        print(text, text1)
        if text != "":
            account_sid = "AC5254d1a390a9a02dac0cfa0efd4e53c3"
            auth_token = "e845d1569a1d37a61c8908cfd945f0ab"
            client = Client(account_sid, auth_token)

            client.messages.create(body=text, from_="+12565679867", to=text1)
            print(client)
    else:
        text = ""
        text1 = ""
    return render_template("index.html", text=text, to=text1)


if __name__ == "__main__":
    app.run(port=8000)
    # app.run(debug=True, port=8000)
