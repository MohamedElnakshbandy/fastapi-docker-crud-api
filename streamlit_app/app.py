import requests
import streamlit as st

API_URL = "http://api:8000"

st.set_page_config(
    page_title="FastAPI + Celery Demo",
    page_icon=":rocket:",
    layout="centered",
)

st.title("FastAPI + Celery Demo")
st.write("Submit a background task and monitor its progress.")

st.divider()

x = st.number_input(
    "First Number",
    value=1,
    step=1,
)

y = st.number_input(
    "Second Number",
    value=2,
    step=1,
)

if st.button("Submit Task"):
    try:
        response = requests.post(
            f"{API_URL}/tasks/slow-add",
            params={"x": x, "y": y},
            timeout=10,
        )
        response.raise_for_status()

        task_id = response.json()["task_id"]
        st.session_state["task_id"] = task_id

        st.success("Task submitted successfully!")
        st.code(task_id)

    except requests.RequestException as error:
        st.error(f"Could not submit task: {error}")

if "task_id" in st.session_state:
    st.divider()

    st.write("Current Task ID:")
    st.code(st.session_state["task_id"])

    if st.button("Check Task Status"):
        try:
            response = requests.get(
                f"{API_URL}/tasks/{st.session_state['task_id']}",
                timeout=10,
            )
            response.raise_for_status()
            task_data = response.json()

            st.write(f"Status: **{task_data['status']}**")

            if task_data["status"] == "SUCCESS":
                st.success(f"Result: {task_data['result']}")
            elif task_data["status"] == "FAILURE":
                st.error(task_data.get("error", "Task failed"))
            else:
                st.info("The task is still running.")

            st.json(task_data)

        except requests.RequestException as error:
            st.error(f"Could not check task status: {error}")