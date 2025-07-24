from flask import Flask,jsonify,render_template,redirect,request

app=Flask(__name__)

##Initial Data in my to do list
items = [
    {"id": 1, "name": "Item 1", "description": "This is item 1"},
    {"id": 2, "name": "Item 2", "description": "This is item 2"}
]

@app.route("/")
def home():
    return "Welcome to sample To do list"


@app.route("/items")
def get_items():
    return jsonify(items)

@app.route('/items/<int:item_id>',method=['GET'])
def get_item(item_id):
    item=next((item for item in items if item["id"]==item_id),None)
    








if __name__=="__main__":
    app.run(debug=True)