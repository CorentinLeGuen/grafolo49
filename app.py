from ariadne import load_schema_from_path, make_executable_schema, graphql_sync, ObjectType
from ariadne.constants import PLAYGROUND_HTML
from flask import request, jsonify

from api import app
from api.queries import list_draws_resolver

query = ObjectType("Query")
query.set_field("listDraws", list_draws_resolver)

type_defs = load_schema_from_path("schema.graphql")
schema = make_executable_schema(type_defs, query)


@app.route("/graphql", methods=["GET"])
def graphql_playground():
    return PLAYGROUND_HTML, 200


@app.route("/graphql", methods=["POST"])
def graphql_server():
    data = request.get_json()
    success, result = graphql_sync(
        schema,
        data,
        context_value=request,
        debug=app.debug
    )
    status_code = 200 if success else 400
    return jsonify(result), status_code
