"""
Steam Game Recommendation Quiz Web Application
A Streamlit-based interactive quiz that recommends Steam games based on user preferences.
"""
import json
import streamlit as st
from pathlib import Path
from services.matching import get_recommendations


# Configure page
st.set_page_config(
    page_title="Steam Game Recommendation Quiz",
    page_icon="🎮",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS
st.markdown("""
    <style>
    .game-card {
        background-color: #f0f0f0;
        padding: 20px;
        border-radius: 10px;
        margin: 10px 0;
        border-left: 4px solid #1f1f1f;
    }
    .match-score {
        font-size: 24px;
        font-weight: bold;
        color: #2ecc71;
    }
    .progress-container {
        background-color: #e0e0e0;
        border-radius: 10px;
        padding: 10px;
        margin: 10px 0;
    }
    </style>
""", unsafe_allow_html=True)


def load_questions() -> dict:
    """Load quiz questions from JSON file."""
    questions_path = Path(__file__).parent / "data" / "questions.json"
    with open(questions_path, "r") as f:
        return json.load(f)


def load_games() -> dict:
    """Load game database from JSON file."""
    games_path = Path(__file__).parent / "data" / "games.json"
    with open(games_path, "r") as f:
        return json.load(f)


def initialize_session_state() -> None:
    """Initialize Streamlit session state variables."""
    if "current_question" not in st.session_state:
        st.session_state.current_question = 0
    if "user_tags" not in st.session_state:
        st.session_state.user_tags = []
    if "quiz_complete" not in st.session_state:
        st.session_state.quiz_complete = False


def reset_quiz() -> None:
    """Reset quiz to start over."""
    st.session_state.current_question = 0
    st.session_state.user_tags = []
    st.session_state.quiz_complete = False


def display_progress(current: int, total: int) -> None:
    """Display progress indicator for current question."""
    progress_percent = (current / total) * 100
    st.markdown(f"""
    <div class="progress-container">
        <p style="margin: 0;">Question {current} of {total}</p>
        <div style="background-color: #ddd; border-radius: 5px; overflow: hidden;">
            <div style="background-color: #2ecc71; height: 8px; width: {progress_percent}%;"></div>
        </div>
    </div>
    """, unsafe_allow_html=True)


def display_question(question: dict, question_num: int, total_questions: int) -> None:
    """Display a quiz question with options."""
    st.markdown(f"### {question['question']}")
    
    # Create buttons for each option
    selected_option = None
    cols = st.columns(len(question["options"]))
    
    for idx, (col, option) in enumerate(zip(cols, question["options"])):
        with col:
            if st.button(option["text"], key=f"option_{idx}", use_container_width=True):
                selected_option = idx
    
    return selected_option


def display_results(recommendations: list) -> None:
    """Display game recommendations based on quiz results."""
    st.markdown("## 🎮 Your Game Recommendations")
    
    if not recommendations:
        st.warning("No matches found. Try the quiz again!")
        return
    
    for idx, (game, score) in enumerate(recommendations, 1):
        col1, col2 = st.columns([1, 2])
        
        with col1:
            # Display game banner image
            app_id = game.get("app_id")
            img_url = f"https://cdn.akamai.steamstatic.com/steam/apps/{app_id}/header.jpg"
            st.image(img_url, use_column_width=True)
        
        with col2:
            st.markdown(f"### #{idx} - {game['name']}")
            st.markdown(f"<p class='match-score'>Match: {score:.1f}%</p>", unsafe_allow_html=True)
            
            # Display matching tags
            user_tags_set = set(st.session_state.user_tags)
            game_tags_set = set(game.get("tags", []))
            matching_tags = user_tags_set & game_tags_set
            
            if matching_tags:
                tags_str = ", ".join(sorted(matching_tags))
                st.markdown(f"**Matching preferences:** {tags_str}")
            
            # Steam store link
            store_url = game.get("store_url", "")
            if store_url:
                st.markdown(f"[🔗 View on Steam Store]({store_url})")
        
        st.divider()


def main() -> None:
    """Main application logic."""
    st.title("🎮 Steam Game Recommendation Quiz")
    st.markdown("Answer a few questions about your gaming preferences and we'll recommend the perfect games for you!")
    
    # Initialize session state
    initialize_session_state()
    
    # Load data
    questions_data = load_questions()
    games_data = load_games()
    
    questions = questions_data["questions"]
    games = games_data["games"]
    total_questions = len(questions)
    
    # Quiz flow
    if not st.session_state.quiz_complete:
        # Display progress
        display_progress(st.session_state.current_question + 1, total_questions)
        
        # Get current question
        current_q = questions[st.session_state.current_question]
        
        # Display question
        st.markdown("---")
        st.markdown(f"### {current_q['question']}")
        
        # Create columns based on number of options
        num_options = len(current_q["options"])
        cols = st.columns(num_options)
        
        # Display options as clickable buttons in columns
        for idx, (col, option) in enumerate(zip(cols, current_q["options"])):
            with col:
                if st.button(option["text"], use_container_width=True, key=f"q{st.session_state.current_question}_opt{idx}"):
                    # Add tags to user selections
                    st.session_state.user_tags.extend(option["tags"])
                    
                    # Move to next question or complete quiz
                    if st.session_state.current_question < total_questions - 1:
                        st.session_state.current_question += 1
                        st.rerun()
                    else:
                        st.session_state.quiz_complete = True
                        st.rerun()
    
    else:
        # Quiz complete - show results
        st.markdown("## ✨ Quiz Complete!")
        st.markdown(f"Based on your preferences: **{', '.join(st.session_state.user_tags)}**")
        st.divider()
        
        # Get recommendations
        recommendations = get_recommendations(st.session_state.user_tags, games)
        
        # Display results
        display_results(recommendations)
        
        # Start over button
        if st.button("🔄 Start Over", use_container_width=True):
            reset_quiz()
            st.rerun()


if __name__ == "__main__":
    main()
