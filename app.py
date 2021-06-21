from flask import Flask, jsonify
from models import *
from __init__ import *
import recommendation_system

recommendation = recommendation_system.Recommendation_system()


@app.route('/get_reccomend/<personId>', methods=['POST'])
def reccomendation(personId):
    res: list = Result.query.all()
    likes: list = LikeTwitt.query.filter(LikeTwitt.person_id == personId).all()
    q = jsonify([i.serialize for i in res])
    recommendation.initialization_matrix(q.data)
    res = []
    for like in likes:
        app = recommendation.recommend(like.twit_id, 5)
        if (len(app) != 0):
            for i in app:
                res.append(Result.query.get(int(i)))
    result = list(set(res))
    return jsonify([i.serialize for i in result])


if __name__ == '__main__':
    app.run()
