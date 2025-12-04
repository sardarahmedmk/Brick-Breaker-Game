from PIL import Image, ImageDraw
import os

# Create images directory if it doesn't exist
os.makedirs('static/images', exist_ok=True)

# Product image data
products_images = [
    {
        'filename': 'headphones.jpg',
        'name': 'Wireless Headphones',
        'color': (102, 126, 234),
        'emoji': '🎧'
    },
    {
        'filename': 'usb-cable.jpg',
        'name': 'USB-C Cable',
        'color': (118, 75, 162),
        'emoji': '🔌'
    },
    {
        'filename': 'phone-stand.jpg',
        'name': 'Phone Stand',
        'color': (100, 200, 150),
        'emoji': '📱'
    },
    {
        'filename': 'power-bank.jpg',
        'name': 'Power Bank',
        'color': (255, 167, 38),
        'emoji': '🔋'
    },
    {
        'filename': 'screen-protector.jpg',
        'name': 'Screen Protector',
        'color': (200, 150, 255),
        'emoji': '💎'
    },
    {
        'filename': 'speaker.jpg',
        'name': 'Bluetooth Speaker',
        'color': (41, 128, 185),
        'emoji': '🔊'
    }
]

# Create images
for product in products_images:
    # Create image with light gradient background
    img = Image.new('RGB', (300, 250), color=(245, 247, 250))
    draw = ImageDraw.Draw(img)
    
    # Draw gradient-like rectangles
    for i in range(250):
        color_intensity = 240 - int(i * 0.1)
        draw.line([(0, i), (300, i)], fill=(color_intensity, color_intensity + 10, color_intensity + 20))
    
    # Draw centered colored circle for product representation
    circle_size = 100
    x, y = 150, 125
    draw.ellipse([x - circle_size, y - circle_size, x + circle_size, y + circle_size], 
                 fill=product['color'], outline=product['color'])
    
    # Add lighter overlay
    draw.ellipse([x - circle_size + 10, y - circle_size + 10, x + circle_size - 10, y + circle_size - 10],
                 fill=tuple(min(c + 40, 255) for c in product['color']))
    
    # Save image
    img.save(f"static/images/{product['filename']}")
    print(f"Created: {product['filename']}")

print("All product images created successfully!")
