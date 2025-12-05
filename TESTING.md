# Testing Guide 🧪

Complete testing checklist before GitHub submission.

## Pre-Testing Setup

1. **Install dependencies:**
   ```bash
   pip install google-generativeai
   ```

2. **Set environment variables** (see QUICKSTART.md)

3. **Prepare test inbox:**
   - Have at least 3-5 unread emails
   - Mix of different types (work, personal, newsletters)
   - Emails from the last 24 hours

## Test Cases

### Test 1: Dry Run (Connection Test)
**Purpose:** Verify IMAP connection works

```bash
python main.py --dry-run
```

**Expected Output:**
- "Found X unread emails"
- Email preview with sender, subject, body
- No summary generated
- No API call made

**Pass Criteria:**
- ✓ Connects to IMAP server
- ✓ Authenticates successfully
- ✓ Fetches unread emails
- ✓ Displays email count

### Test 2: Preview Mode
**Purpose:** Verify email formatting

```bash
python main.py --preview
```

**Expected Output:**
- Email list with formatting
- Sender, subject, and preview text
- Summary generated after preview

**Pass Criteria:**
- ✓ Emails formatted correctly
- ✓ Text is readable
- ✓ No encoding errors
- ✓ Summary still generates

### Test 3: Basic Summary Generation
**Purpose:** End-to-end test

```bash
python main.py
```

**Expected Output:**
- "Fetching unread emails..."
- "Found X unread emails"
- "Generating summary with Gemini AI..."
- Summary displayed in terminal
- "Summary saved to daily_summary.md"
- File created successfully

**Pass Criteria:**
- ✓ Emails fetched
- ✓ Gemini API called
- ✓ Summary generated
- ✓ File saved
- ✓ Markdown formatted correctly

### Test 4: Multi-Day Fetch
**Purpose:** Test date filtering

```bash
python main.py --days 3
```

**Expected Output:**
- More emails fetched (if available)
- Summary includes older emails

**Pass Criteria:**
- ✓ Fetches emails from specified days
- ✓ Date filtering works correctly

### Test 5: Custom Output File
**Purpose:** Test file naming

```bash
python main.py --output test_summary.md
```

**Expected Output:**
- File saved as `test_summary.md`

**Pass Criteria:**
- ✓ Custom filename used
- ✓ File created in correct location

### Test 6: CLI Arguments
**Purpose:** Test argument passing

```bash
python main.py --email test@gmail.com --password testpass --api-key testkey --days 2
```

**Expected Output:**
- Uses provided credentials instead of env vars

**Pass Criteria:**
- ✓ Arguments override environment variables
- ✓ All parameters accepted

### Test 7: Error Handling - No Credentials
**Purpose:** Test error messages

```bash
# Clear environment variables first
python main.py
```

**Expected Output:**
- "Error: Email credentials not provided"
- Helpful message about setting env vars

**Pass Criteria:**
- ✓ Graceful error handling
- ✓ Clear error message
- ✓ No crash

### Test 8: Error Handling - No Unread Emails
**Purpose:** Test empty inbox scenario

```bash
# Mark all emails as read first
python main.py
```

**Expected Output:**
- "No unread emails found. Nothing to summarize."

**Pass Criteria:**
- ✓ Handles empty result gracefully
- ✓ No API call made
- ✓ Clear message to user

### Test 9: Summary Quality Check
**Purpose:** Verify AI output quality

**Manual Check:**
1. Read generated `daily_summary.md`
2. Compare with actual emails

**Pass Criteria:**
- ✓ Summary is accurate
- ✓ Key points captured
- ✓ Organized and readable
- ✓ No hallucinations
- ✓ Markdown formatted

### Test 10: File Content Verification
**Purpose:** Check output file structure

```bash
type daily_summary.md
```

**Expected Content:**
- Title: "# Daily Email Summary"
- Timestamp
- Separator lines
- Summary content
- Footer: "Powered by Gemini API"

**Pass Criteria:**
- ✓ Proper markdown structure
- ✓ Timestamp present
- ✓ Content readable
- ✓ UTF-8 encoding

## Performance Tests

### Test 11: Large Email Volume
**Purpose:** Test with many emails

**Setup:** Have 20+ unread emails

```bash
python main.py
```

**Pass Criteria:**
- ✓ Handles large volume
- ✓ Completes in reasonable time (<30s)
- ✓ No memory issues
- ✓ Summary still coherent

### Test 12: Long Email Content
**Purpose:** Test with lengthy emails

**Setup:** Have emails with long bodies

**Pass Criteria:**
- ✓ Truncates appropriately (500 chars)
- ✓ No API token limit errors
- ✓ Summary still useful

## Security Tests

### Test 13: Credential Security
**Purpose:** Verify no credential leakage

**Check:**
- Review terminal output
- Check generated files
- Verify no passwords in logs

**Pass Criteria:**
- ✓ No passwords displayed
- ✓ No API keys in output
- ✓ Credentials not in files

## Cross-Platform Tests (if applicable)

### Test 14: Windows
```cmd
python main.py
```

### Test 15: Linux/Mac
```bash
python main.py
```

**Pass Criteria:**
- ✓ Works on target platform
- ✓ File paths correct
- ✓ Encoding handled properly

## Final Checklist

Before GitHub submission:

- [ ] All 15 tests passed
- [ ] No errors in terminal
- [ ] Summary quality is good
- [ ] Files created correctly
- [ ] README instructions accurate
- [ ] Requirements.txt complete
- [ ] .gitignore configured
- [ ] Demo recording created
- [ ] Code is clean and commented
- [ ] No hardcoded credentials

## Troubleshooting Common Issues

**Issue:** "Authentication failed"
- **Fix:** Use app password, not regular password

**Issue:** "Module not found"
- **Fix:** `pip install google-generativeai`

**Issue:** "API quota exceeded"
- **Fix:** Wait or use different API key

**Issue:** "No emails found"
- **Fix:** Check date range, mark emails unread

**Issue:** "Encoding errors"
- **Fix:** Already handled with UTF-8 encoding

## Test Report Template

```
Date: ___________
Tester: ___________

Test Results:
- Test 1 (Dry Run): PASS / FAIL
- Test 2 (Preview): PASS / FAIL
- Test 3 (Basic): PASS / FAIL
- Test 4 (Multi-day): PASS / FAIL
- Test 5 (Custom Output): PASS / FAIL
- Test 6 (CLI Args): PASS / FAIL
- Test 7 (No Creds): PASS / FAIL
- Test 8 (No Emails): PASS / FAIL
- Test 9 (Quality): PASS / FAIL
- Test 10 (File Content): PASS / FAIL

Overall: PASS / FAIL

Notes:
___________
```

Happy testing! 🎯
