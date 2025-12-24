# RUN Index

**Purpose:** Quick reference to all RUN phase scenarios and their status.

**Last Updated:** 2025-12-24

---

## Active Runs

| Run | Date | Base | Status | Key Decisions |
|-----|------|------|--------|---------------|
| [RUN-001](run-001/run-001.md) | 2025-12-24 | sc-002 | **Under Review** | Stream + VideoProvider, Cloudflare stack, 144 P0 stories |

---

## Approved Scenario

**Current:** None yet

*When a run is approved, its scenario.md will be copied to `/runs/approved/SPECS.md` and then to root `SPECS.md` for handoff.*

---

## Run Status Legend

| Status | Meaning |
|--------|---------|
| **Draft** | Being generated |
| **In Progress** | Generation complete, under review |
| **Under Review** | Awaiting client feedback |
| **Approved** | Client approved, ready for handoff |
| **Rejected** | Not proceeding with this approach |
| **Superseded** | Replaced by a later run |

---

## Workflow

1. Create new run folder: `run-NNN/`
2. Fill in `run-NNN.md` with inputs and parameters
3. Generate `scenario.md` based on inputs
4. Review with client, document in `review-notes.md`
5. Record decisions in run file
6. Update status in this index
7. If approved: copy to `/approved/SPECS.md`

---

## Statistics

| Metric | Value |
|--------|-------|
| Total Runs | 1 |
| Approved | 0 |
| Rejected | 0 |
| In Progress | 1 |
