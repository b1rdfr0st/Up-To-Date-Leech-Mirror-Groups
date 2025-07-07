# Up-To-Date Leech Mirror Groups

Last updated: 2025-07-07 01:56:57 UTC

- https://t.me/MrUnknown114
- https://t.me/Opleech
- https://t.me/powerleech
- https://t.me/thoursbridi
- https://t.me/Luna073x
- https://t.me/KCxTG
- https://t.me/PrimeXLeech
- https://t.me/WZML_X
- https://t.me/botdownloadall
- https://t.me/atomicXgroup
- https://t.me/CyberPunkGrp
- https://t.me/ScienceEduAdmin
- https://t.me/ACE_ML
- https://t.me/Siva_Soft
- https://t.me/CloudxLeech
- https://t.me/alone_rio

---

This repository automatically collects and updates a list of unique leech mirror group links from [graph.org](https://graph.org) every day at midnight (00:00 UTC). The script fetches all available pages for the previous day's date (to ensure all content is fully posted and available), extracts unique author links, and updates the [`unique_leech_mirror_links.txt`](unique_leech_mirror_links.txt) file in real time. The process is fully automated using GitHub Actions.

## Features

- **Automated Daily Updates:** Runs every day at 00:00 UTC via GitHub Actions.
- **Previous Day Data:** Fetches data from the previous day to ensure complete content availability and avoid missing any late posts.
- **Fast & Efficient:** Uses asynchronous requests for rapid data collection.
- **Real-Time Writing:** New unique links are appended to the output file as soon as they are found.
- **Persistent Storage:** All unique links are stored in [`unique_leech_mirror_links.txt`](unique_leech_mirror_links.txt) and updated with each run.
- **Open Source:** Licensed under GPLv3.

## How It Works

1. The script fetches pages from URLs like:  
   `https://graph.org/MediaInfo-X-MM-DD`,  
   `https://graph.org/MediaInfo-X-MM-DD-2`,  
   `https://graph.org/MediaInfo-X-MM-DD-3`, ...  
   where `MM-DD` is the current month and day.
2. It stops when a page returns a 404 error.
3. All unique `<a rel="author" href="...">` links are extracted and saved to [`unique_leech_mirror_links.txt`](unique_leech_mirror_links.txt).
4. The script is scheduled to run daily via GitHub Actions, ensuring the list is always up to date.
5. Both the README and `unique_leech_mirror_links.txt` are automatically committed and pushed to the repository after each update.

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

The repository includes a workflow that runs the script every day at 00:00 UTC and commits any changes to the repository.  
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

**Repo GitHub:** [github/fr0stb1rd/Up-To-Date Leech Mirror Groups](https://github.com/b1rdfr0st/Up-To-Date-Leech-Mirror-Groups)

**Repo GitLab:** [gitlab/fr0stb1rd/Up-To-Date Leech Mirror Groups](https://gitlab.com/fr0stb1rd/up-to-date-leech-mirror-groups)

**Blog Post:**  [fr0stb1rd.gitlab.io](https://fr0stb1rd.gitlab.io/posts/up-to-date-leech-mirror-groups-automatic-telegram-group-link-collector/)

**License:** GPL-3.0

**SPDX-License-Identifier:** GPL-3.0
