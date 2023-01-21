from flask import Flask, request
from flask_restful import Api, Resource
from pony import orm

__author__ = "@britodfbr"  # pragma: no cover
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


db.bind(provider="sqlite", filename="database.sqlite", create_db=True)
db.generate_mapping(create_tables=True)


# API
class GameList(Resource):
    def get(self):
        with orm.db_session:
            items = orm.select(p for p in Game)
            result = [i.to_dict() for i in items]

        return {"results": result}

    def post(self):
        new_game = request.json
        try:
            with orm.db_session:
                Game(
                    game_id=new_game["game_id"],
                    home_team=new_game["home_team"],
                    away_team=new_game["away_team"],
                    home_score=new_game["home_score"],
                    away_score=new_game["away_score"],
                )
                return {"game": new_game}
        except orm.TransactionIntegrityError as err:
            print(err)
            return {
                "error": f"game id " f"**{new_game.get('game_id')}** already exists"
            }


class GameDetail(Resource):
    def get(self, game_id):
        try:
            with orm.db_session:
                item = Game.get(game_id=game_id)
            return {"result": item.to_dict()}
        except AttributeError:
            return {"error": "Game does not exists!"}


api.add_resource(GameList, "/")
api.add_resource(GameDetail, "/<string:game_id>")

if __name__ == "__main__":  # pragma: no cover
    app.run(debug=True, port=5555)
