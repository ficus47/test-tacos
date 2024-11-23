from flask import Flask, request, render_template

def get_tacos_dict(ID):
    if ID in [ID]:
        options = ["frites grandes : + 0.5"]
        return {"img":"website/tacos", "description":"bonjours ! this is a desc !", 
                "name":"tacos horrible", "options":[option.split(":") for option in options],
                "price":5.50, "link":"/search/"+"tacos_horrible"}    
    else:
        return False
    
def get_tacos_list():
    options = ["frites grandes : + 0.5"]
    return { "menus":
                [
                {"img":"website/tacos", "description":"bonjours ! this is a desc !", 
                "name":"tacos horrible", "options":[option.split(":") for option in options],
                "price":5.50, "link":"/search/"+"tacos_horrible"}
                ],
             "description":"""Fort de plusieurs années d’expérience dans la vente de tacos, le vendeur a su développer une expertise culinaire et commerciale qui lui permet de proposer des produits de qualité, alliant saveurs authentiques et service rapide. Son parcours dans divers établissements de restauration rapide et de street food lui a permis de perfectionner son savoir-faire, en maîtrisant la préparation des tacos avec une variété de garnitures fraîches, de sauces maison et de recettes créatives.

                                Au-delà de la technique culinaire, ce vendeur incarne des valeurs d’hospitalité, de respect et d’engagement envers ses clients. Chaque client est accueilli chaleureusement, et le vendeur s'assure que chaque commande soit préparée avec soin et attention, dans le respect des standards d’hygiène et de qualité. Il met un point d’honneur à offrir un service rapide tout en maintenant une ambiance conviviale et agréable.

                                Passionné par son métier, le vendeur de tacos accorde une importance particulière à la qualité des ingrédients utilisés. Il privilégie les produits frais et locaux, dans un souci constant d'amélioration de l'expérience gustative. L'authenticité, la satisfaction du client et l'esprit d'équipe sont les piliers qui guident son approche professionnelle. Il s’efforce de transmettre à ses collègues cet amour du travail bien fait et cette volonté de satisfaire chaque client, du plus fidèle au plus occasionnel.

                                En somme, ce vendeur de tacos est un passionné, un professionnel engagé, et un ambassadeur de la cuisine rapide mais soignée, toujours à l’écoute des attentes des clients et prêt à offrir une expérience culinaire de qualité."""

            }    

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
        return 404, "404.T error : tacos not found"
    
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
