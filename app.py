from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
shopping_cart = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add', methods=['POST'])
def add_item():
    item = request.form.get('item')
    if item:  # 确保输入不为空
        shopping_cart.append(item)
    return redirect(url_for('index'))

@app.route('/cart')
def show_cart():
    return render_template('cart.html', cart=shopping_cart)

@app.route('/remove', methods=['POST'])
def remove_item():
    item_to_remove = request.form.get('item')
    if item_to_remove in shopping_cart:
        shopping_cart.remove(item_to_remove)
    return redirect(url_for('show_cart'))

if __name__ == '__main__':

    app.run(debug=True)
