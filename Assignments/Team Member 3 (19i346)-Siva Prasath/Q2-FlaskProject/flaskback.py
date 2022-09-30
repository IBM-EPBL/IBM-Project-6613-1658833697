import flask 
from flask import request, jsonify
app = flask.Flask(__name__) 
app.config["DEBUG"] = False


products_dict = [
{ 'obid': 1, 'productname': 'kitkat', 'price': "10" }, 
{ 'obid': 2, 'productname': 'Dairymilk', 'price': "80" }
                ]

@app.route('/products', methods=['GET'])
def get_AllProducts():
    return jsonify(products_dict)
def get_product_by_obid():
    if 'obid' in request.args:
        obid = int(request.args['obid'])
    else:
        return "Error,No id field provided"
    for product in products_dict: 
        if product['obid'] == obid:
            return jsonify(product) 
    return {}

@app.route("/products/<obid>", methods=['GET'])
def get_product_by_pathobid(obid): 
    for product in products_dict: 
        if product['obid'] == int(obid):
            return jsonify (product) 
    return {"Error":"Product with given id not found"}

@app.route('/deleteproduct/<obid>', methods=['DELETE'])
def delete_product(obid): 
    for product in products_dict:
        if product['obid'] == int(obid):
            products_dict.remove(product)
            return{"msg":"product deleted sucessfully"}
    return {"Error":"Product with given id not found"}

@app.route('/addproduct', methods=['POST'])
def post_product():
    product = request.get_json() 
    product['obid'] = len(products_dict) + 1 
    products_dict.append(product) 
    return jsonify(product)

@app.route('/updateproduct', methods=['PUT']) 
def put_product():
    product = request.get_json() 
    for i, p in enumerate(products_dict): 
        if p['obid'] == product['obid']:
            products_dict[i] = product
            return {"msg":"Sucess"}
    return {"Error":"Product not found"}



if __name__=="__main__":
    app.run()
