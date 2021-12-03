import json, logging

from flask import Blueprint, current_app, jsonify, make_response, request

stack_route = Blueprint('stack_route', __name__)

# from blueprint import responses

# Routes
@stack_route.route('', defaults={'stack_id': None}, methods=['POST', 'GET'])
@stack_route.route('/<int:stack_id>', methods=['DELETE', 'POST', 'GET'])
def stack_route_fct(stack_id):

    response = None
    try:
        stacks = current_app.config["STACKS"]

        if stack_id == None:
            if request.method == 'POST':
                response = create_stack(stacks)

            elif request.method == 'GET':
                response = list_stacks(stacks)

        else:
            if request.method == 'DELETE':
                response = delete_stack(stacks, stack_id)

            elif request.method == 'POST':
                post_data = request.get_json()
                if not isinstance(post_data, dict):
                    post_data = json.loads(post_data)
                value = post_data.get('value') # TODO: Error if not present
                response = push_value(stacks, stack_id, value)

            elif request.method == 'GET':
                response = get_stack(stacks, stack_id)

    except Exception as ex:
        logging.error(ex)
        responseObject = {
            'status': 'fail',
            'message': 'Try again'
        }
        return make_response(jsonify(responseObject)), 500

    return response

def create_stack(stacks):

    current_app.config['STACKID'] += 1
    id = current_app.config['STACKID']
    stacks[id] = [];
    responseObject = { 'stack_id': id }
    return make_response(jsonify(responseObject)), 201

def list_stacks(stacks):

    responseObject = { 'stack_ids': list(stacks.keys()) }
    return make_response(jsonify(responseObject)), 200

def delete_stack(stacks, stack_id):

    if stack_id in stacks:
        del stacks[stack_id]
        responseObject = { 'response': 'deleted' }
        return make_response(jsonify(responseObject)), 200

    responseObject = {
        'status': 'fail',
        'message': 'Try again'
    }
    return make_response(jsonify(responseObject)), 400

def push_value(stacks, stack_id, value):

    if stack_id in stacks:
        stacks[stack_id].append(value)
        responseObject = { 'response': 'pushed' }
        return make_response(jsonify(responseObject)), 200

    responseObject = {
        'status': 'fail',
        'message': 'Try again'
    }
    return make_response(jsonify(responseObject)), 400

def get_stack(stacks, stack_id):

    if stack_id in stacks:
        responseObject = { stack_id: stacks[stack_id] }
        return make_response(jsonify(responseObject)), 200

    responseObject = {
        'status': 'fail',
        'message': 'Try again'
    }
    return make_response(jsonify(responseObject)), 400
