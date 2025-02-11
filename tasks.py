import asyncio
from crewai import Task

class NewsletterTasks:
    def __init__(self, researcher, insights_expert, writer, editor, user_input):
        self.research_task = Task(
            description=(
                f"Research recent advancements and key trends in {user_input}. Identify the most important developments."
            ),
            expected_output=f"A list of noteworthy developments in {user_input}, with reliable sources included.",
            agent=researcher
        )

        self.insights_task = Task(
            description=(
                f"Analyze the research provided by the Researcher and add detailed insights into the significance of each development in {user_input}. "
                "Focus on highlighting practical applications, strategic implications, and potential future directions."
            ),
            expected_output=f"A detailed analysis of each {user_input} advancement, including its applications, challenges, and broader implications for the industry. "
                            "Include commentary on its potential to impact various sectors and any notable limitations.",
            agent=insights_expert
        )

        self.write_task = Task(
            description=(
                f"Create concise and engaging content for the newsletter based on the insights provided. "
                "Include the following sections: \n"
                "- Innovation of the Week\n"
                "- Key Advancements in {user_input}\n"
                "- Notable Trends and Insights"
            ),
            expected_output=f"A well-structured newsletter draft with categorized sections and summaries for each development in {user_input}.",
            agent=writer
        )

        self.edit_task = Task(
            description=(
                "Proofread, refine, and structure the newsletter to ensure it is publication-ready. "
                "Should have an opening intro blurb that greets the readers. "
                f"Include highlights of the week's biggest changes and developments in {user_input}. "
                "The intro should provide a short wrap-up of the week in the industry, not limited to specific advancements but also significant trends and news. "
                "Ensure valid website URLs are provided for all sources referenced in the research."
            ),
            expected_output=f"A finalized newsletter, ready for publication, with captivating and comprehensive sections covering {user_input}.",
            agent=editor
        )

    def get_tasks(self):
        return [
            self.research_task,
            self.insights_task,
            self.write_task,
            self.edit_task
        ]

    async def run_tasks_async(self):
        """Run all tasks concurrently for faster execution."""
        tasks = [
            asyncio.create_task(self.research_task.run()),
            asyncio.create_task(self.insights_task.run()),
            asyncio.create_task(self.write_task.run()),
            asyncio.create_task(self.edit_task.run())
        ]
        return await asyncio.gather(*tasks)
