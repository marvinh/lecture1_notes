from flask import Blueprint, render_template, abort
from sqlalchemy import text
import jsonify
from db import db
from flask_json import FlaskJSON, JsonError, json_response, as_json

api_task_blueprint = Blueprint('api_task_blueprint', __name__ )

@api_task_blueprint.route("")
def index():
    statement = text(
        """
        SELECT * FROM task
        """
    )
    tasks = db.session.execute(statement,None)
    
    return json_response(tasks=tasks)