# Quick start of an agent

The goal of this exercise is to start a quick agent. The targeted structure involves only a minimal agent with a simple tool for demonstration.

## High-level instructions and notes
- Create a new virtual environment (then log in to the new environment!).
- Install the google-adk package.
- Get a Google authentication. For the case of API key, do the following.
    - Log on to your Google account (you do need a Google account).
    - Go to the Console.
    - Select APIs & Services from the drop down menu.
    - Within APIs & Services, choose Credentials, then create a new API key (make sure to read the best practices).
- Create an environment file .env (make sure it is not committed to your github repo). In the file, set the two environment variables:
    - GOOGLE_GENAI_USE_VERTEXAI=FALSE
    - GOOGLE_API_KEY=PASTE_YOUR_ACTUAL_API_KEY_HERE
- Create a parent_folder and then a folder quick_agent inside the parent_folder. 
- Create __init__.py inside the quick_agent folder.
- Create agent.py inside the quick_agent folder.
- Start a terminal on parent_folder and run adk web.
- Fix running rrors encountered and notes
    - root_agent not found: the agent in the agent file has to be named root_agent. Essentially a root_agent has to be defined.
    - Generative AI not enabled, has to activate Generative AI for this API key. I didn't run into this error before when I didn't have a Google Platform account and will need to investigate this further.
    - Some minor errors with string method capitalize (i.e., it is not capital).
- Finally! It works and passes the tested scenarios below.
    - When asked about weather for New York, the agent return the set answer as in the agent.py file. 
    - When asked about the weather anywhere else, the agent should politely appologize. 
    - When asked about anything else, the agent should say it is only for weather request.