var winston = require('winston');
var expressWinston = require('express-winston');


var logger = expressWinston.logger({
  	transports: [
    	new winston.transports.Console({
    		json: false,
      		colorize: true
    	})
  	],
  	meta: false, // optional: control whether you want to log the meta data about the request (default to true) 
  	msg: "HTTP {{req.method}} {{req.url}}", // optional: customize the default logging message. E.g. "{{res.statusCode}} {{req.method}} {{res.responseTime}}ms {{req.url}}" 
  	expressFormat: true, // Use the default Express/morgan request formatting, with the same colors. Enabling this will override any msg and colorStatus if true. Will only output colors on transports with colorize set to true 
  	colorStatus: true, // Color the status code, using the Express/morgan color palette (default green, 3XX cyan, 4XX yellow, 5XX red). Will not be recognized if expressFormat is true 
  	ignoreRoute: function (req, res) { return false; } // optional: allows to skip some log messages based on request and/or response 
});


module.exports = logger;