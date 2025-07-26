#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: https://fr0stb1rd.gitlab.io/
# License: GPL-3.0
# SPDX-License-Identifier: GPL-3.0

import asyncio
import aiohttp
import re
import sys
import os
from datetime import datetime,timedelta

AUTHOR_LINK_REGEX = re.compile(r'<a\s+rel="author"\s+href="([^"]+)"')
CONCURRENT_REQUESTS = 10
OUTPUT_FILE = "unique_leech_mirror_links.txt"
MAX_PAGES = 0  # Limitless if 0

def get_date_str():
    if len(sys.argv) > 1:
        return sys.argv[1]
    else:
        yesterday = datetime.now() - timedelta(days=1)
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
    
    return unique_links

async def send_telegram_notification(links):
    """Send scraped links to Telegram channel with double line breaks between each link"""
    bot_token = os.environ.get('TELEGRAM_BOT_TOKEN')
    chat_id = os.environ.get('TELEGRAM_CHAT_ID') 
    
    if not bot_token or not chat_id:
        print("⚠️  Telegram credentials not found in environment variables")
        return
    
    if not links:
        print("ℹ️  No links to send to Telegram")
        return

    # Create message with double line breaks between links
    message = f"🔄 <b>Up-To-Date Leech Mirror Groups | {(datetime.now() - timedelta(days=1)).strftime("%d-%m-%Y")}</b>\n"
    
    # Start quoted block for all links
    message += "<blockquote>"
    for link in links:
        message += f"🔗 {link}\n"  # Links with line breaks
    message = message.rstrip()
    message += "</blockquote>\n"
    
    # Add footer with embedded links
    message += "✨ <b>fr0stb1rd / Up-To-Date-Leech-Mirror-Groups</b>\n"
    message += "📱 <a href='https://t.me/Up_To_Date_Leech_Mirror_Groups'>Channel</a> | "
    message += "🐙 <a href='https://github.com/b1rdfr0st/Up-To-Date-Leech-Mirror-Groups'>See in Web</a> | "
    message += "💻 <a href='https://gitlab.com/fr0stb1rd/up-to-date-leech-mirror-groups'>Source Code</a>"
    

    url = f'https://api.telegram.org/bot{bot_token}/sendMessage'
    data = {
        'chat_id': chat_id,
        'text': message,
        'parse_mode': 'HTML',
        'disable_web_page_preview': True
    }
    
    try:
        async with aiohttp.ClientSession() as session:
            async with session.post(url, json=data) as response:
                if response.status == 200:
                    result = await response.json()
                    if result.get('ok'):
                        print('✅ Message sent successfully to Telegram')
                    else:
                        print(f'❌ Telegram API error: {result}')
                else:
                    print(f'❌ HTTP error: {response.status}')
                    error_text = await response.text()
                    print(f'Error details: {error_text}')
    except Exception as e:
        print(f'❌ Error sending message to Telegram: {e}')

def main():
    with open(OUTPUT_FILE, "w", encoding="utf-8") as file:  # Changed from "a" to "w" to start fresh
        unique_links = asyncio.run(async_main(file))
        
        # Send notification to Telegram if credentials are available
        asyncio.run(send_telegram_notification(unique_links))

if __name__ == "__main__":
    main()
