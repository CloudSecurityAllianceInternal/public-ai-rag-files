#!/usr/bin/env python3

import os
import xml.etree.ElementTree as ET
from urllib.parse import urljoin
from xml.dom import minidom

def prettify(element):
    """Return a pretty-printed XML string for the Element."""
    rough_string = ET.tostring(element, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="  ")

def generate_sitemap(base_url, start_path='.'):
    # Define the root element
    urlset = ET.Element('urlset', xmlns='http://www.sitemaps.org/schemas/sitemap/0.9')
    
    # Traverse the directory and file structure
    for root, dirs, files in os.walk(start_path):
        for file in files:
            # Construct the file path
            file_path = os.path.join(root, file)
            # Create a URL for the file
            url = urljoin(base_url, file_path.replace(os.sep, '/'))  # replace os.sep with '/' for URL
            
            # Create a url element
            url_element = ET.SubElement(urlset, 'url')
            loc = ET.SubElement(url_element, 'loc')
            loc.text = url

    # Pretty print and write to file
    with open('sitemap.xml', 'w', encoding='utf-8') as f:
        f.write(prettify(urlset))

# Usage example
base_url = 'http://www.yourwebsite.com/'  # Replace with your website's base URL
generate_sitemap(base_url)
