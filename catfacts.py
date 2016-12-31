from flask import Flask, render_template
from random import randint

app = Flask(__name__)

@app.route("/")
def index():
    facts = [
        "A female cat is also known to be called a 'queen' or a 'molly'",
        "Cats are unable to detect sweetness in anything they taste.",
        "A cat can reach up to five times its own height per jump.",
        "Cats have the cognitive ability to sense a human's feelings and overall mood.",
        "Each side of a cat's face has about 12 whiskers.",
        "A cat's field of vision does not cover the area right under its nose.",
        "Cats show affection and mark their territory by rubbing on people. Glands on their face, tail and paws release a scent to make its mark.",
        "Talk about Facetime: Cats greet one another by rubbing their noses together.",
        "Cats came to the Americas from Europe as pest controllers in the 1750s."
    ]
    randNumber = randint(0, len(facts) - 1)
    catfact = facts[randNumber]

    return render_template("index.html", catfact=catfact)

if __name__ == "__main__":
    app.run()