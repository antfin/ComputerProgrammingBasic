$(function () {
     var model = new TaskModel();
     var view = new TaskView(model);
     var controller = new TaskController(model, view);
 });