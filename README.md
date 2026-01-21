# GenAI Agent–Driven ETL Pipeline (PoC)

This project demonstrates a **Generative AI-powered ETL agent** that can intelligently orchestrate Extract–Transform–Load (ETL) workflows using Python, SQL, and APIs.  

> **Note:** This is a Proof of Concept (PoC) to showcase AI-driven ETL orchestration. Not intended for production deployment.

---

## Table of Contents

- [Overview](#overview)  
- [Problem Scope](#problem-scope)  
- [Architecture](#architecture)  
- [ETL Flow Example](#etl-flow-example)  
- [Tooling Stack](#tooling-stack)  
- [Trade-offs & Limitations](#trade-offs--limitations)  
- [Adaptation Scenarios](#adaptation-scenarios)  
- [How to Run](#how-to-run)  
- [Console Output Example](#console-output-example)  
- [Philosophy](#philosophy)  

---

## Overview

The GenAI ETL agent is capable of:

- Understanding input data schemas.
- Reasoning about necessary transformations.
- Orchestrating ETL steps automatically.
- Handling errors and revising plans as needed.

**Goal:** Show how AI agents can improve adaptability, automation, and intelligence in data pipelines.

---

## Problem Scope

| Aspect | Details |
|--------|---------|
| Source | CSV files (e.g., sales transaction data) |
| Target | SQLite database (conceptual data warehouse) |
| Scale | Small-to-medium datasets (PoC) |
| Focus | AI-driven design, reasoning, and decision-making for ETL |

---

## Architecture

The GenAI agent acts as the **brain** of the system, orchestrating ETL tools.

