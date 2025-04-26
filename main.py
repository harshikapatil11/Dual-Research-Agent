import os  # ✅ Required
from tavily import TavilyClient
from langchain.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI  # ✅ NEW

# ---------------------- Agent 1: Research Agent ----------------------
class ResearchAgent:
    def __init__(self, api_key):
        self.client = TavilyClient(api_key)

    def gather_data(self, query):
        try:
            results = self.client.search(query, search_depth="advanced", max_results=5)
            processed_data = []

            for result in results['results']:
                processed_data.append({
                    'title': result.get('title', ''),
                    'content': result.get('content', ''),
                    'score': result.get('score', 0)
                })
            return processed_data
        except Exception as e:
            print("❌ Error while fetching data from Tavily:", e)
            return []

# ---------------------- Agent 2: Answer Drafting Agent ----------------------
class AnswerDraftingAgent:
    def __init__(self, google_api_key):
        self.llm = ChatGoogleGenerativeAI(
            model="models/gemini-1.5-pro-latest",
            google_api_key=google_api_key,
            temperature=0.2
        )

    def draft_answer(self, combined_content, query):
        content_str = "\n\n".join([f"**{item['title']}**:\n{item['content']}" for item in combined_content])
        prompt_template = ChatPromptTemplate.from_template(
            "Using the following information:\n{data}\n\nAnswer the question:\n{question}\n\nFormat the answer neatly with headings, bullet points, and short paragraphs wherever appropriate."
        )
        chain = prompt_template | self.llm
        return chain.invoke({"data": content_str, "question": query})

# ---------------------- Dual-Agent System ----------------------
class DeepResearchSystem:
    def __init__(self, tavily_api_key, google_api_key):
        self.research_agent = ResearchAgent(tavily_api_key)
        self.answer_drafting_agent = AnswerDraftingAgent(google_api_key)

    def run(self, query):
        print(f"\n🔎 Query: {query}")
        data = self.research_agent.gather_data(query)
        print(f"📄 Collected {len(data)} documents from Tavily.")
        answer = self.answer_drafting_agent.draft_answer(data, query)
        return answer

# ---------------------- Main Entry Point ----------------------
def main():
    tavily_key = "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"  # Your Tavily API key
    google_key = "AIzaSyBLz5yBy5e_nkHcnOvL1d6kmqzm0moJzi8"  # Your Google Gemini API key
    system = DeepResearchSystem(tavily_key, google_key)

    query = input("🔍 Enter your research question: ")
    answer = system.run(query)

    # ✅ Fetch only the clean content part
    if hasattr(answer, 'content'):
        clean_answer = format_answer(answer.content)
    else:
        clean_answer = format_answer(str(answer))  # Fallback if somehow it's plain text

    print("\n✅ Generated Answer:\n")
    print(clean_answer)


def format_answer(text):
    # Add clean formatting
    clean_text = text.strip()
    clean_text = clean_text.replace("\\n", "\n")  # Handle escaped newlines
    clean_text = clean_text.replace("\n\n", "\n")  # Avoid too many blank lines
    return clean_text


if __name__ == "__main__":
    main()
