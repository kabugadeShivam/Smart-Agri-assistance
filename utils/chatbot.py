import pandas as pd

knowledge = pd.read_csv("data/agriculture_knowledge.csv")


def ask_ai(question):

    question = question.lower()

    for _, row in knowledge.iterrows():

        if row["Question"].lower() in question:

            return row["Answer"]

    return (
        "I don't have an exact answer. "
        "Please consult an agricultural expert or expand the knowledge base."
    )