import os
from datetime import datetime

def create_sitemap(site_url, docs_folder='docs', output_file='sitemap.xml'):
    """
    Generates a sitemap.xml file by scanning for HTML files in the project.

    Args:
        site_url (str): The full base URL of the website (e.g., 'https://www.niscalajyoti.org/').
        docs_folder (str, optional): The directory containing your HTML pages. Defaults to 'docs'.
        output_file (str, optional): The name of the output sitemap file. Defaults to 'sitemap.xml'.
    """
    # Ensure the site_url doesn't have a trailing slash
    if site_url.endswith('/'):
        site_url = site_url[:-1]

    # Get the current date in YYYY-MM-DD format for the <lastmod> tag
    last_modified_date = datetime.now().strftime('%Y-%m-%d')

    urls = []

    # 1. Add the main index.html file from the root directory
    if os.path.exists('index.html'):
        urls.append(f"{site_url}/index.html")

    # 2. Scan the /docs directory for all other HTML files
    if os.path.isdir(docs_folder):
        for filename in os.listdir(docs_folder):
            if filename.endswith('.html'):
                # Construct the full URL for each page
                page_url = f"{site_url}/{docs_folder}/{filename}"
                urls.append(page_url)
    else:
        print(f"Warning: The '{docs_folder}' directory was not found.")

    # 3. Build the XML content for the sitemap
    xml_content = '<?xml version="1.0" encoding="UTF-8"?>\n'
    xml_content += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'

    for url in urls:
        xml_content += '  <url>\n'
        xml_content += f'    <loc>{url}</loc>\n'
        xml_content += f'    <lastmod>{last_modified_date}</lastmod>\n'
        xml_content += '  </url>\n'

    xml_content += '</urlset>\n'

    # 4. Write the XML content to the output file
    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(xml_content)
        print(f"Successfully created '{output_file}' with {len(urls)} URLs.")
    except IOError as e:
        print(f"Error writing to file '{output_file}': {e}")


if __name__ == '__main__':
    # --- IMPORTANT ---
    # Replace this with your website's actual URL
    WEBSITE_URL = 'https://www.niscalajyoti.org/'
    
    if WEBSITE_URL == 'https://www.your-website.com':
        print("Please update the WEBSITE_URL variable in this script before running.")
    else:
        create_sitemap(WEBSITE_URL)

