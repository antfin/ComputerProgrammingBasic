var proxy = (function() {
	var timeout = 60000;
	
	
	function _httpGetRequest(options, callback) 
	{ 	
		var http = require('http');
		var request = http.request(options, function(response) {
			var string = '';
	
				
			response.on('data', function (chunk) {
				string += chunk;
			});
			
			response.on('end', function () {		  		
				if (response.statusCode == 200)
		  		{
			    	callback(null, string);		  			
		  		}
		  		else
		  		{
		  			var err = new Error("HTTP Error");
		  			
		  			err.status = response.statusCode;	
			    	callback(err, null);	
		  		}
			});
			
			
			return;
		});
		
		
		request.on('socket', function (socket) {
		    socket.setTimeout(timeout);  
		    socket.on('timeout', function() {
	        	request.abort();
		      	callback("TIMEOUT", null);
		    });
		});
		
		request.on('error', function(err) {
		    if (err.code === "ECONNRESET") {
          		console.log("Timeout occurs");
		    }
		    console.log('Unable to connect');
			callback(err, null);
		});
		
		request.end();
		
		return;
	}
	
	function _httpPostRequest(options, data, callback) {
		var http = require('http');
		var request = http.request(options, function(response) {
			var string = '';
		  	
		  	response.on('data', function (chunk) {
		    	string += chunk;
			});
		
		  	response.on('end', function () {
		  		if (response.statusCode == 200)
		  		{
			    	callback(null, string);		  			
		  		}
		  		else
		  		{
		  			var err = new Error("HTTP Error");
		  			
		  			err.status = response.statusCode;	
			    	callback(err, null);	
		  		}
		  	});		  	
		});
				
				
	  	request.on('error', function(err) {
		    if (err.code === "ECONNRESET") {
          		console.log("Timeout occurs");
		    }
		    console.log('Unable to connect');
			callback(err, null);
		});
		
		request.write(JSON.stringify(data));
		request.end();
				
		return;
	}
	
	return {	
		get: function(address, callback) 
		{
			var options = {
			  host: address.ip,
			  port: address.port,
			  path: address.path
			};
			
      		console.log(options);
			_httpGetRequest(options, callback); 
						
			return;
		},			
		post: function(address, data, callback) 
		{
			var options = {
			  	host: address.ip,
		  		port: address.port,
		  		path: address.path,				
		  		method: "POST",
		  		headers: {
          			'Content-Type': 'application/json',
  	    		}
			};
			
			_httpPostRequest(options, data, callback); 
						
			return;
		}
	};	
})();


module.exports = proxy;
