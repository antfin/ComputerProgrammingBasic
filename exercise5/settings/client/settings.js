function configureSubmit() 
{ 
	$("#saveButton").click(function() {
		console.log("Click Saving Button");
		_postSettings();
	});
		
	return;
}

function _postSettings() 
{	
	$.post("../api/settings?save=all", _readSettings(), function() {
		console.log("Setings Post completed");
	}, function () {
    	console.log("Post error");
	});

	return;	
}

function _readSettings() 
{			
	var data = {	
		"mongodb": {
			"host": $('#mongoHost').val(),
			"port": $('#mongoPort').val()
		}
	};
	
	return {settings: JSON.stringify(data)};
}
