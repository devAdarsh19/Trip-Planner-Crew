# Trip-Planner-Crew
Using CrewAI's capabilities to create travel itineraries

## Install Dependencies
```
pip install -r requirements.txt
```

Install crewai_tools:
```
pip install 'crewai[tools]'
```

## Setting Up Serper Search
- Get your free Serper API key from [here](https://serper.dev/)
- Create an env file named '.env' and paste this line:
  ```
  SERPER_API_KEY=<YOUR_SERPER_API_KEY>
  ```

## Installing and Running Models Locally

- Download Ollama from [here](https://ollama.com/)
- In the terminal, run the command:
  ```
  ollama run <model_name>
  ```
- This particular crew uses llama3.2:latest (3B)
- Ensure Ollama is running before running the crew

## Kicking Off the Crew
To kickoff the crew, run the command:
```
python main.py
```
