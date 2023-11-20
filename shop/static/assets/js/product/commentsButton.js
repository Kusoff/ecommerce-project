const form = document.querySelector('form');
const nameInput = document.querySelector('#form-name');
const label = document.querySelectorAll('label')
const textInput = document.querySelector('#form-text');
const ratingInput = document.querySelector('#form-rating');
const publishButton = document.querySelector('#leave-a-comment__button');
const usersComments = document.querySelector('.users-comments');

// Rating input limit
ratingInput.addEventListener('input', function () {
if (ratingInput.value >  10) {
    ratingInput.value = 10
} else if (ratingInput.value < 0) {
    ratingInput.value = 1
}
});

// Add a comment
publishButton.addEventListener('click', function (event) {
    event.preventDefault();
    
    // Validate
    if (ratingInput.value === '' && nameInput.value === '') {
        label.forEach(element => {
            element.style.opacity = 100;
        })
        publishButton.setAttribute('disabled')
    } else {
        label.forEach(element => {
            element.style.opacity = 0;
    })

        publishButton.removeAttribute('disabled');
    }

    // Create a comment
    const createDiv = document.createElement('div');
    createDiv.classList.add('users-comments__item');
    const createPName = document.createElement('p');
    const createRating = document.createElement('p');
    const createDate = document.createElement('p');
    createDate.classList.add('comment-date');
    const createPText = document.createElement('p');
    for (i = 0; i < rating.length; i++) {
        let dateToday = new Date();
        let splitDate = dateToday.toLocaleString().split(',')
        createDate.textContent = dateText[i].textContent = splitDate[0];
    }
    createPName.textContent = nameInput.value;
    if (createPName.textContent === '') {
        createPName.textContent = 'Имя не указано';
    };
    createPText.textContent = textInput.value;
    createRating.textContent = `Оценка: ${ratingInput.value}/10`;
    usersComments.append(createDiv);
    createDiv.append(createPName);
    createDiv.append(createRating);
    createDiv.append(createDate);
    createDiv.append(createPText);
    nameInput.value = '';
    textInput.value = '';
    ratingInput.value = '';

    // Publish successfully on button
    this.textContent = 'Опубликовано!';
    this.style.border = '2px solid #08B251';
    this.setAttribute('disabled', '');
    this.style.backgroundColor = 'green';
    setTimeout(()=>{
        this.style.backgroundColor = 'transparent';
    }, 1000)
});