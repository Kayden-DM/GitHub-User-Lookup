import requests
import sys

def get_username():
    return input("Enter GitHub username: ").strip()

def user_data(username):
    url = f"https://api.github.com/users/{username}"
    try:
        response = requests.get(url, timeout=10)
    except requests.exceptions.RequestException as e:
        print(f"Could not reach the API: {e}")
        return None

    if response.status_code == 404:
        print(f"{username} not found.")
        return None
    if response.status_code != 200:
        print(f"API error: {response.status_code}")
        return None

    return response.json()

def display_result(user):
    print("=====GitHub User Profile=====")
    print(f"Username:  {user.get('login', 'N/A')}")
    print(f"Name:      {user.get('name', 'Not set')}")
    print(f"Bio:       {user.get('bio') or 'Not set'}")
    print(f"Location:  {user.get('location') or 'Not set'}")
    print(f"Followers: {user.get('followers', 0)}")
    print(f"Repos:     {user.get('public_repos', 0)}")
    print(f"Joined:    {user.get('created_at', 'N/A')[:10]}")

def main():
    print("=====GitHub Profile Finder=====")
    while True:
        username = get_username()
        user = user_data(username)
        if user is None:
            print("Lookup failed.")
        else:
            display_result(user)

        again = input("Search another profile? (y/n): ").lower().strip()
        if again != "y":
            break

if __name__ == "__main__":
    main()