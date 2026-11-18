import streamlit as st
import random, time

st.set_page_config(page_title="Musa Games", page_icon="🎮")
st.title("🎮 MUSA GAMES - 5 Rare Games")

if "level" not in st.session_state:
    st.session_state.level = 1
if "score" not in st.session_state:
    st.session_state.score = 0

st.sidebar.write(f"⭐ Level: {st.session_state.level}")
st.sidebar.write(f"🏆 Score: {st.session_state.score}")
game = st.sidebar.selectbox("Choose Game", ["Memory Maze", "Colour Chaos", "Math Rush", "Word Hunter", "Bomb Defuse"])
level = st.sidebar.slider("Select Level", 1, 5, st.session_state.level)
st.session_state.level = level

if game == "Memory Maze":
    st.header("🧠 Memory Maze")
    st.write(f"Level {level}: Remember {2+level} colours")
    colours = ["🔴", "🔵", "🟢", "🟡", "🟣", "🟠"]
    seq = random.sample(colours, 2+level)
    st.write("Memorize this:", " ".join(seq))
    guess = st.text_input("Type colours e.g. 🔴 🔵 🟢")
    if st.button("Check"):
        if guess.strip() == " ".join(seq):
            st.success("Correct! +100"); st.session_state.score += 100
        else:
            st.error(f"Wrong! It was {' '.join(seq)}")

elif game == "Colour Chaos":
    st.header("🌈 Colour Chaos")
    st.write(f"Level {level}: Click the COLOUR, not the word!")
    words = ["RED", "BLUE", "GREEN", "YELLOW"]
    word = random.choice(words)
    colour = random.choice(words)
    st.markdown(f"### Word is: {word} - But what COLOUR is it written in?")
    choice = st.selectbox("What colour is the word?", words)
    if st.button("Check Colour"):
        if choice == colour:
            st.success("Correct! Your brain is fast! +100"); st.session_state.score += 100
        else:
            st.error(f"No! The real colour was {colour}")

elif game == "Math Rush":
    st.header("⚡ Math Rush")
    a = random.randint(2, 5*level+5)
    b = random.randint(2, 5*level+5)
    op = random.choice(["+", "-", "x"])
    ans = a+b if op=="+" else a-b if op=="-" else a*b
    st.write(f"Level {level}: What is {a} {op} {b} ?")
    user = st.number_input("Your answer", step=1)
    if st.button("Check"):
        if user == ans:
            st.success(f"Correct! +{level*50}"); st.session_state.score += level*50
        else:
            st.error(f"Wrong! Answer was {ans}")

elif game == "Word Hunter":
    st.header("🔤 Word Hunter")
    words_by_level = {1: ["CAT","DOG","SUN"], 2: ["BALL","FISH","LION"], 3: ["PYTHON","FOOTBALL","SCHOOL"], 4: ["COMPUTER","CHAMPION","AFRICA"], 5: ["CHAMPIONSHIP","ENTREPRENEUR","MUSAGAMES"]}
    word = random.choice(words_by_level[level])
    scrambled = "".join(random.sample(word, len(word)))
    st.write(f"Level {level}: Unscramble: **{scrambled}**")
    guess = st.text_input("Your word").upper()
    if st.button("Check"):
        if guess == word:
            st.success(f"Yes! It was {word} +100"); st.session_state.score += 100
        else:
            st.error(f"No! It was {word}")

elif game == "Bomb Defuse":
    st.header("💣 Bomb Defuse")
    secs = 35 - level*5
    st.write(f"Level {level}: You have {secs} seconds! Cut ONE wire!")
    wires = ["🔴 Red", "🔵 Blue", "🟢 Green", "🟡 Yellow", "⚪ White"][:2+level]
    safe = random.choice(wires)
    cut = st.selectbox("Which wire do you cut?", wires)
    if st.button("CUT IT!"):
        if cut == safe:
            st.success("You defused it! +200"); st.session_state.score += 200
            st.balloons()
        else:
            st.error(f"💥 BOOM! The safe wire was {safe}. Game Over!")

if st.button("Next Level Up"):
    if st.session_state.level < 5:
        st.session_state.level += 1
        st.rerun()
