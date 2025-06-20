from pdfminer.high_level import extract_text
import io

def parse_resume(file_bytes):
    try:
        return extract_text(io.BytesIO(file_bytes))[:3000]
    except Exception as e:
        return f"Error parsing resume: {str(e)}"
