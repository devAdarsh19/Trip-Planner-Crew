from crewai import Agent, LLM
from crewai.tools import BaseTool
from textwrap import dedent
from tools.search_tool import SearchTools
from tools.calculator_tool import CalculatorTools



# This is an example of how to define custom agents.
# You can define as many agents as you want.
# You can also define custom tasks in tasks.py
class TravelAgents:
    
    def __init__(self):
        self.Ollama = LLM(
            model="ollama/llama3.2:latest",
            base_url="http://localhost:11434",
            temperature=0.7
        )

    def expert_travel_agent(self):
        return Agent(
            role="Expert Travel Agent",
            backstory=dedent(f"""Expert in travel planning and logistics. I have decades of experience making travel itineraries"""),
            goal=dedent(f"""Create a 7-day itinerary with a detailed per-day plan, 
                        include budget, packing suggestions and safety tips."""),
            tools=[SearchTools(), CalculatorTools()],
            allow_delegation=False,
            verbose=True,
            llm=self.Ollama,
        )

    def city_selection_expert(self):
        return Agent(
            role="City Selection Expert",
            backstory=dedent(f"""Expert at analyzing travel data to pick ideal destinations"""),
            goal=dedent(f"""Select the best cities based on weather, season, prices, and travel interests"""),
            tools=[SearchTools()],
            allow_delegation=False,
            verbose=True,
            llm=self.Ollama,
        )
        
    def local_tour_guide(self):
        return Agent(
            role="Local Tour Guide",
            backstory=dedent(f"""Highly knowledgeable tour guide with extensive information about the city,
                             its attractions and customs"""),
            goal=dedent(f"""Provide the BEST insights about selected cities"""),
            tools=[SearchTools()],
            allow_delegation=False,
            verbose=True,
            llm=self.Ollama,
        )
