var express = require('express');
var tracker = require('../entities/tracker');
var statistics = require('./controller');


var statistics_interface = (function() {	
	var router = express.Router();
		
	function _addRoute(app) {	     	
		router.get('/', function(req, res) {
			tracker.trackStart();	
				
			res.locals = statistics.get();
			
		  	res.render(__dirname +'/view', {
		    	title: 'Statistics',
		    	layout: 'layout' 
		  	});
		  	
			tracker.trackEnd();
		});
		app.use('/statistics', router);
	}		
	
	return {		
		init: function(app) {
			_addRoute(app); 
		}			
	};	
})();

module.exports = statistics_interface;
