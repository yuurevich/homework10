import utils
from flask import Flask

app = Flask(__name__)

candidates = utils.load_candidates()

@app.route("/")
def page_index():

    result = '<pre>'
    for candidate in candidates:
        result += f"{candidate['name']} \n{candidate['position']} \n{candidate['skills']}\n\n"
    result += '<pre>'
    return result

@app.route("/profile/<id>")
def profile(id):
    candidate = candidates[int(id)-1]
    result = '<pre>'
    result += f"<img src='{candidate['picture']}'> \n{candidate['name']} \n{candidate['position']} \n{candidate['skills']}\n\n"
    result += '<pre>'
    return result

@app.route("/skills/<skill>")
def skills(skill):
    result = '<pre>'
    for candidate in candidates:
        if skill.lower() in candidate['skills'].lower().split(', '):
            result += f"{candidate['name']} \n{candidate['position']} \n{candidate['skills']}\n\n"
    result += '<pre>'
    return result

app.run()