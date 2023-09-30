from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager, jwt_required, create_access_token
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ecommerce.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'super-secret-key'
jwt = JWTManager(app)
db = SQLAlchemy(app)

# Define User and Product models (you can expand these models as needed)
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    barcode = db.Column(db.String(20))
    brand = db.Column(db.String(50))
    description = db.Column(db.String(200))
    price = db.Column(db.Float)
    available = db.Column(db.Boolean)

# Registration API
@app.route('/api/register', methods=['POST'])
def register():
    data = request.json
    user = User(
        first_name=data['first_name'],
        last_name=data['last_name'],
        email=data['email'],
        password=data['password']
    )
    db.session.add(user)
    db.session.commit()
    return jsonify({"message": "User registered successfully"})

# Login API
@app.route('/api/login', methods=['POST'])
def login():
    data = request.json
    user = User.query.filter_by(email=data['email']).first()
    if user and user.password == data['password']:
        access_token = create_access_token(identity=user.id)
        return jsonify({"access_token": access_token})
    return jsonify({"message": "Invalid credentials"}), 401

# Product Upload API (Admin)
@app.route('/api/admin/upload-products', methods=['POST'])
@jwt_required()
def upload_products():
    if request.files:
        # Process and save the CSV file containing product data
        # You can use a library like pandas for CSV processing
        # Ensure proper authentication and validation for admin users
        return jsonify({"message": "CSV file uploaded successfully"})
    return jsonify({"message": "No CSV file uploaded"}), 400

# Product Review API
@app.route('/api/products/<int:product_id>/reviews', methods=['POST'])
@jwt_required()
def add_product_review(product_id):
    data = request.json
    # Validate and process the review data
    # You can link reviews to specific products using the product_id
    return jsonify({"message": "Review added successfully"})

# Product View Pagination API
@app.route('/api/products', methods=['GET'])
def get_products():
    page = int(request.args.get('page', 1))
    per_page = 10  # Adjust as needed
    # Fetch and paginate products from the database
    # Implement sorting based on review or other criteria
    products = Product.query.paginate(page, per_page, False).items
    product_list = [{"name": p.name, "barcode": p.barcode, "brand": p.brand, "description": p.description,
                     "price": p.price, "available": p.available} for p in products]
    return jsonify(product_list)

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)






