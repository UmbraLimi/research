# Alpha Peer - Client Documents Index

**Purpose:** Track all client-provided documents with upload dates and concise summaries focused on utility for SPECS.md creation.

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

### CD-001: Alpha_Peer_Business_Plan_92825old.pdf
**Date Uploaded:** 2025-11-25
**Summary for SPECS.md:**

Comprehensive business plan defining Alpha Peer's core concept: a peer-to-peer AI education platform built on a "Learn, Teach, Earn" flywheel model.

**Key elements for SPECS.md:**
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

### CD-002: Feature_Summary_WIPold.pdf
**Date Uploaded:** 2025-11-29
**Summary for SPECS.md:**

Detailed feature specification and UI/UX design document outlining the complete platform architecture for Rapid Learning Community (Alpha Peer). Includes 11 pages of UI mockups created with Cursor.

**Key elements for SPECS.md:**
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

### CD-003: Alpha Peer User Stories • Nov 29 2025.pdf
**Date Uploaded:** 2025-11-29
**Summary for SPECS.md:**

Working-level user stories document defining routine operational needs across 6 user roles. Organized as "mini user stories" in tabular format.

**Key elements for SPECS.md:**

- **User Roles Defined:**
  1. **Admin (AP Rep):** Platform operations and oversight
  2. **Creator-Instructor:** Course creators who also teach
  3. **Student:** Learners who can progress to teaching
  4. **Student-Teacher:** Students who have leveled up to teach
  5. **Employer/Funder:** Third parties paying for student enrollment
  6. **Tutor Session:** System entity for live sessions

- **Admin/Platform Needs:**
  - Enroll and cancel teachers/students (with reasons)
  - Payment distribution from enrollments; refunds and chargebacks
  - Vet teacher certificates
  - Third-party organization billing with progress/completion reporting
  - Email marketing for referrals from students/teachers
  - Facilitate video sessions with recording, AI summaries/transcripts, time tracking, screen sharing
  - Store session metadata (date/time/participants)
  - Analytics: user retention, course stats, fee tracking, session monitoring, student-to-teacher conversion, grade averages, user acquisition sources

- **Creator-Instructor Needs:**
  - Availability calendar for tutoring
  - Course content management: syllabi, quizzes, reference materials, completion criteria, progression/leveling
  - Rich profile (pictures, videos, PDFs)
  - Session/student cancellation
  - Vet and monitor student-turned-teachers
  - Messaging: students, AP platform
  - Course retirement
  - Certificate granting
  - Student progress assessments
  - Referral capability
  - AI assistance during sessions
  - Earn teaching certificates (displayed on profile)

- **Student Needs:**
  - Pay for tutors; view available courses
  - Profile with public/private sections
  - Cancel course (with reason); reschedule/cancel sessions
  - Messaging: teachers, other students (noted as "tricky"), AP
  - Referral capability
  - Apply for teacher status
  - AI assistance during sessions

- **Student-Teacher Needs:**
  - Availability calendar
  - Rich profile (pictures, videos, PDFs)
  - Session cancellation
  - Messaging: students, AP
  - Grant completion certificates
  - Referral capability
  - AI assistance during sessions

- **Employer/Funder Needs:**
  - Pay for student course enrollment
  - Receive student progress/completion reports
  - Receive copy of certifications
  - Profile (potentially all private)
  - Messaging: AP, their funded students

- **Tutor Session Requirements:**
  - Video chat with participant limits
  - In-session messaging and file sharing
  - Time monitoring
  - Conversation recording
  - Post-session assessment by each participant

**Technical Implications:**
- Multi-role user system with role-specific permissions and views
- Payment processing: enrollment fees, refunds, chargebacks, third-party billing
- Video conferencing integration with recording, AI transcription, screen sharing
- Session data storage with comprehensive metadata
- Messaging system with role-based routing (student-to-student flagged as complex)
- Certificate issuance and verification system
- Course lifecycle management (create, update, retire)
- Analytics dashboard for platform metrics
- Referral tracking system
- AI integration for in-session assistance

