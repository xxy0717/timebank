import streamlit as st
import datetime

def main():
    st.set_page_config(page_title="Time Bank", page_icon="⏰")

    # Initialize state variables
    st.session_state.time_bank = datetime.timedelta(seconds=0)
    st.session_state.is_adding_time = False
    st.session_state.is_subtracting_time = False
    st.session_state.time_since_last_update = datetime.datetime.now()

    # Set up layout
    st.title("Time Bank")
    st.write("Click the buttons below to add or subtract time.")
    st.write("Time added is displayed in green, time subtracted in red.")
    st.write("Current Time Bank Balance:")
    time_bank_display = st.empty()
    st.write("")

    add_button = st.button("Add Time")
    subtract_button = st.button("Subtract Time")

    # Update time bank and display
    while True:
        current_time = datetime.datetime.now()
        time_delta = current_time - st.session_state.time_since_last_update
        st.session_state.time_since_last_update = current_time
        if st.session_state.is_adding_time:
            st.session_state.time_bank += time_delta
            time_bank_display.write(
                f"<div style='color:green;font-size:64px;'>{str(st.session_state.time_bank)}</div>",
                unsafe_allow_html=True,
            )
        elif st.session_state.is_subtracting_time:
            st.session_state.time_bank -= time_delta
            time_bank_display.write(
                f"<div style='color:red;font-size:64px;'>{str(st.session_state.time_bank)}</div>",
                unsafe_allow_html=True,
            )
        else:
            time_bank_display.write(
                f"<div style='font-size:64px;'>{str(st.session_state.time_bank)}</div>",
                unsafe_allow_html=True,
            )
        if st.session_state.is_adding_time and not add_button:
            st.session_state.is_adding_time = False
            add_button = st.button("Add Time")
        elif not st.session_state.is_adding_time and add_button:
            st.session_state.is_adding_time = True
            add_button = st.button("Stop Adding Time")
        if st.session_state.is_subtracting_time and not subtract_button:
            st.session_state.is_subtracting_time = False
            subtract_button = st.button("Subtract Time")
        elif not st.session_state.is_subtracting_time and subtract_button:
            st.session_state.is_subtracting_time = True
            subtract_button = st.button("Stop Subtracting Time")

if __name__ == "__main__":
    main()
