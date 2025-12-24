# Questions for Brian

**Purpose:** Consolidated list of all open questions requiring Brian's input, organized by source document.

**Last Updated:** 2025-12-24

---

## From CD-005: Slack - GetStream Feed Discussion

1. **GetStream.io vs Bluesky protocol** - CD-002 (Nov 29) mentions Bluesky protocol for community, but CD-005 (Nov 13) mentions GetStream.io. CD-008 clarified "feeds only" from Stream. Is Bluesky still in consideration, or is GetStream.io the confirmed choice?

---

## From CD-007 & CD-028: Video Platform Decision

2. **Video platform final decision** - Originally three options (Daily.co, Digital Samba, BBB). CD-009 confirmed Blindside Networks for BBB. BUT CD-028 introduces **PlugNmeet** as modern BBB replacement. What is the final choice?
   - **PlugNmeet:** Modern UI, microservices architecture, flat pricing ($5-10/mo self-hosted), same classroom features as BBB
   - **BBB:** Established but "old and dated", monolithic architecture, per-session fees via Blindside
   - **Daily.co/Digital Samba:** P2P options for 1:1 cost savings

3. **PlugNmeet evaluation status** - Brian mentioned needing to "look deeper" at PlugNmeet. What's the verdict? Should DIR-001 (MUST-USE BigBlueButton) be updated?

4. **Single platform or hybrid?** - Should we use one video solution for everything, or different solutions for different use cases (1:1 vs group)?

---

## From CD-010: Miro Board - Main Activities by Role

5. **Newsletter with subscription payments** - Is a paid newsletter feature planned? Document mentions "Newsletter possibility with subscription payments" as a question.

---

## From CD-011: Miro Board - Drivers & Action Items

6. **AI Assistant technology** - Document lists AI Assistant for Students as "TBD". What is the scope and technology choice for AI assistance? MVP or post-MVP?

7. **Newsletters technology** - Document lists Newsletters as "TBD". What is the scope for newsletters? Is this related to the paid newsletter question in CD-010?

8. **Bluesky vs GetStream.io** - CD-011 explicitly mentions Bluesky for community tool, but CD-005/CD-008/CD-013 confirm GetStream.io for feeds. Which is correct? Are both used for different purposes?

9. **Certificate of Mastery vs Completion** - Document mentions two certificate types. What's the difference? How does a student earn Mastery vs Completion? Is Mastery MVP or post-MVP?

---

## From CD-018: Student Profile System

10. **Profile visibility default** - Should new profiles default to Public or Private? Document notes "default TBD".

---

## From CD-027: Prototype Walkthrough

### Community & Feed Structure
11. **Community Structure** - Is instructor community the same as `instructor_followers` from CD-024, or a separate entity?

12. **Channels within Communities** - Are "Everyone" and "creator-2" (seen in post badges) channels/sub-groups, or test artifacts?

13. **Auto-join Rules** - Which communities do new users automatically join? Just Town Hall, or also some instructors?

14. **Course vs Instructor Feed Access** - User pays for course → gets course feed access. User pays for ANY course from instructor → gets instructor feed access. Is this correct?

### Sessions & Availability
15. **Availability States** - Just Available/Unavailable, or more states (Busy, Away, etc.)?

16. **Session Booking Integration** - Is booking calendar-first (schedule then get BBB/PlugNmeet link), or video-platform-first?

17. **Group Sessions** - Are group sessions (4+ students) part of MVP? Prototype shows "Group Session · 4 students" in Teaching Dashboard.

### Role-Specific Features
18. **Creator Dashboard** - Does Creator need a separate "Creator Studio" or third tab beyond Learning/Teaching? Currently Creator shows identical view to Student-Teacher.

19. **Admin Features** - What admin capabilities are needed for MVP vs post-MVP? Current prototype has no admin implementation.

### Course Content
20. **Homework System** - Is homework submission/grading part of MVP? Prototype shows detailed homework tracking with due dates and scores.

21. **Session Resources** - Are per-session resources (Recording, Slides, Code Files) stored in platform or external links (like course content)?

### UX Decisions
22. **User Menu in Header** - Confirm need for header user dropdown with avatar, settings, logout? Currently missing from prototype.

---

## Summary

| Source | Questions |
|--------|-----------|
| CD-005 | 1 |
| CD-007 & CD-028 | 3 |
| CD-010 | 1 |
| CD-011 | 4 |
| CD-018 | 1 |
| CD-027 | 12 |
| **Total** | **22** |

---

## How to Use This Document

1. Review questions before meeting with Brian
2. Check off or annotate answers as received
3. After answers received, update relevant docs (SPECS.md, architecture docs)
4. Move answered questions to "Resolved" section below

---

## Resolved Questions

*(Move questions here after Brian answers them, with the answer noted)*

| Question | Answer | Date | Updated In |
|----------|--------|------|------------|
| - | - | - | - |
