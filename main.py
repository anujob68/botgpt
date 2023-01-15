import openai
import flask

app = flask.Flask(__name__)

openai.api_key = os.getenv("OPENAI_API_KEY")

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
