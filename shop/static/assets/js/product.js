const dateText = document.querySelectorAll('.comment-date');
const rating = document.querySelectorAll('.user-rating');

// Product name page title
const  pageTitle = document.querySelector('title');
const  productName = document.querySelector('.product-title');
pageTitle.textContent = productName.textContent


let currentDate = 0;
for (i = 0; i < rating.length; i++) {
    // Set current date
    let dateToday = new Date();
    let splitDate = dateToday.toLocaleString().split(',')
    let currentDate = dateText[i].textContent = splitDate[0];
    
    // Random rating
    let randomRating = Math.random()*10;
    rating[i].textContent = `Оценка: ${Math.round(randomRating)}/10`;
}

// Add a comment
const nameInput = document.querySelector('#form-name');
const textInput = document.querySelector('#form-text');
const ratingInput = document.querySelector('#form-rating');
const publishButton = document.querySelector('#leave-a-comment__button');

const usersComments = document.querySelector('.users-comments');

const commentPublishSuccess = document.querySelector('.comment-publish-success');

publishButton.addEventListener('click', function() {

    const nameInputValue = nameInput.value;
    const textInputValue = textInput.value;
    const ratingInputValue = ratingInput.value;

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
    
    createPName.textContent = nameInputValue;

    if (createPName.textContent === '') {
        createPName.textContent = 'Имя Фамилия';
    };

    createPText.textContent = textInputValue;
    createRating.textContent = `Оценка: ${ratingInputValue}/10`;

    usersComments.append(createDiv);
    createDiv.append(createPName);
    createDiv.append(createRating);
    createDiv.append(createDate);
    createDiv.append(createPText);

    nameInput.value = '';
    textInput.value = '';

    commentPublishSuccess.style.right = 0;
    
    setTimeout(() => {
        commentPublishSuccess.style.right = '-180px';
    }, 5000);
});