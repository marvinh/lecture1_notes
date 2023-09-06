from flask import Blueprint, render_template, abort
from api.task.routes import api_task_blueprint


api_blueprint = Blueprint('api_blueprint', __name__ )

api_blueprint.register_blueprint(api_task_blueprint,url_prefix="/task")