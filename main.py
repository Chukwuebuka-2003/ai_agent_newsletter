__import__('pysqlite3')
import sys
sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')
import os

from crewai import Crew, Process
from search_tool import SearchAndContents
from agents import ResearchCrewAgents
from tasks import ResearchCrewTasks

from dotenv import load_dotenv

load_dotenv()

class ResearchCrew:
    def __init__(self, inputs):
        self.inputs = inputs
        self.search_tool = SearchAndContents()
        self.agents = ResearchCrewAgents(llm=None, search_tool=self.search_tool)  # Pass the LLM and search tool
        self.tasks = ResearchCrewTasks(
            self.agents.get_agents()["researcher"],
            self.agents.get_agents()["partnership_expert"],
            self.agents.get_agents()["writer"],
            self.agents.get_agents()["editor"]
        )

    def run(self):
        # Initialize agents
        researcher = self.agents.get_agents()["researcher"]
        partnership_expert = self.agents.get_agents()["partnership_expert"]
        writer = self.agents.get_agents()["writer"]
        editor = self.agents.get_agents()["editor"]

        # Initialize tasks
        tasks = self.tasks.get_tasks()

        # Form the crew with defined agents and tasks
        crew = Crew(
            agents=[researcher, partnership_expert, writer, editor],
            tasks=tasks,
            process=Process.sequential,
            planning=True,
            verbose=True
        )

        # Execute the crew to carry out the research project
        return crew.kickoff(inputs={"user_input": self.inputs})

