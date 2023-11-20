const arrowNext = document.querySelector('.fa-chevron-right');
const arrowPrev = document.querySelector('.fa-chevron-left')
const productImg = document.querySelector('.product-img img');
const sliderItemArr = document.querySelectorAll('.slider__item');
const activeSlide = document.querySelector('.active-slide')

const clicked = [sliderItemArr[0]]

for (i = 0; i < sliderItemArr.length; i++) {
    sliderItemArr[i].addEventListener('click', function () {
        clicked.unshift(this);
        clicked[i].classList.remove('active-slide');
        sliderItemArr[0].classList.remove('active-slide');
        this.classList.add('active-slide');
        productImg.setAttribute('src', this.firstChild.getAttribute('src'));
    });
};

let nextArrowClickCount = 2;
arrowNext.addEventListener('click', function () {
    nextArrowClickCount++;
    let sliderItem = document.querySelector(`.slider-line .slider__item:nth-child(${nextArrowClickCount})`);
    let prevSliderItem = document.querySelector(`.slider-line .slider__item:nth-child(${nextArrowClickCount - 1})`);
    let lastChild = document.querySelector('.slider-line .slider__item:last-of-type')

    if (nextArrowClickCount < sliderItemArr.length + 1) {
        sliderItem.classList.add('active-slide');
        productImg.setAttribute('src', sliderItem.firstChild.getAttribute('src'));
    }

    prevSliderItem.classList.remove('active-slide');
    if (nextArrowClickCount > sliderItemArr.length) {
        nextArrowClickCount = 2;
        lastChild.classList.remove('active-slide')
        productImg.setAttribute('src', document.querySelector('.slider-line .slider__item:first-of-type img').getAttribute('src'))
        sliderItemArr[0].classList.add('active-slide');
    }
})

arrowPrev.addEventListener('click', function () {
    let prevArrowClickCount = --nextArrowClickCount;
    let sliderItem = document.querySelector(`.slider-line .slider__item:nth-child(${prevArrowClickCount})`);
    let prevSliderItem = document.querySelector(`.slider-line .slider__item:nth-child(${prevArrowClickCount+1})`);
    let firstChild = document.querySelector('.slider-line .slider__item:first-of-type')
    if (prevArrowClickCount > 1) {
        sliderItem.classList.add('active-slide');
        productImg.setAttribute('src', sliderItem.firstChild.getAttribute('src'));
        prevSliderItem.classList.remove('active-slide');
    }
    if (prevArrowClickCount < 2) {
        nextArrowClickCount = 6;
        firstChild.classList.remove('active-slide')
        sliderItemArr[sliderItemArr.length - 2].classList.add('active-slide')
        productImg.setAttribute('src', document.querySelector('.slider-line .slider__item:last-of-type img').getAttribute('src'))
    } 
});