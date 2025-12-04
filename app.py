from flask import Flask, render_template, request, jsonify, session
import json
import os
from currency import convert_currency

app = Flask(__name__, template_folder='templates', static_folder='static')
app.secret_key = 'your_secret_key_here'

# Get the base directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Load products
def load_products():
    products_file = os.path.join(BASE_DIR, 'products.json')
    with open(products_file, 'r', encoding='utf-8') as f:
        return json.load(f)

# Load translations
def load_translations(lang='en'):
    trans_file = os.path.join(BASE_DIR, 'translations', f'{lang}.json')
    if os.path.exists(trans_file):
        with open(trans_file, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {}

@app.route('/')
def index():
    lang = request.args.get('lang', 'en')
    products = load_products()
    translations = load_translations(lang)
    currency = request.args.get('currency', 'USD')
    
    # Convert prices if needed
    if currency != 'USD':
        for product in products:
            product['price'] = round(convert_currency(product['price'], 'USD', currency), 2)
    
    return render_template('index.html', products=products, translations=translations, lang=lang, currency=currency)

@app.route('/product/<int:product_id>')
def product(product_id):
    lang = request.args.get('lang', 'en')
    products = load_products()
    currency = request.args.get('currency', 'USD')
    translations = load_translations(lang)
    
    product = next((p for p in products if p['id'] == product_id), None)
    if product:
        if currency != 'USD':
            product['price'] = round(convert_currency(product['price'], 'USD', currency), 2)
        return render_template('product.html', product=product, translations=translations, lang=lang, currency=currency)
    return "Product not found", 404

@app.route('/cart')
def cart():
    lang = request.args.get('lang', 'en')
    translations = load_translations(lang)
    currency = request.args.get('currency', 'USD')
    return render_template('cart.html', translations=translations, lang=lang, currency=currency)

@app.route('/checkout')
def checkout():
    lang = request.args.get('lang', 'en')
    translations = load_translations(lang)
    currency = request.args.get('currency', 'USD')
    return render_template('checkout.html', translations=translations, lang=lang, currency=currency)

@app.route('/orders')
def orders():
    lang = request.args.get('lang', 'en')
    translations = load_translations(lang)
    currency = request.args.get('currency', 'USD')
    return render_template('orders.html', translations=translations, lang=lang, currency=currency)

@app.route('/api/products', methods=['GET'])
def api_products():
    products = load_products()
    currency = request.args.get('currency', 'USD')
    
    if currency != 'USD':
        for product in products:
            product['price'] = round(convert_currency(product['price'], 'USD', currency), 2)
    
    return jsonify(products)

@app.route('/api/product/<int:product_id>', methods=['GET'])
def api_product(product_id):
    products = load_products()
    currency = request.args.get('currency', 'USD')
    
    product = next((p for p in products if p['id'] == product_id), None)
    if product:
        if currency != 'USD':
            product['price'] = round(convert_currency(product['price'], 'USD', currency), 2)
        return jsonify(product)
    return jsonify({'error': 'Product not found'}), 404

if __name__ == '__main__':
    app.run(debug=True, port=5000)
