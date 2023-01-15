import openai
import flask

app = flask.Flask(__name__)

openai.api_key = "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"

@app.route("/message", methods=["POST"])
def message():
    message = flask.request.values.get("Body")
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=message,
        max_tokens=2048
    )
    reply = response["choices"][0]["text"]
    return f'<Response><Message>{reply}</Message></Response>'

if __name__ == "__main__":
    app.run(port=3000)
