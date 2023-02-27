import streamlit as st
from streamlit import session_state as state
import datetime

def main():
    st.title("Time Bank")

    # Initialize session state variables
    state.start_adding = False
    state.start_deducting = False
    state.total_time = datetime.timedelta(seconds=0)

    # Create the "Add Time" button
    add_button_text = "Start Adding Time" if not state.start_adding else "Stop Adding Time"
    add_button = st.button(add_button_text)

    # Create the "Deduct Time" button
    deduct_button_text = "Start Deducting Time" if not state.start_deducting else "Stop Deducting Time"
    deduct_button = st.button(deduct_button_text)

    # Create the "Reset Time" button
    reset_button = st.button("Reset Time")

    # Calculate total time
    if state.start_adding:
        state.total_time += datetime.timedelta(seconds=1)
    if state.start_deducting:
        state.total_time -= datetime.timedelta(seconds=1)

    # Update the UI
    st.write(f"Total Time: {state.total_time}")
    st.bar_chart({"total time": state.total_time.total_seconds()})

    # Handle button clicks
    if add_button_text == "Start Adding Time":
        state.start_adding = True
    else:
        state.start_adding = False

    if deduct_button_text == "Start Deducting Time":
        state.start_deducting = True
    else:
        state.start_deducting = False

    if reset_button:
        state.total_time = datetime.timedelta(seconds=0)

if __name__ == "__main__":
    main()
