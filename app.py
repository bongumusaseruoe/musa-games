import streamlit as st
import random
import time

st.set_page_config(page_title="MUSA GAMES", layout="wide")
st.title("MUSA GAMES - 5 Rare Games")

if "score" not in st.session_state:
    st.session_state.score = 0
if "level" not in st.session_state:
    st.session_state.level = 1

st.sidebar.write(f"Level: {st.session_state.level}")
st.sidebar.write(f"Score: {st.session_state.score}")
game = st.sidebar.selectbox("Choose Game", ["Memory Maze", "Colour Chaos", "Math Rush", "Word Hunter", "Bomb Defuse"])
level = st.sidebar.slider("Select Level", 1, 5, 1)
st.session_state.level = level

# 1. MEMORY MAZE - PC VERSION
if game == "Memory Maze":
    st.header("Memory Maze")
    colours = ["RED", "BLUE", "GREEN", "YELLOW", "PURPLE", "ORANGE"]
    n = 2 + level
    if "seq" not in st.session_state or st.button("New Sequence"):
        st.session_state.seq = [random.choice(colours) for _ in range(n)]
    st.write(f"Level {level}: Remember {n} colours")
    st.write("Memorize this: " + " - ".join(st.session_state.seq))
    st.write("Tip: Write them down on paper, then type below")
    ans = st.text_input("Type colours e.g. RED BLUE GREEN")
    if st.button("Check"):
        user = ans.upper().replace(",", " ").split()
        if user == st.session_state.seq:
            st.success("Correct! +100 points")
            st.session_state.score += 100
            st.session_state.seq = [random.choice(colours) for _ in range(n)]
        else:
            st.error(f"Wrong! It was: {' '.join(st.session_state.seq)}")
    if st.button("Next Level Up"):
        st.session_state.level = min(5, level + 1)
        st.rerun()

# 2. COLOUR CHAOS
elif game == "Colour Chaos":
    st.header("Colour Chaos")
    st.write("What COLOUR is the word written in? Not what the word says!")
    words = ["RED", "BLUE", "GREEN", "YELLOW"]
    word = random.choice(words)
    colour = random.choice([w for w in words if w != word])
    st.markdown(f"<h1 style='color:{colour.lower()}'>{word}</h1>", unsafe_allow_html=True)
    ans = st.text_input("Type the COLOUR you see (not the word)")
    if st.button("Check"):
        if ans.upper().strip() == colour:
            st.success("Correct! +100")
            st.session_state.score += 100
        else:
            st.error(f"Wrong! The colour was {colour}")
    if st.button("New Word"):
        st.rerun()

# 3. MATH RUSH
elif game == "Math Rush":
    st.header("Math Rush")
    if "a" not in st.session_state or st.button("New Question"):
        st.session_state.a = random.randint(2, 12) * level
        st.session_state.b = random.randint(2, 12)
        st.session_state.op = random.choice(["+", "-", "x"])
    a, b, op = st.session_state.a, st.session_state.b, st.session_state.op
    st.write(f"What is {a} {op} {b} ?")
    ans = st.number_input("Your answer", value=0, step=1)
    if st.button("Check"):
        correct = a+b if op=="+" else a-b if op=="-" else a*b
        if ans == correct:
            st.success("Correct! +100")
            st.session_state.score += 100
            st.session_state.a = random.randint(2, 12) * level
            st.session_state.b = random.randint(2, 12)
            st.session_state.op = random.choice(["+", "-", "x"])
        else:
            st.error(f"Wrong! Answer was {correct}")

# 4. WORD HUNTER
elif game == "Word Hunter":
    st.header("Word Hunter")
    words = ["MUSA", "GAME", "SOWETO", "PYTHON", "STREAMLIT", "AFRICA", "FOOTBALL"]
    w = random.choice(words)
    scrambled = "".join(random.sample(w, len(w)))
    st.write(f"Unscramble: **{scrambled}**")
    ans = st.text_input("What is the word?")
    if st.button("Check"):
        if ans.upper().strip() == w:
            st.success("Correct! +100")
            st.session_state.score += 100
        else:
            st.error(f"Wrong! It was {w}")
    if st.button("New Word"):
        st.rerun()

# 5. BOMB DEFUSE
elif game == "Bomb Defuse":
    st.header("Bomb Defuse")
    st.write("Cut the correct wire! Hint: Cut wire number 2 to win, others explode.")
    col1, col2, col3, col4 = st.columns(4)
    if col1.button("Cut Wire 1 - RED"):
        st.error("BOOM! Wrong wire!")
    if col2.button("Cut Wire 2 - BLUE"):
        st.success("You defused it! +200 points")
        st.session_state.score += 200
    if col3.button("Cut Wire 3 - GREEN"):
        st.error("BOOM! Wrong wire!")
    if col4.button("Cut Wire 4 - YELLOW"):
        st.error("BOOM! Wrong wire!")
