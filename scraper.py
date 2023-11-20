from duckduckgo_search import DDGS
from dataclasses import dataclass
from typing import Optional, List
from colorama import Fore, Style
from tls_client import Session
from bs4 import BeautifulSoup
from tqdm import tqdm
import json

session = Session(client_identifier='chrome_115', random_tls_extension_order=True)

@dataclass
class SearchResult:
    title: str
    body: str
    href: str
    scraped_content: Optional[str] = None

    @classmethod
    def from_json(cls, data: dict) -> 'SearchResult':
        return cls(title=data['title'], body=data['body'], href=data['href'])

    def scrape_url(self):
        self.print_log(f"Scraping content from {self.href}")
        try:
            response = session.get(self.href)
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                self.scraped_content = soup.get_text()
                self.print_log(f"Content scraped successfully from {self.href}")
            else:
                self.print_log(f"Failed to retrieve content from {self.href}")
        except Exception as e:
            self.print_log("Failed to send request to scrape content.")

    def print_info(self):
        self.print_log("Title:", {'value': self.title})
        self.print_log("Body:", {'value': self.body})
        self.print_log("URL:", {'value': self.href})

    @staticmethod
    def print_log(message: str, data: Optional[dict] = None):
        log_message = f"{Fore.CYAN}[LOG]{Style.RESET_ALL} | {message}"
        if data:
            log_message += f" {Fore.LIGHTMAGENTA_EX}| {data}"
        print(log_message)

class DataScrape:
    def __init__(self, query: str, max_results: int = 2):
        self.query: str = query
        self.max_results: int = max_results
        self.results: List[SearchResult] = []

    def search(self) -> List[SearchResult]:
        with DDGS() as ddgs:
            results_json: List[dict] = [r for r in ddgs.text(self.query, max_results=self.max_results)]

        for result_json in tqdm(results_json, desc="Scraping"):
            search_result: SearchResult = SearchResult.from_json(result_json)
            search_result.scrape_url()
            search_result.print_info()
            self.results.append(search_result)

        return self.results
