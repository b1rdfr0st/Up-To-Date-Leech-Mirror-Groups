# Up-To-Date Leech Mirror Groups

Last updated: 2025-12-18 01:49:29 UTC

- https://t.me/WZML_X
- https://telegram.me/PlaceholderDip
- https://t.me/Anime_Sensei_Network
- https://t.me/SpaceXleech4GB
- https://t.me/MarvelCloud
- https://t.me/thugsmirror
- https://t.me/AMCDEV
- https://t.me/botdownloadall
- https://t.me/AKImaxCloud
- https://t.me/GautamS_Mirror
- https://t.me/JUPITERxTG
- https://t.me/MarinKitagawaCosplayer
- https://t.me/Team_HDT
- https://t.me/chewmo
- https://t.me/ReLeech
- https://t.me/telegram
- https://t.me/WhitE_DeviL099
- https://t.me/srilinks4k_In
- https://t.me/HeyHeartBeat
- https://t.me/KCxTG
- https://t.me/
- https://mjwebhacks.com/
- https://t.me/KristyXLeech
- https://t.me/YumikooOfficial
- https://telegram.me/TamilUpdatesOfficial
- https://t.me/nh_177013
- https://t.me/White_DeviL099
- https://t.me/satyamisme
- https://t.me/sachin_769
- https://t.me/Shotalover2
- https://t.me/itsniloybhowmick
- https://t.me/MrUnknown114
- https://github.com/imsay3m
- https://nohello.net/
- https://t.me/BasharSYR
- https://t.me/Mookhyang16
- https://t.me/Owner_of_qtmve
- https://t.me/kavirunethsara
- https://t.me/Mahsoommjm

---

This repository automatically collects and updates a list of unique leech mirror group links from [graph.org](https://graph.org) every day at midnight (00:00 UTC). The script fetches all available pages for the previous day's date (to ensure all content is fully posted and available), extracts unique author links, and updates the [`unique_leech_mirror_links.txt`](unique_leech_mirror_links.txt) file in real time. The process is fully automated using GitHub Actions.

## Features

- **Automated Daily Updates:** Runs every day at 00:00 UTC via GitHub Actions.
- **Previous Day Data:** Fetches data from the previous day to ensure complete content availability and avoid missing any late posts.
- **Fast & Efficient:** Uses asynchronous requests for rapid data collection.
- **Real-Time Writing:** New unique links are appended to the output file as soon as they are found.
- **Persistent Storage:** All unique links are stored in [`unique_leech_mirror_links.txt`](unique_leech_mirror_links.txt) and updated with each run.
- **Telegram Notifications:** Automatically sends daily updates to Telegram channel with formatted links and project information.
- **Open Source:** Licensed under GPLv3.

## How It Works

1. The script fetches pages from URLs like:  
   `https://graph.org/MediaInfo-X-MM-DD`,  
   `https://graph.org/MediaInfo-X-MM-DD-2`,  
   `https://graph.org/MediaInfo-X-MM-DD-3`, ...  
   where `MM-DD` is the current month and day.
2. It stops when a page returns a 404 error.
3. All unique `<a rel="author" href="...">` links are extracted and saved to [`unique_leech_mirror_links.txt`](unique_leech_mirror_links.txt).
4. **Telegram Notification:** The script sends a formatted message to the configured Telegram channel with all collected links, project information, and relevant links.
5. The script is scheduled to run daily via GitHub Actions, ensuring the list is always up to date.
6. Both the README and `unique_leech_mirror_links.txt` are automatically committed and pushed to the repository after each update.

## Usage

You can run the script manually if you wish:

```bash
# Install required package
pip install aiohttp

# Run the script
python scraper.py
```

The script will:
- Use today's date automatically
- Check up to all pages by default (configurable via `MAX_PAGES` in the script)
- Save results to `unique_leech_mirror_links.txt`

## GitHub Actions

The repository includes a workflow that runs the script every day at 00:00 UTC and commits any changes to the repository. The workflow also sends Telegram notifications with the collected links.

### Telegram Setup

To enable Telegram notifications, you need to set up the following GitHub Secrets:

1. **TELEGRAM_BOT_TOKEN**: Your Telegram bot token (get it from [@BotFather](https://t.me/botfather))
2. **TELEGRAM_CHAT_ID**: Your Telegram channel/chat ID where notifications will be sent

The script will automatically send formatted messages with:
- Daily update timestamp
- All collected leech mirror group links (in quoted format)
- Project information and relevant links

No manual intervention is required.

## Contributing

Contributions, issues, and feature requests are welcome!  
Feel free to open an issue or submit a pull request.

## License

This project is licensed under the [GNU General Public License v3.0](LICENSE).

## Disclaimer
This repository is for educational and archival purposes only. Please respect the terms of service of any third-party sites

## About

**Author:** [fr0stb1rd](https://fr0stb1rd.gitlab.io/) 

**Telegram Channel:** [@Up_To_Date_Leech_Mirror_Groups](https://t.me/Up_To_Date_Leech_Mirror_Groups)

**Repo GitHub:** [github/fr0stb1rd/Up-To-Date Leech Mirror Groups](https://github.com/b1rdfr0st/Up-To-Date-Leech-Mirror-Groups)

**Repo GitLab:** [gitlab/fr0stb1rd/Up-To-Date Leech Mirror Groups](https://gitlab.com/fr0stb1rd/up-to-date-leech-mirror-groups)

**Blog Post:**  [fr0stb1rd.gitlab.io](https://fr0stb1rd.gitlab.io/posts/up-to-date-leech-mirror-groups-automatic-telegram-group-link-collector/)

**License:** GPL-3.0

**SPDX-License-Identifier:** GPL-3.0
