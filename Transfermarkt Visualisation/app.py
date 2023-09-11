from flask import Flask, render_template, send_file, request, redirect
#from flask_cors import CORS
import folium
import map_transferts as mt


app = Flask(__name__)
#CORS(app)




#.HTML
@app.route('/', methods=['GET', 'POST'])
def index():
    mt.init_map()
    return render_template('Home.html')

@app.route('/Home.html', methods=['GET', 'POST'])
def render_home():
    mt.init_map()
    return render_template('Home.html')

@app.route('/map', methods=['GET', 'POST'])
def render_test():
    requestedClub = request.args.get('Clubs')
    mt.init_map_club(requestedClub)
    return render_template('home.html')

@app.route('/transferts')
def render_the_map():
    return render_template('Transferts.html')

@app.route('/Joueurs.html')
def render_players():
    return render_template('Joueurs.html')

@app.route('/Clubs.html')
def render_clubs():
    return render_template('Clubs.html')

@app.route('/Mercato.html')
def render_mercato():
    return render_template('Mercato.html')

@app.route('/Contact.html')
def render_contact():
    return render_template('Contact.html')

@app.route('/Championnats.html')
def render_champs():
    return render_template('Championnats.html')

@app.route('/API.html')
def render_API():
    return render_template('API.html')


#.CSS
@app.route('/styles.css')
def render_css():
    return send_file('templates/styles.css')

#.JSon
@app.route('/Championnats')
def render_json():
    return send_file('Championnats.json')

#JS
@app.route('/script.js')
def render_script():
    return send_file('templates/script.js')

@app.route('/gestion_joueurs.js')
def render_gestion_joueurs():
    return send_file('templates/gestion_joueurs.js')

@app.route('/client_joueurs.js')
def render_client_joueurs():
    return send_file('templates/client_joueurs.js')

@app.route('/open_popup.js')
def render_open_popup():
    return send_file('templates/open_popup.js')

@app.route('/gestion_championnats.js')
def render_gestion_championnats():
    return send_file('templates/gestion_championnats.js')

@app.route('/client_championnats.js')
def render_client_championnats():
    return send_file('templates/client_championnats.js')

@app.route('/gestion_clubs.js')
def render_gestion_clubs():
    return send_file('templates/gestion_clubs.js')

@app.route('/client_clubs.js')
def render_client_clubs():
    return send_file('templates/client_clubs.js')

@app.route('/gestion_transferts.js')
def render_gestion_transferts():
    return send_file('templates/gestion_transferts.js')

@app.route('/client_transferts.js')
def render_client_transferts():
    return send_file('templates/client_transferts.js')

@app.route('/gestion_map.js')
def render_gestion_map():
    return send_file('templates/gestion_map.js')


if __name__ == '__main__':
    app.run(debug=True)
