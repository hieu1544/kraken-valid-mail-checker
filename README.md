### README

---

# Kraken Valid Email Checker Bot

## Overview

The **Kraken Valid Email Checker Bot** is a Python script designed to verify if email addresses are registered on the Kraken platform. By sending requests to Kraken's sign-up endpoint, the script can determine if an email is already associated with an account. This tool is valuable for tracking which emails are valid on Kraken, and it offers color-coded console output for easy readability.

### Features

- **Automated Email Verification**: Checks a list of email addresses and identifies if they are registered with Kraken.
- **Color-Coded Console Output**: Uses `colorama` to distinguish between valid (`Hit`) and invalid (`Invalid`) emails.
- **Thread Mode**: Placeholder for enabling multi-threading to speed up the process.
- **Save Results to File**: Saves all valid emails to `Kraken_Valid_Emails.txt` for easy reference.
- **Realistic User-Agent**: Uses a realistic browser user-agent to simulate real requests.

### Requirements

- **Python 3.x**
- **Libraries**:
  - `requests`: For HTTP requests.
  - `colorama`: For colored console output.

Install required libraries:

```bash
pip install requests colorama
```

### Usage

1. **Prepare Email List**:
   - Add the emails you want to check to a text file named `Emails.txt`, located in a `Files` folder within the same directory as the script.

2. **Run the Script**:
   - Execute the script:
     ```bash
     py kraken_email_checker.py
     ```

3. **Enable Threading**:
   - When prompted, enter `y` to enable threading (for faster execution) or `n` to process emails one at a time.

4. **View Results**:
   - The script will display each email’s status in a color-coded format. Valid emails (associated with an account) will appear as `Hit`, while unregistered emails will appear as `Invalid`.

5. **Save Results**:
   - After the scan, a summary displays the total number of valid emails. These results are saved to `Kraken_Valid_Emails.txt`.

### Example Output

```plaintext
$ [Credits] * Kraken Checker by Capybara
$ [Discord Server] * https://discord.gg/YourDiscordLink
$ [Mode (v.1)] * Kraken Account Email Checker

% [Enable Threads (y/n)] ..> y

$ [Scanning] * 100 Emails

$ [Hit] * example1@example.com
$ [Invalid] * example2@example.com
...

$ [Total Hits] * 25
Results saved to Kraken_Valid_Emails.txt
```

### Important Notes

- **Ethical Use**: This script is designed for personal and educational use. Ensure you have permission to verify these email addresses.
- **Realistic Request Headers**: Uses a User-Agent string to simulate requests from a real browser, reducing the chance of being flagged by Kraken.
- **File Handling**: The `Emails.txt` file should be placed in the `Files` directory, and valid emails will be saved in `Kraken_Valid_Emails.txt`.

### Future Enhancements

- **Threading Support**: Add multi-threading for faster email processing.
- **Proxy Support**: Integrate proxies to avoid request limits or IP bans.
- **Detailed Error Handling**: Log detailed errors for failed requests.
- **Configurable Output**: Allow users to specify the output file name or path.

---

This script provides a straightforward way to check email validity on Kraken, with customization options for advanced users. Let me know if you need further help or additional features!print('uwbodi')