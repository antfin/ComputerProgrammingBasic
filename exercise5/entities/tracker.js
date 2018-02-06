var tracker = (function() {
	var startTimeInMs = Date.now();
	var startTime;
	var numRequests = 0;
	var longestProcess = 0;
	var shortestProcess = 0;
	var avgProcess = 0;
	
	
	return {		
		trackStart: function() {
			startTime = Date.now();
		},		
		trackEnd: function() {			
			var duration = Date.now() - startTime;
			
			if (shortestProcess === 0 || duration < shortestProcess) {
				shortestProcess = duration;
			}
			if (duration > longestProcess) {
				longestProcess = duration;
			}
			avgProcess = ((avgProcess * numRequests) + duration) / (numRequests + 1); 
			
			numRequests++;
		},		
		getUptime: function() {
			return ((Date.now() - startTimeInMs) / 60000);
		},		
		getNumRequests: function() {
			return numRequests;
		},		
		getAverageProcess: function() {
			return avgProcess;
		},		
		getLongestProcess: function() {
			return longestProcess;
		},		
		getShortestProcess: function() {
			return shortestProcess;
		}		
	};	
})();


module.exports = tracker;
