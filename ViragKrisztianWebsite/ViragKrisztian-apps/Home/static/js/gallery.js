function openModal(img, modalId) {
  const modal = document.getElementById(modalId);
  const modalImg = document.getElementById('modal-image-' + modalId);
  modal.style.display = "block";
  modalImg.src = img.src;
}

function closeModal(modalId) {
  const modal = document.getElementById(modalId);
  modal.style.display = "none";
}

let slideIndex = 1;

function changeImage(n) {
  showImage(slideIndex += n);
}

function currentImage(n) {
  showImage(slideIndex = n);
}

function showImage(n) {
  let i;
  let slides = document.getElementsByClassName("modal-content");
  if (n > slides.length) { slideIndex = 1 }
  if (n < 1) { slideIndex = slides.length }
  for (i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";
  }
  slides[slideIndex - 1].style.display = "block";
}