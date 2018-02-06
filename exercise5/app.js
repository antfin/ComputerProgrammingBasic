var express = require('express');
var bodyParser = require('body-parser');
var path = require('path');
var logger = require('./entities/logger');
var viewer = require('./viewer/setup');
var home = require('./home/interface');
var kanban = require('./kanban/interface');
var settings = require('./settings/interface');
var statistics = require('./statistics/interface');


/**
 * Configure Web App
 */
var app = express();

app.use(logger);
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({extended: false}));
viewer.init(app, __dirname);

/**
 * Add Widgets
 */
home.init(app);
kanban.init(app);
settings.init(app);
statistics.init(app);

/**
 * Add Statics
 */
app.use(express.static(path.join(__dirname, 'public')));
app.use(express.static(path.join(__dirname, 'public/plugins')));

/**
 * Add Error Handling
 */
// catch 404 and forward to error handler
app.use(function(req, res, next) {
	var err = new Error('Not Found');
	err.status = 404;
	next(err);
});

// production error handler
// no stacktraces leaked to user
app.use(function(err, req, res, next) {
	res.status(err.status || 500);
	res.send(err.message);
});


module.exports = app;
