---
name: serving-api
description: Generate a FastAPI model serving endpoint with input validation. Use during CRISP-DM Deployment phase.
argument-hint: "[model path]"
user-invocable: true
---

# Model Serving API Generator (CRISP-DM Phase 6)

Generate a serving API for: $ARGUMENTS

Create:
1. `src/serving/app.py` -- FastAPI app with:
   - `/predict` endpoint with Pydantic input validation
   - `/health` health check endpoint
   - `/model-info` endpoint returning model card metadata
   - Input validation matching the training feature schema
   - Preprocessing pipeline (same as training)
   - Structured logging with correlation IDs
   - Error handling for malformed inputs
2. `src/serving/schemas.py` -- Pydantic models for request/response
3. `Dockerfile` -- Container for the serving app
4. `tests/test_serving.py` -- Tests for the API
5. Update requirements.txt with serving dependencies (fastapi, uvicorn, pydantic)
