// mappa.js
var map = L.map('map').setView([41.1256, 14.7835], 13); // Coordinate di Benevento

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
  attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);

// Aggiungi un marker per un punto di interesse
L.marker([41.1256, 14.7835]).addTo(map)
  .bindPopup('<b>Benevento</b><br>Città storica.')
  .openPopup();
