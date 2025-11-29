# Alpha Peer - Client Documents Index

**Purpose:** Track all client-provided documents with upload dates and concise summaries focused on utility for Needs.md creation.

**Process for adding new documents:**
1. Drop file(s) into `/MyResearch/file_holding/` on your Mac
2. Drag file(s) from file_holding into Claude Desktop chat
3. Type `/add-client-doc` (no parameters needed)
4. Claude automatically:
   - Detects which files were uploaded
   - Reads and analyzes each document
   - Moves files to `/client-docs/`
   - Adds entries to this index
   - Deletes files from file_holding
   - Updates session file

**Supports batch processing:** Drag multiple files at once and use single `/add-client-doc` command.

---

## Document Entries

### Alpha_Peer_Business_Plan_92825old.pdf
**Date Uploaded:** 2025-11-25  
**Summary for Needs.md:**

Comprehensive business plan defining Alpha Peer's core concept: a peer-to-peer AI education platform built on a "Learn, Teach, Earn" flywheel model.

**Key elements for Needs.md:**
- **Business Model:** Three-sided network (Course Creators, Student-Teachers, Students) with 15/15/70 revenue split
- **Core User Journey:** Students master courses, become Student-Teachers, earn 70% commission teaching others
- **Value Propositions:** 
  - Creators: 15% perpetual royalty, community ownership tools
  - Student-Teachers: Earn while mastering material (protégé effect)
  - Students: Recoup 70% of course fee by teaching one peer
- **Pedagogical Foundation:** Solves Bloom's 2-Sigma Problem through scalable 1-on-1 peer tutoring
- **Target Market:** Initially AI education (strategic beachhead), expandable to any skill-based learning
- **Platform Features:** Creator community hubs, forums, role management, peer verification systems
- **Go-to-Market:** Phase 1: Recruit 10-15 AI educators; Phase 2: Genesis cohorts; Phase 3: Flywheel ignition
- **Competitive Differentiation:** Creates new category vs. Coursera/Udemy's linear marketplace model
- **Monetization:** 15% platform fee per transaction, scalable through network effects

**Technical Implications:**
- Needs user roles system (Creator, Student-Teacher, Student)
- Payment/commission distribution engine (15/15/70 split)
- Course mastery verification system
- Community features (forums, chat, role management)
- Student-to-teacher transition workflow
- Creator community hub infrastructure

**Non-Functional Requirements:**
- Must support exponential growth (viral flywheel)
- Quality assurance through peer verification
- Secure payment processing
- Community engagement metrics
- Student-to-teacher conversion rate tracking

---

### Feature_Summary_WIPold.pdf
**Date Uploaded:** 2025-11-29
**Summary for Needs.md:**

Detailed feature specification and UI/UX design document outlining the complete platform architecture for Rapid Learning Community (Alpha Peer). Includes 11 pages of UI mockups created with Cursor.

**Key elements for Needs.md:**
- **Three Core Pillars:**
  1. Community Flywheel: Learn → Certify → Teach → Grow cycle (based on "Helper Therapy Principle")
  2. Monetization Engine: 70% Student-Teacher, 15% Creator, 15% Platform split (flexible per creator, platform minimum required)
  3. Credentialing System: Learning Certificates, Teaching Certificates, Community Roles (paid assistants with revenue sharing), Reputation System

- **Core Features to Build:**
  - **Creator & Course Hub:** Open EdX LMS integration, flexible assessments, creator profiles
  - **Algorithmic X.com-Style Feed:** Intelligent content prioritization, teacher discovery, session booking/purchasing
  - **Student Lifecycle Engine:** Unified dashboard, dual-certificate system, public profiles, gated communities, earnings tracking
  - **Screen Sharing:** Big Blue Button integration for peer-to-peer sessions with flexible content delivery (BYO lesson plans, web apps)
  - **AI Integration:** Strategic force multiplier for personalization and efficiency

- **UI/UX Navigation Structure (with mockups in PDF):**
  - Browse Menu: Course search, Creator/Instructor search with detailed profiles
  - My Community: X.com-style algorithmic feed of followed content
  - Dashboard: Student/teacher activity tracking, calendar, quick actions
  - Messages: Private messaging system
  - Profile: Student-Teacher vs Creator-Instructor views with "Switch User" and "Creator Studio" buttons

- **Course Detail Page Elements:**
  - Curriculum outline with time estimates
  - Creator profile card with stats (Active Student-Teachers, Avg Taught per Teacher, badges)
  - Action buttons: Enroll, Explore Teaching, Follow Course, Join Community
  - Related courses suggestions

- **Tech Stack Decisions:**
  - LMS: Open EdX for content creation and delivery
  - Social Feed: Bluesky protocol for community posts
  - Video: Big Blue Button for 1-on-1 sessions with screen sharing

**Technical Implications:**
- Integration layer between Open EdX, Bluesky, and Big Blue Button
- Algorithmic feed engine for content relevance and engagement
- Dual-mode profile system (Student-Teacher vs Creator-Instructor)
- Certificate issuance and verification system (Teaching Certificate dynamically updates with student count)
- Revenue tracking and distribution dashboard
- Gated community access control based on credentials
- Real-time scheduling and video conferencing integration
- Creator Studio for course management (Open EdX wrapper)
- Community Roles system with revenue sharing for creator assistants

**Non-Functional Requirements:**
- Social media-like endless scrolling engagement ("TikTok for education")
- Simple, clean X.com-inspired interface design
- Seamless role switching between student and creator modes
- Real-time updates for community feed
- Scalable video conferencing infrastructure
- Flexible revenue split configuration per creator (with platform minimum)

**Key Design Decisions:**
- X.com interface pattern for familiarity and engagement
- Community feed as marketing funnel (discovery → enrollment)
- Creator control over community organization and content delivery
- Screen sharing enables web-based collaborative learning beyond LMS constraints
- AI as fabric-level integration, not add-on feature
- "Switch User" button enables fluid role transitions within single account

---

## Index Statistics
- **Total Documents:** 2
- **Last Updated:** 2025-11-29
