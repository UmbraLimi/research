# tech-006-plugnmeet.md

**Service:** PlugNmeet
**Type:** Video Conferencing / Virtual Classroom
**Website:** https://www.plugnmeet.org/
**Source:** CD-028 (Brian LeBlanc Slack message, Dec 24, 2025)
**Status:** 🔄 EVALUATING (Potential BBB Replacement)

---

## Overview

PlugNmeet positions itself as a **"modern BigBlueButton replacement"** - open-source like BBB but built with newer technology (WebRTC/LiveKit). Brian discovered this after concerns were raised that BBB's software is "quite old and dated."

**Key Value Proposition:**
- Modern, Zoom-like interface (vs BBB's clunky UI)
- Same classroom features as BBB
- Better scalability due to microservices architecture
- Pay-per-session or flat server cost model

---

## Pricing

| Model | Cost | Notes |
|-------|------|-------|
| **Self-Hosted** | Free (VPS cost only) | $5-10/month for VPS, flat rate regardless of user count |
| **Cloud (Flex Plan)** | Flat monthly fee | Based on concurrent usage/capacity, NOT registered users |

**vs BBB/Blindside Networks:** BBB typically charges per-session fees. PlugNmeet's flat rate model could be more cost-effective for high-volume usage.

---

## Interface & UX

- **Modern, responsive, customizable**
- Looks more like **Zoom or Google Meet** than traditional LMS/BBB interfaces
- Drops the "clunky interface" of BBB while keeping classroom features

---

## Features

### Core Video Features
- HD video
- Screen sharing
- Waiting rooms
- Breakout rooms

### Classroom/Education Tools
| Feature | Description |
|---------|-------------|
| **Whiteboard** | Upload PDFs or Office documents and draw on them |
| **Breakout Rooms** | Essential for group work |
| **Polls & Voting** | Instant student feedback |
| **Shared Notepad** | Collaborative note-taking during lecture |
| **Moderator Controls** | Lock students' mics, webcams, or chat permissions (critical for maintaining order) |

### Accessibility
- **AI-powered "Meeting Agent"**
- Live speech-to-text
- Translations
- Significant plus for accessibility compliance

### LMS Integration
- Ready-made plugins for **Moodle, WordPress, Joomla**
- Students can join directly from course pages without separate login
- Retains the deep Moodle/LMS integration that makes BBB popular

---

## Scalability

**Verdict: Highly scalable - more so than BBB**

### BBB Limitations (Why PlugNmeet is Better)
- BBB is **"monolithic"** - heavy and difficult to split across servers
- Scaling BBB requires load balancer redirecting to completely separate servers (adds cost and complexity)

### PlugNmeet Architecture
- Built on **Go and LiveKit** (modern WebRTC infrastructure)
- Uses **microservices approach**

### Scaling Tiers

| Scale | Capability |
|-------|------------|
| **Small** | Single robust server handles hundreds of concurrent users (lightweight software) |
| **Large** | Separate "heavy lifting" components (e.g., Recording engine on cheap separate server so live video isn't slowed) |
| **Massive** | Cluster media servers - distribute video streams across multiple servers while keeping them in same "session" logic. Can handle 1,000+ students |

---

## Fit for PeerLoop

### Alignment with Requirements

| Requirement | PlugNmeet Support |
|-------------|-------------------|
| 1:1 tutoring sessions | ✅ Lightweight, cost-effective for small sessions |
| Group sessions | ✅ Breakout rooms, scales to many concurrent users |
| Recording | ✅ Can run recording on separate server |
| LMS/Course integration | ✅ Plugin ecosystem (though we'd need custom integration) |
| Modern UX | ✅ Zoom-like interface vs BBB's dated look |
| Pay-per-session model | ✅ Self-hosted = flat cost regardless of sessions |
| Education-specific features | ✅ Whiteboard, polls, shared notepad, moderator controls |
| Accessibility | ✅ AI transcription and translation |

### Potential Concerns
- **Newer/less established** than BBB (need to verify production stability)
- **Custom integration needed** - not using Moodle/WordPress plugins directly
- **Self-hosted complexity** - need to manage infrastructure (vs Blindside Networks managed BBB)

---

## Comparison: PlugNmeet vs BBB

| Aspect | BigBlueButton | PlugNmeet |
|--------|---------------|-----------|
| Architecture | Monolithic | Microservices (Go + LiveKit) |
| Interface | Traditional LMS look | Modern Zoom-like |
| Scalability | Difficult (load balancer) | Easy (component separation) |
| Self-hosted cost | Complex setup | $5-10/month VPS |
| Managed hosting | Blindside Networks (per-session) | Cloud Flex Plan (capacity-based) |
| Education features | ✅ Full | ✅ Full (equivalent) |
| LMS plugins | Moodle, WordPress, etc. | Moodle, WordPress, Joomla |
| AI features | Limited | Meeting Agent (transcription, translation) |
| Maturity | Established (10+ years) | Newer (needs verification) |

---

## Recommendation

**PlugNmeet appears to be a strong candidate to replace BBB for PeerLoop.**

### Advantages over BBB:
1. Modern interface (better UX for students)
2. Better scalability architecture
3. Potentially lower cost (flat VPS vs per-session)
4. AI accessibility features built-in
5. Same classroom features

### Next Steps:
1. **Brian to "look deeper"** - awaiting his final assessment
2. Research PlugNmeet documentation and API
3. Evaluate self-hosted vs Cloud pricing for expected scale
4. Check production stability/references
5. Update DIR-001 (MUST-USE BBB) if decision changes

---

## Questions to Resolve

1. **Stability:** Is PlugNmeet production-ready? Any case studies/references?
2. **API:** Does it have the APIs we need for custom integration?
3. **Recording storage:** Where are recordings stored? Can we use our own storage?
4. **Hosted option:** Is the Cloud Flex Plan viable, or should we self-host?
5. **Migration:** If we start with BBB, how hard to switch to PlugNmeet later?

---

## User Stories Covered

Same as BBB (tech-001):
- US-V001-V007 (Video/Session stories)
- US-A013-A018 (Admin video management)
- US-T007 (Student-Teacher sessions)

---

## Source Document

**CD-028:** Brian LeBlanc Slack messages (Dec 24, 2025)
- Context: Fraser's son (former TopHat coder) noted BBB is "quite old and dated"
- Brian researched modern alternatives
- Found PlugNmeet as "Best Modern BBB Replacement"
- Still needs deeper investigation before final decision
