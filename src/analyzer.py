import requests
from src.logger import setup_logger
from src.config import OLLAMA_URL, OLLAMA_MODEL, AI_TIMEOUT
from src.f5_commands import f5_knowledge_base

logger = setup_logger(__name__)

def validate_log_input(log_content: str, max_size: int = 50000) -> bool:
    """Validate user input log content"""
    if not log_content or not log_content.strip():
        logger.warning("Empty log content provided")
        return False
    if len(log_content) > max_size:
        logger.warning(f"Log content exceeds max size of {max_size}")
        return False
    return True

def analyze_with_ai(log: str, issue_type: str) -> str:
    """Attempt to analyze log using AI"""
    prompt = f"""
    You are a senior F5 L3 network engineer.
    
    Analyze the issue below:
    
    {log}
    
    Issue Type: {issue_type}
    
    Provide:
    1. Root Cause
    2. Troubleshooting steps
    3. Fix
    """
    
    try:
        response = requests.post(
            OLLAMA_URL,
            json={
                "model": OLLAMA_MODEL,
                "prompt": prompt,
                "stream": False
            },
            timeout=AI_TIMEOUT
        )
        response.raise_for_status()
        logger.info("AI analysis completed successfully")
        return response.json()["response"]
    except (requests.RequestException, TimeoutError, ConnectionError) as e:
        logger.error(f"AI service unavailable: {e}")
        return None

def get_fallback_analysis(log: str, issue_type: str) -> dict:
    """Fallback to rule-based analysis"""
    logger.info(f"Using fallback analysis for issue type: {issue_type}")
    
    if "VIP" in log.upper() or issue_type == "VIP Down":
        return {
            "analysis": f5_knowledge_base.get('VIP_DOWN', {}).get('root_cause', 'Unknown issue'),
            "troubleshooting": f5_knowledge_base.get('VIP_DOWN', {}).get('troubleshooting_steps', []),
            "command": f5_knowledge_base.get('VIP_DOWN', {}).get('commands', [])[0] if f5_knowledge_base.get('VIP_DOWN', {}).get('commands') else ""
        }
    elif "SSL" in log.upper() or issue_type == "SSL Issue":
        return {
            "analysis": f5_knowledge_base.get('SSL_ISSUE', {}).get('root_cause', 'Unknown issue'),
            "troubleshooting": f5_knowledge_base.get('SSL_ISSUE', {}).get('troubleshooting_steps', []),
            "command": f5_knowledge_base.get('SSL_ISSUE', {}).get('commands', [])[0] if f5_knowledge_base.get('SSL_ISSUE', {}).get('commands') else ""
        }
    elif "timeout" in log.lower() or issue_type == "Timeout":
        return {
            "analysis": f5_knowledge_base.get('TIMEOUT', {}).get('root_cause', 'Unknown issue'),
            "troubleshooting": f5_knowledge_base.get('TIMEOUT', {}).get('troubleshooting_steps', []),
            "command": f5_knowledge_base.get('TIMEOUT', {}).get('commands', [])[0] if f5_knowledge_base.get('TIMEOUT', {}).get('commands') else ""
        }
    else:
        logger.warning(f"Unknown issue type: {issue_type}")
        return {
            "analysis": "Unable to determine the issue. Please provide more details.",
            "troubleshooting": [],
            "command": ""
        }

def analyze_log(log: str, issue_type: str) -> dict:
    """Main analysis function - tries AI first, then falls back"""
    logger.info(f"Starting analysis for issue type: {issue_type}")
    
    # Validate input
    if not validate_log_input(log):
        logger.error("Invalid log input")
        return {"error": "Please enter or upload a valid log"}
    
    # Try AI first
    ai_result = analyze_with_ai(log, issue_type)
    if ai_result:
        return {"result": ai_result, "source": "AI"}
    
    # Fall back to rule-based analysis
    fallback_result = get_fallback_analysis(log, issue_type)
    logger.info("Fallback analysis completed")
    return {"result": fallback_result, "source": "Fallback"}