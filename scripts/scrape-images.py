#!/usr/bin/env python3
"""
Scrape images from websites and save them locally
"""

import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import os
import json
from pathlib import Path

def scrape_site_images(url, output_dir):
    """Scrape all images from a website"""
    try:
        # Fetch the page
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()

        # Parse HTML
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all images
        images = []

        # Regular img tags
        for img in soup.find_all('img'):
            src = img.get('src') or img.get('data-src')
            if src:
                full_url = urljoin(url, src)
                alt = img.get('alt', '')
                images.append({
                    'url': full_url,
                    'alt': alt,
                    'type': 'img'
                })

        # CSS background images
        for elem in soup.find_all(style=True):
            style = elem.get('style', '')
            if 'background-image' in style or 'background:' in style:
                # Extract URL from CSS
                import re
                urls = re.findall(r'url\(["\']?([^"\')]+)["\']?\)', style)
                for bg_url in urls:
                    full_url = urljoin(url, bg_url)
                    images.append({
                        'url': full_url,
                        'alt': 'Background image',
                        'type': 'background'
                    })

        # Create output directory
        Path(output_dir).mkdir(parents=True, exist_ok=True)

        # Save metadata
        with open(f'{output_dir}/images.json', 'w') as f:
            json.dump(images, f, indent=2)

        print(f"Found {len(images)} images from {url}")
        for i, img in enumerate(images[:10]):  # Print first 10
            print(f"  {i+1}. {img['url']}")
            if img['alt']:
                print(f"     Alt: {img['alt']}")

        return images

    except Exception as e:
        print(f"Error scraping {url}: {e}")
        return []

if __name__ == '__main__':
    sites = [
        ('https://liankok.com', 'outputs/landing-page/assets/liankok'),
        ('https://owllight-sleep.com', 'outputs/landing-page/assets/owllight'),
        ('https://vpublish.com.sg', 'outputs/landing-page/assets/vpublish'),
    ]

    for url, output_dir in sites:
        print(f"\n{'='*60}")
        print(f"Scraping: {url}")
        print('='*60)
        scrape_site_images(url, output_dir)
