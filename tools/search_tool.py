import json
import os
import requests
from langchain.tools import tool
from crewai.tools import BaseTool
from pydantic import BaseModel, Field
from typing import Type
from crewai_tools import PDFSearchTool

class QuerySchema(BaseModel):
    query: str = Field(..., description="A string parameter thta defines what to search the web for.")

class SearchTools(BaseTool):
    
    name: str = "Search the web"
    description: str = (
        "Helps search the web for most relevant travel destinations"
        ""
    )
    args_schema: Type[BaseModel] = QuerySchema
    
    def _run(self, query):
        '''
        Helps search the internet for top destinations
        '''
        top_result_to_return = 4
        url = "https://google.serper.dev/search"
        payload = json.dumps({"q": query})
        headers = {
            'X-API-KEY': os.environ['SERPER_API_KEY'],
            'Content-Type': 'application/json'
            }
        response = requests.request("POST", url, headers=headers, data=payload)
        
        if 'organic' not in response.json():
            return "Sorry I could not search the web. Could be an issue with your Serper API"
        else:
            results = response.json()['organic']
            string = []
            for result in results[:top_result_to_return]:
                try:
                    string.append('\n'.join([
                        f"Title: {result['title']}", f"Link: {result['link']}", f"Snippet: {result['snippet']}", "\n----------------"
                    ]))
                except KeyError:
                    next
                    
            return '\n'.join(string)