**Non-Functional Requirements:**
- Secure payment handling with chargeback support
- Video session reliability and quality
- Data retention for session recordings and transcripts
- Privacy controls for employer/funder profiles
- Scalable messaging infrastructure
- Real-time session monitoring capabilities

**New Requirements Not in Previous Docs:**
- Employer/Funder role (B2B sponsorship model)
- Chargeback handling for teacher cancellations
- Post-session mutual assessments
- Course retirement workflow
- Student-to-student messaging (flagged as needing careful design)
- User acquisition source tracking

---

### CD-004: The Impact Filter 110425 Mission Statement.pdf
**Date Uploaded:** 2025-11-29
**Summary for SPECS.md:**

Strategic planning document (dated 10/29/2025) using the "Impact Filter" framework to define Alpha Peer's purpose, success criteria, and vision. Authored by Brian LeBlanc.

**Key elements for SPECS.md:**

- **Purpose Statement:**
  Launch Alpha Peer as a functioning peer-to-peer learning platform for AI education with three founding course creators. Validate that students transition to paid Student-Teachers, proving the learn-teach-earn flywheel creates self-sustaining teaching capacity.

- **Quantified Success Criteria (MVP Validation Targets):**
  | Metric | Target | Rationale |
  |--------|--------|-----------|
  | Student-to-Teacher Conversion | 10% (ideal: 20%) | Proves flywheel creates value beyond learning |
  | Student-Teacher Satisfaction | ≥95% | Validates peer teachers can effectively guide others |
  | Learning Outcomes (grades) | ≥90% average | Maintains educational quality |
  | Course Completion Rate | ≥75% | Far above MOOC industry average of 15-20% |
  | Monthly Active User Retention | 60% higher than traditional platforms | Measured via login frequency, forum participation, session bookings |
  | Student-Teacher Recruitment | ≥2 new students per teacher in first 3 months | Evidence of exponential growth pattern |
  | Break-even Timeline | 12 months to cover operational costs | 15% platform fee viability at scale |

- **Ideal Outcome Vision:**
  - Three thriving course communities with daily peer-to-peer teaching
  - Collaborative (not transactional) atmosphere
  - Creators earn meaningful income while Student-Teacher networks expand organically
  - Creators spend time deepening content rather than repetitive teaching
  - Students feel connected; don't want to let peers down
  - Student-Teachers report deeper mastery through teaching

- **Best Result (Success Vision):**
  - Each founder creator builds 50+ active Student-Teachers
  - Sustainable income streams for creators
  - Students earn back course fees by teaching others
  - Attracts investment interest
  - Expansion beyond AI into other skill-based learning
  - Creates new category in online education

- **Worst Result (Failure Scenario):**
  - Miss critical window in AI education market
  - Model remains theoretical and unproven
  - Competitor captures space with inferior approach
  - Course creators stuck in one-to-many teaching models

- **Monetization Note:**
  - 15% platform fee as primary revenue
  - Also considering monthly subscription fee for creators

- **Core Philosophy:**
  - Solves the "2 Sigma Problem" by democratizing 1-on-1 tutoring
  - Teaching deepens understanding for both parties (protégé effect)
  - Education as reciprocal relationship, not one-way transaction
  - Aligns financial incentives with pedagogical best practices

**Technical Implications:**
- Analytics dashboard must track all success metrics listed above
- Student-to-teacher conversion funnel tracking
- Satisfaction/rating system for peer teaching sessions
- Grade/assessment tracking at course and platform level
- User retention and engagement metrics
- Referral tracking (students recruited per teacher)
- Revenue/transaction volume reporting

**Non-Functional Requirements:**
- Platform must support 3 creators with 50+ Student-Teachers each at MVP
- Performance to enable daily peer-to-peer session activity
- Forum and community engagement features
- Session booking system

**Key Insights for Development:**
- MVP scope: 3 founding creators, their initial cohorts
- Primary validation: Does the flywheel work? (conversion rate is key metric)
- Quality bar: 75% completion, 90% grades, 95% satisfaction
- Growth proof: Each teacher recruits 2+ students in 3 months

---

