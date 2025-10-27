"""pdf_parser.py

Purpose: Parse PDF documents and extract raw text content for further processing.
Provides functionality to extract text by page, detect tables, and chunk documents.
"""

import PyPDF2
from typing import List, Dict, Optional
import os


def extract_text_by_page(pdf_path: str) -> List[Dict[str, any]]:
    """
    Extract text from a PDF file, organized by page.
    
    Args:
        pdf_path (str): Path to the PDF file to be parsed.
    
    Returns:
        List[Dict[str, any]]: A list of dictionaries, each containing:
            - 'page_num' (int): The page number (1-indexed)
            - 'text' (str): The extracted text content from that page
    
    Raises:
        FileNotFoundError: If the PDF file does not exist.
        Exception: If there's an error reading the PDF file.
    
    Example:
        >>> pages = extract_text_by_page('document.pdf')
        >>> print(pages[0]['page_num'], pages[0]['text'][:100])
    """
    # Validate file exists
    if not os.path.exists(pdf_path):
        raise FileNotFoundError(f"PDF file not found: {pdf_path}")
    
    pages_data = []
    
    try:
        # Open the PDF file in binary read mode
        with open(pdf_path, 'rb') as pdf_file:
            # Create a PDF reader object
            pdf_reader = PyPDF2.PdfReader(pdf_file)
            
            # Get total number of pages
            num_pages = len(pdf_reader.pages)
            
            # Iterate through each page
            for page_num in range(num_pages):
                # Extract the page object
                page = pdf_reader.pages[page_num]
                
                # Extract text from the page
                text = page.extract_text()
                
                # Store page data with 1-indexed page number
                pages_data.append({
                    'page_num': page_num + 1,  # Convert to 1-indexed
                    'text': text
                })
        
        return pages_data
    
    except Exception as e:
        raise Exception(f"Error reading PDF file {pdf_path}: {str(e)}")


def extract_tables(pdf_path: str, page_num: Optional[int] = None) -> List[Dict[str, any]]:
    """
    Extract tables from a PDF file.
    
    This function provides a header for advanced table extraction functionality.
    Implementation is left for advanced parsing libraries (e.g., tabula-py, camelot).
    
    Args:
        pdf_path (str): Path to the PDF file to be parsed.
        page_num (Optional[int]): Specific page number to extract tables from.
                                   If None, extract from all pages.
    
    Returns:
        List[Dict[str, any]]: A list of dictionaries, each containing:
            - 'page_num' (int): The page number where the table was found
            - 'table_data' (any): The extracted table data (format TBD)
            - 'position' (dict): Table position metadata (x, y, width, height)
    
    TODO:
        - Implement using tabula-py or camelot for advanced table detection
        - Add support for different table formats (CSV, DataFrame, etc.)
        - Handle merged cells and complex table structures
        - Add confidence scores for table detection
    
    Example:
        >>> tables = extract_tables('document.pdf', page_num=1)
        >>> print(f"Found {len(tables)} tables on page 1")
    """
    # Placeholder implementation
    # TODO: Implement advanced table extraction logic
    print(f"Table extraction for {pdf_path} is not yet implemented.")
    print("Future implementation will use tabula-py or camelot.")
    return []


def chunk_document_by_pages(pdf_path: str) -> List[Dict[str, any]]:
    """
    Chunk a PDF document by pages for processing.
    
    This function is a convenience wrapper around extract_text_by_page that
    provides semantic chunking at the page level. Each page is treated as
    a discrete chunk of information.
    
    Args:
        pdf_path (str): Path to the PDF file to be chunked.
    
    Returns:
        List[Dict[str, any]]: A list of page chunks, each containing:
            - 'page_num' (int): The page number (1-indexed)
            - 'text' (str): The text content from that page
    
    Raises:
        FileNotFoundError: If the PDF file does not exist.
        Exception: If there's an error processing the PDF file.
    
    Example:
        >>> chunks = chunk_document_by_pages('document.pdf')
        >>> for chunk in chunks:
        ...     print(f"Page {chunk['page_num']}: {len(chunk['text'])} characters")
    """
    # Use the extract_text_by_page function to get page-level chunks
    return extract_text_by_page(pdf_path)


def get_pdf_metadata(pdf_path: str) -> Dict[str, any]:
    """
    Extract metadata from a PDF file.
    
    Args:
        pdf_path (str): Path to the PDF file.
    
    Returns:
        Dict[str, any]: Dictionary containing PDF metadata such as:
            - 'num_pages' (int): Total number of pages
            - 'author' (str): Document author (if available)
            - 'title' (str): Document title (if available)
            - 'subject' (str): Document subject (if available)
            - 'creator' (str): PDF creator software (if available)
    
    Raises:
        FileNotFoundError: If the PDF file does not exist.
        Exception: If there's an error reading the PDF file.
    """
    if not os.path.exists(pdf_path):
        raise FileNotFoundError(f"PDF file not found: {pdf_path}")
    
    try:
        with open(pdf_path, 'rb') as pdf_file:
            pdf_reader = PyPDF2.PdfReader(pdf_file)
            
            metadata = {
                'num_pages': len(pdf_reader.pages),
                'author': pdf_reader.metadata.get('/Author', 'Unknown') if pdf_reader.metadata else 'Unknown',
                'title': pdf_reader.metadata.get('/Title', 'Unknown') if pdf_reader.metadata else 'Unknown',
                'subject': pdf_reader.metadata.get('/Subject', 'Unknown') if pdf_reader.metadata else 'Unknown',
                'creator': pdf_reader.metadata.get('/Creator', 'Unknown') if pdf_reader.metadata else 'Unknown',
            }
            
            return metadata
    
    except Exception as e:
        raise Exception(f"Error reading PDF metadata from {pdf_path}: {str(e)}")


if __name__ == "__main__":
    # Example usage and testing
    print("PDF Parser Module")
    print("This module provides functionality for parsing PDF documents.")
    print("\nAvailable functions:")
    print("  - extract_text_by_page(pdf_path): Extract text organized by page")
    print("  - extract_tables(pdf_path, page_num): Extract tables (to be implemented)")
    print("  - chunk_document_by_pages(pdf_path): Chunk document by pages")
    print("  - get_pdf_metadata(pdf_path): Extract PDF metadata")
