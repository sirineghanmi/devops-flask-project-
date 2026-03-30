from flask import Flask

# Créer l'application Flask
app = Flask(__name__)

# Définir une route
@app.route("/")
def home():
    return "Hello, Flask!"

# Lancer le serveur si on exécute directement ce fichier
if __name__ == "__main__":
    app.run(debug=True)
