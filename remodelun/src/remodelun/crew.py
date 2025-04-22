from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

@CrewBase
class MUNCrew:
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    @agent
    def researcher(self) -> Agent:
        return Agent(config=self.agents_config['researcher'], verbose=True)

    @agent
    def country_specialist(self) -> Agent:
        return Agent(config=self.agents_config['country_specialist'], verbose=True)

    @task
    def research_task(self) -> Task:
        return Task(config=self.tasks_config['research_task'])

    @task
    def cheat_sheet_task(self) -> Task:
        return Task(config=self.tasks_config['cheat_sheet_task'], output_file="cheat_sheet.md")

    @task
    def position_summary_task(self) -> Task:
        return Task(config=self.tasks_config['position_summary_task'], output_file="position_summary.md")

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True
        )
