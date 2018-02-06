var express = require('express');
var path = require('path');
var tracker = require('../entities/tracker');
var settings = require('./controller');


var settings_interface = (function() {	
	var router = express.Router();
		
	function _addRoute(app) {	     	
		router.get('/', function(req, res) {
			tracker.trackStart();	
				
			res.locals = settings.get();
			
		  	res.render(__dirname +'/view', {
		    	title: 'Settings',
		    	layout: 'layout' 
		  	});	
		  	
			tracker.trackEnd();
		});
		app.use('/settings', router);
	}	
	
	function _addApi(app) {	
		router.post('/', function(req, res, next) {
			tracker.trackStart();	
					
			if (req.query.save == "all")
			{
				settings.set(JSON.parse(req.body.settings));
				settings.save();
				res.send("Config Update Completed");
			}
			else
			{
				var err = new Error("REST API not supported");
				
		  		err.status = 500;     
		     	next(err);
			}			
			
			tracker.trackEnd();
		});	
		
		app.use('/api/settings', router);		
	}		
		
	function _addClientJavacript(app) {	  
		app.use(express.static(path.join(__dirname, 'client')));
	}			
	
	return {		
		init: function(app) {
			settings.init();
			_addRoute(app); 
			_addApi(app); 
			_addClientJavacript(app);
		}			
	};	
})();


module.exports = settings_interface;