// E-Commerce Store Main JavaScript

/**
 * Show loading spinner for 3 seconds
 */
function showLoading() {
    const overlay = document.createElement('div');
    overlay.className = 'loading-overlay';
    overlay.innerHTML = `
        <div style="text-align: center;">
            <div class="loading-spinner"></div>
            <div class="loading-text">PROCESSING...</div>
        </div>
    `;
    document.body.appendChild(overlay);
    
    setTimeout(() => {
        overlay.classList.add('fade-out');
        setTimeout(() => {
            overlay.remove();
        }, 300);
    }, 3000);
}

/**
 * Add item to cart
 */
function addToCart(productId, productName, price, lang = 'en', currency = 'USD') {
    try {
        showLoading();
        
        let cart = JSON.parse(localStorage.getItem('cart')) || [];
        let existingItem = cart.find(item => item.id === productId);

        if (existingItem) {
            existingItem.quantity += 1;
        } else {
            cart.push({
                id: productId,
                name: productName,
                price: price,
                quantity: 1
            });
        }

        localStorage.setItem('cart', JSON.stringify(cart));
        updateCartCount();
        showNotification('Item added to cart!');
    } catch(e) {
        console.error('Error adding to cart:', e);
        alert('Error adding item to cart');
    }
}

/**
 * Remove item from cart
 */
function removeFromCart(productId) {
    showLoading();
    let cart = JSON.parse(localStorage.getItem('cart')) || [];
    cart = cart.filter(item => item.id !== productId);
    localStorage.setItem('cart', JSON.stringify(cart));
    updateCartCount();
}

/**
 * Update item quantity in cart
 */
function updateQuantity(productId, quantity) {
    showLoading();
    let cart = JSON.parse(localStorage.getItem('cart')) || [];
    let item = cart.find(p => p.id === productId);

    if (item) {
        item.quantity = parseInt(quantity);
        if (item.quantity <= 0) {
            cart = cart.filter(p => p.id !== productId);
        }
    }

    localStorage.setItem('cart', JSON.stringify(cart));
}

/**
 * Get cart count
 */
function getCartCount() {
    let cart = JSON.parse(localStorage.getItem('cart')) || [];
    return cart.reduce((sum, item) => sum + item.quantity, 0);
}

/**
 * Update cart count display
 */
function updateCartCount() {
    const cartCountElements = document.querySelectorAll('#cartCount');
    const count = getCartCount();
    cartCountElements.forEach(element => {
        element.textContent = count;
    });
}

/**
 * Get cart total
 */
function getCartTotal() {
    let cart = JSON.parse(localStorage.getItem('cart')) || [];
    return cart.reduce((total, item) => total + (item.price * item.quantity), 0);
}

/**
 * Clear cart
 */
function clearCart() {
    localStorage.removeItem('cart');
    updateCartCount();
}

/**
 * Format price
 */
function formatPrice(price, currency = 'USD') {
    return `${currency} ${price.toFixed(2)}`;
}

/**
 * Show notification
 */
function showNotification(message) {
    const notification = document.createElement('div');
    notification.className = 'notification';
    notification.textContent = message;
    notification.style.cssText = `
        position: fixed;
        top: 80px;
        right: 20px;
        background-color: #4CAF50;
        color: white;
        padding: 1rem 2rem;
        border-radius: 4px;
        box-shadow: 0 2px 10px rgba(0,0,0,0.2);
        z-index: 1000;
        animation: slideIn 0.3s ease-in-out;
    `;

    document.body.appendChild(notification);

    setTimeout(() => {
        notification.style.animation = 'slideOut 0.3s ease-in-out';
        setTimeout(() => notification.remove(), 300);
    }, 2000);
}

/**
 * Format date for order
 */
function formatDate(date) {
    return new Date(date).toLocaleDateString('en-US', {
        year: 'numeric',
        month: 'long',
        day: 'numeric'
    });
}

/**
 * Validate email
 */
function validateEmail(email) {
    const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return re.test(email);
}

/**
 * Validate phone
 */
function validatePhone(phone) {
    const re = /^[\d\s\-\+\(\)]{10,}$/;
    return re.test(phone);
}

/**
 * Calculate shipping cost
 */
function calculateShipping(subtotal) {
    return subtotal > 100 ? 0 : 10;
}

/**
 * Calculate tax
 */
function calculateTax(subtotal, taxRate = 0.1) {
    return subtotal * taxRate;
}

/**
 * Get order summary
 */
function getOrderSummary() {
    let cart = JSON.parse(localStorage.getItem('cart')) || [];
    const subtotal = getCartTotal();
    const shipping = calculateShipping(subtotal);
    const tax = calculateTax(subtotal);
    const total = subtotal + shipping + tax;

    return {
        items: cart,
        subtotal: subtotal,
        shipping: shipping,
        tax: tax,
        total: total,
        itemCount: getCartCount()
    };
}

/**
 * Generate order ID
 */
function generateOrderId() {
    return 'ORD-' + Date.now() + '-' + Math.floor(Math.random() * 1000);
}

/**
 * Save order to localStorage
 */
function saveOrder(orderData) {
    let orders = JSON.parse(localStorage.getItem('orders')) || [];
    const order = {
        id: generateOrderId(),
        date: new Date().toISOString(),
        ...orderData,
        summary: getOrderSummary()
    };
    orders.push(order);
    localStorage.setItem('orders', JSON.stringify(orders));
    return order;
}

/**
 * Get order history
 */
function getOrderHistory() {
    return JSON.parse(localStorage.getItem('orders')) || [];
}

/**
 * Initialize cart on page load
 */
document.addEventListener('DOMContentLoaded', function() {
    updateCartCount();
});

// Add animation styles
const style = document.createElement('style');
style.textContent = `
    @keyframes slideIn {
        from {
            transform: translateX(400px);
            opacity: 0;
        }
        to {
            transform: translateX(0);
            opacity: 1;
        }
    }

    @keyframes slideOut {
        from {
            transform: translateX(0);
            opacity: 1;
        }
        to {
            transform: translateX(400px);
            opacity: 0;
        }
    }
`;
document.head.appendChild(style);
