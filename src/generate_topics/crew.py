from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task, before_kickoff, after_kickoff

# Uncomment the following line to use an example of a custom tool
from generate_topics.tools.custom_tool import TopicFormat,ListTopics

# Check our tools documentations for more information on how to use them
# from crewai_tools import SerperDevTool
from crewai_tools import SerperDevTool, ScrapeWebsiteTool, WebsiteSearchTool

from pyairtable import Api

anthropic_llm = "anthropic/claude-3-5-sonnet-20241022"

# Initialize the tools
search_tool = SerperDevTool()
scrape_tool = ScrapeWebsiteTool()

@CrewBase
class GenerateTopics():
	"""GenerateTopics crew"""

	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'


	@agent
	def TopicGeneratorAgent(self) -> Agent:
		return Agent(
			config=self.agents_config['TopicGeneratorAgent'],
			# tools=[MyCustomTool()], # Example of custom tool, loaded on the beginning of file
			# verbose=True,
			# llm=anthropic_llm
		)

	@agent
	def ReconcileAgent(self) -> Agent:
		return Agent(
			config=self.agents_config['ReconcileAgent'],
			# verbose=True,
			# llm=anthropic_llm
		)

	@task
	def TopicGeneratorTask(self) -> Task:
		return Task(
			config=self.tasks_config['TopicGeneratorTask'],
			tools=[SerperDevTool(), ScrapeWebsiteTool()],
			agent=self.TopicGeneratorAgent()
		)

	@task
	def TopicGeneratorTask2(self) -> Task:
		return Task(
			config=self.tasks_config['TopicGeneratorTask2'],
			tools=[SerperDevTool(), ScrapeWebsiteTool()],
			agent=self.TopicGeneratorAgent()
		)

	@task
	def ReconcileTask(self) -> Task:
		return Task(
			config=self.tasks_config['ReconcileTask'],
			agent=self.ReconcileAgent(),
			output_pydantic=ListTopics,
			output_file="Result.md",
		)

	# @task
	# def reporting_task(self) -> Task:
	# 	return Task(
	# 		config=self.tasks_config['reporting_task'],
	# 		output_file='report.md'
	# 	)

	@crew
	def crew(self) -> Crew:
		"""Creates the GenerateTopics crew"""
		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			# verbose=True,
			# process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
		)

@CrewBase
class ContentWriter():
	"""GenerateTopics crew"""

	agents_config = 'config/agents2.yaml'
	tasks_config = 'config/tasks2.yaml'


	@agent
	def OutlineAgent(self) -> Agent:
		return Agent(
			config=self.agents_config['OutlineAgent'],
			# tools=[MyCustomTool()], # Example of custom tool, loaded on the beginning of file
			# verbose=True
		)

	@agent
	def ContentGeneratorAgent(self) -> Agent:
		return Agent(
			config=self.agents_config['ContentGeneratorAgent'],
			# verbose=True
		)

	@agent
	def ReconcileAgent(self) -> Agent:
		return Agent(
			config=self.agents_config['ReconcileAgent'],
			# verbose=True
		)		

	@agent
	def PlagiarismCheckerAgent(self) -> Agent:
		return Agent(
			config=self.agents_config['PlagiarismCheckerAgent'],
			# verbose=True
		)

	@agent
	def TranslationAgent(self) -> Agent:
		return Agent(
			config=self.agents_config['TranslationAgent'],
			# verbose=True,
			llm=anthropic_llm
		)

	@task
	def OutlineAgent_task(self) -> Task:
		return Task(
			config=self.tasks_config['OutlineAgent_task'],
			agent=self.OutlineAgent()
		)

	@task
	def ContentGeneratorAgent_task(self) -> Task:
		return Task(
			config=self.tasks_config['ContentGeneratorAgent_task'],
			agent=self.ContentGeneratorAgent()
		)

	@task
	def ReconcileAgent_task(self) -> Task:
		return Task(
			config=self.tasks_config['ReconcileAgent_task'],
			agent=self.ReconcileAgent(),
			output_file='refined_output.md'
		)

	@task
	def PlagiarismCheckerAgent_task(self) -> Task:
		return Task(
			config=self.tasks_config['PlagiarismCheckerAgent_task'],
			tools=[search_tool, scrape_tool],
			agent=self.PlagiarismCheckerAgent(),			
		)		

	@task
	def TranslationAgent_task(self) -> Task:
		return Task(
			config=self.tasks_config['TranslationAgent_task'],
			agent=self.TranslationAgent(),
			output_file='content_output.md'
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the ContentWriter crew"""
		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=True,
			# process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
		)
