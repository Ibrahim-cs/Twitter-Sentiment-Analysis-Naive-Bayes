const express = require('express');
const path = require('path');
const EventEmitter = require('events');
const fetch = require('node-fetch');
const MW = require('./middleware');

const app = express();
const Stream = new EventEmitter(); // my event emitter instance

app.use(MW.enableCors)
app.use(express.static(path.join(__dirname, 'static')))
app.use(express.static(path.join(__dirname, 'templates')))

app.get('/?', async (req, res, next) => {
    return res.sendFile(path.join(__dirname + '/index.html'));
});

app.get('/stream', function (request, response) {
    response.writeHead(200, {
        'Content-Type': 'text/event-stream',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive'
    });

    Stream.on("push", function (event, data) {
        response.write("event: " + String(event) + "\n" + "data: " + JSON.stringify(data) + "\n\n");
    });
});

setInterval(function () {
    fetch('http://localhost:8000/sayHello')
        .then(res => res.json())
        .then(data => {
            Stream.emit("push", "message", data);
        })
        .catch(err => console.error(err));
}, 2000)

app.listen(3001, () => console.log('Server started. Press Ctrl+C to quit'));