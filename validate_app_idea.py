import os
from dotenv import load_dotenv
from crewai import Agent, Task, Crew
from crewai_tools import SerperDevTool
from langchain_groq import ChatGroq
import warnings
from crewai import Process

# ignore warning
warnings.filterwarnings('ignore')

load_dotenv()

llama = ChatGroq(
    model="llama3-8b-8192",
    api_key=os.getenv("GROQ_API_KEY")
)

serper_dev_tool = SerperDevTool()

# Senior market researcher agent
market_researcher = Agent(
    role="Senior market researcher",
    goal="Ensure the business {idea} is backed by solid research and data \n"
    "Carry out a comprehensive and realistic research for the given {idea}."
    "Provide insights of your research to the enterpeneur.",
    backstory="You are an expert market researcher skilled at validating business ideas"
              "You are skilled at doing market research for a given {idea}"
              "YOu have worked with numerous startups and established companies, helping them identify market trends and develop successful business strategies."
              "Your expertise lies in giving research reports for a given {idea}.",
    allow_delegation=False,
    verbose=True,
    llm=llama
)

# enterpreneur agent
enterpreneur_agent = Agent(
    role="Experienced Entrepreneur",
    goal="Create a marketing plan and business plan for {idea}",
    backstory="You have built more than 10 successful companies."
              "You are skilled at creating business ideas and marketing plans"
              "You possess high experience in crafting business and marketing plans"
              "You need to make sure that proper business plan and marketing plan is generated for {idea}",
    verbose=True,
    allow_delegation=False,
    llm=llama
)

# task for market researcher
task_market_researcher = Task(
    description=(
        "Analyze the strengths, weaknesses, opportunities, and threats (SWOT analysis) of the business idea {idea}"
        "Estimate market size and growth potential."
        "Assess the feasibility of the business model."
        "Give your insights for creating a Business Plan."
    ),
    expected_output=(
        "A detailed market research report for the mentioned idea {idea}"
        "Include references to external data for market analysis"
    ),
    tools=[serper_dev_tool],
    agent=market_researcher,
)

# enterprenuer
task_enterpreneur = Task(
    description=("Create the marketing plan and business plan for {idea}"
                 "Ensure that there are no discrepancies for the generated plans"
                 "There should be no inconsistences in either of the plans"
                 "Verify that all important concepts of business and marketing plans are covered"
                 ),
    expected_output=("Output should contain two main things: a final business plan for the {idea}\n"
                     "A final marketing plan for the {idea}"
                     ),
    tools=[serper_dev_tool],
    agent=enterpreneur_agent
)

crew = Crew(
    agents=[market_researcher, enterpreneur_agent],
    tasks=[task_market_researcher, task_enterpreneur],
    verbose=2,
    max_rpm=5000,
    memory=True
)

result = crew.kickoff(
    inputs={"idea": "oversized tshirts in ontario canada"})
print(result)
