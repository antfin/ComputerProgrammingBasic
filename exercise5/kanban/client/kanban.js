function init() 
{ 
	var json = {};
	

	$.post("../api/kanban?group=get", {}, function(groups, status) {			
		$.post("../api/kanban?task=get", {}, function(tasks, status) {
			json.data = _calculateKanban(groups, tasks);
			$.post("../api/kanban?color=get", {}, function(colors, status) {			
				json.color = colors;				
				initKanban(json);
			}).error(function() { 
				alert("Unable to find color file"); 
			});
		}).error(function() { 
			alert("Unable to find task file"); 
		});
	}).error(function() { 
   		alert("Unable to find group file"); 
	});			
      	
	return;	
}

function _calculateKanban(groups, tasks) 
{ 
	var kanban = 
	{
		"class": "go.GraphLinksModel",
		"nodeDataArray": [],
		"linkDataArray": []
	}
	
	_addGroups(kanban, groups.data);	
	_addTasks(kanban, groups.data, tasks.data);

	return kanban;
}

function _addGroups(kanban, groups) 
{ 
	for (var index=0; index<groups.length; index++) 
	{
		group = groups[index];
		group["isGroup"] = true;
		group["loc"] = (index * 125) + " 23.52284749830794";
		kanban.nodeDataArray.push(group);		
	}

	return;
}

function _addTasks(kanban, groups, tasks) 
{ 
	for (var index=0; index<tasks.length; index++) 
	{
		task = tasks[index];
		kanban.nodeDataArray.push(task);	
	}

	return;
}

function save() 
{ 
	var kanban = JSON.parse(saveKanban());
	var tasks = {
		"data": []
	};
	
	
	for (var index=0; index<kanban.nodeDataArray.length; index++) 
	{
		task = kanban.nodeDataArray[index];
		if (task["isGroup"] != true)
		{
			delete task["loc"];
			tasks.data.push(task);
		}
	}
	
	console.log(tasks);
}

/* Example data for GO Kanban
{ 
	"class": "go.GraphLinksModel",
	"nodeDataArray": [
		{"key":"Problems", "text":"Problems", "isGroup":true, "loc":"0 23.52284749830794" },
		{"key":"Reproduced", "text":"Reproduced", "isGroup":true, "color":"0", "loc":"109 23.52284749830794" },
		{"key":"Identified", "text":"Identified", "isGroup":true, "color":"0", "loc":"235 23.52284749830794" },
		{"key":"Fixing", "text":"Fixing", "isGroup":true, "color":"0", "loc":"343 23.52284749830794" },
		{"key":"Reviewing", "text":"Reviewing", "isGroup":true, "color":"0", "loc":"451 23.52284749830794"},
		{"key":"Testing", "text":"Testing", "isGroup":true, "color":"0", "loc":"562 23.52284749830794" },
		{"key":"Customer", "text":"Customer", "isGroup":true, "color":"0", "loc":"671 23.52284749830794" },
		{"key":-1, "group":"Problems", "category":"newbutton",  "loc":"12 35.52284749830794" },
		{"key":1, "text":"text for oneA", "group":"Problems", "color":"0", "loc":"12 35.52284749830794"},
		{"key":2, "text":"text for oneB", "group":"Problems", "color":"1", "loc":"12 65.52284749830794"},
		{"key":3, "text":"text for oneC", "group":"Problems", "color":"0", "loc":"12 95.52284749830794"},
		{"key":4, "text":"text for oneD", "group":"Problems", "color":"1", "loc":"12 125.52284749830794"},
		{"key":5, "text":"text for twoA", "group":"Reproduced", "color":"1", "loc":"121 35.52284749830794"},
		{"key":6, "text":"text for twoB", "group":"Reproduced", "color":"1", "loc":"121 65.52284749830794"},
		{"key":7, "text":"text for twoC", "group":"Identified", "color":"0", "loc":"247 35.52284749830794"},
		{"key":8, "text":"text for twoD", "group":"Fixing", "color":"0", "loc":"355 35.52284749830794"},
		{"key":9, "text":"text for twoE", "group":"Reviewing", "color":"0", "loc":"463 35.52284749830794"},
		{"key":10, "text":"text for twoF", "group":"Reviewing", "color":"1", "loc":"463 65.52284749830794"},
		{"key":11, "text":"text for twoG", "group":"Testing", "color":"0", "loc":"574 35.52284749830794"},
		{"key":12, "text":"text for fourA", "group":"Customer", "color":"1", "loc":"683 35.52284749830794"},
		{"key":13, "text":"text for fourB", "group":"Customer", "color":"1", "loc":"683 65.52284749830794"},
		{"key":14, "text":"text for fourC", "group":"Customer", "color":"1", "loc":"683 95.52284749830794"},
		{"key":15, "text":"text for fourD", "group":"Customer", "color":"0", "loc":"683 125.52284749830794"},
		{"key":16, "text":"text for fiveA", "group":"Customer", "color":"0", "loc":"683 155.52284749830795"}
	],
	"linkDataArray": []
}  
*/