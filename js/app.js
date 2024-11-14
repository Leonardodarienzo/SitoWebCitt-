// app.js

// Esempio di una funzione che mostra un messaggio di successo quando si invia il modulo
document.querySelector("form").addEventListener("submit", function(e) {
    e.preventDefault(); // Impedisce il comportamento di invio del modulo
    alert("Il tuo messaggio è stato inviato con successo!");
  });
  