from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
from time import sleep
#
from threading import Event, Thread
import os

@CrewBase
class TitleBuildMyValuePropositionAndMarketingStrategyCrewCrew():
    """TitleBuildMyValuePropositionAndMarketingStrategyCrew crew"""

    @agent
    def value_proposition_canvas_creator(self) -> Agent:
        return Agent(
            config=self.agents_config['value_proposition_canvas_creator'],
            llm=LLM(api_key=os.getenv("ANTHROPIC_API_KEY"), model="anthropic/claude-3-haiku-20240307", )
        )

    @agent
    def marketing_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['marketing_analyst'],
            llm=LLM(api_key=os.getenv("ANTHROPIC_API_KEY"), model="anthropic/claude-3-haiku-20240307",  )
        )

    @agent
    def swot_analyzer(self) -> Agent:
        return Agent(
            config=self.agents_config['swot_analyzer'],
            llm=LLM(api_key=os.getenv("ANTHROPIC_API_KEY"), model="anthropic/claude-3-haiku-20240307", )
        )

    @agent
    def buyers_journey_mapper(self) -> Agent:
        return Agent(
            config=self.agents_config['buyers_journey_mapper'],
            llm=LLM(api_key=os.getenv("ANTHROPIC_API_KEY"), model="anthropic/claude-3-haiku-20240307", )
        )

    @agent
    def output_formatter(self) -> Agent:
        return Agent(
            config=self.agents_config['output_formatter'],
            llm=LLM(api_key=os.getenv("ANTHROPIC_API_KEY"), model="anthropic/claude-3-haiku-20240307",  )
        )


    @task
    def create_value_proposition_canvas_task(self) -> Task:
        print(f"Akki is analyzing the inputs...")
        sleep(3),  # Simulate task duration
        print(f"Task value_proposition_canvas_creator is in progress...!")
        sleep(2),
        return Task(
            config=self.tasks_config['create_value_proposition_canvas_task'],
            output_file='output/report_canvas.md'
        )

    @task
    def analyze_4ps_task(self) -> Task:
        return Task(
            config=self.tasks_config['analyze_4ps_task'],
            output_file='output/report_4p.md'
        )

    @task
    def conduct_swot_analysis_task(self) -> Task:
        return Task(
            config=self.tasks_config['conduct_swot_analysis_task'],
            output_file='output/report_swot.md'
        )

    @task
    def map_buyers_journey_task(self) -> Task:
        return Task(
            config=self.tasks_config['map_buyers_journey_task'],
            output_file='output/report_buyers.md'
        )

    @task
    def combine_task(self) -> Task:
        return Task(
            config=self.tasks_config['combine_task'],
            output_file='output/reports_combine.md'
        )

    @crew
    def crew(self) -> Crew:
        """Creates the TitleBuildMyValuePropositionAndMarketingStrategyCrew crew"""
        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True
        )