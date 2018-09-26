from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

#create a dictionary to order variables
orders = [
	{
		'order_name': 'Ugali',
		'order_id': [
			{
				'Id_no': 'Hv001',
				'price': '245'
			}
		]
	},
	{
		'order_name': 'Ugali',
		'order_id': [
			{
				'Id_no': 'Hv001',
				'price': '245'
			}
		]
	}

]

@app.route('/')
def home():
	return render_template('index.html')



# POST - used to recieve data
# GET - used to send data back only

# POST/order data: {order_name} .....(to request data)
@app.route('/order', methods=['POST'])
def create_order():
	request_data = request.get_json()
	new_order = {
		'order_name': request_data['order_name']
		
		
	}
	orders.append(new_order)
	return jsonify(new_order)



# GET/order/<string:order_name>...........(to retrieve a order)
@app.route('/order/<string:order_name>') #'http://127.0.0.1:5000/order/some_order_name'
def get_order(order_name):
	# iterate over order
	for order in orders:
	# if the stor order_name matches, return it
		if order['order_name'] == order_name:
			return jsonify(order)
	# if no match, return an error message
	return jsonify({'message': 'order not found'})

# GET/order..... (to get date)
@app.route('/order')
def get_orders():
	return jsonify({'orders':orders})

# POST/order/<string:order_name>/order_id{order_name:, order_id}
@app.route('/order/<string:name>/order_id', methods=['POST'])
def create_order_idin_order(order_name):
	request_data = request.get_json()
	for order in orders:
		if order['order_name'] == order_name:
			new_order = {
					'order_name': request_data['order_name']
					
			}
			order['order_id'].append(new_order_id)
			return jsonify(new_order_id)
	return jsonify({'message': 'order not found'})

# GET/order/<string:order_name>/order_id
@app.route('/order/<string:order_name>/order_id')
def get_order_id_in_order(order_name):
	for order in orders:
		if order['order_name'] == order_name:
			return jsonify({'order_ids': order['order_ids']})

	return jsonify({'message': 'order not found'})

app.run()