# EbayXlister

A Python-based command-line tool for managing eBay listings. Import, export, and organize your eBay inventory with ease.

## Features

- 📥 Import listings from CSV files
- 📤 Export listings to JSON format
- ➕ Add individual listings via command line
- 📋 View all listings with detailed information
- 💰 Calculate total inventory value
- ✨ Simple and intuitive CLI interface

## Installation

1. Clone this repository:
```bash
git clone https://github.com/Trollz1004/EbayXlister.git
cd EbayXlister
```

2. Make the script executable (optional):
```bash
chmod +x ebay_xlister.py
```

## Usage

### Import listings from CSV

```bash
python ebay_xlister.py --import-csv example_listings.csv
```

### Add a single listing

```bash
python ebay_xlister.py --add "Vintage Watch" 299.99 "Beautiful vintage timepiece"
```

### List all current listings

```bash
python ebay_xlister.py --list
```

### Export listings to JSON

```bash
python ebay_xlister.py --import-csv example_listings.csv --export-json my_listings.json
```

### Combine operations

```bash
python ebay_xlister.py --import-csv example_listings.csv --list --export-json output.json
```

## CSV Format

Your CSV file should have the following columns:

- `title` - Item title (required)
- `price` - Item price (required)
- `description` - Item description (optional)
- `category` - Item category (optional)
- `condition` - Item condition (optional, default: "New")
- `quantity` - Quantity available (optional, default: 1)

See `example_listings.csv` for a sample file.

## Example Output

```
✓ Added listing: Vintage Camera Lens 50mm - $125.00 (Used - Like New)
✓ Added listing: Gaming Mouse RGB - $45.99 (New)
✓ Added listing: Leather Wallet - $29.99 (New)
✓ Added listing: Coffee Maker - $89.99 (New)
✓ Added listing: Wireless Headphones - $149.99 (New)

✓ Successfully imported 5 listings from example_listings.csv

============================================================
Total Listings: 5
============================================================

1. Vintage Camera Lens 50mm - $125.00 (Used - Like New)
   Description: Classic 50mm lens in excellent condition...
   Category: Photography | Quantity: 1

2. Gaming Mouse RGB - $45.99 (New)
   Description: High DPI gaming mouse with customizable RGB l...
   Category: Electronics | Quantity: 5

...

Total Inventory Value: $1169.90
```

## Requirements

- Python 3.6 or higher
- No external dependencies required (uses only Python standard library)

## License

MIT License - feel free to use and modify as needed.

## Contributing

Contributions are welcome! Feel free to submit issues or pull requests.