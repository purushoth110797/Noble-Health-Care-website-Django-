document.addEventListener("DOMContentLoaded", function () {
    var galleryNav = document.querySelector('.gallery-nav');
    var mainNav = document.querySelector('.main-nav');
    var mainNavHeight = mainNav.offsetHeight;
  
    window.addEventListener('scroll', function () {
      var scrollTop = window.scrollY;
  
      if (scrollTop >= mainNavHeight) {
        galleryNav.style.top = mainNavHeight + 'px';
      } else {
        galleryNav.style.top = '0';
      }
    });
});
  