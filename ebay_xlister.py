#!/usr/bin/env python3
"""
EbayXlister - A tool for managing eBay listings

This module provides functionality to create, update, and manage eBay listings
from CSV files or individual item data.
"""

import csv
import json
import argparse
from typing import List, Dict
from datetime import datetime


class EbayListing:
    """Represents a single eBay listing"""
    
    def __init__(self, title: str, price: float, description: str = "", 
                 category: str = "", condition: str = "New", quantity: int = 1):
        self.title = title
        self.price = price
        self.description = description
        self.category = category
        self.condition = condition
        self.quantity = quantity
        self.created_at = datetime.now().isoformat()
    
    def to_dict(self) -> Dict:
        """Convert listing to dictionary"""
        return {
            'title': self.title,
            'price': self.price,
            'description': self.description,
            'category': self.category,
            'condition': self.condition,
            'quantity': self.quantity,
            'created_at': self.created_at
        }
    
    def __str__(self) -> str:
        return f"{self.title} - ${self.price:.2f} ({self.condition})"


class EbayXlister:
    """Main class for managing eBay listings"""
    
    def __init__(self):
        self.listings: List[EbayListing] = []
    
    def add_listing(self, listing: EbayListing):
        """Add a new listing"""
        self.listings.append(listing)
        print(f"✓ Added listing: {listing}")
    
    def import_from_csv(self, filepath: str):
        """Import listings from a CSV file"""
        try:
            with open(filepath, 'r', newline='', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile)
                count = 0
                for row in reader:
                    listing = EbayListing(
                        title=row.get('title', ''),
                        price=float(row.get('price', 0)),
                        description=row.get('description', ''),
                        category=row.get('category', ''),
                        condition=row.get('condition', 'New'),
                        quantity=int(row.get('quantity', 1))
                    )
                    self.add_listing(listing)
                    count += 1
                print(f"\n✓ Successfully imported {count} listings from {filepath}")
        except FileNotFoundError:
            print(f"✗ Error: File '{filepath}' not found")
        except Exception as e:
            print(f"✗ Error importing CSV: {e}")
    
    def export_to_json(self, filepath: str):
        """Export all listings to a JSON file"""
        try:
            data = [listing.to_dict() for listing in self.listings]
            with open(filepath, 'w', encoding='utf-8') as jsonfile:
                json.dump(data, jsonfile, indent=2)
            print(f"✓ Exported {len(self.listings)} listings to {filepath}")
        except Exception as e:
            print(f"✗ Error exporting JSON: {e}")
    
    def list_all(self):
        """Display all listings"""
        if not self.listings:
            print("No listings found.")
            return
        
        print(f"\n{'='*60}")
        print(f"Total Listings: {len(self.listings)}")
        print(f"{'='*60}\n")
        
        for idx, listing in enumerate(self.listings, 1):
            print(f"{idx}. {listing}")
            if listing.description:
                print(f"   Description: {listing.description[:50]}...")
            print(f"   Category: {listing.category} | Quantity: {listing.quantity}")
            print()
    
    def get_total_value(self) -> float:
        """Calculate total value of all listings"""
        return sum(listing.price * listing.quantity for listing in self.listings)


def main():
    """Main entry point for the application"""
    parser = argparse.ArgumentParser(
        description='EbayXlister - Manage your eBay listings',
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    
    parser.add_argument(
        '--import-csv',
        dest='csv_file',
        help='Import listings from a CSV file'
    )
    
    parser.add_argument(
        '--export-json',
        dest='json_file',
        help='Export listings to a JSON file'
    )
    
    parser.add_argument(
        '--list',
        action='store_true',
        help='List all current listings'
    )
    
    parser.add_argument(
        '--add',
        nargs='+',
        metavar=('TITLE', 'PRICE'),
        help='Add a new listing (format: --add "Title" 29.99 "Description")'
    )
    
    args = parser.parse_args()
    
    xlister = EbayXlister()
    
    # Import from CSV if specified
    if args.csv_file:
        xlister.import_from_csv(args.csv_file)
    
    # Add individual listing if specified
    if args.add:
        if len(args.add) >= 2:
            title = args.add[0]
            try:
                price = float(args.add[1])
                description = args.add[2] if len(args.add) > 2 else ""
                listing = EbayListing(title, price, description)
                xlister.add_listing(listing)
            except ValueError:
                print("✗ Error: Price must be a number")
        else:
            print("✗ Error: --add requires at least title and price")
    
    # List all listings if specified
    if args.list or (not args.csv_file and not args.add and not args.json_file):
        xlister.list_all()
        if xlister.listings:
            total_value = xlister.get_total_value()
            print(f"Total Inventory Value: ${total_value:.2f}\n")
    
    # Export to JSON if specified
    if args.json_file:
        xlister.export_to_json(args.json_file)


if __name__ == '__main__':
    main()
