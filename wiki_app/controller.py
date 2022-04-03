from wiki_app import app
from wiki_app import LOG
from flask import jsonify, request
from wiki_app import continent_services as CS1
from wiki_app import country_services as CS2
from wiki_app import city_services as CS3

@app.route('/', methods=['GET'],endpoint='home')
def get_continents():
    return jsonify({
        'status_code': 200,
        'message':'All good'
    })

@app.route('/wiki/continents', methods=['GET'],endpoint='get_continents')
def get_continents():
    continents_list = CS1.get_all_continents()
    if continents_list:
        return jsonify(
            message='OK',
            continents_list= continents_list
        ), 200
    else:
        return jsonify(
            message='Not Found',
            continents_list=continents_list
        ), 500

@app.route('/wiki/add/continent', methods=['POST'],endpoint='add_continent')
def add_continent():
    content = request.get_json()
    rec = CS1.add_continent(content)
    if rec:
        return jsonify(
            message= 'continent added successfully'
        ), 200
    else:
        return jsonify(
            message= 'Insert Failed'
        ), 500

@app.route('/wiki/update/continent/<int:id>', methods=['PUT'],endpoint='update_continent')
def updated_continent(id):
    content = request.get_json()
    rec = CS1.update_continent(id,content)
    if rec:
        return jsonify(
            message= 'continent updated successfully'
        ), 200
    else:
        return jsonify(
            message= 'Update Failed'
        ), 500

@app.route('/wiki/del/continent/<int:id>', methods=['DELETE'],endpoint='delete_continent')
def delete_continent(id):
    rec = CS1.delete_continent(id)
    if rec:
        return jsonify(
            message= 'continent Deleted successfully'
        ), 200
    else:
        return jsonify(
            message= 'Delete Failed'
        ), 500

# ----------------------------------------------------------------------------------------
@app.route('/wiki/countries', methods=['GET'],endpoint='get_countries')
def get_countries():
    countries_list = CS2.get_all_countries()
    if countries_list:
        return jsonify(
            message='OK',
            countries_list= countries_list
        ), 200
    else:
        return jsonify(
            message='Not Found',
            continents_list=countries_list
        ), 500

@app.route('/wiki/add/country', methods=['POST'],endpoint='add_country')
def add_country():
    content = request.get_json()
    rec = CS2.add_country(content)
    if rec:
        return jsonify(
            message= 'country added successfully'
        ), 200
    else:
        return jsonify(
            message= 'Insert Failed'
        ), 500

@app.route('/wiki/update/country/<int:id>', methods=['PUT'],endpoint='update_country')
def updated_country(id):
    content = request.get_json()
    rec = CS2.update_country(id,content)
    if rec:
        return jsonify(
            message= 'country updated successfully'
        ), 200
    else:
        return jsonify(
            message= 'Update Failed'
        ), 500

@app.route('/wiki/del/country/<int:id>', methods=['DELETE'],endpoint='delete_country')
def delete_country(id):
    rec = CS2.delete_country(id)
    if rec:
        return jsonify(
            message= 'country Deleted successfully'
        ), 200
    else:
        return jsonify(
            message= 'Delete Failed'
        ), 500

# ----------------------------------------------------------------------------------------
@app.route('/wiki/cities', methods=['GET'],endpoint='get_cities')
def get_cities():
    city_list = CS3.get_all_cities()
    if city_list:
        return jsonify(
            message='OK',
            city_list= city_list
        ), 200
    else:
        return jsonify(
            message='Not Found',
            continents_list=city_list
        ), 500

@app.route('/wiki/add/city', methods=['POST'],endpoint='add_city')
def add_city():
    content = request.get_json()
    rec = CS3.add_city(content)
    if rec:
        return jsonify(
            message= 'city added successfully'
        ), 200
    else:
        return jsonify(
            message= 'Insert Failed'
        ), 500

@app.route('/wiki/update/city/<int:id>', methods=['PUT'],endpoint='update_city')
def updated_city(id):
    content = request.get_json()
    rec = CS3.update_city(id,content)
    if rec:
        return jsonify(
            message= 'country updated successfully'
        ), 200
    else:
        return jsonify(
            message= 'Update Failed'
        ), 500

@app.route('/wiki/del/city/<int:id>', methods=['DELETE'],endpoint='delete_city')
def delete_city(id):
    rec = CS3.delete_city(id)
    if rec:
        return jsonify(
            message= 'city Deleted successfully'
        ), 200
    else:
        return jsonify(
            message= 'Delete Failed'
        ), 500