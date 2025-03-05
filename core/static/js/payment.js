document.addEventListener('DOMContentLoaded', function() {
    var stripe = Stripe('{{ stripe_publishable_key }}');
    var elements = stripe.elements();
    var card = elements.create('card');
    card.mount('#card-element');

    card.on('change', function(event) {
        var displayError = document.getElementById('card-errors');
        if (event.error) {
            displayError.textContent = event.error.message;
        } else {
            displayError.textContent = '';
        }
    });

    var form = document.getElementById('payment-form');
    form.addEventListener('submit', function(event) {
        event.preventDefault();

        stripe.createPaymentMethod({
            type: 'card',
            card: card,
        }).then(function(result) {
            if (result.error) {
                var errorElement = document.getElementById('card-errors');
                errorElement.textContent = result.error.message;
            } else {
                // Handle successful payment
                fetch("{% url 'process_payment' %}", {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        'X-CSRFToken': '{{ csrf_token }}'
                    },
                    body: JSON.stringify({
                        payment_method_id: result.paymentMethod.id
                    })
                }).then(response => {
                    if (response.ok) {
                        window.location.href = "{% url 'finishing' %}";
                    } else {
                        window.location.href = "{% url 'payment_failed' %}";
                    }
                });
            }
        });
    });
});
