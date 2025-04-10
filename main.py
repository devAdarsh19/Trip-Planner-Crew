import os
from crewai import Crew

from typing import List
from textwrap import dedent
from agents import TravelAgents
from tasks import TravelTasks

from dotenv import load_dotenv
load_dotenv()


class TravelCrew:
    def __init__(self, current_location, place_of_interest, date_range, interests):
        self.current_location: str = current_location
        self.place_of_interest: str = place_of_interest
        self.date_range: str = date_range
        self.interests: List[str] = interests

    def run(self):
        # Define your custom agents and tasks in agents.py and tasks.py
        agents = TravelAgents()
        tasks = TravelTasks()

        # Define your custom agents and tasks here
        expert_travel_agent = agents.expert_travel_agent()
        city_selection_expert = agents.city_selection_expert()
        local_tour_guide = agents.local_tour_guide()

        # Custom tasks include agent name and variables as input
        plan_itinerary = tasks.plan_itinerary(
            expert_travel_agent,
            self.place_of_interest,
            self.date_range,
            self.interests
        )

        identify_city = tasks.identify_city(
            city_selection_expert,
            self.current_location,
            self.place_of_interest,
            self.date_range,
            self.interests
        )

        gather_city_info = tasks.gather_city_info(
            local_tour_guide,
            self.place_of_interest,
            self.date_range,
            self.interests
        )

        # Define your custom crew here
        crew = Crew(
            agents=[expert_travel_agent, city_selection_expert, local_tour_guide],
            tasks=[plan_itinerary, identify_city, gather_city_info],
            verbose=True,
        )

        result = crew.kickoff()
        return result


# This is the main function that you will use to run your custom crew.
# if __name__ == "__main__":
#     print("## Trip Planner Crew")
#     print("-------------------------------")
#     current_location = input(dedent("""Where will you be traveling from? : """))
#     place_of_interest = input(dedent("""What place would you like to travel to? : """))
#     date_range = input(dedent("""What is your travel date range? : """))
#     interests = input(dedent("""What are some of your high level interests and hobbies? : """))

#     travel_crew = TravelCrew(current_location, place_of_interest, date_range, interests)
#     result = travel_crew.run()
#     print("\n\n########################")
#     print("## Here is you custom crew run result:")
#     print("########################\n")
#     print(result)
