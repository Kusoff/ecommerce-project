const searchInput = document.querySelector('.header-search');
const searchIcon = document.querySelector('.search-icon');
const searchIconText = document.querySelector('.fa-search')
const logoIcon = document.querySelector('.logo-icon');
const logoText = document.querySelector('.logo span');
const headerMenu = document.querySelector('.header-menu');
const searchInputMinimized = document.querySelector('.header-search-minimized');

searchIcon.addEventListener('click', function () {
    searchInput.focus;
});

// Search animation
searchInput.addEventListener('focus', function() {
    searchIcon.classList.toggle('search-icon-right');
    searchInput.style.paddingLeft = 15 + 'px';
});

searchInput.addEventListener('blur', function searchInputBlur() {
    searchIcon.classList.toggle('search-icon-right');
    searchInput.style.paddingLeft = 45 + 'px';

});

if (window.innerWidth <= 500) {
    searchInput.addEventListener('focus', function() {
        searchIcon.classList.toggle('search-icon-right');
        searchInput.style.paddingLeft = 25 + 'px';
    });

    searchInput.addEventListener('blur', function searchInputBlur() {
        searchIcon.classList.toggle('search-icon-right');
        searchInput.style.paddingLeft = 25 + 'px';
    });
}

// Fix bug with search minimized width on scroll
searchIcon.addEventListener('click', function() {
    searchInput.style.width = '230px';
    
    if (window.innerWidth <= 500) {
        searchInput.style.width = '150px';
    }
});

// Header minimized on scroll
window.onscroll = function() {myFunction()};
let header = document.getElementById("header");
let sticky = header.offsetTop;
const body = document.querySelector('body');

function myFunction() {
if (window.scrollY > sticky) {

    body.style.paddingTop = '100px';

    header.classList.add('header-minimized');
    header.classList.remove('header');

    logoText.classList.add('logo-hidden')
    
    logoIcon.classList.remove('logo-icon');
    logoIcon.classList.add('logo-icon-minimized');

    searchInput.classList.add('header-search-minimized');

    headerMenu.classList.add('header-menu-minimized');
    headerMenu.classList.remove('header-menu');

} else {

    body.style.paddingTop = '0';

    header.classList.remove("header-minimized");
    header.classList.add("header");
    
    logoText.classList.remove('logo-hidden');
    logoText.style.fontSize = '40px';
    logoText.style.transition = '.3s linear font-size';
    
    logoIcon.classList.add('logo-icon');
    logoIcon.classList.remove('logo-icon-minimized');
    
    searchInput.classList.remove('header-search-minimized')
    searchInput.classList.add('header-search')

    headerMenu.classList.add('header-menu');
    headerMenu.classList.remove('header-menu-minimized');
}
}