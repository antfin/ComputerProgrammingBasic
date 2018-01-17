var TaskModel = function () {
     this.tasks = [];
     this.selectedTasks = [];
     this.addTaskEvent = new Event(this);
     this.removeTaskEvent = new Event(this);
     this.setTasksAsCompletedEvent = new Event(this);
     this.deleteTasksEvent = new Event(this);
 };

 TaskModel.prototype = {
     addTask: function (taskName) {
		 var task = this.validateTask(taskName);
		 if (task != undefined)
		 {
			 this.tasks.push(task);			 			 
		 }
		 else
		 {
			 alert("No Valid Task Name")
		 }
         this.addTaskEvent.notify();
     },
	 
     getTasks: function () {
         return this.tasks;
     },

     setSelectedTask: function (taskIndex) {
         this.selectedTasks.push(taskIndex);
     },

     unselectTask: function (taskIndex) {
         this.selectedTasks.splice(taskIndex, 1);
     },

     setTasksAsCompleted: function () {
         var selectedTasks = this.selectedTasks;
		 
         for (var index in selectedTasks) {
             this.tasks[selectedTasks[index]].taskStatus = 'completed';
			 this.tasks[selectedTasks[index]].taskColor = "green";
			 this.tasks[selectedTasks[index]].taskSize = "110%";
         }
         this.setTasksAsCompletedEvent.notify();
         this.selectedTasks = [];
     },

     deleteTasks: function () {
         var selectedTasks = this.selectedTasks.sort();

         for (var i = selectedTasks.length - 1; i >= 0; i--) {
             this.tasks.splice(this.selectedTasks[i], 1);
         }
         // clear the selected tasks
         this.selectedTasks = [];
         this.deleteTasksEvent.notify();
     },

     validateTask: function (taskName) {
         var task = {
			taskName: taskName,
			taskStatus: 'uncompleted'
		 };
		         
		 if (taskName != "")
		 {
			 task.taskColor = "black";
			 task.taskSize = "100%";
		 }
		 else
		 {
			 task = undefined;
		 }
		 
		 return task;
     }
 };