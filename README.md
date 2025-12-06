# Daily Email Summarizer 📧✨

## Problem Statement

Reading through dozens of unread emails every day is boring, time-consuming, and mentally draining. Important information gets buried in promotional content, newsletters, and routine updates. What if you could get a concise daily brief of all your unread emails in seconds?

## Solution

This Python automation script connects to your email inbox via IMAP, fetches unread emails from the last 24 hours, and uses Google's Gemini API to generate an intelligent summary. Get the key points, action items, and important information without reading every single email.

## Features

- 📬 **IMAP Email Fetching**: Connects to any IMAP-enabled email service (Gmail, Outlook, etc.)
- 🤖 **AI-Powered Summarization**: Uses Google Gemini API for intelligent email summarization
- ⏰ **Time-Based Filtering**: Fetch emails from the last N days
- 📝 **Markdown Output**: Saves summary to a clean markdown file
- 🔍 **Preview Mode**: Review emails before summarizing
- 🧪 **Dry Run**: Test IMAP connection without generating summaries
- ⚙️ **CLI Arguments**: Flexible command-line interface for customization

## Tech Stack

- **Python 3.7+**
- **IMAP** (built-in email library)
- **Google Generative AI** (Gemini API)
- **argparse** for CLI

## Project Structure

```
daily-email-summarizer/
├── fetch_emails.py      # IMAP email fetching logic
├── summarize.py         # Gemini API integration
├── main.py              # Main orchestration script
├── requirements.txt     # Python dependencies
├── README.md            # This file
├── daily_summary.md     # Generated summary (after running)
└── .kiro/               # Kiro demo and session files
    ├── daily-email-summarizer demo.mp4
    └── session.json
```

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/daily-email-summarizer.git
cd daily-email-summarizer
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

Or install directly:

```bash
pip install google-generativeai
```

### 3. Get Your Gemini API Key

1. Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Create a new API key
3. Copy the key for use in the script

### 4. Configure Email Access

For **Gmail**, you need to:
1. Enable 2-Factor Authentication
2. Generate an [App Password](https://myaccount.google.com/apppasswords)
3. Use the app password instead of your regular password

For **other email providers**, ensure IMAP is enabled and use your regular credentials.

### 5. Set Environment Variables (Recommended)

```bash
# Windows (CMD)
set EMAIL_ADDRESS=your.email@gmail.com
set EMAIL_PASSWORD=your_app_password
set GEMINI_API_KEY=your_gemini_api_key

# Windows (PowerShell)
$env:EMAIL_ADDRESS="your.email@gmail.com"
$env:EMAIL_PASSWORD="your_app_password"
$env:GEMINI_API_KEY="your_gemini_api_key"

# Linux/Mac
export EMAIL_ADDRESS=your.email@gmail.com
export EMAIL_PASSWORD=your_app_password
export GEMINI_API_KEY=your_gemini_api_key
```

## How to Run

### Basic Usage

```bash
python main.py
```

### With Command-Line Arguments

```bash
python main.py --email your.email@gmail.com --password your_app_password --api-key your_gemini_key
```

### Dry Run (Test Connection)

```bash
python main.py --dry-run
```

### Preview Emails Before Summarizing

```bash
python main.py --preview
```

### Fetch Emails from Last 3 Days

```bash
python main.py --days 3
```

### Custom Output File

```bash
python main.py --output weekly_summary.md
```

## CLI Arguments

| Argument | Description | Default |
|----------|-------------|---------|
| `--email` | Email address | From env var |
| `--password` | App password | From env var |
| `--api-key` | Gemini API key | From env var |
| `--days` | Days to look back | 1 |
| `--dry-run` | Test without summarizing | False |
| `--preview` | Preview emails first | False |
| `--output` | Output filename | daily_summary.md |

## Optional: Schedule Daily Runs

### Windows Task Scheduler

1. Open Task Scheduler
2. Create Basic Task
3. Set trigger to daily at your preferred time
4. Action: Start a program
5. Program: `python`
6. Arguments: `C:\path\to\main.py`

### Linux/Mac Cron

```bash
# Edit crontab
crontab -e

# Add daily run at 9 AM
0 9 * * * cd /path/to/daily-email-summarizer && python main.py
```

## Example Output

```markdown
# Daily Email Summary

**Generated:** 2025-12-05 15:30:00

---

**Key Highlights:**

- **Work Updates**: 3 project status emails from team members
- **Action Items**: Review PR #234, approve budget proposal by Friday
- **Newsletters**: Tech digest with AI trends, Python weekly roundup
- **Personal**: Dentist appointment confirmation for next Tuesday

**Priority Items:**
1. Respond to client inquiry about project timeline
2. Review and merge pending pull requests
3. Confirm attendance for team meeting

---

*Powered by Gemini API*
```

## GitHub Requirements

- ✅ Public repository
- ✅ Complete README with setup instructions
- ✅ Clean, documented code
- ✅ requirements.txt for dependencies
- ✅ .kiro folder with demo recording

## Blog Post Ideas

- "How I Automated My Email Inbox with AI"
- "Building a Daily Email Summarizer with Python and Gemini"
- "Stop Reading Every Email: Let AI Do It For You"
- "IMAP + Gemini API: The Perfect Email Automation Stack"

## Troubleshooting

**IMAP Connection Failed**
- Ensure IMAP is enabled in your email settings
- For Gmail, use an app password, not your regular password
- Check firewall settings

**Gemini API Error**
- Verify your API key is valid
- Check API quota limits
- Ensure you have internet connection

**No Emails Found**
- Check the date range (--days parameter)
- Verify emails are actually unread
- Try with --preview to see what's being fetched

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

## License

MIT License - feel free to use this project however you'd like!

## Author

Built By Mayank Bansal
using Kiro IDE

---

**Star this repo if you find it useful!** ⭐
