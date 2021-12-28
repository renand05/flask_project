import os

from flask import Flask, jsonify
from flask_restful import Api

from app.common.exceptions import AppExceptionBaseClass, ObjectNotFound
from app.customers.api_v1_0.resources import customers_v1_0_bp

from .ext import migrate


def create_app(settings_env):
    app = Flask(__name__)
    settings_module = f"config.default.{settings_env.capitalize()}Config"
    app.config.from_object(settings_module)

    from app.db import db

    db.init_app(app)
    migrate.init_app(app, db)

    Api(app, catch_all_404s=True)
    app.url_map.strict_slashes = False
    app.register_blueprint(customers_v1_0_bp)
    register_error_handlers(app)
    return app


def register_error_handlers(app):
    @app.errorhandler(Exception)
    def handle_exception_error(e):
        return jsonify({"msg": "Internal server error"}), 500

    @app.errorhandler(405)
    def handle_405_error(e):
        return jsonify({"msg": "Method not allowed"}), 405

    @app.errorhandler(403)
    def handle_403_error(e):
        return jsonify({"msg": "Forbidden error"}), 403

    @app.errorhandler(404)
    def handle_404_error(e):
        return jsonify({"msg": "Not Found error"}), 404

    @app.errorhandler(AppExceptionBaseClass)
    def handle_app_base_error(e):
        return jsonify({"msg": str(e)}), 500

    @app.errorhandler(ObjectNotFound)
    def handle_object_not_found_error(e):
        return jsonify({"msg": str(e)}), 404
