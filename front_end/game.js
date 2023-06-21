const websocket = new WebSocket("ws://localhost:8001/");

websocket.addEventListener('open', function(event) {
    console.log('WebSocket connection established.');

    // Envoyer un message au serveur
    const message = "Hello from client!";
    websocket.send(message);
});

websocket.addEventListener('message', function(event) {
    const message = event.data;
    console.log('Received from server:', message);
});

websocket.addEventListener('close', function(event) {
    console.log('WebSocket connection closed.');
});

websocket.addEventListener('error', function(event) {
    console.error('WebSocket error:', event);
});

