import argparse
import os
from datetime import datetime
from fetch_emails import fetch_unread_emails, format_emails_for_summary
from summarize import generate_summary

def save_summary(summary, filename="daily_summary.md"):
    """Save summary to a markdown file"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"# Daily Email Summary\n\n")
        f.write(f"**Generated:** {timestamp}\n\n")
        f.write("---\n\n")
        f.write(summary)
        f.write("\n\n---\n")
        f.write(f"\n*Powered by Gemini API*\n")
    
    print(f"Summary saved to {filename}")

def main():
    parser = argparse.ArgumentParser(description="Daily Email Summarizer using Gemini API")
    parser.add_argument("--email", help="Email address", required=False)
    parser.add_argument("--password", help="App password", required=False)
    parser.add_argument("--api-key", help="Gemini API key", required=False)
    parser.add_argument("--days", type=int, default=1, help="Days to look back (default: 1)")
    parser.add_argument("--dry-run", action="store_true", help="Fetch emails without summarizing")
    parser.add_argument("--preview", action="store_true", help="Preview emails before summarizing")
    parser.add_argument("--output", default="daily_summary.md", help="Output file name")
    
    args = parser.parse_args()
    
    # Get credentials from environment or arguments
    email_address = args.email or os.getenv("EMAIL_ADDRESS")
    password = args.password or os.getenv("EMAIL_PASSWORD")
    api_key = args.api_key or os.getenv("GEMINI_API_KEY")
    
    if not email_address or not password:
        print("Error: Email credentials not provided")
        print("Set EMAIL_ADDRESS and EMAIL_PASSWORD environment variables or use --email and --password")
        return
    
    if not api_key and not args.dry_run:
        print("Error: Gemini API key not provided")
        print("Set GEMINI_API_KEY environment variable or use --api-key")
        return
    
    print("=" * 60)
    print("Daily Email Summarizer")
    print("=" * 60)
    print(f"Fetching unread emails from last {args.days} day(s)...\n")
    
    # Fetch emails
    emails = fetch_unread_emails(email_address, password, days=args.days)
    
    if not emails:
        print("No unread emails found. Nothing to summarize.")
        return
    
    # Format emails
    email_text = format_emails_for_summary(emails)
    
    # Preview mode
    if args.preview or args.dry_run:
        print("\n" + "=" * 60)
        print("EMAIL PREVIEW")
        print("=" * 60)
        print(email_text)
        print("=" * 60)
        
        if args.dry_run:
            print("\nDry run complete. No summary generated.")
            return
    
    # Generate summary
    print("\nGenerating summary with Gemini AI...\n")
    summary = generate_summary(email_text, api_key)
    
    # Display summary
    print("=" * 60)
    print("SUMMARY")
    print("=" * 60)
    print(summary)
    print("=" * 60)
    
    # Save summary
    save_summary(summary, args.output)
    print(f"\n✓ Done! Check {args.output} for the full summary.")

if __name__ == "__main__":
    main()
