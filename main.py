from src.graph import graph, qa


def main():
    print("=== Autonomous arXiv Paper Digest & QA Agent ===")

    user_input = input(
        "\nEnter a topic, arXiv paper ID, or arXiv URL: "
    ).strip()

    if not user_input:
        print("Please provide an input.")
        return

    print("\nProcessing paper...")

    result = graph.invoke({
        "user_input": user_input,
    })

    if result.get("error"):
        print("\nERROR:")
        print(result["error"])
        return

    print("\n" + "=" * 60)
    print("EXECUTIVE BRIEFING")
    print("=" * 60)

    print(result.get("briefing", "No briefing generated."))

    print("\n" + "=" * 60)
    print("PAPER QA")
    print("=" * 60)

    while True:
        question = input(
            "\nAsk a question about the paper "
            "(type 'exit' to quit): "
        ).strip()

        if question.lower() == "exit":
            print("\nExiting agent. Goodbye!")
            break

        if not question:
            print("Please enter a question.")
            continue

        qa_result = qa(
            {
                **result,
                "question": question,
            }
        )

        if qa_result.get("error"):
            print("\nERROR:")
            print(qa_result["error"])
            continue

        print("\nAnswer:")
        print(qa_result.get("answer", "No answer generated."))


if __name__ == "__main__":
    main()