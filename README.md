# SMOUCHA: Personal AI-Powered Assistant

SMOUCHA is an ambitious project to build a comprehensive, AI-powered personal assistant designed to help users manage and optimize various aspects of their lives. The goal is to create a modular, extensible system that can integrate multiple intelligent agents for different domains.

## Current Status

The first major component is a **Personal Financial Advisor** powered by [crewAI](https://crewai.com). This module helps users organize, analyze, and optimize their personal finances using specialized AI agents.

## Features (Current & Planned)

- **Personal Financial Advisor:**  
  - Automated financial data collection
  - Expense and income analysis
  - Budget proposal generation
  - Goal alignment and actionable financial planning

- **Future Modules (Planned):**
  - Task and schedule management
  - Health and wellness tracking
  - Knowledge management

## Getting Started

1. **Python Version:**  
   Ensure you have Python >=3.10 and <3.13 installed.

2. **Install [uv](https://docs.astral.sh/uv/):**
   ```bash
   pip install uv
   ```

3. **Install Dependencies:**  
   From the project root directory:
   ```bash
   crewai install
   ```

4. **Environment Variables:**  
   Add your API keys (e.g., `OPENAI_API_KEY`) to a `.env` file.

## Project Structure

```
persona_finance/
  src/
    persona_finance/
      __init__.py
      crew.py
      main.py
      config/
      tools/
  output/
  knowledge/
  tests/
pfa/
  __init__.py
  agents.py
  llm.py
  main.py
  tasks.py
```

- **src/persona_finance/**: Main financial advisor implementation.
- **pfa/**: Experimental/alternative financial agent framework.
- **output/**: Generated reports and analysis.
- **knowledge/**: User preferences and reference data.

## Usage

To run the Personal Financial Advisor from the project root:

```bash
crewai run
```

Or, to run directly using Python:

```bash
python -m src.persona_finance.main
```

---