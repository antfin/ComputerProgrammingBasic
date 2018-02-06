var express = require('express');
var path = require('path');
var tracker = require('../entities/tracker');
	

var homeInterface = (function() {			
	var router = express.Router();
	
	function _addRoute(app) {	     	
		router.get('/', function(req, res) {
			tracker.trackStart();						
				
			res.render(__dirname +'/view', {
				title: 'Exercise 5',
				layout: 'layout' 
			});				
			
			tracker.trackEnd();
		});
		app.use('/', router);
	}			
		
	return {		
		init: function(app) {
			_addRoute(app); 		
		}			
	};	
})();


module.exports = homeInterface;