// Location 
const items = document.querySelectorAll('.item');
items.forEach(el => {
    el.addEventListener('click', () => {
        window.location.href = './product.html';
    })
});