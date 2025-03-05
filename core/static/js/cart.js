// static/js/cart.js
document.addEventListener('DOMContentLoaded', function() {
    const addToCartButton = document.querySelector('.add-to-cart-btn');

    addToCartButton.addEventListener('click', function() {
        const productId = this.getAttribute('data-product-id');
        const isAdded = this.classList.toggle('added');

        if (isAdded) {
            this.textContent = 'Added to Cart';
            this.disabled = true; // Optional: disable button after adding

            // Make AJAX call to add item to cart
            fetch(`/cart/add/${productId}/`)
                .then(response => response.json())
                .then(data => console.log('Added to cart:', data))
                .catch(error => console.error('Error:', error));
        } else {
            this.textContent = 'Add to Cart';
            this.disabled = false; // Re-enable button if needed

            // Make AJAX call to remove item from cart
            fetch(`/cart/remove/${productId}/`)
                .then(response => response.json())
                .then(data => console.log('Removed from cart:', data))
                .catch(error => console.error('Error:', error));
        }
    });
});
