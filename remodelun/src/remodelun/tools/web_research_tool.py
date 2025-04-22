from crewai.tools import BaseTool
import requests
from bs4 import BeautifulSoup
from typing import Type
from pydantic import BaseModel, Field

class WebResearchInput(BaseModel):
    query: str = Field(..., description="Sujet à rechercher sur le web.")

class WebResearchTool(BaseTool):
    name: str = "Web Research Tool"
    description: str = "Récupère des informations sur le web basées sur une requête spécifique."
    args_schema: Type[BaseModel] = WebResearchInput

    def _run(self, query: str) -> str:
        # Exemple simple : à adapter selon tes besoins
        search_url = f"https://www.google.com/search?q={query}"
        response = requests.get(search_url)
        soup = BeautifulSoup(response.text, "html.parser")
        return soup.get_text()[:1000]  # Simplifié pour illustration
