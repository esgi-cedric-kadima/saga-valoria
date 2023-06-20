const websocket = new WebSocket("ws://localhost:8001/");

websocket.addEventListener('open', function (event) {
    console.log('WebSocket connection established.');
    websocket.send(JSON.stringify('HELLO'));

});

websocket.addEventListener('message', function (event) {
    console.log('Received message from server:', event.data);
});

websocket.addEventListener('close', function (event) {
    console.log('WebSocket connection closed.');
});

websocket.addEventListener('error', function (event) {
    console.error('WebSocket error:', event);
});