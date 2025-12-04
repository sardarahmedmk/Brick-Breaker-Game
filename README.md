# ✨ TechHub Pro - E-Commerce Store

A modern, feature-rich e-commerce platform built with Flask and modern web technologies. Beautiful light-themed UI with multi-language support, multi-currency conversion, and real-time order tracking.

## 🌟 Features

- **🛍️ Product Catalog**: Browse beautiful tech products with high-quality images
- **🛒 Shopping Cart**: Add items, adjust quantities, manage your cart
- **💳 Checkout System**: Easy checkout with shipping address and payment details
- **📦 Order Tracking**: Real-time order status tracking with timeline visualization
- **🌍 Multi-Language**: English & Urdu language support
- **💱 Multi-Currency**: Support for USD, EUR, GBP, PKR, INR and more
- **🎨 Modern UI**: Beautiful light color theme with smooth animations
- **📱 Responsive Design**: Works perfectly on desktop, tablet, and mobile devices
- **🔐 Secure**: Client-side data storage with localStorage

## 📋 Prerequisites

Before you begin, make sure you have the following installed on your system:

- **Python 3.7 or higher** - [Download Python](https://www.python.org/downloads/)
- **pip** (Python Package Manager) - Usually comes with Python
- **Git** (Optional, for cloning) - [Download Git](https://git-scm.com/downloads)

### Check if Python is installed:
```bash
python --version
```

## 🚀 Installation & Setup

### Step 1: Download/Clone the Project
```bash
# If using git
git clone <repository-url>
cd ecommerce

# OR manually download and extract the files
# Navigate to the ecommerce folder
cd d:\html\ecommerce
```

### Step 2: Install Python Dependencies

Open Command Prompt or PowerShell and run:

```bash
pip install -r requirements.txt
```

**Or install packages individually:**

```bash
pip install Flask
pip install Pillow
pip install python-dotenv
```

### Required Dependencies:
- **Flask** - Web framework
- **Pillow** - Image processing library

## 📁 Project Structure

```
ecommerce/
├── app.py                      # Main Flask application
├── products.json               # Product database
├── currency.py                 # Currency conversion module
├── generate_images.py          # Image generation script
├── requirements.txt            # Project dependencies
├── README.md                   # This file
│
├── static/
│   ├── css/
│   │   └── main.css           # Main stylesheet
│   ├── js/
│   │   └── script.js          # Frontend JavaScript
│   └── images/
│       ├── headphones.jpg
│       ├── usb-cable.jpg
│       ├── phone-stand.jpg
│       ├── power-bank.jpg
│       ├── screen-protector.jpg
│       └── speaker.jpg
│
├── templates/
│   ├── index.html             # Homepage
│   ├── product.html           # Product detail page
│   ├── cart.html              # Shopping cart
│   ├── checkout.html          # Checkout page
│   └── orders.html            # Order tracking page
│
└── translations/
    ├── en.json                # English translations
    └── ur.json                # Urdu translations
```

## 🏃 Running the Application

### Step 1: Navigate to Project Directory
```bash
cd d:\html\ecommerce
```

### Step 2: Start Flask Server
```bash
python app.py
```

You should see output like:
```
* Serving Flask app 'app'
* Debug mode: on
* Running on http://127.0.0.1:5000
Press CTRL+C to quit
```

### Step 3: Open in Browser
Open your web browser and go to:
```
http://localhost:5000
```

## 📖 How to Use

### Browsing Products
1. Go to homepage to see all available products
2. Each product shows: Name, Description, Rating, Reviews, Price
3. Click "View Details" to see full product information

### Shopping
1. Click "Add to Cart" to add products
2. Go to "Cart" page to review items
3. Adjust quantities or remove items as needed

### Checkout
1. Click "Proceed to Checkout"
2. Fill in your shipping address
3. Enter payment details (demo - any card works)
4. Click "Place Order"
5. You'll get an Order ID

### Tracking Orders
1. Click "My Orders" from navigation
2. See all your orders with status
3. Track delivery progress: Pending → Processing → Shipped → Delivered
4. View order details and items

### Language & Currency
1. Use dropdown menus in navbar to switch language (English/Urdu)
2. Use currency selector to view prices in different currencies
3. Prices automatically convert based on current exchange rates

## 🔧 Configuration

### Adding New Products
Edit `products.json`:
```json
{
  "id": 7,
  "name": "New Product",
  "price": 99.99,
  "description": "Product description",
  "category": "Electronics",
  "image": "product-image.jpg",
  "rating": 4.5,
  "reviews": 100
}
```

### Adding New Languages
1. Create new translation file in `translations/` folder (e.g., `fr.json` for French)
2. Add language option to HTML select dropdowns
3. Follow the same key-value structure as existing translations

### Updating Exchange Rates
Edit `currency.py`:
```python
EXCHANGE_RATES = {
    'USD': 1.0,
    'EUR': 0.92,  # Update this value
    # ... other currencies
}
```

## 🎨 Customization

### Change Store Name
Edit `translations/en.json` and `translations/ur.json`:
```json
"store_name": "Your New Store Name"
```

### Change Colors
Edit `static/css/main.css` - Look for color values:
- Primary color: `#667eea`
- Secondary color: `#764ba2`

### Update Product Images
Replace images in `static/images/` folder with your own images (JPG, PNG, etc.)

## 🌐 Supported Languages
- English (en)
- Urdu (ur)

Easy to add more languages - just create a new JSON file in `translations/` folder!

## 💱 Supported Currencies
- USD (US Dollar)
- EUR (Euro)
- GBP (British Pound)
- PKR (Pakistani Rupee)
- INR (Indian Rupee)
- CAD (Canadian Dollar)
- AUD (Australian Dollar)
- JPY (Japanese Yen)
- CNY (Chinese Yuan)
- AED (UAE Dirham)
- SAR (Saudi Riyal)

## 💾 Data Storage

All data is stored in browser's localStorage:
- **Cart**: Saved locally until checkout
- **Orders**: All orders saved with status tracking
- **Session**: Language and currency preferences

Data persists until manually cleared from browser storage.

## 🐛 Troubleshooting

### Flask Server Won't Start
```bash
# Make sure you're in the correct directory
cd d:\html\ecommerce

# Check Python version
python --version

# Reinstall Flask
pip uninstall flask
pip install flask
```

### Images Not Loading
```bash
# Make sure images are in static/images/ folder
# File names should match product.json exactly

# Regenerate images
python generate_images.py
```

### Port Already in Use
If port 5000 is already in use:
```python
# Edit the last line of app.py
if __name__ == '__main__':
    app.run(debug=True, port=5001)  # Change to different port
```

### ModuleNotFoundError
```bash
# Install all dependencies
pip install -r requirements.txt

# Or install individually
pip install flask pillow
```

## 📦 Creating requirements.txt

To create a requirements file:
```bash
pip freeze > requirements.txt
```

Current requirements:
```
Flask==2.3.0
Pillow==9.5.0
Werkzeug==2.3.0
```

## 🔒 Security Notes

- This is a **demo/development** application
- Payment information is NOT actually processed
- Use in production requires proper security measures:
  - HTTPS/SSL encryption
  - Real payment gateway integration
  - Backend validation
  - Database backend instead of localStorage
  - User authentication

## 📱 Responsive Breakpoints

The site is optimized for:
- Desktop (1200px and above)
- Tablet (768px - 1199px)
- Mobile (below 768px)

## 🎯 API Endpoints

### Product APIs
- `GET /` - Homepage with products
- `GET /api/products` - Get all products (JSON)
- `GET /api/product/<id>` - Get specific product (JSON)
- `GET /product/<id>` - Product detail page

### Shopping
- `GET /cart` - Shopping cart page
- `GET /checkout` - Checkout page

### Orders
- `GET /orders` - My orders page

### Parameters
- `lang` - Language (en, ur)
- `currency` - Currency (USD, EUR, GBP, PKR, INR, etc.)

Example:
```
http://localhost:5000/?lang=ur&currency=PKR
http://localhost:5000/product/1?lang=en&currency=USD
```

## 🚀 Deployment

To deploy to production:

1. **Install a production WSGI server:**
   ```bash
   pip install gunicorn
   ```

2. **Run with Gunicorn:**
   ```bash
   gunicorn -w 4 -b 0.0.0.0:8000 app:app
   ```

3. **Use a reverse proxy** (Nginx, Apache)
4. **Set up HTTPS/SSL** certificates
5. **Migrate from localStorage to database**
6. **Implement proper authentication**

## 📝 License

This project is open source and available for educational and commercial use.

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest features
- Submit pull requests
- Improve documentation

## 📞 Support

For issues or questions:
1. Check the Troubleshooting section above
2. Review Flask documentation: https://flask.palletsprojects.com/
3. Check browser console for errors (F12 Developer Tools)

## 🎓 Learning Resources

- **Flask**: https://flask.palletsprojects.com/
- **HTML/CSS**: https://www.w3schools.com/
- **JavaScript**: https://developer.mozilla.org/en-US/docs/Web/JavaScript/
- **Python**: https://docs.python.org/3/

## ✨ Features Coming Soon

- User accounts & authentication
- Real payment gateway integration
- Email notifications
- Admin dashboard
- Product reviews & ratings
- Wishlist functionality
- Advanced search & filters
- Inventory management

---

**Made with ❤️ for TechHub Pro**

Last Updated: December 2025
