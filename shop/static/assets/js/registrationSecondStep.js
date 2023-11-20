const mailingListButton = document.querySelector('#mailing-list-on__button');
const mailingListCheckbox = document.querySelector('#id_1-mailing_list');
const checked = mailingListCheckbox.getAttribute('checked');

// Change checkbox and button styles
mailingListButton.addEventListener('click', function () {
    this.style.boxShadow = '0 0 0 3px #2CC283';
    this.classList.toggle('clicked');
    this.textContent = 'Включена';
    mailingListCheckbox.setAttribute('checked', '');
    
    if (mailingListButton.classList.contains('clicked')) {
        // this.classList.remove('clicked');
        this.textContent = 'Выключена';
        this.style.boxShadow = '0 0 0 3px red';
        mailingListCheckbox.removeAttribute('checked', '');
    }
});