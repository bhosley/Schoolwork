#!/usr/bin/env bash

#Add your curl statements here

# Create db names resturaunts:
curl -i -X PUT "http://couchdb:5984/restaurants/"

# Add 3 documents to db with a specific format:
curl -i -X POST "http://couchdb:5984/restaurants/" -H "Content-Type: application/json" -d '{"_id":"brauhaus_am_markt","name":"Brauhaus Am Markt","food_type":["European","German"],"phone_number":"+49 631 61944","website":"brauhausammarkt-kl.de"}'
curl -i -X POST "http://couchdb:5984/restaurants/" -H "Content-Type: application/json" -d '{"_id":"thai_mint","name":"Thai Mint","food_type":["Asian","Thai","Fusion"],"phone_number":"+1 719-598-7843","website":"http://www.thai-mint.com/"}'
curl -i -X POST "http://couchdb:5984/restaurants/" -H "Content-Type: application/json" -d '{"_id":"sicilys_pizza_st_martin","name":"Sicily`s Pizza St. Martin","food_type":["Italian","Buffet"],"phone_number":"+1 228-392-1991","website":"https://www.sicilysmorevariety.com/stmartin"}'

#DO NOT REMOVE
curl -Ssf -X PUT http://couchdb:5984/restaurants/_design/docs -H "Content-Type: application/json" -d '{"views": {"all": {"map": "function(doc) {emit(doc._id, {rev:doc._rev, name:doc.name, food_type:doc.food_type, phonenumber:doc.phonenumber, website:doc.website})}"}}}'
curl -Ssf -X GET http://couchdb:5984/restaurants/_design/docs/_view/all
