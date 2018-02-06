var tracker = require('../entities/tracker');

			
var statistics = (function() {	
	return {	
		get: function() {				
			return {
				uptime: tracker.getUptime().toFixed(2),
				numRequests: tracker.getNumRequests(),
				avgProcess: tracker.getAverageProcess().toFixed(2),
				shortestProcess: tracker.getShortestProcess().toFixed(2),
				longestProcess: tracker.getLongestProcess().toFixed(2)
		   	};
		}	
	};	
})();


module.exports = statistics;