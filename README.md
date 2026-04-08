---
title: CyberGuard
emoji: 🛡️
colorFrom: red
colorTo: blue
sdk: docker
pinned: false
tags:
  - openenv
  - cybersecurity
  - reinforcement-learning
---

# CyberGuard — Cyber Scam Detection Environment

## Description
CyberGuard is a real-world OpenEnv environment that trains AI agents to detect cyber scams including phishing emails, fake OTP messages, SMS fraud, and suspicious links.

## Action Space
- `safe` — genuine message
- `suspicious` — needs review
- `highly_suspicious` — likely a scam
- `scam` — confirmed scam, block immediately

## Observation Space
- `message` — raw text message
- `message_type` — email/sms
- `difficulty` — easy/medium/hard
- `done` — episode finished
- `reward` — score received

## Tasks
- **Easy** — Obvious scams, multiple red flags, reward +0.5
- **Medium** — Mixed signals, 1-2 red flags, reward +0.7
- **Hard** — Realistic messages, subtle red flags, reward +1.0

## Reward Function
| Difficulty | Correct | Wrong |
|------------|---------|-------|
| Easy | +0.5 | 0.0 |
| Medium | +0.7 | 0.1 |
| Hard | +1.0 | 0.2 |
| One level off | +0.3 | — |

## Setup
```bash
pip install -r requirements.txt
uvicorn server.app:app --host 0.0.0.0 --port 8000
```

## Run Inference
```bash
python inference.py
```