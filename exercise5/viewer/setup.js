var fs = require('fs');
var hbs = require('hbs');


var viewer = (function() {
	function _initViewRender(app, dirname) {	     	
		app.set('view engine', 'hbs');
		app.set('views', [dirname, dirname + '/viewer/layout']);
	}
			
	function _initViewPartials(dirname) {	     	
		hbs.registerPartial('styles', fs.readFileSync(dirname + '/viewer/partials/styles.hbs', 'utf8'));
		hbs.registerPartial('scripts', fs.readFileSync(dirname + '/viewer/partials/scripts.hbs', 'utf8'));
		hbs.registerPartial('topbar', fs.readFileSync(dirname + '/viewer/partials/topbar.hbs', 'utf8'));
		hbs.registerPartial('bottombar', fs.readFileSync(dirname + '/viewer/partials/bottombar.hbs', 'utf8'));
	}		
	
	return {		
		init: function(app, dirname) {	
			_initViewRender(app, dirname);
			_initViewPartials(dirname);
		}
	};	
})();


module.exports = viewer;