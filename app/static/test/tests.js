// documentation on writing tests here: http://docs.jquery.com/QUnit
// example tests: https://github.com/jquery/qunit/blob/master/test/same.js

module("example tests");
test("True",function(){
  expect(1);
  equals(true, true, "true is true");
  
})

test("Environment",function(){
  expect(2);
  ok( !!window.log, "log function present");
  ok( !!window.Modernizr, "Modernizr present");
})



