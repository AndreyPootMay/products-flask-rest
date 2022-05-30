from flask import Flask, jsonify, request

app = Flask(__name__)

from products import products

@app.route('/ping')
def ping():
    return jsonify({"message": "pong"});

@app.route('/products', methods=['GET'])
def getProducts():
    return jsonify(products)

@app.route('/products/<int:id>')
def getProduct(id):
    productModel = [product for product in products if product['id'] == id]
    if (len(productModel) > 0):
        return jsonify(productModel[0])
    return jsonify({"message": "Product not found."})

@app.route('/products', methods=['POST'])
def addProduct():
    newProduct = {
        "id": len(products) + 1,
        "name": request.json['name'],
        "price": request.json['price'],
        "quantity": request.json['quantity']
    }

    products.append(newProduct)

    return jsonify({"message": "Product added successfully", "products": products})

@app.route('/products/<int:id>', methods=['PUT'])
def updateProduct(id):
    productModel = [product for product in products if product['id'] == id]
    if (len(productModel) > 0):
        productModel[0]['name'] = request.json['name']
        productModel[0]['price'] = request.json['price']
        productModel[0]['quantity'] = request.json['quantity']

        return jsonify({
            "message": "Product updated",
            "product": productModel[0]
        })

    return jsonify({"message": "Product not found."})

@app.route('/products/<int:id>', methods=['DELETE'])
def deleteProduct(id):
    productModel = [product for product in products if product['id'] == id]
    if (len(productModel) > 0):
        products.remove(productModel[0])
        return jsonify({
            "message": "Product deleted",
            "products": products
        })

    return jsonify({"message": "Product not found."})

if __name__ == '__main__':
    app.run(debug=True, port=4000)