### CD-005: Slack Message - GetStream Feed Discussion
**Date Uploaded:** 2025-11-30
**Original Date:** 2025-11-13
**Summary for SPECS.md:**

Client Slack message clarifying technology preferences and MVP priorities for the social feed component.

**Key elements for SPECS.md:**

- **Technology Decision:** GetStream.io mentioned as preferred solution for algorithmic feed
  - Specifically wants the "feed option" from GetStream
  - Target UX: X.com, Skool.com, Substack.com style feeds
  - Purpose: "users to gather in a common area and see relevant posts based on their interests"

- **MVP Requirements (client's stated priorities):**
  1. Profiles
  2. Payments
  3. Calendar options
  4. Algorithmic feed (interest-based content)

- **Discord Evaluation:**
  - Acceptable as temporary solution for initial technical users
  - Client explicitly states: "I really don't like the idea of discord"
  - "would be ok for technical users who we will target initially"
  - Must be replaced by in-site X.com-style feed "in the near future"
  - Discord is a compromise, not a preference

- **Feed Vision:**
  - Common gathering area for users
  - Interest-based content relevance ("relevant posts based on their interests")
  - Social media-style engagement pattern (X.com, Skool.com, Substack.com)

**Technical Implications:**
- GetStream.io integration for activity feeds (or equivalent)
- Interest/preference system for algorithmic content delivery
- Profile system must support feed interactions
- Calendar integration for scheduling
- Payment processing for transactions

**Relationship to Other Docs:**
- Reinforces CD-002's "Algorithmic X.com-Style Feed" requirement
- Provides specific technology choice (GetStream.io) vs CD-002's mention of Bluesky protocol
- **Chronology Note:** This message (Nov 13) predates CD-002 (Nov 29)
- **⚠️ Requires Clarification:** GetStream.io vs Bluesky protocol—which is current preference? Later document (CD-002) typically takes precedence, but Stream is already marked REQUIRED in tech research

**Goals Referenced:** GO-010 (Community & Engagement Features)
**Stories Referenced:** US-S025, US-P002

---

### CD-006: Slack Message - Calendar, BBB, Discord Discussion
**Date Uploaded:** 2025-11-30
**Original Date:** 2025-11-16
**Summary for SPECS.md:**

Client Slack message clarifying infrastructure priorities and technology decisions for scheduling, video, and real-time communication.

**Key elements for SPECS.md:**

- **Calendar Feature:** "Full blown calendar feature" required
  - Rationale: Avoid manual behind-the-scenes scheduling management
  - Core MVP component alongside profiles
  - Client quote: "we don't have to try and keep up behind the scenes with scheduling"

- **Video Conferencing:** BigBlueButton (BBB) confirmed
  - Use hosted service providers (not self-hosted)
  - Pricing model: Per-session vs per-user (cost savings vs Zoom)
  - Avoids user-paid monthly fees (reduces friction)
  - Client quote: "BBB charges by the session instead of by the user. This is a huge cost savings versus zoom"

- **Real-Time Communication:** Discord accepted as interim solution
  - Alternatives mentioned: Slack, Telegram
  - Users will need to set up external accounts
  - Implies real-time chat is not MVP priority for in-platform build

- **Cost Considerations:**
  - BBB per-session pricing preferred over Zoom per-user pricing
  - Avoiding user-paid monthly fees reduces friction and overhead
  - Hosted BBB services preferred over self-hosting

**Technical Implications:**
- Calendar system must be robust ("full blown")
- BBB integration via hosted provider API
- External chat platform (Discord/Slack/Telegram) for real-time communication initially
- No immediate need to build in-platform real-time chat for MVP

**Relationship to Other Docs:**
- Reinforces CD-002's BigBlueButton mention for video sessions
- Reinforces CD-005's Discord as interim solution
- Confirms calendar as MVP priority (also mentioned in CD-005)
- **Chronology:** Nov 16 - between CD-005 (Nov 13) and CD-002 (Nov 29)

**Goals Referenced:** GO-009 (Video Session Infrastructure)
**Stories Referenced:** US-C006, US-T001, US-P020–P025 (calendar stories)

---

### CD-007: Slack Message - BBB Alternatives & P2P Video Research
**Date Uploaded:** 2025-11-30
**Original Date:** 2025-11-18
**Summary for SPECS.md:**

Client research on video conferencing alternatives to BBB, specifically optimized for 1:1 peer tutoring sessions.

**Key elements for SPECS.md:**

- **P2P Architecture Insight:** For 1:1 sessions, Peer-to-Peer architecture is critical
  - Video data travels directly between devices
  - Bypasses expensive SFU (Selective Forwarding Unit) servers
  - Benefits: Lower latency, higher security, significantly lower costs

- **Three Options Evaluated:**

  | Service | Best For | Free Tier | Key Feature |
  |---------|----------|-----------|-------------|
  | Digital Samba | Low code (iframe) | 10,000 mins/mo (~83 hrs 1:1) | Pre-built Zoom-like UI |
  | Daily.co | Developer SDK | 10,000 mins/mo | Auto P2P switching for 1:1 |
  | VideoSDK.live | Scale/cost priority | N/A | $0.003/min (below industry $0.004) |

- **Daily.co Highlighted Feature:** Automatic P2P switching
  - 2 people → P2P mode (efficient)
  - 3+ people → SFU mode (seamless switch)
  - Many competitors always use SFU (inefficient for 1:1)

- **Whereby Warning:** Recently imposed 30-minute limit on free calls (avoid)

- **Client Recommendations:**
  - Digital Samba: Quick integration, no UI code needed
  - Daily.co: Professional SDK with intelligent P2P handling

**Technical Implications:**
- 1:1 tutoring sessions benefit from P2P-optimized solutions
- May reconsider BBB if primarily 1:1 sessions (P2P alternatives more cost-effective)
- Daily.co offers best developer experience with automatic optimization
- Digital Samba offers fastest time-to-market

**Relationship to Other Docs:**
- **Potentially supersedes CD-006's BBB preference** for 1:1 use case
- Aligns with CD-006's cost-consciousness (avoiding per-user fees)
- **Chronology:** Nov 18 - after CD-006 (Nov 16), before CD-002 (Nov 29)
- CD-002 still mentions BBB - may be for group sessions vs 1:1

**⚠️ Requires Clarification:**
- Daily.co vs Digital Samba vs BBB - final decision?
- BBB for groups + P2P for 1:1? Or single solution?

**Goals Referenced:** GO-009 (Video Session Infrastructure)
**Stories Referenced:** US-V001, US-V002, US-T007, US-A014

---

### CD-008: Meeting Transcript - Budget, Timeline, Community Feed
**Date Uploaded:** 2025-11-30
**Original Date:** 2025-11-26
**Summary for SPECS.md:**

Meeting transcript capturing Brian's (client) stated positions on budget, timeline, and community feed priorities.

**Key elements for SPECS.md:**

- **Budget & Timeline (NEW):**
  - Budget: **$75,000** (increased from earlier conservative estimates)
  - Timeline: **4 months**
  - Client quote: "I want to take a bigger risk"

- **Community Feed - Critical MVP Priority:**
  - Must build now, not later: "would be a nut house after the fact"
  - Fallback value: Even if thesis fails, "I'll have a tutoring site with unique functionality"
  - Purpose: **Marketing funnel** that overcomes resistance to purchase

- **Community Feed as Marketing Funnel (User Journey):**
  1. Student arrives → sees courses → clicks "follow" to explore
  2. Sees creator → clicks "follow"
  3. Subject/course feeds appear in their community feed
  4. Social proof: "I took this course, built this app, got 8 weeks work in a week"
  5. Public discussion of pros/cons
  6. Conversion: "You can talk somebody into the course"
  7. Retention: After course, stay in community to teach others

- **Stream (GetStream.io) - Clarified Scope:**
  - **Feeds only** - not their video conferencing
  - Chat is "much lower on the priority list"
  - Quote: "The community feeds is all I want out of there"

- **Skool.com as Prototype:**
  - Agreed to use Skool as reference for community feed design
  - Quote: "Let's use Skool as the prototype to build our community feed"

- **Core Philosophy - Human Connection:**
  - "People motivate people. Computers don't motivate people."
  - "The human connections are overlooked in this quest to educate people"
  - "Just the one hour paid session is not enough of a connection"
  - Self-paced sites create isolation; community feed combats this

- **Video Conferencing:**
  - Jitsi mentioned as possibility (from Claude/Q feedback)
  - Concern: "doesn't seem like it's quite as full featured"

**Technical Implications:**
- Stream integration scoped to feeds only (reduces complexity)
- Community feed is MVP-critical, not post-launch
- Skool.com UX patterns should inform feed design
- 4-month timeline requires focused scope

**Relationship to Other Docs:**
- **Supersedes** earlier budget/timeline assumptions
- **Clarifies** CD-005's Stream mention (feeds only, not chat)
- **Reinforces** CD-005's feed priority
- Adds Jitsi to video options (CD-006, CD-007)
- **Chronology:** Nov 26 - after CD-007 (Nov 18), before CD-002 (Nov 29)

**Goals Referenced:** GO-010, GO-014 (Community & Combat Isolation)
**Stories Referenced:** US-S025, US-P002, US-S001, US-S006

---

### CD-009: Slack Conversation - BBB Blindside Networks & Cloudflare Setup
**Date Uploaded:** 2025-11-30
**Original Date:** 2025-11-28
**Summary for SPECS.md:**

Slack conversation confirming BBB hosting provider selection and Cloudflare deployment.

**Key elements for SPECS.md:**

- **BBB Hosting Provider Confirmed:** Blindside Networks (https://blindsidenetworks.com/)
  - They are the original creators of BigBlueButton
  - Managed hosting - no SSH/root access (security/stability)
  - Control via API or LMS integration
  - Custom configurations, usage reports, and logs available on request

- **Managed Hosting Rationale:**
  - Quote: "It will get us to market quicker. We have lots of moving parts. We need to cut corners where ever possible."
  - Speed to market is priority over self-hosting flexibility

- **Cloudflare Hosting Confirmed:**
  - Domain: **peerloop.com** set up on Cloudflare free tier
  - Generic splash page deployed
  - Quote: "I setup a cloudflare free site, pointed dns and setup a generic splash page. Free is good lol"

- **Landing Page Purpose:**
  - Form for prospective students and creators to invite
  - Logo pending (Brian's wife will design)

**Technical Implications:**
- BBB integration will be API-based (no server customization)
- Cloudflare free tier for hosting (confirms comp-001 preference)
- peerloop.com is the production domain
- Managed services preferred over self-hosting for speed

**Relationship to Other Docs:**
- **Confirms** CD-006's BBB decision with specific provider
- **Confirms** comp-001's Cloudflare preference
- **Reinforces** CD-008's "cut corners" / speed-to-market priority
- **Chronology:** Nov 28 - after CD-008 (Nov 26), before CD-002 (Nov 29)

**Goals Referenced:** GO-009 (Video Session Infrastructure), GO-018 (Budget/Timeline)
**Stories Referenced:** US-V001-V007, US-A013-A018 (video/session stories)

---

## Index Statistics
- **Total Documents:** 9
- **Next CD Number:** CD-010
- **Last Updated:** 2025-11-30

## Quick Reference

| ID | Document | Key Content |
|----|----------|-------------|
| CD-001 | Business Plan | Revenue model, flywheel, go-to-market |
| CD-002 | Feature Summary | UI/UX mockups, tech stack, navigation |
| CD-003 | User Stories | Role-based needs, 6 user types |
| CD-004 | Impact Filter | Mission, success metrics, vision |
| CD-005 | Slack - GetStream | Feed tech choice, MVP priorities, Discord concerns |
| CD-006 | Slack - Calendar/BBB | Calendar priority, BBB hosting, Discord interim |
| CD-007 | Slack - P2P Video | Daily.co, Digital Samba, P2P for 1:1 sessions |
| CD-008 | Meeting - Budget/Feed | $75K budget, 4mo timeline, Skool prototype, feeds-only Stream |
| CD-009 | Slack - Blindside/Cloudflare | BBB via Blindside Networks, peerloop.com on Cloudflare |
