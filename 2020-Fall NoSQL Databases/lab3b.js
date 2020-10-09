
distinctDigits = function(phone){
    var number = phone.components.number + '',
    seen = [],
    result = [],
    i = number.length;
    while(i--) {
        seen[+number[i]] = 1;
    }
    for (i=0; i<10; i++) {
        if (seen[i]) {
            result[result.length] = i;
        }
    }
    return result;
}
        
db.system.js.save({_id: 'distinctDigits', value: distinctDigits})
        
map = function() {
    var digits = distinctDigits(this);
    emit({
        digits : digits, 
        country : this.components.country}, 
        {count : 1});
}
        
reduce = function(key, values) {
    var total = 0;
    for(var i=0; i<values.length; i++) {
        total += values[i].count;
    }
    return { count : total };
}

/**
*  Implement a finalize method that outputs the count as a total.
*  *Hint* To do this, you need to create and add a finalize function
*  that renames the attribute count to total.
*  Then add the finalize attribute to your mapreduce command.
*  You can check your results db.phones.report.find()
**/ 
    
//Ex:
// { "_id" : { "digits" : [ 0, 1, 2, 3, 4, 5, 6 ], "country" : 8 }, "value" : { "count" : 13 } }
// to
// { "_id" : { "digits" : [ 0, 1, 2, 3, 4, 5, 6 ], "country" : 8 }, "value" : { "total" : 13 } }
finalize = function(key, value){
    value["total"] = value["count"];
    delete value["count"];
    return value;
}

results = db.runCommand({
    mapReduce: 'phones',
    map: map,
    reduce: reduce,
    finalize: finalize,
    out: 'phones.report'
})
        