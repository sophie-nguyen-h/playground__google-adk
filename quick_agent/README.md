# Quick start of an agent

The goal is to start an agent to initial an conversation with a Google model. The scope of this testing involved minimal a minimal agent a minimal tool.

## High-level instructions and notes
- Create a new virtual environment (then log in to the new environment!)
- Install the google-adk package.
- Get a Google authentication, for this case, for this case, try Google API key.At the time of this writing, you can create and API key for free. 
    - Log on to your Google account (you do need a Google account which is also free)
    - Go to the Console.
    - Select APIs & Services from the drop down menu.
    - Within APIs & Services, choose Credentials, then create a new API key (make sure to read the best practices)
- Create an environment file env (make sure it is not committed to your github repo). In the file, set the two environment variables
    - GOOGLE_GENAI_USE_VERTEXAI=FALSE
    - GOOGLE_API_KEY=PASTE_YOUR_ACTUAL_API_KEY_HEREv
- Folder setup parent_folder/quick_agent. 
- Create __init__.py inside the quick_agent folder.
- Create agent.py inside the quick_agent folder.
- Start a terminal on parent_folder and run adk web
- Errors encountered and notes
    - root_agent not found: the agent in the agent file has to be named root_agent. Essentially a root_agent has to be defined.
    - Generative AI not enabled, has to activate Generative AI for this API key. I didn't run into this error before when I didn't start my Google Platform account. Not sure if this is different now.
    - Minor errors: string method is capitalize not capital! Oh ...
- Finally! It works!
    - Expected behaviors: When ask about weather for New York, the agent return the set answer as in the agent.py file. But when asked about the weather anywhere else, the agent should politely appologize. When asked about anything else, the agent should say it is only for weather request.