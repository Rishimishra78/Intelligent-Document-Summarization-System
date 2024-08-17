from langchain import OpenAI
from langchain.chains import SummarizationChain
from langchain.prompts import PromptTemplate

class DocumentSummarizer:
    def _init_(self, api_key, max_length=150):
        # Initialize the OpenAI language model
        self.model = OpenAI(api_key=api_key)

        # Define a prompt template for summarization
        self.prompt_template = PromptTemplate(
            input_variables=["text"],
            template="Please summarize the following text:\n{text}"
        )

        # Create a SummarizationChain instance
        self.summarization_chain = SummarizationChain(
            model=self.model,
            prompt_template=self.prompt_template
        )

        self.max_length = max_length

    def generate_summary(self, text):
        """
        Generate a summary of the given text.
        :param text: The text to summarize.
        :return: The summarized text.
        """
        summary = self.summarization_chain.run(text)
        # Optionally truncate summary to max_length
        return summary[:self.max_length]

    def summarize_document(self, document_text, custom_length=None):
        """
        Summarize the document with an optional custom length.
        :param document_text: The text to summarize.
        :param custom_length: Custom maximum length of the summary (optional).
        :return: The summarized text.
        """
        length = custom_length if custom_length else self.max_length
        self.max_length = length
        return self.generate_summary(document_text)

def main():
    # Replace with your actual OpenAI API key
    api_key = 'your_openai_api_key'

    # Create an instance of DocumentSummarizer
    summarizer = DocumentSummarizer(api_key)

    # Example document text
    document_text = """
    Your long document text goes here. This is an example of a long text that you want to summarize.
    The summarization system should extract the key points and present a concise summary.
    """

    # Generate summary with default length
    summary = summarizer.summarize_document(document_text)
    print("Summary (default length):", summary)

    # Generate summary with custom length
    custom_length = 100
    custom_summary = summarizer.summarize_document(document_text, custom_length)
    print(f"Summary (custom length {custom_length}):", custom_summary)

if _name_ == "_main_":
    main()