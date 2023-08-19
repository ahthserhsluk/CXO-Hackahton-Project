// Function to change the color of text in a specific class
function changeTextColor() {
    const elements = document.querySelectorAll('.text-to-change');
    elements.forEach(element => {
      element.style.color = 'red'; // Change the color to your desired value
    });
  }
  
  // Add a click event listener to the button
  document.addEventListener('DOMContentLoaded', function () {
    const button = document.getElementById('changeColorButton');
    button.addEventListener('click', changeTextColor);
  });