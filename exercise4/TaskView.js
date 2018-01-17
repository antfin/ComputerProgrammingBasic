var TaskView = function (model) {
    this.model = model;
    this.addTaskEvent = new Event(this);
    this.selectTaskEvent = new Event(this);
    this.unselectTaskEvent = new Event(this);
    this.completeTaskEvent = new Event(this);
    this.deleteTaskEvent = new Event(this);
    this.init();
};

TaskView.prototype = {
    init: function () {
        this._createChildren()
            ._setupHandlers()
            ._enable();
    },

    addTaskButton: function () {
        this.addTaskEvent.notify({
            task: this.$taskTextBox.val()
        });
    },

    completeTaskButton: function () {
        this.completeTaskEvent.notify();
    },

    deleteTaskButton: function () {
        this.deleteTaskEvent.notify();
    },

    selectOrUnselectTask: function () {
        var taskIndex = $(event.target).attr("data-index");

        if ($(event.target).attr('data-task-selected') == 'false') {
            $(event.target).attr('data-task-selected', true);
            this.selectTaskEvent.notify({
                taskIndex: taskIndex
            });
        } else {
            $(event.target).attr('data-task-selected', false);
            this.unselectTaskEvent.notify({
                taskIndex: taskIndex
            });
        }
    },

    buildList: function () {
        var $tasksContainer = this.$tasksContainer;
        var tasks = this.model.getTasks();
        var html = "";
        var index = 0;
		
        $tasksContainer.html('');
        for (var task in tasks) {
			html = "<div style='color:" + tasks[task].taskColor + ";font-size:" + tasks[task].taskSize+ ";'>";
            $tasksContainer.append(html + "<label><input type='checkbox' class='js-task' data-index='" + index + "' data-task-selected='false'>" + tasks[task].taskName + "</label></div>");
            index++;
        }
    }, 
	

    _createChildren: function () {
        // Cache the document object
        this.$container = $('#AppContainer');
        this.$addTaskButton = this.$container.find('#AddButton');
        this.$taskTextBox = this.$container.find('#TaskName');
        this.$tasksContainer = this.$container.find('#TaskList');
        return this;
    },

    _setupHandlers: function () {
        this.addTaskButtonHandler = this.addTaskButton.bind(this);
        this.selectOrUnselectTaskHandler = this.selectOrUnselectTask.bind(this);
        this.completeTaskButtonHandler = this.completeTaskButton.bind(this);
        this.deleteTaskButtonHandler = this.deleteTaskButton.bind(this);
        // Handlers from Event Dispatcher        
        this.addTaskHandler = this._addTaskEvent.bind(this);
        this.clearTaskTextBoxHandler = this._clearTaskTextBoxEvent.bind(this);
        this.setTasksAsCompletedHandler = this._setTasksAsCompletedEvent.bind(this);
        this.deleteTasksHandler = this._deleteTasksEvent.bind(this);
        return this;
    },

    _enable: function () {
        this.$addTaskButton.click(this.addTaskButtonHandler);
        this.$container.on('click', '.js-task', this.selectOrUnselectTaskHandler);
        this.$container.on('click', '#CompleteButton', this.completeTaskButtonHandler);
        this.$container.on('click', '#DeleteButton', this.deleteTaskButtonHandler);
        // Event Dispatcher
        this.model.addTaskEvent.attach(this.addTaskHandler);
        this.model.addTaskEvent.attach(this.clearTaskTextBoxHandler);
        this.model.setTasksAsCompletedEvent.attach(this.setTasksAsCompletedHandler);
        this.model.deleteTasksEvent.attach(this.deleteTasksHandler);
        return this;
    },
	
    _clearTaskTextBoxEvent: function () {
        this.$taskTextBox.val('');
    },

    _addTaskEvent: function () {
        this._show();
    },

    _setTasksAsCompletedEvent: function () {
        this._show();
    },

    _deleteTasksEvent: function () {
        this._show();
    },

    _show: function () {
        this.buildList();
    }
};
