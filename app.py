from flask import Flask, render_template, redirect
import scrape_mars
import pymongo

app = Flask(__name__)
conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)

db = client.mars_db
db.collection.drop()

@app.route("/")
def home():
    collection_list = db.collection.find_one()
    return render_template('index.html', collections=collection_list)


@app.route("/scrape")
def scrape():
    listings_data = scrape_mars.scrape()

    db.collection.update_one({}, {"$set":listings_data}, upsert=True)
    return redirect("/", code=302)

if __name__ == "__main__":
    app.run(debug=True)