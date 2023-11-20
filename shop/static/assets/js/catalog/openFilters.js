// Open filters
const openFilterIcon = document.querySelector('.filters-icon__container');
const filtersContainer = document.querySelector('.filters-container');
const main = document.querySelector('main');
openFilterIcon.addEventListener('click', () => {
    filtersContainer.style.right = '0';
    main.style.padding = '40px 307px 40px 100px';
});

// Close filters
const closeFilterIcon = document.querySelector('.fa-times');
closeFilterIcon.addEventListener('click', () => {
    filtersContainer.style.right = '-307px';
    main.style.padding = '40px 100px';
})


// Open filters item container
const categorieTitle = document.querySelectorAll('.filters__item-title');
const categorieTitleIcon = document.querySelectorAll('.fa-chevron-right');
const categorieContainer = document.querySelectorAll('.filters__item-container-list');

categorieTitle.forEach((el, i) => {
    el.addEventListener('click', () => {
        categorieContainer[i - 1].classList.toggle('filters__item-container-list-show');
        categorieTitleIcon[i - 1].classList.toggle('filters__item-title-icon-rotated');
    })
});