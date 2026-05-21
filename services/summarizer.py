from transformers import pipeline

class SummarizerService:
    def __init__(self):
        # Using facebook/bart-large-cnn as requested. 
        # Note: This will download ~1.6GB on first run.
        print("Initializing summarizer model... (This may take a while on first run)")
        self.summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

    def summarize(self, text):
        if not text or text == "No description available.":
            return "No summary available."

        try:
            # BART has a max input length, typically 1024 tokens.
            # We'll truncate if necessary, though descriptions are usually shorter.
            summary = self.summarizer(text, max_length=130, min_length=30, do_sample=False)
            return summary[0]['summary_text']
        except Exception as e:
            return f"Summarization failed: {str(e)}"
