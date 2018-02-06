var fs = require('fs');


var kanban = (function() {	
	return {						
		getGroup: function(callback) {
			try
			{
				var group = JSON.parse(fs.readFileSync("settings/" + global.config.files.group, {encoding: 'utf-8'}));
				
				
				callback(null, group);				
			}
			catch (err) 
			{
				callback(err, null);
			}
		},							
		getTask: function(callback) {
			try
			{
				var task = JSON.parse(fs.readFileSync("settings/" + global.config.files.task, {encoding: 'utf-8'}));
				
				
				callback(null, task);				
			}
			catch (err) 
			{
				callback(err, null);
			}
		},							
		setTask: function(tasks, callback) {
			try
			{				
				fs.writeFileSync("settings/" + global.config.files.task, JSON.stringify(tasks), {encoding: 'utf-8'});
				
				callback(null, {"result": "Success"});				
			}
			catch (err) 
			{
				callback(err, null);
			}
		},						
		getColor: function(callback) {
			try
			{
				var color = JSON.parse(fs.readFileSync("settings/" + global.config.files.color, {encoding: 'utf-8'}));
				
				
				callback(null, color);				
			}
			catch (err) 
			{
				callback(err, null);
			}
		}
	};	
})();


module.exports = kanban;