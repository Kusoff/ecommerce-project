const minPriceSlider = document.querySelector('#price-min__input');
const minPriceText = document.querySelector('#price-range-min');
const maxPriceSlider = document.querySelector('#price-max__input');
const maxPriceText = document.querySelector('#price-range-max');
const itemPrice = document.querySelectorAll('.item p:nth-of-type(2)');

// Set input max value
let maxPrices = [];
itemPrice.forEach(el => {
    maxPrices.push(el.textContent.split('рублей')[0] / 1);
});
const getMaxPrice = Math.max(...maxPrices);
minPriceSlider.setAttribute('max', getMaxPrice);
maxPriceSlider.setAttribute('max', getMaxPrice);
maxPriceSlider.setAttribute('value', getMaxPrice);
maxPriceText.setAttribute('value', getMaxPrice);

// Set input values on input
function setInputValues(input) {
    input.addEventListener('input', () => {
        switch (input) {
            case minPriceSlider:
                minPriceText.value = minPriceSlider.value
                break;
            case minPriceText:
                minPriceSlider.value = minPriceText.value;
                break
                case maxPriceSlider:
                    maxPriceText.value = maxPriceSlider.value;
            default:
                maxPriceSlider.value = maxPriceText.value;
                break;
        }
    })
}
setInputValues(minPriceSlider);
setInputValues(minPriceText);
setInputValues(maxPriceSlider);
setInputValues(maxPriceText);