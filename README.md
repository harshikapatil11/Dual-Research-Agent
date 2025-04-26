# Dual-Research-Agent


I've built a "Smart Research Assistant" - like a mini team of two workers who talk to each other:
Worker 1: The Researcher (ResearchAgent)
- This guy's job is to go on the internet, search for information related to your question, and bring
back useful articles.
- He uses a tool called Tavily (an API) to search fast and smartly - better than basic Googling.
- Once he gathers some good material, he organizes it neatly: Title, Content, Relevance.
Worker 2: The Answer Writer (AnswerDraftingAgent)
- After the Researcher collects the info, it's handed to the Writer.
- The Writer is very smart - he uses Google's Gemini AI.
- His job is to read all the collected info, understand it, and write a neat, clear answer.
- He doesn't write randomly - you even told him to stay logical and not get too creative (by setting
temperature=0.2).
The Manager (DeepResearchSystem)
- Think of this like a Project Manager.
- When you ask a question:
1. It tells the Researcher: "Go get some info!"
2. Then it tells the Writer: "Use this info to write a good answer!"
3. Finally, it gives the finished answer back to you.
Where You Work (Flask Backend)
- You set up an office - a small Flask web server.
- You made a door (/ask route) where people can walk in and ask questions.
- Inside the office:
- It checks if they asked a valid question.
- If yes, it sends it to the Manager (DeepResearchSystem).
- After the answer is ready, it wraps it nicely (formats it) and gives it back as a clean JSON.
- You also made a welcome door (/) and ignored unnecessary knocks (favicon).
The Fancy Front Office (Streamlit App)
- You made a fancy reception desk using Streamlit.
- It has:
- A clean title: "Deep Research Bot "
- A text box for typing questions
- A button that says "Ask".
- When a user types a question:
- The reception guy sends it to your Flask backend.
- Waits for the answer.
- Shows the answer beautifully on the screen.
- If anything goes wrong (like the server crashes), it apologizes with a nice error message.
How You Keep Secrets Safe (Environment Variables)
- You don't hardcode your API keys (good practice!).
- You hide them safely in a .env file and load them secretly.
- This keeps your Tavily and Google Gemini keys private.
Overall
You built a system that acts like:
- A smart librarian (finds information fast),
- A professional writer (writes a clear, logical answer),
- A reception desk (takes questions from users),
- And a clean-looking website (to interact with).
In One Sentence:
"You built an AI-powered research and answering machine that you can interact with via a website,
making information gathering faster, cleaner, and user-friendly."

