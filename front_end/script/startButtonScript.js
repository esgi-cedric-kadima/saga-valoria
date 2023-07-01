// Récupérer le bouton "Start Play"
const startButton = document.getElementById('start-button');

// Ajouter un gestionnaire d'événement pour le clic sur le bouton
startButton.addEventListener('click', function() {
  // Masquer le bouton en modifiant sa propriété 'display'
  startButton.style.display = 'none';
});
