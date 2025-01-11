from crewai import Task

class ResearchCrewTasks:
    def __init__(self, researcher, insights_expert, writer, editor):
        self.research_task = Task(
            description=(
                "Research recent advancements in machine learning, deep learning, and AI. Identify the 'Innovation of the Week'."
            ),
            expected_output="A list of noteworthy developments in AI categorized as 'Machine Learning', 'Deep Learning', and 'AI Innovations', with reliable sources included.",
            agent=researcher
        )

        self.insights_task = Task(
            description=(
                "Analyze the research provided by the AI Researcher and add detailed insights into the significance of each advancement."
                "Focus on highlighting practical applications, strategic implications, and potential future directions for each innovation."
            ),
            expected_output="A detailed analysis of each AI advancement, including its applications, challenges, and broader implications for the industry."
                            "Include commentary on its potential to impact various sectors and any notable limitations.",
            agent=insights_expert
        )

        self.write_task = Task(
            description=(
                "Create concise and engaging content for the newsletter based on the insights provided."
                "Include the following sections: \n"
                "- Innovation of the Week\n"
                "- Key Advancements in Machine Learning\n"
                "- Highlights from Deep Learning\n"
                "- Notable AI Innovations"
            ),
            expected_output="A well-structured newsletter draft with categorized sections and summaries for each development.",
            agent=writer
        )

        self.edit_task = Task(
            description="Proofread, refine, and structure the newsletter to ensure it is publication-ready."
                        "Should have an opening intro blurb that always greets the readers."
                        "Include highlights of the week's biggest changes and developments in the AI ecosystem."
                        "The intro should provide a short wrap-up of the week in AI, not limited to specific advancements but also significant trends and news."
                        "The content should be engaging, informative, and organized into sections of at least five paragraphs each."
                        "Ensure valid website URLs are provided for all sources referenced in the research."
                        "The newsletter should always start with 'Welcome to Team Geto Weekly Digest on AI Innovations' and end with 'Written by The Team'.",
            expected_output="A finalized newsletter, ready for weekly publication, with captivating and comprehensive sections.",
            agent=editor
        )

    def get_tasks(self):
        return [
            self.research_task,
            self.insights_task,
            self.write_task,
            self.edit_task
        ]
