# Agentic AI-Powered Multi-Tenant Promotion Engine

An AI-driven SaaS platform for creating, verifying, and applying promotional coupons, where **agentic AI workflows** autonomously evaluate business intent and decide whether a promotion should be activated, blocked, or require clarification before reaching checkout.

---

## Overview

Traditional coupon systems directly execute predefined rules.
This project introduces an **agentic decision layer** where AI assists in **design-time reasoning**, while execution remains **deterministic and performant**.

Key principle:

> AI designs and verifies promotion rules.
> Code executes promotions at runtime.

---

## Core Capabilities

* Multi-tenant SaaS architecture with organization-level isolation
* API key–based authentication per organization
* Natural language coupon creation using AI
* Agentic verification to assess safety, completeness, and business risk
* Deterministic coupon application engine for checkout flows
* Admin visibility into AI-generated rules and agent decisions

---

## Agentic Behavior Explained

The system is agentic because it **decides what to do next**, not just what to generate.

For each coupon creation request, the system autonomously decides to:

* Activate the coupon
* Block the coupon due to safety or risk
* Request clarification due to incomplete intent

These decisions are persisted and auditable.

---

## High-Level Architecture

```
Merchant Input (Natural Language)
            |
            v
     AI Rule Generator
            |
            v
  Agentic Verification Layer
            |
   --------------------------
   |        |               |
 ACTIVE   NEED_INFO       BLOCKED
            |
            v
 Deterministic Coupon Engine
            |
            v
     Checkout Application
```

---

## Tech Stack

* Backend: Django, Django REST Framework
* Language: Python
* AI Integration: OpenAI API
* Database: SQLite (development), PostgreSQL (production-ready)
* Authentication: API Key–based multi-tenancy
* Tooling: Git, Curl, Django Admin

---

## Project Structure

```
coupon_system/
├── core/
│   ├── agents/          # AI rule generation and agentic verification
│   ├── rules/           # Deterministic coupon evaluation logic
│   ├── auth.py          # Organization API key authentication
│   ├── models.py        # Organization and Coupon models
│   ├── views.py         # Coupon creation and application APIs
│   └── admin.py         # Admin configuration
├── coupon_system/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
└── db.sqlite3
```

---

## Setup Instructions

### Prerequisites

* Python 3.10 or higher
* pip
* Virtual environment support

---

### 1. Clone Repository

```bash
git clone git@github.com:priyanshu-kr03/promoflow-ai.git
cd promoflow-ai
```

---

### 2. Create and Activate Virtual Environment

```bash
python -m venv .venv
source .venv/bin/activate
```

---

### 3. Install Dependencies

```bash
pip install django djangorestframework openai python-dotenv
```

---

### 4. Environment Variables

Create a `.env` file in the project root:

```env
OPENAI_API_KEY=your_openai_api_key_here
```

---

### 5. Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

---

### 6. Create Admin User

```bash
python manage.py createsuperuser
```

---

### 7. Run Server

```bash
python manage.py runserver
```

The application will be available at:

```
http://127.0.0.1:8000/
```

---

## Admin Panel

Access the admin interface at:

```
http://127.0.0.1:8000/admin/
```

From the admin panel you can:

* Create organizations (API keys auto-generated)
* View coupons and their agentic decision status
* Inspect AI-generated rule configurations
* Review verification notes and decisions

---

## API Usage

### Create Coupon (Agentic Verification)

```bash
curl -X POST http://127.0.0.1:8000/api/coupons/create/ \
  -H "Content-Type: application/json" \
  -H "X-API-KEY: <ORGANIZATION_API_KEY>" \
  -d '{
    "code": "NEW10",
    "description": "10% off for first time users above 500, max discount 100"
  }'
```

---

### Apply Coupon (Checkout)

```bash
curl -X POST http://127.0.0.1:8000/api/coupons/apply/ \
  -H "Content-Type: application/json" \
  -H "X-API-KEY: <ORGANIZATION_API_KEY>" \
  -d '{
    "coupon_code": "NEW10",
    "order": {
      "amount": 1200
    }
  }'
``` 

---

## Design Decisions

* AI is used only at **coupon creation time**, never during checkout
* Coupon application logic is deterministic and low-latency
* All AI decisions are persisted for auditability
* Multi-tenancy is enforced at the data and API layers

---

## Future Enhancements

* Coupon usage limits and redemption tracking
* Clarification resubmission workflow
* Coupon simulation before activation
* Organization-level analytics
* Subscription and rate limiting

---

## License

This project is intended for learning, demonstration, and portfolio purposes.

---
