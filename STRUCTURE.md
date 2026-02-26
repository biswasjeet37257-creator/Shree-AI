# ShreeApp Build Structure

## Backend (`/backend`)
- `main.py`: FastAPI entry point with orchestration routes (`/ask`, `/system/report`, `/memory/search`, `/memory/stats`).
- `core/orchestrator.py`: Logic for smart-routing, failover, monetary tracking, and **Semantic Memory retrieval** (cosine-similarity on vector embeddings).
- `db/models.py`: SQLAlchemy/PGVector models for Harvesting (with SQLite/JSON fallback).
- `db/database.py`: Async database engine with PostgreSQL → SQLite auto-fallback.
- `initialize_db.py`: Script to create all database tables.
- `requirements.txt`: Python dependency list.

## Frontend (`/frontend`)
- `pages/index.tsx`: The Radiant Chat Interface with Crystal Core, **Markdown rendering**, **Memory toggle**, model selector, and voice I/O.
- `pages/oversight.tsx`: The Intelligence Dashboard — pulls **live data** from `/system/report` for provider health, latency spectrum, and autonomous suggestions.
- `components/RadiantIcon.tsx`: Three.js / R3F component for the animated crystal core.
- `styles/globals.css`: Core design system with animations and glow effects.
- `package.json`: Frontend dependency list.

## Ecosystem Model Architecture (2026)
- **Diagnostics**: `nvidia/nemotron-3-nano-30b-a3b:free`
- **Orchestration**: `arcee-ai/trinity-mini:free`
- **Vision**: `qwen/qwen3-vl-30b-a3b-thinking`
- **Strategy**: `openai/gpt-oss-120b:free`
- **Edge UI**: `google/gemma-3n-e2b-it:free`
- **Creative Image**: `black-forest-labs/flux.2-max`
- **Logic Filter**: `liquid/lfm-2.5-1.2b-thinking:free`
- **Translation**: `sarvam-m`

## Deployment
- `Dockerfile`: Multi-stage build (Node + Python) for production deployment.
- `docker-entrypoint.sh`: Startup script for containerized deployment.
- `.dockerignore`: Build context exclusions.

## Documentation
- `MANIFESTO.md`: The 2026 vision, legal framework, and detailed description of the 8-model ecosystem.

---
**Status**: Core Intelligence Node Operational + Semantic Memory Active.
**Completed Features**:
- ✅ Multi-API Orchestration mapped to the 8-Model "Bhuban Ecosystem" roles.
- ✅ Smart intent-based routing (code, reasoning, image, summarization, general).
- ✅ Monetary tracking with shadow-cost analysis.
- ✅ Semantic Memory — Vector DB harvesting + cosine-similarity retrieval (Semantic Caching).
- ✅ Live Oversight Dashboard with real API health data for Developer Control.
- ✅ Voice input + Text-to-Speech handling.
- ✅ PII scrubbing before data harvest.

**Next Steps**:
- Connect the frontend app logic to strictly assign models dynamically based on user intent (Bhuban Video vs Creator App flows).
- Implement specific API Rate Limit Queues for free limits.
- Enforce "Consent Architecture" logic in DB.
