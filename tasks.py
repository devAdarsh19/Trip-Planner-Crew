# To know more about the Task class, visit: https://docs.crewai.com/concepts/tasks
from crewai import Task
from textwrap import dedent

"""
Develop a 7-day travel plan, including city selection. Keep in mind the weather, season, travel interests, prices, etc.

Tasks:
    - Itinerary planning : 7-day travel plan
    Agent: Expert Travel Agent
    - City Selection: Select the best cities to travel to
    Agent: City Selection Expert
    - Local Tour Guide: Find a local expert to provide insights and suggestions
    Agent: Local Tour Guide
"""

class TravelTasks:
    def __tip_section(self):
        return "If you do your BEST WORK, I'll give you a $10,000 commission!"

    def plan_itinerary(self, agent, city, travel_dates, interests):
        return Task(
            description=dedent(
                f"""
                **Task**: Create a 7-day travel itinerary
                **Description**: Expand the city guide into a full 7-day travel plan with detailed per-day plans, inclduing weather forecasts, 
                places to eat, packing suggestions and budget breakdown. You MUST suggest actual places to visit, actual hotels to stay, and 
                actual restaurants to go to. This itinerary must include all aspects of the trip, from arrival to departure, integrating the 
                city guide information with practical travel logistics.
                
                **Parameters**:
                - City: {city}
                - Travel Dates: {travel_dates}
                - Interests: {interests}
                
                **NOTE**: {self.__tip_section()}
                """
            ),
            expected_output="The expected output of the task",
            agent=agent,
        )
        
    def identify_city(self, agent, origin, place_of_interest, travel_dates, interests):
        return Task(
            description=dedent(
                f"""
                **Task**: Identify the best city for the trip
                **Description**: Analyze and select the best city for the trip based on specific criteria such as weather patterns,
                seasonal events, and travel costs.
                This task involves comparing multiple cities, considering factors like weather patterns, seasonal events and festivals,
                and overal travel expenses.
                Your final answer must be a detailed report on the chosen city, including actual flight costs, weather forecast, and attractions
                
                **Parameters**:
                - Origin: {origin}
                - Place of Interest: {place_of_interest}
                - Travel Dates: {travel_dates}
                - Interests: {interests}
                
                **NOTE**: {self.__tip_section()}
                """
            ),
            expected_output="The expected output of the task",
            agent=agent,
        )

    def gather_city_info(self, agent, city, travel_dates, interests):
        return Task(
            description=dedent(
                f"""
                **Task**: Gather in-depth city guide information
                **Description**: Compile an in-depth guide for the chosen city, gathering information about key attractions, local customs, 
                special events, and daily activity recommendations.
                This guide should provide a thorough overview of what the city has to offer, including hidden gems, cultural hotspots, 
                must-visit landmarks, weather forecasts, and high-level costs.
                
                **Parameters**:
                - Chosen city: {city}
                - Travel Dates: {travel_dates}
                - Interests: {interests}
                
                **NOTE**: {self.__tip_section()}
                """
            ),
            expected_output="The expected output of the task",
            agent=agent,
        )
