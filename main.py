__import__('pysqlite3')
import sys
sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')
import os

from crewai import Crew, Process
from search_tool import SearchAndContents
from agents import NewsletterAgents
from tasks import NewsletterTasks

from dotenv import load_dotenv

load_dotenv()

class NewsletterCrew:
    def __init__(self, inputs):
        self.inputs = inputs
        self.search_tool = SearchAndContents()
        self.agents = NewsletterAgents(llm=None, search_tool=self.search_tool)  # Pass the LLM and search tool
        self.tasks = NewsletterTasks(
            self.agents.get_agents()["researcher"],
            self.agents.get_agents()["insights_expert"],
            self.agents.get_agents()["writer"],
            self.agents.get_agents()["editor"]
        )

    def run(self):
        # Initialize agents
        researcher = self.agents.get_agents()["researcher"]
        insights_expert = self.agents.get_agents()["insights_expert"]
        writer = self.agents.get_agents()["writer"]
        editor = self.agents.get_agents()["editor"]

        # Initialize tasks
        tasks = self.tasks.get_tasks()

        # Form the crew with defined agents and tasks
        crew = Crew(
            agents=[researcher, insights_expert, writer, editor],
            tasks=tasks,
            process=Process.sequential,
            planning=True,
            verbose=True
        )

        # Execute the crew to carry out the newsletter creation process
        return crew.kickoff(inputs={"user_input": self.inputs})
