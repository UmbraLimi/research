# Conversation Lifecycle Flowchart

## Mermaid Diagram

```mermaid
flowchart TD
    START([Starting Work]) --> RSTART["/r-start<br/><i>pull → inc conv → push → resume</i>"]

    RSTART --> WORK

    WORK(["★ WORK ★<br/><i>optional /r-commit mid-session</i>"])

    WORK --> Q2{Done for the day?}

    Q2 -->|YES| REND_QUIT["/r-end<br/><i>eos → commit → push</i>"]
    REND_QUIT --> EXIT([exit Claude Code])

    Q2 -->|NO| Q3{Need fresh context?<br/><i>token limit, new task, etc.</i>}

    Q3 -->|NO| KEEP["Just keep working!<br/><i>/r-commit if you want<br/>to save progress</i>"]
    KEEP --> WORK

    Q3 -->|YES| REND_CONT["/r-end<br/><i>eos → commit → push</i>"]
    REND_CONT --> RPRECLEAR["/r-pre-clear<br/><i>save state → inc conv → STOP</i>"]
    RPRECLEAR --> CLEAR["/clear<br/><i>you type this manually</i>"]
    CLEAR --> RSTART2["/r-start<br/><i>you type this manually</i>"]
    RSTART2 --> WORK

    style WORK fill:#ffd700,stroke:#333,color:#000
    style EXIT fill:#90ee90,stroke:#333,color:#000
    style KEEP fill:#e0e0e0,stroke:#333,color:#000
    style CLEAR fill:#ffb3b3,stroke:#333,color:#000
    style RPRECLEAR fill:#ffb3b3,stroke:#333,color:#000
    style RSTART fill:#87ceeb,stroke:#333,color:#000
    style RSTART2 fill:#87ceeb,stroke:#333,color:#000
    style REND_QUIT fill:#87ceeb,stroke:#333,color:#000
    style REND_CONT fill:#87ceeb,stroke:#333,color:#000
```

## ASCII Flowchart

```
┌─────────────────────────────────────────┐
│           STARTING WORK                 │
│                                         │
│  Always run /r-start                    │
│  (handles both cold + warm starts)      │
└──────────────┬──────────────────────────┘
               │
      ┌────────▼────────┐
      │    /r-start     │
      │                 │
      │ pull → inc conv │
      │ → push → resume │
      └────────┬────────┘
               │
               ▼
┌──────────────────────────┐
│                          │
│        ★ WORK ★          │
│                          │
│  (optional mid-session   │
│   /r-commit as needed)   │
│                          │
└────────────┬─────────────┘
             │
             ▼
┌──────────────────────────┐
│   READY TO SAVE WORK     │
│                          │
│   Am I done for the day? │
└────────────┬─────────────┘
             │
   ┌─────────┴─────────┐
   │                   │
┌──▼──┐           ┌────▼────┐
│ YES │           │   NO    │
└──┬──┘           └────┬────┘
   │                   │
   │                   ▼
   │         ┌──────────────────┐
   │         │ Do I need fresh  │
   │         │ context?         │
   │         │ (token limit,    │
   │         │  new task, etc.) │
   │         └────────┬─────────┘
   │                  │
   │           ┌──────┴──────┐
   │           │             │
   │      ┌────▼────┐   ┌───▼─────┐
   │      │  YES    │   │   NO    │
   │      └────┬────┘   └────┬────┘
   │           │             │
   │           │             ▼
   │           │    ┌─────────────────┐
   │           │    │  Just keep      │
   │           │    │  working!       │
   │           │    │                 │
   │           │    │  /r-commit if   │
   │           │    │  you want to    │
   │           │    │  save progress  │
   │           │    └─────────────────┘
   │           │
   │           ▼
   │  ┌─────────────────────┐
   │  │     /r-end          │
   │  │                     │
   │  │ eos → commit → push │
   │  └─────────┬───────────┘
   │            │
   │            ▼
   │  ┌─────────────────────┐
   │  │   /r-pre-clear      │
   │  │                     │
   │  │ save state →        │
   │  │ inc conv → STOP     │
   │  └─────────┬───────────┘
   │            │
   │            ▼
   │  ┌─────────────────────┐
   │  │   /clear            │
   │  │   (you type this)   │
   │  └─────────┬───────────┘
   │            │
   │            ▼
   │  ┌─────────────────────┐
   │  │   /r-start          │
   │  │   (you type this)   │
   │  │                     │
   │  │ pull → inc conv →   │
   │  │ push → resume       │
   │  └─────────┬───────────┘
   │            │
   │            ▼
   │     back to ★ WORK ★
   │
   ▼
┌─────────────────────┐
│      /r-end         │
│                     │
│ eos → commit → push │
└─────────┬───────────┘
          │
          ▼
┌─────────────────────┐
│      exit           │
│                     │
│  Close terminal or  │
│  Ctrl-C / "exit"   │
└─────────────────────┘
```

## Quick Reference

| I want to...                        | Run                                      |
|-------------------------------------|------------------------------------------|
| Start working (any context)         | `/r-start`                               |
| Save & keep working (fresh context) | `/r-end` → `/r-pre-clear` → `/clear` → `/r-start` |
| Save & keep working (same context)  | `/r-commit`                              |
| Save & quit for the day             | `/r-end` → `exit`                        |
| Save state without ending conv      | `/r-save-state`                          |
| Switch to other machine             | `/r-end` → `exit` → (other machine) `/r-start` |

## What Each Command Does

```
/r-start   = pull + increment conv + push + show resume context
/r-end     = session docs + commit + push + cleanup .conv-current
/r-pre-clear   = save state + increment conv locally + STOP (then YOU run /clear)
/r-resume  = read RESUME-STATE.md + PLAN.md (no git sync) — called internally by /r-start
/r-commit  = commit this folder only (Conv + Machine in message)
```
