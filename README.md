**Project Title**
 Crew AI Starter

**Description**
The Crew AI Starter is a Python project that utilizes the Crew AI framework to automate various use-cases. The project is designed to demonstrate the capabilities of the Crew AI framework in various use cases.
**Table of Contents**
================================================================================================

1. [Project Description](#project-description)
2. [Installation](#installation)
3. [Usage](#usage)
4. [Code Overview](#code-overview)
5. [Features](#features)
6. [Contributing](#contributing)
7. [License](#license)
8. [Contact Information](#contact-information)

**Installation**
To install the Crew AI Starter, follow these steps:

1. Clone the repository: `git clone https://github.com/october7sveryown/crew-ai-starter.git`
2. Install the required dependencies: `pip install dotenv crewai langchain_groq`
3. Set the GROQ_API_KEY environment variable: `export GROQ_API_KEY=your_api_key`

**Usage**
To run the Crew AI Starter, follow these steps:

1. Load the environment variables: `load_dotenv()`
2. Create a ChatGroq instance: `llama = ChatGroq(model="llama3-8b-8192", api_key=os.getenv("GROQ_API_KEY"))`
3. Create an instance of the Crew class: `crew = Crew(agents, tasks, verbose=2, memory=True, max_rpm=5000)`
4. Kick off the crew: `result = crew.kickoff()`

**Code Overview**
The code is divided into several sections:

### Agents
The code defines two agents: `technical_writer` and `software_engineer`. These agents are responsible for writing and editing the blog post, respectively.

### Tasks
The code defines two tasks: `write_task` and `edit_task`. These tasks are responsible for writing and editing the blog post, respectively.

### Crew
The code defines a `Crew` instance that manages the agents and tasks.

### Tools
The code uses various tools, including `FileReadTool`, `SerperDevTool`, and `ChatGroq`.

**Features**
The Crew AI Starter features:

* Automated blog post generation using natural language processing
* Collaboration between agents to generate high-quality content
* Integration with various tools and frameworks

**Contributing**
Contributions to the Crew AI Starter are welcome! Please submit pull requests with any suggested changes or improvements.

**License**
The Crew AI Starter is licensed under the MIT License.

**Contact Information**
For any questions or support, please contact [yashthaker.777@gmail.com](mailto:yashthaker.777@gmail.com)
