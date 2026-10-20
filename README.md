GitHub Profile Finder
A command-line Python program that fetches and displays public GitHub user profile details via the GitHub REST API.

Concepts Used
requests Library — queries https://api.github.com/users/{username} for profile data.

HTTP Status Handling — checks 404 for missing users and non-200 codes for other API errors.

Dictionary .get() with Fallbacks — safely reads JSON fields, using or 'Not set' for empty values.

Features
Profile Lookup — retrieves username, name, bio, location, followers, and repo count.

Error Messaging — distinguishes network failures, not-found users, and generic API errors.

Loop-Back Searching — cleanly re-prompts to search another profile instead of recursing.

Improvements
Handle Rate Limits — unauthenticated GitHub requests are capped at 60/hour; detect 403 and mention the limit.

Validate Empty Input — an empty username hits /users/ and returns a confusing result; reject blank input early.

Fix created_at Slicing — if created_at is missing, [:10] on the default 'N/A' is fine, but slicing a real missing key via .get before indexing would error; read once, then trim safely.

