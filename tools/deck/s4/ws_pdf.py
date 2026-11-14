"""Print the 1G worksheet HTML files to A4 PDFs (Chrome). Run: python3 tools/deck/s4/ws_pdf.py [png]"""
import asyncio, sys, os
from playwright.async_api import async_playwright
ROOT=os.path.abspath(os.path.join(os.path.dirname(__file__),'..','..','..'))
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(executable_path='/usr/bin/google-chrome',args=['--no-sandbox'])
        pg=await b.new_page()
        for n in ('S4-worksheet','S4-worksheet-solutions'):
            await pg.goto(f'file://{ROOT}/lessons/{n}.html'); await pg.wait_for_timeout(500)
            await pg.pdf(path=f'{ROOT}/lessons/{n}.pdf',format='A4',prefer_css_page_size=True,print_background=True)
        await b.close()
asyncio.run(main())
