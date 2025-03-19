document.getElementById('js_folder-collapse-button-icon').addEventListener('click', function(){
  document.getElementById('js_folder-collapse-button-icon').classList.toggle('rotate')
  document.getElementById('language_box').classList.toggle('d-none')
})
function toggleFilter(id, element) {
  var options = document.getElementById(id);
  var icon = element.querySelector("svg");

  if (options.style.display === "block") {
      options.style.display = "none";
      icon.style.transform = "rotate(0deg)";
  } else {
      options.style.display = "block";
      icon.style.transform = "rotate(180deg)";
  }
}
function increaseQuantity(button) {
  let input = button.previousElementSibling;
  input.value = parseInt(input.value) + 1;
}

function decreaseQuantity(button) {
  let input = button.nextElementSibling;
  if (parseInt(input.value) > 1) {
      input.value = parseInt(input.value) - 1;
  }
}
const fabricProducts = document.getElementById('fabric__products');
const dropdownBox = document.getElementById('dropdown___box');

fabricProducts.addEventListener('mouseover', function() {
    dropdownBox.classList.remove('d-none'); // Show dropdown
});

fabricProducts.addEventListener('mouseleave', function() {
    setTimeout(() => {
        if (!dropdownBox.matches(':hover')) { // Check if dropdown is not hovered
            dropdownBox.classList.add('d-none'); // Hide dropdown
        }
    }, 200); // Delay to allow moving into the dropdown
});

dropdownBox.addEventListener('mouseleave', function() {
    dropdownBox.classList.add('d-none'); // Hide dropdown when mouse leaves
});

const fabricProducts1 = document.getElementById('fabric__products1');
const dropdownBox1 = document.getElementById('dropdown___box1');

fabricProducts1.addEventListener('mouseover', function() {
    dropdownBox1.classList.remove('d-none'); // Show dropdown
});

fabricProducts1.addEventListener('mouseleave', function() {
    setTimeout(() => {
        if (!dropdownBox1.matches(':hover')) { // Check if dropdown is not hovered
            dropdownBox1.classList.add('d-none'); // Hide dropdown
        }
    }, 200); // Delay to allow moving into the dropdown
});

dropdownBox1.addEventListener('mouseleave', function() {
    dropdownBox1.classList.add('d-none'); // Hide dropdown when mouse leaves
});

const fabricProducts2 = document.getElementById('fabric__products2');
const dropdownBox2 = document.getElementById('dropdown___box2');

fabricProducts2.addEventListener('mouseover', function() {
    dropdownBox2.classList.remove('d-none'); // Show dropdown
});

fabricProducts2.addEventListener('mouseleave', function() {
    setTimeout(() => {
        if (!dropdownBox2.matches(':hover')) { // Check if dropdown is not hovered
            dropdownBox2.classList.add('d-none'); // Hide dropdown
        }
    }, 200); // Delay to allow moving into the dropdown
});

dropdownBox2.addEventListener('mouseleave', function() {
    dropdownBox2.classList.add('d-none'); // Hide dropdown when mouse leaves
});
const fabricProducts3 = document.getElementById('fabric__products3');
const dropdownBox3 = document.getElementById('dropdown___box3');

fabricProducts3.addEventListener('mouseover', function() {
    dropdownBox3.classList.remove('d-none'); // Show dropdown
});

fabricProducts3.addEventListener('mouseleave', function() {
    setTimeout(() => {
        if (!dropdownBox3.matches(':hover')) { // Check if dropdown is not hovered
            dropdownBox3.classList.add('d-none'); // Hide dropdown
        }
    }, 200); // Delay to allow moving into the dropdown
});

dropdownBox3.addEventListener('mouseleave', function() {
    dropdownBox3.classList.add('d-none'); // Hide dropdown when mouse leaves
});
function toggleFilter(filterId, element) {
    const filterOptions = document.getElementById(filterId);
    if (filterOptions.style.display === "none" || filterOptions.style.display === "") {
        filterOptions.style.display = "block"; // Show the filter options
    } else {
        filterOptions.style.display = "none"; // Hide the filter options
    }
}








document.addEventListener("DOMContentLoaded", function() {
    const decreaseBtn = document.getElementById("decrease");
    const increaseBtn = document.getElementById("increase");
    const quantityInput = document.getElementById("quantity");

    let quantity = 1;

    decreaseBtn.addEventListener("click", function() {
        if (quantity > 1) {
            quantity--;
            quantityInput.value = `${quantity} Meter`;
        }
    });

    increaseBtn.addEventListener("click", function() {
        quantity++;
        quantityInput.value = `${quantity} Meter`;
    });
});





