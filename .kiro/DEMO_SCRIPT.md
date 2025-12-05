# Demo Recording Script 🎬

Follow this script to create a professional demo recording for GitHub.

## Pre-Recording Checklist

- [ ] Have 3-5 unread emails in your inbox
- [ ] Environment variables are set
- [ ] Terminal font size is readable (14pt+)
- [ ] Screen recording software is ready (OBS, Windows Game Bar, etc.)
- [ ] Close unnecessary windows/tabs
- [ ] Prepare a clean terminal window

## Recording Script (2-3 minutes)

### Scene 1: Introduction (15 seconds)
```
"Hi! This is the Daily Email Summarizer - a Python tool that uses AI 
to summarize your unread emails automatically."
```

**Show:** Project folder in file explorer

### Scene 2: Show Inbox (10 seconds)
```
"Let me show you my inbox with several unread emails..."
```

**Show:** Open Gmail/email client showing unread emails

### Scene 3: Dry Run Test (20 seconds)
```
"First, let's test the connection with a dry run:"
```

**Type and run:**
```bash
cd daily-email-summarizer
python main.py --dry-run
```

**Show:** Output showing "Found X unread emails" and email previews

### Scene 4: Preview Mode (20 seconds)
```
"We can preview the emails before summarizing:"
```

**Type and run:**
```bash
python main.py --preview
```

**Show:** Formatted email list with senders and subjects

### Scene 5: Generate Summary (30 seconds)
```
"Now let's generate the AI summary using Gemini:"
```

**Type and run:**
```bash
python main.py
```

**Show:** 
- "Generating summary with Gemini AI..." message
- Summary output in terminal
- "Summary saved to daily_summary.md" confirmation

### Scene 6: View Summary File (30 seconds)
```
"Let's check the generated summary file:"
```

**Type and run:**
```bash
type daily_summary.md
```
Or open in text editor

**Show:** 
- Markdown formatted summary
- Timestamp
- Organized key points
- Action items

### Scene 7: Show Code Structure (20 seconds)
```
"The project has a clean structure with separate modules:"
```

**Show:** 
- Quick `dir` or `ls` of project files
- Briefly open `main.py` in editor to show clean code

### Scene 8: Closing (15 seconds)
```
"That's it! Check out the README for setup instructions, 
scheduling options, and more features. Star the repo if you find it useful!"
```

**Show:** README.md in browser or editor

## Recording Tips

1. **Audio**: Use a decent microphone or clear system audio
2. **Pace**: Speak clearly and not too fast
3. **Cursor**: Use a cursor highlighter if available
4. **Edits**: Don't worry about perfection - authentic is better
5. **Length**: Keep it under 3 minutes
6. **Format**: Export as .webm or .mp4 (webm preferred for GitHub)

## Post-Recording

1. Review the recording
2. Trim any dead space at start/end
3. Export as `demo-recording.webm`
4. Place in `.kiro/` folder
5. Test playback to ensure quality

## Alternative: Silent Demo

If you prefer not to record audio:

1. Use text overlays to explain each step
2. Slow down actions so viewers can follow
3. Add captions in video editor
4. Use smooth transitions between scenes

## File Size Tips

- Target 1080p resolution
- Use 30fps (not 60fps)
- Compress if over 10MB
- Consider using GitHub LFS for large files

Good luck with your recording! 🎥
