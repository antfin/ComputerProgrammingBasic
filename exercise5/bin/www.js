#!/usr/bin/env node
var app = require('../app');
var debug = require('debug')('ComputerProgrammingBasic:server');
var http = require('http');


/**
 * Get port from environment and store in Express.
 */
var port = _normalizePort(process.env.npm_package_config_port);
app.set('port', port);

/**
 * Create HTTP server. 
 */
var server = http.createServer(app);

/**
 * Boot the WebApp
 */
server.listen(port);
server.on('error', _handleError);
server.on('listening', _handleListening);


/**
 * Local functions
 */
function _normalizePort(val) {
  var port = parseInt(val, 10);

  if (isNaN(port)) {
    // named pipe
    return val;
  }

  if (port >= 0) {
    // port number
    return port;
  }

  return false;
}

function _handleError(error) {
  if (error.syscall !== 'listen') {
    throw error;
  }

  var bind = typeof port === 'string'
    ? 'Pipe ' + port
    : 'Port ' + port;

  // handle specific listen errors with friendly messages
  switch (error.code) {
    case 'EACCES':
      console.error(bind + ' requires elevated privileges');
      process.exit(1);
      break;
    case 'EADDRINUSE':
      console.error(bind + ' is already in use');
      process.exit(1);
      break;
    default:
      throw error;
  }
}

function _handleListening() {
  var addr = server.address();
  var bind = typeof addr === 'string'
    ? 'pipe ' + addr
    : 'port ' + addr.port;
  debug('Listening on ' + bind);
}
