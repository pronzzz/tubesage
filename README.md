# TubeSage: The YouTube Intelligence Engine

![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-0.95+-009688.svg)
![React](https://img.shields.io/badge/React-18+-61DAFB.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

TubeSage is an advanced, AI-driven intelligence system designed to go beyond basic analytics. It uses NLP, predictive modeling, and competitive analysis to provide actionable content strategies for YouTube creators.

**[📚 Read the Comprehensive Guide](GUIDE.md)** | **[🤝 Contributing](CONTRIBUTING.md)** | **[📜 License](LICENSE)**

![TubeSage Dashboard](https://via.placeholder.com/800x400?text=TubeSage+Intelligence+Dashboard)

## 🚀 Key Features

### 🧠 Content Intelligence Engine

- **NLP Analysis**: Extracts entities and keywords from video titles and descriptions using `spaCy`.
- **Semantic Search**: Generates vector embeddings for content to understand semantic similarity using `Sentence Transformers`.

### 📈 Trend Detection & Predictive Modeling

- **Velocity Tracking**: Calculates view velocity and acceleration to detect emerging trends before they peak.
- **Growth Forecasting**: Predicts future video performance using linear regression models.
- **Strategy Simulator**: "What-If" engine to simulate the impact of strategy changes (e.g., "What if I double my upload frequency?").

### ⚔️ Competitor Intelligence

- **Gap Analysis**: Identifies high-performing topics covered by competitors that you are missing.
- **Overlap Mapping**: Visualizes topic intersection between channels using Jaccard Similarity.

### ⚡ Optimization & Architecture

- **Smart Quota Caching**: Dynamic TTL caching (Viral vs. Stagnant content) to minimize YouTube API costs.
- **Batch Processing**: Intelligent request scheduling to respect API limits.
- **Modern Tech Stack**: FastAPI (Python), PostgreSQL, Redis, React + Vite (Glassmorphism UI).

## 🛠️ Installation & Setup

### Prerequisites

- Docker & Docker Compose
- Python 3.11+
- Node.js 18+

### 1. Clone & Configure

```bash
git clone https://github.com/yourusername/tubesage.git
cd tubesage
```

Create a `.env` file in `backend/`:

```env
DATABASE_URL=postgresql+asyncpg://user:password@db/tubesage
REDIS_URL=redis://redis:6379/0
YOUTUBE_API_KEY=your_api_key_here
```

### 2. Run with Docker (Recommended)

```bash
docker compose up -d --build
```

### 3. Manual Run (Development)

**Backend**:

```bash
cd backend
poetry install
poetry run uvicorn app.main:app --reload
```

**Frontend**:

```bash
cd frontend
npm install
npm run dev
```

## 🖥️ Usage

1. Access the **Web Dashboard** at `http://localhost:5173`.
2. View **API Documentation** at `http://localhost:8000/docs`.
3. **Core Endpoints**:
    - `POST /api/v1/analyze/content`: Analyze video title/description.
    - `GET /api/v1/trends/analyze/{video_id}`: Check view velocity trends.
    - `POST /api/v1/predictions/simulate`: Run growth strategy simulations.
    - `POST /api/v1/competitors/analyze`: Compare channel topics.
    - `GET /api/v1/recommendations/{channel_id}`: Get ranked content suggestions.

## 🏗️ Project Structure

- `backend/app/core/intelligence`: NLP & Embeddings.
- `backend/app/core/trends`: Velocity & acceleration logic.
- `backend/app/core/predictions`: Growth models & Simulator.
- `backend/app/core/competitors`: Overlap & Gap detection.
- `backend/app/core/recommendations`: Insight aggregation engine.
- `frontend/`: React + TailwindCSS + Framer Motion UI.

## 📜 License

MIT
