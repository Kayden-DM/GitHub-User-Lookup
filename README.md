This README is made with AI

🐙 Python GitHub Profile Finder
A simple command-line tool built with Python that looks up information about any GitHub user. It uses the free GitHub REST API to fetch details like username, name, bio, location, follower count, public repositories, and account creation date. It's a great beginner-to-intermediate project for learning about APIs, HTTP requests, JSON parsing, and error handling in Python.

📖 Python GitHub Profile Finder
The Python GitHub Profile Finder is a console-based application that lets users look up public profile information for any GitHub account. The user enters a username, and the program queries the free GitHub REST API to retrieve that user's public profile data.

The program displays:

Username – The GitHub login handle.

Name – The user's display name (or "Not set").

Bio – The user's profile bio (or "Not set").

Location – The user's listed location (or "Not set").

Followers – The number of followers.

Repos – The number of public repositories.

Joined – The date the account was created (formatted as YYYY-MM-DD).

If the username doesn't exist, the program prints a friendly "not found" message and lets the user try again. Network errors and non-200 HTTP status codes are handled gracefully, so the program never crashes on an API failure.

After each lookup, the user can choose to search for another profile or exit the program cleanly.

This project is ideal for anyone learning how to work with public web APIs, JSON responses, and clean, loop-based program flow in Python.

✨ Features
GitHub user lookup – Works with any valid GitHub username.

Free API, no key required – Uses the public GitHub REST API (rate-limited but key-free for basic use).

Detailed profile display – Shows username, name, bio, location, followers, repos, and join date.

Safe field access – Uses .get() with sensible defaults like 'N/A' and 'Not set'.

Bio and location fallback – Uses or 'Not set' to handle empty strings.

Friendly 404 handling – Prints "{username} not found." for missing users.

HTTP status checking – Distinguishes 404s from other API errors.

Network error handling – Catches requests.exceptions.RequestException and reports the issue.

Join date formatting – Trims the ISO timestamp to just the date with [:10].

Repeat option – Search another profile without restarting the program.

Clean exit – Break out of the loop by answering anything other than "y".

Entry-point guard – Uses if __name__ == "__main__": for clean script execution.

Modular design – Clear, single-purpose functions.

🛠️ What It Uses
Language & Library
Python 3

requests – A popular third-party library for making HTTP requests.

Install with: pip install requests

sys – Imported but not currently used (can be removed or used for future enhancements like sys.exit()).

External API
GitHub REST API — https://api.github.com/users/{username}

Free, no authentication required for basic lookups.

Subject to rate limits (60 requests/hour per IP for unauthenticated requests).

Returns a JSON object containing public profile data.

Key Functions
Function	Purpose
get_username()	Prompts the user for a GitHub username and strips whitespace.
user_data(username)	Fetches the user's JSON data from the API. Handles network errors, 404s, and other HTTP errors.
display_result(user)	Prints the user's profile information in a clean, labeled layout.
main()	Runs the full program flow — prompts, lookup, display, and repeat handling.
Key Variables
Variable	Purpose
username	The GitHub username entered by the user.
url	The full API endpoint URL, built with an f-string.
response	The HTTP response object returned by requests.get().
user	The parsed JSON data for the GitHub user.
Python Concepts Demonstrated
The requests library – Making HTTP GET requests with a timeout.

JSON parsing – Using response.json() to get structured data.

Exception handling – try/except for requests.exceptions.RequestException.

HTTP status checking – Comparing response.status_code against 404 and 200.

F-strings – Formatting the API URL.

String methods – .strip() and .lower() for clean input.

Dictionary access – Using .get() with default values for safety.

Boolean short-circuiting – Using or 'Not set' to handle empty values.

Slicing – Using [:10] to trim an ISO timestamp to just the date.

Functions – Modular, single-purpose function design.

while True loop – Keeps the program running until the user chooses to stop.

break statement – Exits the main loop cleanly.

if __name__ == "__main__": – Standard Python entry-point pattern.

Built-in Functions Used
input() – Reads user input from the console.

print() – Displays results and messages.

📥 Download
You can download the source file from this repository and save it as a .py file:

text
github_finder.py
Then install the required library:

bash
pip install requests
▶️ How to Run
Make sure you have Python 3 installed (python.org).

Install the requests library:

bash
pip install requests
Save the code as github_finder.py.

Open a terminal or command prompt in the folder containing the file.

Run:

bash
python github_finder.py
Enter any GitHub username and the program will display that user's public profile information. You can keep searching for more profiles until you choose to exit.

🐍 Made with Python
This project is written in Python 3 and uses the requests library to communicate with the public GitHub REST API. It's a clean, practical example of how to integrate a popular web service into a small command-line application.

Whether you're a beginner learning about APIs or someone who wants a quick way to look up GitHub profiles, this project is a great starting point.

💡 Possible Future Improvements
Add an authenticated mode – Use a personal access token to raise the rate limit from 60 to 5,000 requests/hour.

Show more fields – e.g., company, blog/website, Twitter handle, hireable status, or avatar URL.

List repositories – Fetch and display the user's top repos via /users/{username}/repos.

Search by name – Use the GitHub search API to find users by their display name.

Add colors – Use colorama or ANSI codes for a nicer terminal look.

Handle rate limiting – Detect 403 responses with X-RateLimit-Remaining: 0 and inform the user.

Use sys.exit() – The sys module is imported but unused; add a clean exit path using it.

Save results to a file – Log lookups to a CSV or JSON file.

Add a menu – Let users choose between profile lookup, repo lookup, and follower lookup.

Build a Tkinter GUI version for a graphical interface.

📄 License
This project is free to use, modify, and distribute for personal or educational purposes.
