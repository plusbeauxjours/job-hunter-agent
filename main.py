from pathlib import Path
import yaml
from crewai import Crew, Agent, Task
from crewai.project import CrewBase, agent, task, crew
from crewai.knowledge.source.text_file_knowledge_source import TextFileKnowledgeSource
from models import JobList, RankedJobList, ChosenJob
from tools import web_search_tool


def create_resume_knowledge(agent_name: str):
    return TextFileKnowledgeSource(
        file_paths=["resume.txt"], collection_name=f"resume_{agent_name}"
    )


CONFIG_DIR = Path(__file__).parent / "config"
with open(CONFIG_DIR / "agents.yaml", "r") as f:
    AGENTS_CFG = yaml.safe_load(f)
with open(CONFIG_DIR / "tasks.yaml", "r") as f:
    TASKS_CFG = yaml.safe_load(f)


@CrewBase
class JobHunterCrew:
    @agent
    def job_search_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["job_search_agent"], tools=[web_search_tool]
        )

    @agent
    def job_matching_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["job_matching_agent"],
            knowledge_sources=[create_resume_knowledge("job_matching")],
        )

    @agent
    def resume_optimization_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["resume_optimization_agent"],
            knowledge_sources=[create_resume_knowledge("resume_optimization")],
        )

    @agent
    def company_research_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["company_research_agent"],
            knowledge_sources=[create_resume_knowledge("company_research")],
            tools=[web_search_tool],
        )

    @agent
    def interview_prep_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["interview_prep_agent"],
            knowledge_sources=[create_resume_knowledge("interview_prep")],
        )

    @task
    def job_extraction_task(self) -> Task:
        return Task(
            config=self.tasks_config["job_extraction_task"],
            output_pydantic=JobList,
        )

    @task
    def job_matching_task(self) -> Task:
        return Task(
            config=self.tasks_config["job_matching_task"],
            output_pydantic=RankedJobList,
        )

    @task
    def job_selection_task(self) -> Task:
        return Task(
            config=self.tasks_config["job_selection_task"],
            output_pydantic=ChosenJob,
        )

    @task
    def resume_rewriting_task(self) -> Task:
        return Task(
            config=self.tasks_config["resume_rewriting_task"],
            context=[
                self.job_selection_task(),
            ],
        )

    @task
    def company_research_task(self) -> Task:
        return Task(
            config=self.tasks_config["company_research_task"],
            context=[
                self.job_selection_task(),
            ],
        )

    @task
    def interview_prep_task(self) -> Task:
        return Task(
            config=self.tasks_config["interview_prep_task"],
            context=[
                self.job_selection_task(),
                self.resume_rewriting_task(),
                self.company_research_task(),
            ],
        )

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            verbose=True,
        )


JobHunterCrew().crew().kickoff(
    inputs={
        "level": "Senior",
        "position": "Frontend Developer",
        "location": "Germany",
    }
)
