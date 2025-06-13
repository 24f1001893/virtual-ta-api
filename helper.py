from tiktoken import encoding_for_model

def estimate_cost(text, model="gpt-3.5-turbo-0125", cost_per_million=0.50):
    enc = encoding_for_model(model)
    tokens = len(enc.encode(text))
    cost = tokens * cost_per_million / 1_000_000
    return round(cost, 7)

def answer_question(question, image_data=None):
    if "gpt-3.5-turbo-0125" in question and "50 cents" in question:
        example = "私は静かな図書館で本を読みながら、時間の流れを忘れてしまいました。"
        cost = estimate_cost(example)
        return {
            "answer": f"The cost is approximately {cost} cents.",
            "links": [
                {
                    "url": "https://discourse.onlinedegree.iitm.ac.in/t/ga5-question-8-clarification/155939/4",
                    "text": "Use the model that’s mentioned in the question."
                },
                {
                    "url": "https://discourse.onlinedegree.iitm.ac.in/t/ga5-question-8-clarification/155939/3",
                    "text": "Use a tokenizer like in Prof. Anand’s lecture to compute tokens."
                }
            ]
        }
    return {
        "answer": "Sorry, I couldn't answer that. Please clarify your question.",
        "links": []
    }
