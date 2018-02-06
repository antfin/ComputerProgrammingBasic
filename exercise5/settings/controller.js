var fs = require('fs');


var settings = (function() {		
	return {	
		init: function() {
			global.config = JSON.parse(fs.readFileSync('settings/model.json', {encoding: 'utf-8'}));				
		},	
		save: function() {			
			fs.writeFileSync('settings/model.json', JSON.stringify(global.config), {encoding: 'utf-8'});
		},	
		set: function(data) {
			global.config.files.group = data.files.group;
			global.config.files.task = data.files.task;
			global.config.files.color = data.files.color;
		},			
		get: function() {				
			return {
				group: global.config.files.group,
				task: global.config.files.task,
				color: global.config.files.color
		   	};
		}	
	};	
})();


module.exports = settings;