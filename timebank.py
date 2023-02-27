import streamlit as st

# 设置初始累计时长为0
total_time = 0

# 设置柱状图的最大值
max_value = 10

# 定义一个计时器类
class Timer:
    def __init__(self):
        self.start_time = None
        self.total_time = 0
        
    def start(self):
        self.start_time = st.session_state.now
        
    def stop(self):
        elapsed_time = st.session_state.now - self.start_time
        self.total_time += elapsed_time.total_seconds()
        self.start_time = None
        return elapsed_time.total_seconds()

# 创建计时器实例
add_timer = Timer()
subtract_timer = Timer()

# 设置页面标题和初始状态
st.set_page_config(page_title="Add/Subtract Time", page_icon=":watch:", layout="wide")
st.title("Add/Subtract Time")
st.write(f"Total Time: **{total_time:.2f}** seconds")

# 绘制柱状图
st.progress(total_time / max_value)

# 添加“开始增加”按钮
if "add_button" not in st.session_state:
    st.session_state.add_button = st.button("Start Adding")

# 添加“结束增加”按钮
if st.session_state.add_button == False and "stop_add_button" not in st.session_state:
    st.session_state.stop_add_button = st.button("Stop Adding")

# 当点击“开始增加”按钮时
if st.session_state.add_button:
    # 保存当前时间
    st.session_state.now = st.session_state.time or st.session_start_time()
    add_timer.start()
    # 按钮变为“结束增加”
    st.session_state.add_button = False
    st.session_state.stop_add_button = True

# 当点击“结束增加”按钮时
if st.session_state.stop_add_button:
    # 保存当前时间
    st.session_state.now = st.session_state.time or st.session_start_time()
    # 停止计时器并将计时的时长添加到累计时长中
    elapsed_time = add_timer.stop()
    total_time += elapsed_time
    # 更新页面上的累计时长数值和柱状图的长度，并将按钮变回“开始增加”
    st.write(f"Total Time: **{total_time:.2f}** seconds")
    st.progress(total_time / max_value)
    st.session_state.stop_add_button = False
    st.session_state.add_button = True

# 添加“开始扣减”按钮
if "subtract_button" not in st.session_state:
    st.session_state.subtract_button = st.button("Start Subtracting")

# 添加“结束扣减”按钮
if st.session_state.subtract_button == False and "stop_subtract_button" not in st.session_state:
    st.session_state.stop_subtract_button = st.button("Stop Subtracting")

# 当点击“开始扣减”按钮时
if st.session_state.subtract_button:
    # 保存当前时间
    st.session_state.now = st.session_state.time or st.session_start_time()
    subtract_timer.start()
    # 按钮变为“结束扣减”
    st.session_state.subtract_button = False
    st.session_state.stop_subtract_button = True

# 当点击“结束扣减”按钮时
if st.session_state.stop_subtract_button:
    # 保存当前时间
    st.session_state.now = st.session_state.time or st
