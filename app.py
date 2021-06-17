import json

from flask import Flask, jsonify
from models import *
from __init__ import *
import recommendation_system
recommendation = recommendation_system.Recommendation_system()
from AlchemyEncoder import *
@app.route('/')
def reccomendation():
    res:Result = Result.query.all()
    result = '['
    for i in res:
        result+=(i.json)+','

    result+=']'
    # q = json.dumps(result)
    # recommendation.initialization_matrix(result)
    return result


if __name__ == '__main__':
    app.run()
