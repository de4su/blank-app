# � Steam Game Recommendation Quiz

An interactive web application built with Streamlit that recommends Steam games based on your gaming preferences through an engaging quiz.

## Features

- **Interactive Decision-Tree Quiz**: 6 carefully crafted questions covering:
  - Gaming genre preferences (Shooter, RPG, Puzzle, Platformer)
  - Play style (Single-player, Multiplayer, Party)
  - Difficulty level (Casual to Extremely Hard)
  - Game setting (Fantasy, Sci-fi, Sandbox)
  - Pacing preferences (Fast-paced, Relaxing, Strategic)
  - Game mechanics (Competitive, Exploration, Combat, Building)

- **Smart Tag-Based Matching**: Accumulates your preferences as tags and matches them against 15 carefully curated Steam games

- **Top 3 Recommendations**: Shows your best matches with:
  - Game banner images from Steam CDN
  - Match score percentage
  - Direct links to Steam store pages
  - Explanation of why each game matches your preferences

- **Responsive UI**: Progress indicator, clean interface, and start-over functionality

## Installation

### Prerequisites
- Python 3.8+
- pip (Python package installer)

### Setup Instructions

1. **Clone or download this repository**
   ```bash
   cd steam-game-recommendation-quiz
   ```

2. **Create a virtual environment (optional but recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   streamlit run streamlit_app.py
   ```

5. **Open in browser**
   - The app will automatically open at `http://localhost:8501`
   - If not, manually navigate to that URL

## Project Structure

```
steam-game-recommendation-quiz/
├── streamlit_app.py          # Main Streamlit application
├── requirements.txt          # Python dependencies
├── README.md                 # This file
├── data/
│   ├── questions.json        # Quiz questions and options with associated tags
│   └── games.json            # Game database with Steam app IDs and metadata
└── services/
    └── matching.py           # Tag-based recommendation algorithm
```

## How It Works

### Quiz Flow
1. User answers 6 questions about their gaming preferences
2. Each answer adds relevant tags to their profile (e.g., "shooter", "hard", "multiplayer")
3. Tags accumulate throughout the quiz
4. Upon completion, accumulated tags are matched against game profiles

### Matching Algorithm
The recommendation engine uses a simple but effective tag-matching algorithm:
- **Match Score** = (Matching Tags / Total User Tags) × 100%
- Games are ranked by how many of the user's preference tags they contain
- Top 3 matches are displayed with detailed information

### Session State Management
- Uses Streamlit's `st.session_state` to track:
  - Current question number
  - Accumulated user tags
  - Quiz completion status
- Enables seamless navigation without page reloads

## Game Database

The app includes 15 popular Steam games across different genres:

| Game | Genre | Tags | Steam ID |
|------|-------|------|----------|
| Counter-Strike 2 | Shooter | fps, multiplayer, competitive | 730 |
| Elden Ring | RPG | rpg, hard, souls-like, fantasy | 1245620 |
| Portal 2 | Puzzle | puzzle, physics, scifi | 620 |
| Stardew Valley | Simulation | farming, casual, rpg | 413150 |
| The Witness | Puzzle | puzzle, hard, logic | 210970 |
| Hollow Knight | Metroidvania | hard, fantasy, metroidvania | 367520 |
| Celeste | Platformer | platformer, hard, action | 504230 |
| Among Us | Party | party, multiplayer, casual | 945360 |
| Terraria | Sandbox | sandbox, adventure, multiplayer | 105600 |
| And 6 more... | Various | Various | Various |

## Customization

### Adding New Games
Edit `data/games.json`:
```json
{
  "id": 123456,
  "name": "Game Title",
  "app_id": 123456,
  "tags": ["tag1", "tag2", "tag3"],
  "store_url": "https://store.steampowered.com/app/123456"
}
```

### Adding New Questions
Edit `data/questions.json`:
```json
{
  "id": 7,
  "question": "Your question here?",
  "options": [
    {
      "text": "Option text",
      "tags": ["tag1", "tag2"]
    }
  ]
}
```

### Modifying Tags
Tags are arbitrary strings that connect quiz answers to games. Common tags include:
- Genres: `shooter`, `rpg`, `puzzle`, `platformer`, `metroidvania`, `sandbox`
- Playstyle: `singleplayer`, `multiplayer`, `party`
- Difficulty: `casual`, `hard`
- Setting: `fantasy`, `scifi`
- Mechanics: `competitive`, `farming`, `physics`, `logic`, `action`, `adventure`

## Deployment

### Streamlit Community Cloud (Free)

1. **Push to GitHub**
   - Create a GitHub repository
   - Push this project to the repository

2. **Connect to Streamlit Cloud**
   - Go to [share.streamlit.io](https://share.streamlit.io)
   - Sign in with GitHub
   - Click "New app"
   - Select your repository, branch, and main file (`streamlit_app.py`)
   - Click "Deploy"

3. **Your app is live!**
   - Streamlit will provide a public URL
   - Share it with others

### Local Deployment

For local testing and development:
```bash
streamlit run streamlit_app.py
```

## Code Style

The project follows PEP 8 Python style guidelines with:
- Type hints for function parameters and returns
- Comprehensive docstrings for all functions
- Small, focused functions (single responsibility)
- Clear comments for complex logic
- Modular structure separating concerns

## Dependencies

- **streamlit** (1.28.1): Framework for building the web interface
- **pandas** (2.1.3): Data manipulation and analysis (for potential enhancements)

## Troubleshooting

### "Module not found" error
- Ensure you've installed dependencies: `pip install -r requirements.txt`
- Check that you're running from the correct directory

### Game images not loading
- This uses Steam's CDN - verify the Steam app IDs are correct
- Check your internet connection

### Quiz not progressing
- Clear browser cache and refresh
- Try a different browser
- Check browser console for JavaScript errors

## Future Enhancements

Potential improvements:
- Add filters (price range, release date)
- User ratings and reviews integration
- Wishlist sync with Steam
- More detailed game information
- Weighted tag scoring
- User preference history

## License

See LICENSE file for details.

## Contributing

Contributions are welcome! Feel free to:
- Add new games to the database
- Improve the matching algorithm
- Add more quiz questions
- Enhance the UI/UX
- Fix bugs

## Support

For issues, questions, or suggestions, please open an issue on GitHub.

---

**Happy gaming! 🎮**

### How to run it on your own machine

1. Install the requirements

   ```
   $ pip install -r requirements.txt
   ```

2. Run the app

   ```
   $ streamlit run streamlit_app.py
   ```
