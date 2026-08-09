import re
from typing import Tuple

class PromptGuard:
    """
    Lightweight prompt injection defender and input sanitizer.
    """
    SUSPICIOUS_PATTERNS = [
        r"ignore\s+(all\s+|the\s+)?(previous|above|prior)\s+(instructions|directions|prompts|rules)",
        r"disregard\s+(all\s+|the\s+)?(previous|prior|rules|system\s+prompt|instructions)",
        r"reveal\s+(all\s+|the\s+|your\s+)?(secret\s+)?(system\s+prompt|developer\s+instructions|instructions|prompt|secret|api\s+key)",
        r"you\s+are\s+now\s+(in\s+)?(dan|unrestricted|god\s+mode|developer\s+mode)",
        r"print\s+(all\s+|the\s+|your\s+)?(initial\s+instructions|system\s+prompt|configuration)",
        r"override\s+(all\s+|the\s+)?(system\s+prompt|instructions|rules)",
        r"bypass\s+(all\s+|the\s+)?(security|guardrails|safety\s+filters)",
        r"act\s+as\s+an\s+unrestricted",
    ]

    def inspect_input(self, text: str) -> Tuple[bool, str]:
        if not text or not text.strip():
            return True, ""
            
        text_lower = text.lower()
        for pattern in self.SUSPICIOUS_PATTERNS:
            if re.search(pattern, text_lower):
                return False, f"Potential prompt injection detected matching pattern: {pattern}"
                
        return True, ""

    def sanitize(self, text: str) -> str:
        if not text:
            return ""
        # Remove null bytes and dangerous control characters
        clean = re.sub(r'[\x00-\x08\x0b\x0c\x0e-\x1f]', '', text)
        return clean.strip()
