
# GitHub Profile Views

This script gets you github profile views by refreshing the page every second.

## Requirements
- Python 3.x
- `selenium` library (install with `pip install selenium`)
- `colorama` library (install with `pip install colorama`)
- `webdriver-manager` library (install with `pip install webdriver-manager`)
- Google Chrome browser

## Installation & Setup
1. Clone this repository:
   ```sh
   git clone https://github.com/dk6m/github-views-bot.git
   cd github-views-bot
   ```
2. Install dependencies:
   ```sh
   pip install selenium colorama webdriver-manager
   ```
3. Run the script:
   ```sh
   python main.py
   ```
4. Enter a GitHub username when prompted.

## How It Works
- The script prompts the user for a GitHub username.
- It opens multiple browser windows and navigates to the given GitHub profile.
- The profile page is refreshed repeatedly every second.
- The script stops when interrupted by the user.

## Notes
- The number of browser instances can be adjusted by modifying the `num_browsers` variable.
- Ensure that Google Chrome and ChromeDriver are installed.

GitHub: [dk6m](https://github.com/dk6m)

