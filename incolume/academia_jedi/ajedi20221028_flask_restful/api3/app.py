from flask import Flask, request

# ruff: noqa: A001 A002 ANN001 ANN002 ANN003 ANN201 ANN202 ANN204 ANN401 ARG001 ARG002 ASYNC101 B007 B008 B009 B011 B015 B904 B905 BLE001 C408 C419 C901 D100 D101 D102 D103 D104 D105 D107 D205 D402 D415 D419 DTZ001 DTZ003 DTZ005 DTZ007 E501 E741 EM101 EM102 ERA001 EXE005 F402 F403 F405 F601 F811 F821 F841 FBT001 FBT002 FBT003 FIX002 G001 G002 G004 N801 N802 N805 N806 N816 N999 NPY002 PD901 PERF203 PERF401 PERF402 PIE796 PLE1205 PLR0913 PLR1714 PLR2004 PLW0602 PLW0603 PLW2901 PT004 PT006 PT012 PT015 PTH118 PTH123 PYI024 PYI041 RET503 RET504 RUF001 RUF012 RUF013 S101 S113 S201 S301 S307 S310 S311 S602 S603 S605 S607 S608 SIM103 SIM109 SIM113 SIM115 SIM117 SLF001 SLOT000 T201 T203 TCH003 TD002 TD003 TD004 TRY002 TRY003 TRY300 TRY301 TRY401 W293
from flask_restful import Api, Resource
from pony import orm

__author__ = '@britodfbr'  # pragma: no cover
app = Flask(__name__)
api = Api(app)
db = orm.Database()


# Database
class Game(db.Entity):
    game_id = orm.Required(str, unique=True)
    home_team = orm.Required(str)
    away_team = orm.Required(str)
    home_score = orm.Required(int)
    away_score = orm.Required(int)


db.bind(provider='sqlite', filename='database.sqlite', create_db=True)
db.generate_mapping(create_tables=True)


# API
class GameList(Resource):
    def get(self):
        with orm.db_session:
            items = orm.select(p for p in Game)
            result = [i.to_dict() for i in items]

        return {'results': result}

    def post(self):
        new_game = request.json
        try:
            with orm.db_session:
                Game(
                    game_id=new_game['game_id'],
                    home_team=new_game['home_team'],
                    away_team=new_game['away_team'],
                    home_score=new_game['home_score'],
                    away_score=new_game['away_score'],
                )
                return {'game': new_game}
        except orm.TransactionIntegrityError as err:
            print(err)
            return {
                'error': f'game id '
                f"**{new_game.get('game_id')}** already exists",
            }


class GameDetail(Resource):
    def get(self, game_id):
        try:
            with orm.db_session:
                item = Game.get(game_id=game_id)
            return {'result': item.to_dict()}
        except AttributeError:
            return {'error': 'Game does not exists!'}


api.add_resource(GameList, '/')
api.add_resource(GameDetail, '/<string:game_id>')

if __name__ == '__main__':  # pragma: no cover
    app.run(debug=True, port=5555)
