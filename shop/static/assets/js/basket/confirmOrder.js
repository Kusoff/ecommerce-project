const orderAllButton = document.querySelector('#total__button');
const confirmOrder = document.querySelector('.confirm-order');
const confirmOrderBackground = document.querySelector('.confirm-order-bg');

orderAllButton.addEventListener('click', () => {
    confirmOrderBackground.style.zIndex = 1;
    confirmOrderBackground.style.opacity = 100;

    confirmOrder.style.display = 'flex';
    setTimeout(() => {
        confirmOrder.style.bottom = '0';
    }, 300)
});

const changePaymentMethod = document.querySelector('#change-payment-method');
const choiseMethodContainer = document.querySelector('.payment-method-choice');

changePaymentMethod.addEventListener('click', () => {
    choiseMethodContainer.style.top = '-15%';
    changePaymentMethod.style.visibility = 'hidden';
});

const paymentMethods = document.querySelectorAll('.payment-method-item');
paymentMethods.forEach(el => {
    el.addEventListener('click', () => {

        for (i = 0; i < paymentMethods.length; i++) {
            paymentMethods[i].classList.remove('mastercard-active', 'cash-active', 'qiwi-active', 'mts-active', 'visa-active');
        }

        if (el.classList.contains('mastercard')) {
            el.classList.toggle('mastercard-active');
        } else if (el.classList.contains('cash')) {
            el.classList.toggle('cash-active');
        } else if (el.classList.contains('qiwi')) {
            el.classList.toggle('qiwi-active');
        } else if (el.classList.contains('mts')) {
            el.classList.toggle('mts-active');
        } else {
            el.classList.toggle('visa-active');
        }
    })
})

confirmOrderBackground.addEventListener('click', () => {
    confirmOrder.style.bottom = '-100%';
    setTimeout(() => {
        confirmOrderBackground.style.zIndex = -1;
        confirmOrderBackground.style.opacity = 0;
        confirmOrder.style.display = 'none';
    }, 300)
})

const confirmButton = document.querySelector('#confirm');

const orderAcceptedPopup = document.querySelector('.order-is-accepted__popup');
const checkCircle = document.querySelector('.check-circle');
const checkFirstDiv = document.querySelector('.check-circle div:first-child');
const checkLastDiv = document.querySelector('.check-circle div:last-child');

confirmButton.addEventListener('click', () => {
    confirmOrder.style.bottom = '-100%';
    setTimeout(() => {
        confirmOrderBackground.style.zIndex = -1;
        confirmOrderBackground.style.opacity = 0;
        confirmOrder.style.display = 'none';
    }, 300)

    setTimeout(() => {
        orderAcceptedPopup.style.zIndex = 1;
        orderAcceptedPopup.style.opacity = 100;

        setTimeout(() => {
            checkCircle.style.transform = 'scale(1)';
        }, 300)

        setTimeout(() => {
            checkFirstDiv.style.height = '50px';
        }, 600)

        setTimeout(() => {
            checkLastDiv.style.height = '80px';
        }, 900)
    }, 600)
})

const closePopup = document.querySelector('#close-popup');
closePopup.addEventListener('click', () => {
    orderAcceptedPopup.style.height = 0;

    setTimeout(() => {
        orderAcceptedPopup.style.display = 'none';
    }, 300);

    orderAllButton.textContent = 'Заказано';
    orderAllButton.setAttribute('disabled', '');
    orderAllButton.style.backgroundColor = '#2CC283';
})