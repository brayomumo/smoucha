#!/usr/bin/env python
import sys
import warnings

from datetime import datetime

from persona_finance import crew

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Run the crew.
    """
    mock_refined_goals = {
        "house_downpayment": {"target_amount": 5000000, "target_date": "2027-05-30", "currency": "KES"}, # Kenyan Shillings
        "credit_card_debt_clearance": {"target_amount": 0, "current_amount": 250000, "target_date": "2025-11-30", "currency": "KES"},
        "investment_start": {"initial_amount": 10000, "recurring_monthly": 2000, "currency": "KES"}
    }
    inputs = {
        'user': 'Brian Mumo',
        'user_id': 'Brian Mumo',
        "data_source_paths": "google sheets",
        "user_goals_input":"Save 20,000 by end of June",
        'start_year': "2024",
        "end_date": str(datetime.now().year),
        "plan_output_format": "JSON",
        "analysis_depth": "daily_weekly_monthly",
        "category_granularity": "detailed",
        "budget_granularity": "daily_weekly_monthly",
        "budget_optimization_focus": "debt_reduction_priority",
        "refined_user_goals": mock_refined_goals,
        "financial_principles": ["emergency_fund_first", "high_interest_debt_priority", "long_term_wealth_building"],
        "risk_tolerance_profile": "moderate",
        "feedback_channel": "Simulated Chat Interface for User Approval",
        "plan_output_format": "PDF",
        "interaction_mode": "guided_prompts",
        "action_item_tracking_integration": "https://trello.com/b/your_finance_board_in_kenya"
    }
    
    try:
        crew.PersonaFinance().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        "topic": "AI LLMs",
        'current_year': str(datetime.now().year)
    }
    try:
        crew.PersonaFinance().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        crew.PersonaFinance().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        "topic": "AI LLMs",
        "current_year": str(datetime.now().year)
    }
    
    try:
        crew.PersonaFinance().crew().test(n_iterations=int(sys.argv[1]), eval_llm=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")
