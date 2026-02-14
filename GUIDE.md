# TubeSage Comprehensive Guide

Welcome to the detailed guide for **TubeSage**. This document provides an in-depth look at the system architecture, core components, and the verification phases used to ensure system integrity.

## System Architecture

TubeSage is built as a modular intelligence engine for YouTube creators. It consists of a FastAPI backend and a React frontend.

### Backend (`/backend`)

The backend is structured into several core modules:

1. **Intelligence Engine (`app.core.intelligence`)**:
    - Uses `spaCy` for Natural Language Processing to extract entities and keywords.
    - Uses `Sentence Transformers` to create vector embeddings for semantic search.
2. **Trend Detection (`app.core.trends`)**:
    - Calculates view velocity and acceleration.
    - Detects emerging trends based on growth patterns.
3. **Predictive Modeling (`app.core.predictions`)**:
    - Predicts future video performance using linear regression models.
    - Simulates "What-If" scenarios to forecast the impact of strategy changes.
4. **Competitor Intelligence (`app.core.competitors`)**:
    - Analyzes overlap between channels using Jaccard Similarity.
    - Identifies content gaps (topics your competitors cover that you don't).
5. **Optimization (`app.core.optimization`)**:
    - **Smart Cache**: Dynamic TTL (Time-To-Live) based on content "virality". Viral content is cached for shorter periods, while stagnant content is cached longer to save API quota.
    - **Batch Scheduler**: Intelligent request scheduling.

### Frontend (`/frontend`)

The frontend is a modern React application using:

- **Vite**: For fast build tooling.
- **TailwindCSS**: For utility-first styling.
- **Framer Motion**: For smooth animations.
- **Glassmorphism**: For a premium, modern UI aesthetic.

## Feature Walkthrough & Verification

The project includes a set of verification scripts to demonstrate and test each core component.

### Phase 1: Setup Verification (`verify_setup.py`)

Ensures that the environment is correctly configured.

- Loads configuration settings.
- Verifies database models (`Channel`, `Video`, `MetricTimeSeries`).
- Checks YouTube Client and Database connectivity modules.

### Phase 2: Intelligence Engine (`verify_phase2.py`)

Tests the NLP and Embedding capabilities.

- Verifies `spaCy` installation.
- Verifies `sentence_transformers` installation.
- Loads the `analyzer` module.
- *Note*: Requires model weights to be downloaded for full functionality.

### Phase 3: Trend Detection (`verify_phase3.py`)

Validates the mathematics behind trend analysis.

- **Velocity Calculator**: Tests calculation of view growth over time.
- **Trend Detector**: Identifies if a series is "Accelerating", "Stable", or "Decelerating".

### Phase 4: Predictive Modeling (`verify_phase4.py`)

Demonstrates the forecasting engine.

- **Growth Predictor**: projects future views based on historical data.
- **Strategy Simulator**: Simulates scenarios like "Doubling upload frequency" and estimates the impact on views (e.g., using elasticity models).

### Phase 5: Competitor Intelligence (`verify_phase5.py`)

Tests the comparative analysis algorithms.

- **Overlap Analyzer**: Calculates how similar two channels are based on topic intersection.
- **Gap Detector**: Identifies topics present in a competitor's channel but missing from yours.

### Phase 6: Optimization & Quota Management (`verify_phase6.py`)

Verifies the smart infrastructure that saves API costs.

- **Smart Cache**: Checks if TTL adjusts dynamically (e.g., Viral = 1 hour, Stagnant = 7 days).
- **Batch Scheduler**: Tests the ability to process multiple items in chunks to respect rate limits.

### Phase 7: Recommendation Engine (`verify_phase7.py`)

The final output of the system.

- Generates actionable recommendations based on all previous analyses.
- Sorts recommendations by "Impact Score" to prioritize high-value actions.

## Getting Started

To start the application, refer to the `README.md` for Docker or manual installation instructions.
