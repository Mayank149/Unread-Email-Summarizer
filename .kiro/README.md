# Kiro Demo Files

This folder contains demonstration materials for the Daily Email Summarizer project.

## Contents

- **session.json**: Project development session details and steps
- **demo-recording.webm**: Video demonstration of the script in action (to be recorded)

## Demo Recording Instructions

To create the demo recording:

1. **Prepare your inbox**: Ensure you have some unread emails
2. **Set up credentials**: Configure environment variables for email and API key
3. **Start recording**: Use screen recording software (OBS, Windows Game Bar, etc.)
4. **Show the demo**:
   - Open terminal in project directory
   - Run `python main.py --preview` to show email fetching
   - Run `python main.py` to generate summary
   - Open `daily_summary.md` to show the generated summary
   - Highlight key features and output
5. **Save recording**: Export as `demo-recording.webm` and place in this folder

## Recording Tips

- Keep it under 2-3 minutes
- Show both the terminal output and the generated summary file
- Highlight the AI-generated insights
- Demonstrate at least one CLI option (like --preview or --dry-run)
- Use clear, readable terminal font size

## Notes

This project was built using Kiro AI assistant to demonstrate:
- Python automation capabilities
- IMAP email integration
- Google Gemini API usage
- Clean project structure and documentation
- GitHub-ready repository setup
