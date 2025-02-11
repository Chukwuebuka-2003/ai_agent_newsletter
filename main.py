__import__('pysqlite3')
import sys
sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')
import os
import asyncio

from crewai import Crew, Process
from search_tool import SearchAndContents
from agents import NewsletterAgents
from tasks import NewsletterTasks
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI  # Import LLM model

load_dotenv()

class NewsletterCrew:
    def __init__(self, inputs, temperature=0.7):  # Add temperature parameter
        self.inputs = inputs
        self.temperature = temperature  # Store temperature setting

        # Specify OpenAI as the provider and pass the API key explicitly
        self.llm = ChatOpenAI(
            model_name="gpt-4o-mini",  # Ensure correct model name
            temperature=self.temperature,
            openai_api_key=os.getenv("OPENAI_API_KEY")  # Load API key from .env
        )

        self.search_tool = SearchAndContents()
        self.agents = NewsletterAgents(llm=self.llm, search_tool=self.search_tool)  # Pass LLM
        self.tasks = NewsletterTasks(
            self.agents.get_agents()["researcher"],
            self.agents.get_agents()["insights_expert"],
            self.agents.get_agents()["writer"],
            self.agents.get_agents()["editor"]
        )

    async def run(self):
        """Runs the newsletter generation asynchronously for better performance."""
        crew = Crew(
            agents=[
                self.agents.get_agents()["researcher"],
                self.agents.get_agents()["insights_expert"],
                self.agents.get_agents()["writer"],
                self.agents.get_agents()["editor"]
            ],
            tasks=self.tasks.get_tasks(),
            process=Process.sequential,  
            planning=True,
            verbose=True
        )

        #  Directly await kickoff_async since it's already an async function
        result = await crew.kickoff_async({"user_input": self.inputs})
        
        return result
