curl -X POST http://127.0.0.1:8091/mapred -H "Content-Type:application/json" -d @-

<ctrl d>

Problem 1:

{"inputs":"goog",
"query":[{"map":{
"language":"javascript",
"source":"function(value,keyData,arg) {
var data = Riak.mapValuesJson(value)[0];
if(data.Low && data.Low < 450.00)
return[value.key];
else
return[];}",
"keep":true}}]}

Problem 2:

{"inputs":"goog",
"query":[{"map":{
"language":"javascript",
"source":"function(value,keyData,arg) {
var data = Riak.mapValuesJson(value)[0];
if(data.Open > data.Close)
return[value.key];
else
return[];}",
"keep":true}}]}
