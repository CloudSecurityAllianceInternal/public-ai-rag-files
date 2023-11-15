#!/usr/bin/env python3

import os

def create_html_link(path):
    """Create an HTML link for a given path."""
    return f'<li><a href="{path}">{path}</a></li>'

def generate_index_html(directory):
    """Generate index.html for a given directory."""
    index_path = os.path.join(directory, 'index.html')
    with open(index_path, 'w') as file:
        file.write('<html><body>\n')
        file.write('<ul>\n')

        for item in os.listdir(directory):
            if item == 'index.html':
                continue
            full_path = os.path.join(directory, item)
            if os.path.isdir(full_path):
                file.write(create_html_link(item + '/'))
            else:
                file.write(create_html_link(item))

        file.write('</ul>\n')
        file.write('</body></html>')

def traverse_directories(start_dir):
    """Traverse directories starting from start_dir and generate index.html files."""
    for root, dirs, files in os.walk(start_dir):
        generate_index_html(root)

if __name__ == "__main__":
    traverse_directories('.')

    
