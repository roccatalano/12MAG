import sys, asyncio
from playwright.async_api import async_playwright
async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch()
        pg = await b.new_page()
        for src, dst in zip(sys.argv[1::2], sys.argv[2::2]):
            await pg.goto('file://' + src); await pg.wait_for_timeout(500)
            await pg.pdf(path=dst, format='A4', print_background=True, prefer_css_page_size=True)
        await b.close()
asyncio.run(main())
