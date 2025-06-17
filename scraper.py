#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: https://fr0stb1rd.gitlab.io/
# License: GPL-3.0
# SPDX-License-Identifier: GPL-3.0


import asyncio
import aiohttp
import re
import sys
from datetime import datetime

AUTHOR_LINK_REGEX = re.compile(r'<a\s+rel="author"\s+href="([^"]+)"')
CONCURRENT_REQUESTS = 10
OUTPUT_FILE = "unique_leech_mirror_links.txt"
MAX_PAGES = 0  # Limitless if 0

def get_date_str():
    if len(sys.argv) > 1:
        return sys.argv[1]
    else:
        yesterday = datetime.now() - datetime.timedelta(days=1)
        return yesterday.strftime("%m-%d")

async def fetch(session, url):
    async with session.get(url) as resp:
        if resp.status == 404:
            return None
        return await resp.text()

async def process_page(session, base_url, idx, unique_links, file):
    if idx == 1:
        url = base_url
    else:
        url = f"{base_url}-{idx}"
    html = await fetch(session, url)
    if html is None:
        return False
    for match in AUTHOR_LINK_REGEX.findall(html):
        link = match.strip()
        if link and link not in unique_links:  # Only add non-empty, unique links
            unique_links.add(link)
            file.write(link + "\n")
            file.flush()
            print(f"Found and wrote: {link}")
    print(f"Checked: {url}")
    return True

async def async_main(file):
    date_str = get_date_str()
    base_url = f"https://graph.org/MediaInfo-X-{date_str}"
    unique_links = set()
    idx = 1
    stop = False
    async with aiohttp.ClientSession() as session:
        while not stop:
            if MAX_PAGES > 0 and idx > MAX_PAGES:
                print(f"Reached maximum page limit ({MAX_PAGES})")
                break
                
            tasks = [
                process_page(session, base_url, i, unique_links, file)
                for i in range(idx, idx + CONCURRENT_REQUESTS)
                if MAX_PAGES == 0 or i <= MAX_PAGES
            ]
            results = await asyncio.gather(*tasks)
            if not all(results):
                stop = True
            idx += CONCURRENT_REQUESTS

def main():
    with open(OUTPUT_FILE, "w", encoding="utf-8") as file:  # Changed from "a" to "w" to start fresh
        asyncio.run(async_main(file))

if __name__ == "__main__":
    main()
