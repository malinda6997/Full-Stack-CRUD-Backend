from flask import request, jsonify
from config import app, db
from models import Contact


@app.route('/contacts', methods=['GET'])
def get_contacts():
    contactcts = Contact.query.all()
    json_contacts = list(map(lambda contact: contact.to_json(), contactcts))
    return jsonify({"contacts":json_contacts}), 200



if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        
    app.run(debug=True)