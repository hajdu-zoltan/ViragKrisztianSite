const kitchenperPage = 8; // Oldalankénti képek száma (2 sor és 4 oszlop)
let kitchenCurrentPage = 1; // Aktuális oldal
const kitchenTotalPages = Math.ceil(kitchenImages.length / kitchenperPage); // Összes oldal száma

console.log(kitchenTotalPages)

function displayKitchenImages(page) {
const startIndex = (page - 1) * kitchenperPage;
const endIndex = page * kitchenperPage;
$('.kitchen-image-box').hide(); // Minden kép elrejtése a konyha galériában

for (let i = startIndex; i < endIndex && i < kitchenImages.length; i++) {
  $('.kitchen-image-box').eq(i).show(); // Csak az adott oldalhoz tartozó képek megjelenítése a konyha galériában
}
}

function generateKitchenPagination() {
const pagination = document.getElementById("kitchen-pagination");
pagination.innerHTML = ""; // Előző lapozó gombok törlése a konyha lapozónál

for (let i = 1; i <= kitchenTotalPages; i++) {
  const liClass = i === kitchenCurrentPage ? "page-item active" : "page-item";
  const buttonHtml = `<li class="${liClass}"><button class="page-link" onclick="changeKitchenPage(${i})">${i}</button></li>`;
  pagination.innerHTML += buttonHtml;
}
}

function changeKitchenPage(page) {
if (page < 1 || page > kitchenTotalPages) {
  return;
}
kitchenCurrentPage = page;
displayKitchenImages(kitchenCurrentPage);
generateKitchenPagination();
}

displayKitchenImages(kitchenCurrentPage);
generateKitchenPagination();

// Függvény a konyha galériához tartozó modális ablak megnyitásához és a kiválasztott kép megjelenítéséhez
function openModalKitchen(clickedImg) {
  // Az aktuális kép URL-je
  var imgSrc = clickedImg.src;
  // Az index megkeresése az aktuális kép URL-jének alapján a kitchenImages tömbben
  var index = kitchenImages.indexOf(imgSrc);

  // A modális ablak megnyitása
  var modal = document.getElementById("myModalKitchen");
  modal.style.display = "block";

  // A megnyitott kép megjelenítése a modális ablakban
  var modalImg = document.getElementById("modal-image-kitchen");
  modalImg.src = imgSrc;

  // Az előző és következő gombok eseménykezelőjének beállítása
  var prevBtn = document.getElementsByClassName("prev")[0];
  var nextBtn = document.getElementsByClassName("next")[0];

  // Előző gomb eseménykezelője
  prevBtn.onclick = function() {
    index--;
    if (index < 0) {
      index = kitchenImages.length - 1;
    }
    modalImg.src = kitchenImages[index];
  }

  // Következő gomb eseménykezelője
  nextBtn.onclick = function() {
    index++;
    if (index >= kitchenImages.length) {
      index = 0;
    }
    modalImg.src = kitchenImages[index];
  }
}

// Függvény a konyha galériához tartozó modális ablak bezárásához
function closeModal(modalId) {
  var modal = document.getElementById(modalId);
  modal.style.display = "none";
}

// Függvény a képek közötti navigáláshoz a konyha galériához tartozó modális ablakban
function changeImage(direction) {
  var modalImg = document.getElementById("modal-image-kitchen");
  var currentImgSrc = modalImg.src;
  var index = kitchenImages.indexOf(currentImgSrc);

  // Az új kép indexének kiszámítása a navigációs irány alapján
  index += direction;

  // Ha az index túl nagy, vagy túl kicsi, akkor ciklikusan kell kezelni
  if (index >= kitchenImages.length) {
    index = 0;
  } else if (index < 0) {
    index = kitchenImages.length - 1;
  }

  // Az új kép megjelenítése
  modalImg.src = kitchenImages[index];
}
