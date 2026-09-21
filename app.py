from flask import Flask, request
from model import Tripulante

app = Flask(__name__)


@app.route("/tripulantes", methods=["GET"])
def get_tripulantes():
    todos_tripulantes = Tripulante.banco_tripulantes

    return {
        "tripulantes": [
            {
                "id": tripulante.id,
                "nome": tripulante.nome,
                "cargo": tripulante.cargo,
                "nivel_acesso": tripulante.get_nivel_acesso()
            }
            for tripulante in todos_tripulantes
        ]
    }, 200

@app.route("/tripulantes", methods=["POST"])
def criar_tripulante():
    data = request.get_json()

    nome = data["nome"]
    cargo = data["cargo"]
    nivel_acesso = data["nivel_acesso"]

    tripulante = Tripulante(nome, cargo, nivel_acesso)
    tripulante.salvar()

    return {
        "id": tripulante.id,
        "nome": tripulante.nome,
        "cargo": tripulante.cargo,
        "nivel_acesso": tripulante.get_nivel_acesso()
    }, 201

@app.route("/tripulantes/<int:id_tripulante>", methods=["GET"])
def get_tripulante_id(id_tripulante):
    lista_tripulantes = Tripulante.banco_tripulantes

    for tripulante in lista_tripulantes:
        if tripulante.id == id_tripulante:
            return {
                "id": tripulante.id,
                "nome": tripulante.nome,
                "cargo": tripulante.cargo,
                "nivel_acesso": tripulante.get_nivel_acesso()
            }, 200

@app.route("/tripulantes/<int:id_tripulante>", methods=["DELETE"])
def remover_tripulante(id_tripulante):
    lista_tripulantes = Tripulante.banco_tripulantes

    for tripulante in lista_tripulantes:
        if tripulante.id == id_tripulante:
            Tripulante.remover(id_tripulante)
            return {}, 200


if __name__ == "__main__":
    app.run(debug=True)