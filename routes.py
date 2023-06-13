from flask import Flask,render_template
import sqlite3
app = Flask(__name__)

@app.route("/home")
def home():
    return render_template("home.html",title="Home")
    
@app.route("/contacts")
def contacts():
    return render_template("contacts.html",title="Contacts")

@app.route("/about")
def about():
    return render_template("about.html",title="About")

@app.route('/all_cars')
def all_cars():
    return render_template("all_cars",title="all_cars")

@app.route('/all_pizzas')
def all_pizzas():
    conn = sqlite3.connect('car.db')
    cur = conn.cursor()
    cur.execute('SELECT * FROM car')
    results = cur.fetchall()

    return render_template("all_pizzas.html",results=results)

@app.route('/pizza/<int:id>')
def pizza(id):
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()
    cur.execute('SELECT * FROM Pizza WHERE id=?',(id,))
    pizza = cur.fetchone()
    cur.execute('SELECT name FROM Base WHERE id=?',(id,))
    base = cur.fetchone()
    cur.execute('SELECT name FROM Topping WHERE id In (SELECT tid From PizzaTopping WHERE pid=?)',(id,))
    Topping = cur.fetchall()
    
    return render_template("pizza.html",pizza=pizza, base=base,Topping=Topping)


if __name__ == '__main__':
    app.run(debug = True)