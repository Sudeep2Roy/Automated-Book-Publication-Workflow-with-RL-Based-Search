
def simulate_feedback(state, version_tag):
    good_choices = {
        "vivid": "ai-written",
        "formal": "reviewed",
        "short": "final",
        "creative": "ai-written"
    }
    if good_choices[state] == version_tag:
        return 10
    elif version_tag in good_choices.values():
        return 5
    else:
        return -5
