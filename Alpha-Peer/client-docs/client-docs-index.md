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

## Index Statistics
- **Total Documents:** 4
- **Next CD Number:** CD-005
- **Last Updated:** 2025-11-29

## Quick Reference

| ID | Document | Key Content |
|----|----------|-------------|
| CD-001 | Business Plan | Revenue model, flywheel, go-to-market |
| CD-002 | Feature Summary | UI/UX mockups, tech stack, navigation |
| CD-003 | User Stories | Role-based needs, 6 user types |
| CD-004 | Impact Filter | Mission, success metrics, vision |
