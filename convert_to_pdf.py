import asyncio
from pyppeteer import launch
import os

async def convert_notebook_to_pdf():
    browser = await launch()
    page = await browser.newPage()

    # Get the absolute path and convert to file:// URL
    html_path = os.path.abspath('levenshtein.html')
    file_url = f'file://{html_path}'
    await page.goto(file_url, {'waitUntil': 'networkidle0'})

    await page.pdf({
        'path': 'notebook.pdf',
        'format': 'A4',
        'printBackground': True,
        'margin': {
            'top': '1cm',
            'right': '1cm',
            'bottom': '1cm',
            'left': '1cm',
        }
    })

    await browser.close()

asyncio.get_event_loop().run_until_complete(convert_notebook_to_pdf())

