const textInput = document.getElementById('textInput');
const hiddenInput = document.getElementById('hiddenInput');
const letterForm = document.getElementById('letterForm');


// Handle key click
function handleKeyPress(letter, keyElement) {
    if (!letter || keyElement.classList.contains('disabled')) return;

    textInput.value += letter; // add letter to text input
    hiddenInput.value = letter; // set the letter in the hidden field
    keyElement.removeEventListener('click', handleKeyPress); // remove the click event listener

    // automatically submit form
    letterForm.submit();
}


// Create keys from the letter 'A' to 'Z'
const keyboardElement = document.getElementById('keyboard');
const keys = keyboardElement.querySelectorAll('.key');
keys.forEach((key) => {
    const letter = key.textContent;
    key.addEventListener('click', () => {
        handleKeyPress(letter, key);
    });
});
