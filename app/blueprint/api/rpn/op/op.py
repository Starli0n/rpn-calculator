import logging

from flask import Blueprint, current_app, jsonify, make_response, request

op_route = Blueprint('op_route', __name__)

# from blueprint import responses

# Routes
@op_route.route('', defaults={'op': None, 'stack_id': None}, methods=['GET'])
@op_route.route('/<op>/stack/<int:stack_id>', methods=['POST'])
def op_route_fct(op, stack_id):

    response = None
    try:
        if request.method == 'GET':
            response = list_operand()

        elif request.method == 'POST':
            response = apply_operand_to_stack(op, stack_id)

    except Exception as ex:
        logging.error(ex)
        responseObject = {
            'status': 'fail',
            'message': 'Try again'
        }
        return make_response(jsonify(responseObject)), 500

    return response

def list_operand():

    return jsonify(operand=current_app.config["OPERAND"])

def apply_operand_to_stack(op, stack_id):

    ops = current_app.config["OPERAND"]
    if op in ops:
        stacks = current_app.config["STACKS"]
        if stack_id in stacks:
            stack = stacks[stack_id]
            if len(stack) > 2:
                v2 = stack.pop()
                v1 = stack.pop()
                if op == '+':
                    v1 += v2
                elif op == '-':
                    v1 -= v2
                elif op == '*':
                    v1 *= v2
                elif op == '/':
                    v1 /= v2
                stack.append(v1)
                responseObject = { 'response': 'ok' }
                return make_response(jsonify(responseObject)), 200

    responseObject = {
        'status': 'fail',
        'message': 'Try again'
    }
    return make_response(jsonify(responseObject)), 400
