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

## Core Features Deep Dive

This section provides an in-depth look at the capabilities of each core component.

### 1. Intelligence Engine

The brain of TubeSage, responsible for understanding content semantics.

- **NLP Parsing**: Extracts key entities and topics from video titles/descriptions.
- **Semantic Embeddings**: Vectorized representations of content allow for "meaning-based" search rather than just keyword matching.

### 2. Trend Detection

Validates the mathematics behind trend analysis.

- **Velocity Calculator**: Calculates view growth over time to determine momentum.
- **Trend Detector**: Identifies if a series is "Accelerating", "Stable", or "Decelerating".

### 3. Predictive Modeling

The forecasting engine that powers decision making.

- **Growth Predictor**: Projects future views based on historical data using linear regression.
- **Strategy Simulator**: Simulates scenarios like "Doubling upload frequency" and estimates the impact on views (e.g., using elasticity models).

### 4. Competitor Intelligence

Comparative analysis identifying market opportunities.

- **Overlap Analyzer**: Calculates how similar two channels are based on topic intersection.
- **Gap Detector**: Identifies topics present in a competitor's channel but missing from yours.

### 5. Optimization & Quota Management

Smart infrastructure that saves API costs and ensures scalability.

- **Smart Cache**: Adjusts TTL dynamically (e.g., Viral content caches for 1 hour, Stagnant for 7 days).
- **Batch Scheduler**: Processes API requests in optimal chunks to respect rate limits.

### 6. Recommendation Engine

The final output of the system.

- **Recommendation Generator**: Generates actionable recommendations based on all previous analyses.
- **Impact Scoring**: Sorts recommendations by "Impact Score" to prioritize high-value actions.

## Getting Started

To start the application, refer to the `README.md` for Docker or manual installation instructions.
