import streamlit as st
import time

def main():
    # Set initial time and status
    current_time = 0
    is_adding_time = False

    # Set up Streamlit app
    st.set_page_config(page_title="Time Bank", page_icon=":money_with_wings:")
    st.title("Time Bank")

    # Create bar chart to display time
    time_chart = st.bar_chart({"Time": current_time})

    # Create "Add Time" button
    add_button = st.button("Start Adding Time")

    # Create "Subtract Time" button
    subtract_button = st.button("Start Subtracting Time")

    # Update time on each iteration
    while True:
        if is_adding_time:
            current_time += 1
            time_chart.add_rows({"Time": current_time})

        # Check if "Add Time" button has been clicked
        if add_button:
            # Toggle adding time on or off
            is_adding_time = not is_adding_time

            if is_adding_time:
                add_button.button("Stop Adding Time")
            else:
                add_button.button("Start Adding Time")

        # Check if "Subtract Time" button has been clicked
        if subtract_button:
            current_time -= 1
            time_chart.add_rows({"Time": current_time})

        # Wait 1 second before updating time again
        time.sleep(1)

if __name__ == "__main__":
    main()
