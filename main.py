from flask import Flask, request, render_template

def get_tacos_dict(ID):
    if ID in [ID]:
        options = "frites grandes : + 0.5"
        return {"img":"website/tacos", "description":"bonjours ! this is a desc !", 
                "name":"tacos horrible", "options":[option.split(":") for option in options],
                "price":5.50}    
    else:
        return False

app = Flask(__name__)

@app.route("/")
def main_website():
    return render_template("website/index.html")

@app.route("/search/<id>")
def custom_tacos(id):
    dict_tacos = get_tacos_dict(id)
    if dict_tacos:
        return render_template("website/model_page_web.html", product=dict_tacos)
    else:
        return 404.1, "tacos not found"
    
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
