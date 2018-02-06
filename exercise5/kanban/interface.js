var express = require('express');
var path = require('path');
var tracker = require('../entities/tracker');
var kanban = require('./controller');
	

var kanbanInterface = (function() {			
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
		app.use('/kanban', router);
	}		
	
	function _addApi(app) {	
		router.post('/', function(req, res, next) {
			function _answerJson(err, data) {
			    if (err)
			    {
			      	console.log(err);
			  		err.status = 500;     
			     	next(err);
			    }		
			    else
			    {
				    res.json(data);
			    }
			}
			
			tracker.trackStart();						
					
			if (req.query.group == "get")
			{
				kanban.getGroup(function(err, group) {					
					_answerJson(err, group);
				});
			}				
			else if (req.query.task == "get")
			{
				kanban.getTask(function(err, task) {					
					_answerJson(err, task);
				});
			}				
			else if (req.query.task == "set")
			{
				kanban.setTask(JSON.parse(req.body.tasks), function(err, result) {					
					_answerJson(err, result);
				});
			}
			else if (req.query.color == "get")
			{
				kanban.getColor(function(err, color) {					
					_answerJson(err, color);
				});
			}
			else
			{
				var err = new Error("REST API not supported");
				
				_answerJson(err, null);
			}		
			
			tracker.trackEnd();
		});	
		
		app.use('/api/kanban', router);		
	}	
		
	function _addClientJavacript(app) {	  
		app.use(express.static(path.join(__dirname, 'client')));
	}	
		
	return {		
		init: function(app) {
			_addRoute(app); 
			_addApi(app);
			_addClientJavacript(app);			
		}			
	};	
})();


module.exports = kanbanInterface;