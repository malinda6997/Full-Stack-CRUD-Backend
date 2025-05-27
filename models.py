from config import db

class Contact(db.Model):
    id = db.column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    mobile_number = db.Column(db.String(15), nullable=False)
    age = db.Column(db.Integer, nullable=False) 
    
    def to_json(self):
        return {
            'id': self.id,
            'firstName': self.first_name,
            'lastName': self.last_name,
            'mobileNumber': self.mobile_number,
            'age': self.age
        }
