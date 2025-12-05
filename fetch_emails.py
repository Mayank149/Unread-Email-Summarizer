import imaplib
import email
from email.header import decode_header
from datetime import datetime, timedelta
import re

def clean_text(text):
    """Clean and decode email text"""
    if isinstance(text, bytes):
        text = text.decode('utf-8', errors='ignore')
    return text.strip()

def fetch_unread_emails(email_address, password, imap_server="imap.gmail.com", days=1):
    """
    Fetch unread emails from the last N days
    
    Args:
        email_address: Email account to connect to
        password: App password for the email account
        imap_server: IMAP server address (default: Gmail)
        days: Number of days to look back (default: 1)
    
    Returns:
        List of email dictionaries with sender, subject, and body
    """
    emails = []
    
    try:
        # Connect to IMAP server
        mail = imaplib.IMAP4_SSL(imap_server)
        mail.login(email_address, password)
        mail.select("inbox")
        
        # Calculate date for filtering
        since_date = (datetime.now() - timedelta(days=days)).strftime("%d-%b-%Y")
        
        # Search for unread emails
        status, messages = mail.search(None, f'(UNSEEN SINCE {since_date})')
        
        if status != "OK":
            print("No unread emails found")
            return emails
        
        email_ids = messages[0].split()
        print(f"Found {len(email_ids)} unread emails")
        
        for email_id in email_ids:
            # Fetch email
            status, msg_data = mail.fetch(email_id, "(RFC822)")
            
            if status != "OK":
                continue
            
            # Parse email
            msg = email.message_from_bytes(msg_data[0][1])
            
            # Decode subject
            subject = decode_header(msg["Subject"])[0][0]
            if isinstance(subject, bytes):
                subject = subject.decode()
            
            # Get sender
            sender = msg.get("From")
            
            # Get email body
            body = ""
            if msg.is_multipart():
                for part in msg.walk():
                    content_type = part.get_content_type()
                    if content_type == "text/plain":
                        try:
                            body = part.get_payload(decode=True).decode('utf-8', errors='ignore')
                            break
                        except:
                            continue
            else:
                try:
                    body = msg.get_payload(decode=True).decode('utf-8', errors='ignore')
                except:
                    body = ""
            
            # Extract first few lines of body (limit to 500 chars)
            body_preview = body[:500] if body else "No content"
            
            emails.append({
                "sender": sender,
                "subject": subject,
                "body": body_preview
            })
        
        mail.close()
        mail.logout()
        
    except Exception as e:
        print(f"Error fetching emails: {e}")
        return []
    
    return emails

def format_emails_for_summary(emails):
    """Format emails into a readable text block for summarization"""
    if not emails:
        return "No unread emails found."
    
    formatted = []
    for i, email_data in enumerate(emails, 1):
        formatted.append(f"Email {i}:")
        formatted.append(f"From: {email_data['sender']}")
        formatted.append(f"Subject: {email_data['subject']}")
        formatted.append(f"Preview: {email_data['body'][:200]}...")
        formatted.append("-" * 50)
    
    return "\n".join(formatted)
