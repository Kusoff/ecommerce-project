const items = document.querySelectorAll('.item');
const itemsContainer = document.querySelector('.confirm-order-items');
const img = document.querySelectorAll('.item__img-container img');
const title = document.querySelectorAll('.item__title');
const descr = document.querySelectorAll('.item__description');
const count = document.querySelectorAll('.item__counter');
const itemPrice = document.querySelectorAll('.price__text');
const orderButton = document.querySelector('#total__button');


orderButton.addEventListener('click', () => {
    // Clear container every click
    const orderItem = document.querySelectorAll('.confirm-order-item');
    orderItem.forEach(el => {
        el.remove();
    });

    // Get item elements && paste into container
    for (i = 0; i < items.length; i++) {
        const createItem = document.createElement('div');
        createItem.classList.add('confirm-order-item');

        const createImg = document.createElement('img');
        createImg.setAttribute('src', img[i].getAttribute('src', ''));
        createImg.classList.add('order-item-img')

        const createTextContainer = document.createElement('div');
        createTextContainer.classList.add('order-item-text')

        const createTitle = document.createElement('p');
        createTitle.classList.add('order-item-title');
        createTitle.textContent = title[i].textContent;

        const createCount = document.createElement('span');
        createCount.textContent = ` x${count[i].textContent}`;

        const createDescr = document.createElement('p');
        createDescr.classList.add('order-item-description');
        createDescr.textContent = descr[i].textContent;

        const createPriceContainer = document.createElement('p');
        createPriceContainer.classList.add('order-item-price');
        createPriceContainer.textContent = 'Итоговая цена:';
        
        
        const createPrice = document.createElement('span');
        createPrice.textContent = ` ${itemPrice[i].textContent} ₽`;

        itemsContainer.appendChild(createItem);
        createItem.appendChild(createImg);
        createItem.appendChild(createTextContainer);
        createTextContainer.appendChild(createTitle);
        createTitle.appendChild(createCount);
        createTextContainer.appendChild(createDescr);
        createTextContainer.appendChild(createPriceContainer);
        createPriceContainer.appendChild(createPrice);

        if(createPrice.textContent.split('₽')[0] == 0) {
            createPrice.parentElement.parentElement.parentElement.remove();
        }
    }
})