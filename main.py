from flask import request, jsonify
from config import app, db
from models import Contact


@app.route('/contacts', methods=['GET'])
def get_contacts():
    contactcts = Contact.query.all()
    json_contacts = list(map(lambda contact: contact.to_json(), contactcts))
    return jsonify({"contacts":json_contacts}), 200

@app.route('/contacts', methods=['POST'])
def create_contact():
    first_name = request.json.get('firstName')
    last_name = request.json.get('lastName')
    mobile_number = request.json.get('mobileNumber')
    age = request.json.get('age')
    
    if not first_name or not last_name or not mobile_number or not age:
        return (
            jsonify({"message": "All fields are required"}), 400
            )
    new_contact = Contact(
        first_name=first_name,
        last_name=last_name,
        mobile_number=mobile_number,
        age=age
    )
    try:
        db.session.add(new_contact)
        db.session.commit()
        return jsonify({"message": "Contact created successfully"}), 201
    except Exception as e:
        return (
            jsonify({"message": "An error occurred while creating the contact", "error": str(e)}), 400
        )
    
@app.route('/contacts/<int:id>', methods=['UPDATE'])
def update_contact(id):
    contact = Contact.query.get(id)
    
    if not contact:
        return jsonify({"message": "Contact not found"}), 404
    
    data = request.json
    contact.first_name = data.get('firstName', contact.first_name)
    contact.last_name = data.get('lastName', contact.last_name)
    contact.mobile_number = data.get('mobileNumber', contact.mobile_number)
    contact.age = data.get('age', contact.age)
    try:
        db.session.commit()
        return jsonify({"message": "Contact updated successfully"}), 200
    except Exception as e:
        return (
            jsonify({"message": "An error occurred while updating the contact", "error": str(e)}), 400
        )



if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        
    app.run(debug=True)