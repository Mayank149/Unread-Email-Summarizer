import google.generativeai as genai

def configure_gemini(api_key):
    """Configure Gemini API with the provided key"""
    genai.configure(api_key=api_key)

def generate_summary(email_text, api_key):
    """
    Generate a summary of emails using Gemini API
    
    Args:
        email_text: Combined text of all emails
        api_key: Gemini API key
    
    Returns:
        Summary string
    """
    try:
        # Configure API
        configure_gemini(api_key)
        
        # Create model
        model = genai.GenerativeModel('models/gemini-2.5-flash')
        
        # Create prompt
        prompt = f"""Summarize these emails into a short daily brief. 
        Focus on key points, action items, and important information.
        Keep it concise and organized by category if possible.
        Do not include placeholder text like [Date] - just provide the summary content directly.
        
        Emails:
        {email_text}
        
        Please provide a clear, actionable summary."""
        
        # Generate summary
        response = model.generate_content(prompt)
        
        return response.text
    
    except Exception as e:
        return f"Error generating summary: {e}"

def generate_summary_with_custom_prompt(email_text, api_key, custom_prompt=None):
    """
    Generate a summary with a custom prompt
    
    Args:
        email_text: Combined text of all emails
        api_key: Gemini API key
        custom_prompt: Optional custom prompt template
    
    Returns:
        Summary string
    """
    try:
        configure_gemini(api_key)
        model = genai.GenerativeModel('models/gemini-2.5-flash')
        
        if custom_prompt:
            prompt = f"{custom_prompt}\n\nEmails:\n{email_text}"
        else:
            prompt = f"Summarize these emails into a short daily brief:\n\n{email_text}"
        
        response = model.generate_content(prompt)
        return response.text
    
    except Exception as e:
        return f"Error generating summary: {e}"
