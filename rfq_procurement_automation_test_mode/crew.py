import os

from crewai import LLM
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import (
	SerperDevTool,
	FileReadTool
)





@CrewBase
class RfqProcurementAutomationTestModeCrew:
    """RfqProcurementAutomationTestMode crew"""

    
    @agent
    def supplier_research_specialist(self) -> Agent:
        
        return Agent(
            config=self.agents_config["supplier_research_specialist"],
            
            
            tools=[				SerperDevTool()],
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            max_rpm=None,
            
            
            max_execution_time=None,
            llm=LLM(
                model="openai/gpt-4o-mini",
                temperature=0.7,
                
            ),
            
        )
    
    @agent
    def procurement_analyst(self) -> Agent:
        
        return Agent(
            config=self.agents_config["procurement_analyst"],
            
            
            tools=[				FileReadTool(),
				SerperDevTool()],
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            max_rpm=None,
            
            apps=[
                    "google_gmail/get_attachment",
                    ],
            
            
            max_execution_time=None,
            llm=LLM(
                model="openai/gpt-4o-mini",
                temperature=0.7,
                
            ),
            
        )
    
    @agent
    def supply_chain_risk_analyst(self) -> Agent:
        
        return Agent(
            config=self.agents_config["supply_chain_risk_analyst"],
            
            
            tools=[				SerperDevTool()],
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            max_rpm=None,
            
            
            max_execution_time=None,
            llm=LLM(
                model="openai/gpt-4o-mini",
                temperature=0.7,
                
            ),
            
        )
    
    @agent
    def procurement_report_writer(self) -> Agent:
        
        return Agent(
            config=self.agents_config["procurement_report_writer"],
            
            
            tools=[],
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            max_rpm=None,
            
            
            max_execution_time=None,
            llm=LLM(
                model="openai/gpt-4o-mini",
                temperature=0.7,
                
            ),
            
        )
    
    @agent
    def email_filter_specialist(self) -> Agent:
        
        return Agent(
            config=self.agents_config["email_filter_specialist"],
            
            
            tools=[],
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            max_rpm=None,
            
            
            max_execution_time=None,
            llm=LLM(
                model="openai/gpt-4o-mini",
                temperature=0.7,
                
            ),
            
        )
    

    
    @task
    def mock_rfq_processor(self) -> Task:
        return Task(
            config=self.tasks_config["mock_rfq_processor"],
            markdown=False,
            
            
        )
    
    @task
    def supplier_research(self) -> Task:
        return Task(
            config=self.tasks_config["supplier_research"],
            markdown=False,
            
            
        )
    
    @task
    def quote_analysis(self) -> Task:
        return Task(
            config=self.tasks_config["quote_analysis"],
            markdown=False,
            
            
        )
    
    @task
    def risk_assessment(self) -> Task:
        return Task(
            config=self.tasks_config["risk_assessment"],
            markdown=False,
            
            
        )
    
    @task
    def final_procurement_report(self) -> Task:
        return Task(
            config=self.tasks_config["final_procurement_report"],
            markdown=False,
            
            
        )
    

    @crew
    def crew(self) -> Crew:
        """Creates the RfqProcurementAutomationTestMode crew"""
        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            chat_llm=LLM(model="openai/gpt-4o-mini"),
        )


