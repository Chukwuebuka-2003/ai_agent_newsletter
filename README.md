# 📰 AI-Powered Newsletter Generator for AI & ML Developments

An AI-driven CrewAI Multi-Agent application that automatically creates engaging newsletters focused on the latest developments in machine learning, deep learning, and artificial intelligence. The application provides insights and generates reader-friendly content for professionals and enthusiasts.

## 🚀 Features

- **Multi-Agent System**: Utilizes CrewAI to coordinate specialized agents for research, insights generation, content creation, and editing.
- **AI Researcher**: Identifies and categorizes noteworthy developments in AI, machine learning, and deep learning based on the latest trends.
- **AI Expert**: Provides expert analysis on the identified research, offering strategic insights, applications, and potential impacts.
- **Content Writer**: Transforms the research and expert insights into an engaging, informative newsletter format.
- **Newsletter Editor**: Proofreads, refines, and structures the final newsletter, ensuring it’s ready for publication.
- **Custom Search Tool**: Gathers up-to-date, reliable data from various sources to keep the newsletter current.
- **Reader-Friendly Content**: Automatically produces concise, engaging summaries of AI advancements that are easy to digest.

## 🛠️ Tech Stack

- **Agents Framework**: CrewAI
- **Frontend**: Streamlit UI
- **Backend**: Python, SQLite (for data storage)
- **LLM**: OpenAI API 
- **Custom Search Tool**: Tailored search functionality for gathering AI-related content from trusted sources
- **Document Parsing**: Python (handling content from multiple formats)
- **Environment Management**: dotenv for seamless configuration

## 🌟 How It Works

1. **Research Agent**: Gathers recent information on AI, ML, and DL from trusted sources based on user input.
2. **AI Expert Agent**: Analyzes the research and provides in-depth, expert insights into the advancements, trends, and real-world applications.
3. **Writer Agent**: Crafts the insights into reader-friendly content, summarizing complex topics into concise, easy-to-read sections.
4. **Editor Agent**: Proofreads and organizes the content into a structured, well-written newsletter ready for publication.

## 🚀 Getting Started

1. Clone the repository:
    ```bash
    git clone https://github.com/YourGithubRepo/ai_agent_newsletter.git
    cd ai_agent_newsletter
    ```

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Set up environment variables (e.g., API keys for LLM, search tools):
    ```bash
    cp .env.example .env
    ```

4. Run the application:
    ```bash
    python run.py
    ```

## 📄 Example Use Case

Input the latest AI trends or user-defined topics, and the application will:
1. Research recent developments in machine learning, deep learning, and AI.
2. Generate expert-level insights based on those findings.
3. Transform the insights into an engaging, professional newsletter.
4. Provide a final polished document ready for distribution.

## 💬 Future Enhancements

- Integration with external platforms for direct distribution (e.g., email, social media).
- Additional customization options for the newsletter layout.

