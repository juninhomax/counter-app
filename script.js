
// Get the counter element and button
const counter = document.getElementById('counter');
const incrementBtn = document.getElementById('incrementBtn');

// Initialize counter value
let count = 0;

// Add event listener to the button
incrementBtn.addEventListener('click', () => {
  // Increment the counter
  count++;
  // Update the displayed counter value
  counter.textContent = count;
});
