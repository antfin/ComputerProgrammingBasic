/* Web App factory

based on code of https://www.awwwards.com/build-a-simple-javascript-app-the-mvc-way.html
*/
$(function () {
     var model = new TaskModel();
     var view = new TaskView(model);
     var controller = new TaskController(model, view);
 });