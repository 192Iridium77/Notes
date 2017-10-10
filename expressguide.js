# installation

// navigate to folder, then run:
$ npm init
// entry point is like the index of your app
// then edit the Json to include:
"dependencies":{
  "express":"*"
}
// just after the "scripts" entry.
// * indicates the latest version

# set up app.js file in the root directory:
var express = require("express");
var bodyParser = require("body-parser");
var path = require("path");

  // simplify file paths
  var app = express();

  app.listen(3000, function(){
    console.log("Server started on port 3000");

      })

// this will return "Cannot GET /"
// the / indicates root of server

# link url to homepage and make a response:
// place just before app.listen()
app.get("/", function(req, res){
  res.send("Hello Express!")
    });

# add custom middleware

var logger = function(req, res, next) {
  console.log("Logging...");
    next();

}

app.use(logger);

// note that the logger must be just after the var app declaration.

# Parsing json:
// note that putting index.html into the public folder will overwrite response messages
// NOTE: use nodemon so that you don't have to restart the server every time you make a change!!! Do a global npm install
// set up person - {...}
app.get("/", function(req, res){
  res.json(person);
    });


