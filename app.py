import streamlit as st

from src.graph import graph, qa


st.set_page_config(
    page_title="Autonomous arXiv Paper Digest",
    page_icon="📄",
    layout="wide",
)


st.title("📄 Autonomous arXiv Paper Digest & QA Agent")

st.write(
    "Retrieve an arXiv paper, generate an executive briefing, "
    "and ask questions grounded in the paper."
)

st.divider()

st.subheader("Analyze a Paper")

user_input = st.text_input(
    "Enter a research topic, arXiv paper ID, or arXiv URL:",
    placeholder="e.g. 2506.06962",
)


if st.button("Analyze Paper"):
    if not user_input.strip():
        st.warning(
            "Please enter a topic, arXiv paper ID, or arXiv URL."
        )
    else:
        with st.spinner("Analyzing paper..."):
            result = graph.invoke(
                {"user_input": user_input.strip()}
            )

        st.session_state["paper_result"] = result


# --------------------------------------------------
# Display the analyzed paper
# --------------------------------------------------

result = st.session_state.get("paper_result")


if result:

    if result.get("error"):
        st.error(result["error"])

    else:
        st.success("Paper analyzed successfully.")

        st.divider()

        st.subheader("Executive Briefing")

        st.markdown(
            result.get(
                "briefing",
                "No briefing was generated."
            )
        )

        # --------------------------------------------------
        # QA section
        # --------------------------------------------------

        st.divider()

        st.subheader("Ask Questions About This Paper")

        question = st.text_input(
            "Enter your question:",
            placeholder="e.g. What problem does AR-RAG address?",
        )

        if st.button("Ask Question"):
            if not question.strip():
                st.warning("Please enter a question.")
            else:
                with st.spinner(
                    "Finding the answer in the paper..."
                ):
                    qa_result = qa(
                        {
                            **result,
                            "question": question.strip(),
                        }
                    )
        
                if qa_result.get("error"):
                    st.session_state["qa_error"] = qa_result["error"]
                    st.session_state["qa_answer"] = ""
                else:
                    st.session_state["qa_answer"] = qa_result.get(
                        "answer",
                        "No answer generated."
                    )
                    st.session_state["qa_error"] = ""

        # Display the stored QA result after every Streamlit rerun
        if st.session_state.get("qa_error"):
            st.error(st.session_state["qa_error"])
        
        if st.session_state.get("qa_answer"):
            st.markdown("### Answer")
            st.write(st.session_state["qa_answer"])