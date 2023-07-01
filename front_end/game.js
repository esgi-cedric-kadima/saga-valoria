// Création d'une instance de WebSocket et spécification de l'URL du serveur WebSocket
const websocket = new WebSocket("ws://localhost:8001/");

// Gestionnaire d'événement pour l'ouverture de la connexion WebSocket
websocket.addEventListener('open', function (event) {
    // La connexion WebSocket est ouverte avec succès
    console.log('WebSocket connection established.');

    // Envoyer un message au serveur
    const message = "start";
    websocket.send(message);
});

// Gestionnaire d'événement pour la réception de messages du serveur
websocket.addEventListener('message', function (event) {
    // Récupérer le message reçu du serveur
    const message = event.data;

    // Afficher le message reçu dans la console
    console.log('Received from server:', message);
});

// Gestionnaire d'événement pour la fermeture de la connexion WebSocket
websocket.addEventListener('close', function (event) {
    // La connexion WebSocket est fermée
    console.log('WebSocket connection closed.');
});

// Gestionnaire d'événement pour les erreurs de la connexion WebSocket
websocket.addEventListener('error', function (event) {
    // Une erreur s'est produite lors de la connexion WebSocket
    console.error('WebSocket error:', event);
});
