from flask import Flask, jsonify, render_template, request, redirect, url_for
import json

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('home.html')

def run_products():
    with open('products.json','r',encoding='utf-8') as f:
        products = json.load(f)
    return products

@app.route('/api/products',methods=['GET'])
def products_page():
    products = run_products()
    return jsonify(products)

@app.route('/api/filterby/')
def choose_filter():
    return render_template('filterby.html')

@app.route('/api/filterby/categoria/<categoria>',methods=['GET'])
def products_category(categoria):
    products = run_products()
    products_found = {}
    for product in products:
        if product['categoria'].lower() == categoria.lower():
            products_found[product['id']] = product
    return jsonify(products_found)


@app.route('/api/filterby/categoria')
def choose_category_product():
    return render_template('choosecategory.html')

@app.route('/api/filterby/marca')
def choose_brand_product():
    return render_template('choosebrand.html')
           

@app.route('/api/productname',methods=['GET'])
def products_name():
    products = run_products()
    products_found = {}
    q = request.args.get("searchname").lower() if request.args.get("searchname") != '' else ''
    if q == '':
        return redirect(url_for('main'))
    
    for product in products:
        if q in product['nome'].lower() :
            products_found[product['id']] = product
        else:
            pass
    return jsonify(products_found)


@app.route('/api/filterby/marca/<marca>',methods=['GET'])
def products_brand(marca):
    products = run_products()
    products_found = {}
    for product in products:
        if product['marca'].lower() == marca.lower():
            products_found[product['id']] = product
    return jsonify(products_found)


if __name__ == '__main__':
    app.run(debug=True)
