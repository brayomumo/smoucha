from crewai import LLM, Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List

llm = LLM(
    model="ollama/deepseek-r1:1.5b",
    base_url="http://localhost:11434"
)

@CrewBase
class PersonaFinance():
    """PersonaFinance crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    @agent
    def chief_financial_data_officer(self) -> Agent:
        return Agent(
            config=self.agents_config['chief_financial_data_officer'], # type: ignore[index]
            verbose=True
        )

    @agent
    def cashflow_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['cashflow_analyst'], # type: ignore[index]
            verbose=True
        )
    
    @agent
    def strategic_planner(self) -> Agent:
        return Agent(
            config=self.agents_config['strategic_planner'], # type: ignore[index]
            verbose=True
        )
    
    @agent
    def master_plan_articulator(self) -> Agent:
        return Agent(
            config=self.agents_config['master_plan_articulator'], # type: ignore[index]
            verbose=True
        )


    @task
    def user_financial_data_collection(self) -> Task:
        return Task(
            config=self.tasks_config['user_financial_data_collection'], # type: ignore[index]
        )

    @task
    def expense_income_analyst(self) -> Task:
        return Task(
            config=self.tasks_config['expense_income_analyst'], # type: ignore[index]
            output_file='output/expense_income_analyst.json'
        )
    
    @task
    def budget_proposal_generation(self) -> Task:
        return Task(
            config=self.tasks_config['budget_proposal_generation'], # type: ignore[index]
            output_file='output/budget_proposal_generation.json'
        )
    
    @task
    def goal_alignment_and_strategy_development(self) -> Task:
        return Task(
            config=self.tasks_config['goal_alignment_and_strategy_development'], # type: ignore[index]
            output_file='output/goal_alignment_and_strategy_development.json'
        )
    
    @task
    def financial_plan_formulation(self) -> Task:
        return Task(
            config=self.tasks_config['financial_plan_formulation'], # type: ignore[index]
        )
    
    @task
    def user_review_and_iteration(self) -> Task:
        return Task(
            config=self.tasks_config['user_review_and_iteration'], # type: ignore[index]
        )

    @task
    def final_plan_presentation_and_action_steps(self) -> Task:
        return Task(
            config=self.tasks_config['final_plan_presentation_and_action_steps'], # type: ignore[index]
        )


    @crew
    def crew(self) -> Crew:
        """Creates the PersonaFinance crew"""
        
        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            # process=Process.hierarchical,
        )
