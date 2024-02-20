

  const LivingRoomperPage = 8; // Oldalankénti képek száma (2 sor és 4 oszlop)
  let livingRoomCurrentPage = 1; // Aktuális oldal
  const livingRoomTotalPages = Math.ceil(livingRoomImages.length / LivingRoomperPage); // Összes oldal száma

  function displayLivingRoomImages(page) {
    const startIndex = (page - 1) * LivingRoomperPage;
    const endIndex = page * LivingRoomperPage;
    $('.living-room-image-box').hide(); // Minden kép elrejtése a nappali galériában

    for (let i = startIndex; i < endIndex && i < livingRoomImages.length; i++) {
      $('.living-room-image-box').eq(i).show(); // Csak az adott oldalhoz tartozó képek megjelenítése a nappali galériában
    }
  }

  function generateLivingRoomPagination() {
    const pagination = document.getElementById("living-room-pagination");
    pagination.innerHTML = ""; // Előző lapozó gombok törlése a nappali lapozónál

    for (let i = 1; i <= livingRoomTotalPages; i++) {
      const liClass = i === livingRoomCurrentPage ? "page-item active" : "page-item";
      const buttonHtml = `<li class="${liClass}"><button class="page-link" onclick="changeLivingRoomPage(${i})">${i}</button></li>`;
      pagination.innerHTML += buttonHtml;
    }
  }

  function changeLivingRoomPage(page) {
    if (page < 1 || page > livingRoomTotalPages) {
      return;
    }
    livingRoomCurrentPage = page;
    displayLivingRoomImages(livingRoomCurrentPage);
    generateLivingRoomPagination();
  }

  displayLivingRoomImages(livingRoomCurrentPage);
  generateLivingRoomPagination();



