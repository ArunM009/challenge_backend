from flask import Blueprint, jsonify, request 
import json
import os

transaction_blueprint = Blueprint('transactions', __name__)
transactions  = []
def read_transactions():
    with open('transactions.json','r') as file:
        return json.load(file)
def write_transactions(transactions):
    with open('transactions.json', 'w')as file:
        json.dump(transactions,file, indent=4)


@transaction_blueprint.route('/transaction/<id>', methods=['GET'])
def get_transaction(id):
    with open('transactions.json') as data_file:
        transactions_data = json.load(data_file)
    transaction = transactions_data.get(id, None)
    return jsonify(transaction)

@transaction_blueprint.route('/transaction', methods=['POST'])
def add_transaction():
    #TODO
    data = request.json
    transations =read_transactions()
    transations.append(data)
    write_transactions(transactions)
    return jsonify(data), 201

@transaction_blueprint.route('/transaction/<id>', methods=['PUT'])
def update_transaction(id):
    #TODO
    data = request.json
    transations =read_transactions()
    transaction_blueprint[id] = data
    write_transactions(transactions)
    return jsonify(data)

@transaction_blueprint.route('/transaction/<id>', methods=['DELETE'])
def delete_transaction(id):
    #TODO
    transations =read_transactions()
    del transaction_blueprint[id]
    write_transactions(transactions)
    return '', 204


# TODO : ADD A GET ALL TRANSACTIONS ENDPOINT ASWELL
if __name__ == '__main__':
    app.run(debug=True)