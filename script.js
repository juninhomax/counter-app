document.addEventListener('DOMContentLoaded', () => {
    let counter = 0;
    const counterDisplay = document.getElementById('counter');
    const incrementBtn = document.getElementById('incrementBtn');

    incrementBtn.addEventListener('click', () => {
        counter++;
        counterDisplay.textContent = counter;
    });
});