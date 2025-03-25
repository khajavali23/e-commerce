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


function changeImage(element) {
    document.getElementById('mainImage').src = element.src;
}

document.getElementById("increase").addEventListener("click", function() {
    let quantity = document.getElementById("quantity");
    let value = parseInt(quantity.value) || 1;
    quantity.value = (value + 1) + " Meters";
});

document.getElementById("decrease").addEventListener("click", function() {
    let quantity = document.getElementById("quantity");
    let value = parseInt(quantity.value) || 1;
    if (value > 1) {
        quantity.value = (value - 1) + " Meters";
    }
});

function changeImage(element) {
    document.getElementById('mainImage').src = element.src;
}

function removeFromWishlist(productId) {
    fetch(`/remove-from-wishlist/${productId}/`, {
        method: "POST",
        headers: {
            "X-CSRFToken": getCSRFToken(),
            "Content-Type": "application/json"
        }
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            // Remove item instantly from UI
            document.querySelector(`[data-id="${productId}"]`).remove();
        } else {
            alert("Error: Could not remove item.");
        }
    })
    .catch(error => console.error("Error:", error));
}

// Get CSRF Token
function getCSRFToken() {
    return document.querySelector('[name=csrfmiddlewaretoken]').value;
}

function updateQuantity(itemId, change) {
    // Select the input field for the corresponding cart item
    let inputField = document.querySelector(`.cart-item input[value="{{ item.quantity }}"]`);

    if (inputField) {
        let currentQuantity = parseInt(inputField.value);
        let newQuantity = currentQuantity + change;

        if (newQuantity < 1) return; // Prevent quantity from going below 1

        // Update input field value
        inputField.value = newQuantity;

        // Send AJAX request to update quantity in backend
        fetch(`/update-cart/${itemId}/`, {
            method: "POST",
            headers: {
                "X-CSRFToken": getCSRFToken(),
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ quantity: newQuantity })
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                console.log("Quantity updated successfully");
                location.reload(); // Reload to reflect updated price
            } else {
                alert("Error updating quantity");
            }
        })
        .catch(error => console.error("Error:", error));
    }
}

// Get CSRF Token function
function getCSRFToken() {
    return document.querySelector('[name=csrfmiddlewaretoken]').value;
}


function addToCart(element) {
    let productId = element.getAttribute("data-product-id");

    fetch("/add-to-cart/", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": getCSRFToken(),  // Required for Django
        },
        body: JSON.stringify({ product_id: productId })
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            alert("Product added to cart!");
        } else {
            alert("Error adding product to cart.");
        }
    })
    .catch(error => console.error("Error:", error));
}

// Function to get CSRF token for Django security
function getCSRFToken() {
    let cookieValue = null;
    if (document.cookie && document.cookie !== "") {
        let cookies = document.cookie.split(";");
        for (let i = 0; i < cookies.length; i++) {
            let cookie = cookies[i].trim();
            if (cookie.startsWith("csrftoken=")) {
                cookieValue = cookie.substring("csrftoken=".length, cookie.length);
                break;
            }
        }
    }
    return cookieValue;
}
