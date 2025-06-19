from langgraph.graph import StateGraph, END
from agents.candidate_profile_analyzer import analyze_candidate_profiles
from agents.company_preference_modeler_rag import extract_company_preferences
from agents.fit_scoring_agent import compute_fit_scores

def step_analyze(state):
    return {"analyzed": analyze_candidate_profiles(state["students"])}

def step_extract_prefs(state):
    return {"prefs": extract_company_preferences(state["role"])}

def step_rank(state):
    return {"ranked": compute_fit_scores(state["analyzed"], state["prefs"]) }

workflow = StateGraph()
workflow.add_node("analyze_candidates", step_analyze)
workflow.add_node("extract_prefs", step_extract_prefs)
workflow.add_node("score_candidates", step_rank)
workflow.set_entry_point("analyze_candidates")
workflow.add_edge("analyze_candidates", "extract_prefs")
workflow.add_edge("extract_prefs", "score_candidates")
workflow.set_finish_point("score_candidates")
executor = workflow.compile()

if __name__ == "__main__":
    sample = {
        "students": [{"name": "Nisha", "resume": "Skilled in Python, ML, AWS"}],
        "role": {"role": "ML Engineer", "description": "..."}
    }
    result = executor.invoke(sample)
    print(result)
