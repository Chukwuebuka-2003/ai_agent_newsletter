# Developer Documentation

## Overview

The **AI Agent Newsletter** project leverages CrewAI to orchestrate a series of agents that collaboratively generate an AI-powered newsletter. The project combines web search, research, content creation, and editing into a seamless process. It exposes its functionality via a FastAPI web service, making it accessible for both local testing and cloud deployments (e.g., on Render).

## Table of Contents

- [Overview](#overview)
- [Project Structure](#project-structure)
- [Setup & Installation](#setup--installation)
- [Configuration](#configuration)
- [Running the Project Locally](#running-the-project-locally)
- [API Endpoints](#api-endpoints)
- [Deployment](#deployment)


## Project Structure

```
ai_agent_newsletter/
├── agents.py             # Defines the agents (researcher, insights expert, writer, editor)
├── tasks.py              # Specifies the tasks each agent will perform
├── main.py               # Entry point that assembles the Crew and executes the newsletter generation process
├── search_tool.py        # Contains the tool for web searching and content retrieval (via the Exa API)
├── api.py                # FastAPI application exposing the newsletter generation endpoint
├── gunicorn_config.py    # Gunicorn configuration for production deployment
├── requirements.txt      # Python dependencies
```

### File Details

- **`search_tool.py`**  
  Implements the `SearchAndContents` class to perform web searches using the Exa API. It retrieves recent results (from the past week) and their contents.

- **`tasks.py`**  
  Contains the `NewsletterTasks` class that defines four key tasks: research, insights analysis, content writing, and editing. Each task is configured with a description, expected output, and the agent responsible.

- **`agents.py`**  
  Defines the `NewsletterAgents` class which creates four agents using CrewAI. These agents play specific roles:
  - **Researcher:** Gathers recent AI developments.
  - **Insights Expert:** Provides detailed analysis of the research.
  - **Writer:** Converts insights into engaging newsletter content.
  - **Editor:** Refines and finalizes the newsletter.

- **`main.py`**  
  Serves as the main orchestration file. It constructs the Crew with agents and tasks, then executes the process to generate the newsletter. It utilizes environment variables (loaded via `python-dotenv`) for API keys and other configurations.

- **`api.py`**  
  Wraps the newsletter generation functionality in a FastAPI application. It defines endpoints to trigger the process:
  - `GET /` – Returns a welcome message.
  - `POST /generate-newsletter/` – Accepts user input and returns the generated newsletter.

- **`gunicorn_config.py`**  
  Contains configuration settings for running the FastAPI app with Gunicorn. This file is used during production deployments.

- **`start.sh`**  
  A shell script for Render deployments. It starts the app using Gunicorn with the Uvicorn worker.

## Setup & Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/Chukwuebuka-2003/ai_agent_newsletter.git
   cd ai_agent_newsletter
   ```

2. **Create and Activate a Virtual Environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

## Configuration

The project relies on several environment variables for API integrations. Create a `.env` file in the root directory with the following keys:

```
EXA_API_KEY=your_exa_api_key_here
OPENAI_API_KEY=your_openai_api_key_here
```

> **Note:** Adjust or add any additional environment variables as needed by your agents or tools.

## Running the Project Locally

### Using FastAPI (Development Mode)

Start the FastAPI development server with Uvicorn:

```bash
uvicorn api:app --reload
```

Access the following endpoints in your browser:
- **Swagger UI:** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **ReDoc:** [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

### Using Gunicorn (Production Mode)

For production testing, run:

```bash
gunicorn -c gunicorn_config.py api:app
```

## API Endpoints

- **GET `/`**  
  Returns a welcome message.
  
  **Response:**
  ```json
  {
    "message": "Welcome to the AI-Powered Newsletter API"
  }
  ```

- **POST `/generate-newsletter/`**  
  Triggers the newsletter generation process. Accepts a JSON payload with the user input.

  **Request Body Example:**
  ```json
  {
    "user_input": "latest AI advancements"
  }
  ```

  **Response Example:**
  ```json
  {
    "newsletter": "Generated newsletter content..."
  }
  ```

## Deployment

### Deploying on Render

**Prepare Your Repository:**
   - Push your code to GitHub (or another Git-based repository).

     
**Deploy and Test:**
   - After deployment, test your API at:  
     `https://your-app-name.onrender.com/docs`



