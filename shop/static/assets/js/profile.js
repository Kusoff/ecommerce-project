const profileSettingsButton = document.querySelector('.fa-cogs');
const profileSettingsContainer = document.querySelector('.profile-settings__container');
const profileSettings = document.querySelector('.profile-settings');
const closeButtons = document.querySelectorAll('#confirm, .fa-times');
const body = document.querySelector('body');

profileSettingsButton.addEventListener('click', () => {
    profileSettingsContainer.style.display = 'block';
    setTimeout(() => {
        profileSettings.style.opacity = 100;
    }, 0);
    body.style.overflowY = 'hidden';
});

closeButtons.forEach(el => {
    el.addEventListener('click', () => {
        profileSettings.style.opacity = 0;
        setTimeout(() => {
            profileSettingsContainer.style.display = 'none';
        }, 300);
        body.style.overflowY = 'scroll';

        confirmEmail.value = '';
        email.value = '';
        confirmPassword.value = '';
        password.value = '';
    })
})