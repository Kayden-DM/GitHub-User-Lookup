## GitHub Profile Finder
A command-line profile lookup tool written in Python. It uses the requests module to query the GitHub API and displays details about any public GitHub user.

## Features
Username Input — Prompts for a GitHub username, stripped of extra whitespace.

Live Lookup — Fetches user data from https://api.github.com/users/{username}.

Profile Display — Prints the username, name, bio, location, followers, public repos, and join date.

Missing Field Handling — Falls back to Not set or N/A when a field is empty.

Not Found Handling — Prints a clear message when the user doesn't exist (HTTP 404).

Error Handling — Catches network errors with requests.exceptions.RequestException and reports non-200 status codes.

Search Again — Loops back for another username if the user answers y.

## Technologies Used
| Technology | Purpose |
|---|---|
| Python | Application logic |
| `requests` | Sends HTTP requests to the GitHub API |
| GitHub API | Provides public user profile data |
| f-strings | Builds the API URL and output messages |
| `try / except` | Handles network errors |
| `response.status_code` | Checks for 404 and other HTTP errors |
| `dict.get()` | Safely reads fields with fallbacks |
| `input()` / `print()` | Console interaction |
<!-- -->
## How to Use It
Install Python 3.6 or newer from python.org and make sure it's added to your PATH.

Install the requests library by running pip install requests.

Save the code as github_finder.py.

Open a terminal in the folder containing the file.

Run python github_finder.py.

Enter a GitHub username, view the profile details, then answer y or n when asked to search again.

## Improvements
Handle rate limits — GitHub's API allows only 60 unauthenticated requests per hour, and the code treats a 403 rate-limit response as a generic API error; checking for X-RateLimit-Remaining and printing a clearer message would help.

Validate the username — an empty or whitespace-only input still triggers an API request to /users/; checking that the username isn't empty before sending would avoid a wasted request.

