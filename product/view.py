from flask import Blueprint, render_template, abort
from my_app.product.model.products import PRODUCTS
from my_app.product.model.product import Product
product = Blueprint('product',__name__)

@product.route('/')
@product.route('/home')
def index():
    return render_template('product/index.html', products=PRODUCTS)
    
@product.route('/product/<int:id>')
def show(id):
   #print(PRODUCTS.get(3))
    product = PRODUCTS.get(id)
    if not product:
        abort(404)
    return render_template('product/show.html', product=product)

@product.route('/filter/<int:id>')
def filter(id):
    product = PRODUCTS.get(id)
    return render_template('product/filter.html', product=product)

@product.app_template_filter('iva_filter')
def iva_filter(product):
    if not product:
        abort(404)
    elif product["price"] == None:
        return "Sin precio"
    else:
        return product["price"] *.20 + product["price"]