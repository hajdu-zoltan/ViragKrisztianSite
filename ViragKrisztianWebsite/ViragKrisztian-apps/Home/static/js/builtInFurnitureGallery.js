
  const builtInFurnitureperPage = 8; // Oldalankénti képek száma (2 sor és 4 oszlop)
  let builtInFurnitureCurrentPage = 1; // Aktuális oldal
  const builtInFurnitureTotalPages = Math.ceil(builtInFurnitureImages.length / builtInFurnitureperPage); // Összes oldal száma

  function displayBuiltInFurnitureImages(page) {
    const startIndex = (page - 1) * builtInFurnitureperPage;
    const endIndex = page * builtInFurnitureperPage;
    $('.built-in-furniture-image-box').hide(); // Minden kép elrejtése a beépített bútorok galériában

    for (let i = startIndex; i < endIndex && i < builtInFurnitureImages.length; i++) {
      $('.built-in-furniture-image-box').eq(i).show(); // Csak az adott oldalhoz tartozó képek megjelenítése a beépített bútorok galériában
    }
  }

  function generateBuiltInFurniturePagination() {
    const pagination = document.getElementById("built-in-furniture-pagination");
    pagination.innerHTML = ""; // Előző lapozó gombok törlése a beépített bútorok lapozónál

    for (let i = 1; i <= builtInFurnitureTotalPages; i++) {
      const liClass = i === builtInFurnitureCurrentPage ? "page-item active" : "page-item";
      const buttonHtml = `<li class="${liClass}"><button class="page-link" onclick="changeBuiltInFurniturePage(${i})">${i}</button></li>`;
      pagination.innerHTML += buttonHtml;
    }
  }

  function changeBuiltInFurniturePage(page) {
    if (page < 1 || page > builtInFurnitureTotalPages) {
      return;
    }
    builtInFurnitureCurrentPage = page;
    displayBuiltInFurnitureImages(builtInFurnitureCurrentPage);
    generateBuiltInFurniturePagination();
  }

  displayBuiltInFurnitureImages(builtInFurnitureCurrentPage);
  generateBuiltInFurniturePagination();





