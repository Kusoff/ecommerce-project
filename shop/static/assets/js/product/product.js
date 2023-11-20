const dateText = document.querySelectorAll('.comment-date');
const rating = document.querySelectorAll('.user-rating');
const startPrice = document.querySelector('#start-price-number');
const discount = document.querySelector('#discount-number');
const finishPrice = document.querySelector('#finish-price-number');

const addToCartButton = document.querySelector('.add-to-cart__button button');
// Product name page title
const pageTitle = document.querySelector('title');
const productName = document.querySelector('.product-title');
pageTitle.textContent = productName.textContent
for (i = 0; i < rating.length; i++) {
    // Set current date on comment
    const dateToday = new Date();
    const splitDate = dateToday.toLocaleString().split(',')
    const currentDate = dateText[i].textContent = splitDate[0];
    // Random rating
    const randomRating = Math.random() * 10;
    rating[i].textContent = `Оценка: ${Math.round(randomRating)}/10`;
}

// Change add to cart button text and styles on click
addToCartButton.addEventListener('click', function() {
    this.textContent = 'Добавлено!';
    this.style.border = '2px solid #08B251';
    this.style.backgroundColor = 'green';
    setTimeout(()=>{
        this.style.backgroundColor = 'transparent';
    }, 1000)
});

