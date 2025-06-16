# Up-To-Date Leech Mirror Groups

## Latest Found Links

Last updated: 2025-06-16 22:19:57 UTC

- 
- https://t.me/WZML_X
- https://t.me/DhruvMirrorUpdates
- https://t.me/KristyXLeech
- https://t.me/JetMirror
- https://t.me/MrUnknown114
- https://t.me/srilinks4k_In
- https://t.me/djpreetXBot

---


This repository automatically collects and updates a list of unique leech mirror group links from [graph.org](https://graph.org) every day at midnight (00:00 UTC). The script fetches all available pages for the current date, extracts unique author links, and updates the [`unique_leech_mirror_links.txt`](unique_leech_mirror_links.txt) file in real time. The process is fully automated using GitHub Actions.

## Features

- **Automated Daily Updates:** Runs every day at 00:00 UTC via GitHub Actions.
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
pip install aiohttp
python link_looker.py [MM-DD]
```

- If `[MM-DD]` is omitted, today's date is used.
- Results are saved to `unique_leech_mirror_links.txt`.

## GitHub Actions

The repository includes a workflow that runs the script every day at 00:00 UTC and commits any changes to the repository.  
No manual intervention is required.

## Contributing

Contributions, issues, and feature requests are welcome!  
Feel free to open an issue or submit a pull request.

## License

This project is licensed under the [GNU General Public License v3.0](LICENSE).

---

**Disclaimer:**  
This repository is for educational and archival purposes only. Please respect the terms of service of any third-party sites

## About

**Author:** [fr0stb1rd](https://fr0stb1rd.gitlab.io/) 

**Repo:** [gitlab/fr0stb1rd/mdimg-localizer](https://gitlab.com/fr0stb1rd/mdimg-localizer)

**Blog Post:**  [fr0stb1rd.gitlab.io](https://fr0stb1rd.gitlab.io/posts/mdimg_localizer-automatic-markdown-image-localizer/)

**License:** GPL-3.0

**SPDX-License-Identifier:** GPL-3.0
