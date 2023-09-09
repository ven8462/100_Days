const spanElements = document.querySelectorAll('.animated-text span');
spanElements.forEach((span, index) => {
  span.style.setProperty('--index', index);
});