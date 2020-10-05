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
