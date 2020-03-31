import json
from flask import Blueprint, abort
from flask_restful import Resource, reqparse
from my_app.esports.models import Esports
from my_app import api, db

esports = Blueprint('esports', __name__)

parser = reqparse.RequestParser()
parser.add_argument('nome', type=str)
parser.add_argument('nick', type=str)
parser.add_argument('time', type=str)
parser.add_argument('posicao', type=str)
parser.add_argument('abatimentos', type=int)
parser.add_argument('assists', type=int)
parser.add_argument('mortes', type=int)
parser.add_argument('partidas', type=int)
parser.add_argument('vitorias', type=int)

@esports.route("/")
@esports.route("/home")

def home():
    return "Catalogo de Jogadores de E-Sports"

class EsportsAPI(Resource):
    def get(self, id=None, page=1):
        if not id:
            esports = Esports.query.paginate(page, 10).items
        else:
            esports = [Esports.query.get(id)]
        if not esports:
            abort(404)
        res = {}
        for jogador in esports:
            res[jogador.id] = {
                'nome': jogador.nome,
                'nick': jogador.nick,
                'time': jogador.time,
                'posicao': jogador.posicao,
                'abatimentos': str(jogador.abatimentos),
                'assists': str(jogador.assists),
                'mortes': str(jogador.mortes),
                'partidas': str(jogador.partidas),
                'vitorias': str(jogador.vitorias),
                'propKDA': str(jogador.propKDA),
                'porcentVitorias': str(jogador.porcentVitorias)
            }

        return json.dumps(res)

    def post(self):
        args = parser.parse_args()
        nome = args['nome']
        nick = args['nick']
        time = args['time']
        posicao = args['posicao']
        abatimentos = args['abatimentos']
        assists = args['assists']
        mortes = args['mortes']
        partidas = args['partidas']
        vitorias = args['vitorias']

        jogador = Esports(nome, nick, time, posicao, abatimentos, assists, mortes, partidas, vitorias)
        db.session.add(jogador)
        db.session.commit()
        res = {}
        res[jogador.id] = {
            'nome': jogador.nome,
            'nick': jogador.nick,
            'time': jogador.time,
            'posicao': jogador.posicao,
            'abatimentos': str(jogador.abatimentos),
            'assists': str(jogador.assists),
            'mortes': str(jogador.mortes),
            'partidas': str(jogador.partidas),
            'vitorias': str(jogador.vitorias),
            'propKDA': str(jogador.propKDA),
            'porcentVitorias': str(jogador.porcentVitorias)
        }

        return json.dumps(res)

    def delete(self, id):
        con = Esports.query.get(id)
        db.session.delete(con)
        db.session.commit()
        res = {'id':id}
        return json.dumps(res)

    def put(self, id):
        jogador = Esports.query.get(id)
        args = parser.parse_args()

        nome = args['nome']
        nick = args['nick']
        time = args['time']
        posicao = args['posicao']
        abatimentos = args['abatimentos']
        assists = args['assists']
        mortes = args['mortes']
        partidas = args['partidas']
        vitorias = args['vitorias']

        jogador.nome = nome
        jogador.nick = nick
        jogador.time = time
        jogador.posicao = posicao
        jogador.abatimentos = abatimentos
        jogador.assists = assists
        jogador.mortes = mortes
        jogador.partidas = partidas
        jogador.vitorias = vitorias
        jogador.calcularProporcao()

        db.session.commit()
        res = {}
        res[jogador.id] = {
            'nome': jogador.nome,
            'nick': jogador.nick,
            'time': jogador.time,
            'posicao': jogador.posicao,
            'abatimentos': str(jogador.abatimentos),
            'assists': str(jogador.assists),
            'mortes': str(jogador.mortes),
            'partidas': str(jogador.partidas),
            'vitorias': str(jogador.vitorias),
            'propKDA': str(jogador.propKDA),
            'porcentVitorias': str(jogador.porcentVitorias)
        }

        return json.dumps(res)

api.add_resource(
    EsportsAPI, '/api/jogador','/api/jogador/<int:id>','/api/jogador/<int:id>/<int:page>'
)