# PersonaFinance Crew

PersonaFinance Crew is a multi-agent AI system built with [crewAI](https://crewai.com) to help users organize, analyze, and optimize their personal finances. The system leverages specialized AI agents to collect financial data, analyze spending, generate budgets, and formulate actionable financial plans.

## Features

- **Automated Financial Data Collection:** Securely gather income, expenses, assets, and liabilities.
- **Expense & Income Analysis:** Categorize transactions, identify spending patterns, and calculate cash flow.
- **Budget Proposal Generation:** Create daily, weekly, and monthly budgets with optimization recommendations.
- **Goal Alignment & Strategy:** Translate user goals into actionable financial strategies.
- **Comprehensive Financial Plan:** Generate a user-friendly, actionable plan with charts and recommendations.

## Installation

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
   Add your API keys (e.g., `OPENAI_API_KEY`) to the `.env` file in the `persona_finance` directory.

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

- **src/persona_finance/**: Main crewAI implementation and configuration.
- **pfa/**: Alternative or experimental financial agent framework.
- **output/**: Generated reports and analysis.
- **knowledge/**: User preferences and reference data.

## Usage

To run the PersonaFinance Crew from the project root:

```bash
crewai run
```

Or, to run directly using Python:

```bash
python -m src.persona_finance.main
```

## Customization

- **Agents:** Edit `src/persona_finance/config/agents.yaml`
- **Tasks:** Edit `src/persona_finance/config/tasks.yaml`
- **Crew Logic:** Edit `src/persona_finance/crew.py`
- **Inputs/Execution:** Edit `src/persona_finance/main.py`

## Output

- Analytical reports and budget proposals are saved in the `output/` directory as JSON files.
- Final financial plans can be generated in PDF or Markdown formats.

## Support

- [crewAI Documentation](https://docs.crewai.com)
- [GitHub Issues](https://github.com/joaomdmoura/crewai)
- [Discord Community](https://discord.com/invite/X4JWnZnxPb)

---
