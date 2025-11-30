# Alpha Peer - User Stories

**Last Updated:** 2025-11-29
**Sources:** CD-001 (Business Plan), CD-002 (Feature Summary), CD-003 (User Stories), CD-004 (Impact Filter)

---

## Story Format

Stories follow the format: **As a [role], I need to [action] so that [benefit].**

**Story ID Format:** `US-[Role][NNN]` where:
- `US` = User Story prefix
- `[Role]` = Single letter for role (A=Admin, C=Creator, S=Student, T=Student-Teacher, E=Employer, V=Video/Session, P=Platform)
- `[NNN]` = Zero-padded 3-digit number (001-999)

**Priority levels:**
- **P0:** MVP critical - required for Genesis Cohort launch
- **P1:** High priority - needed for full flywheel validation
- **P2:** Medium priority - enhances experience
- **P3:** Nice to have - future consideration

---

## User Roles

| Role | Description |
|------|-------------|
| **Student** | Learner progressing through courses |
| **Student-Teacher** | Graduate who teaches peers (earns 70%) |
| **Creator-Instructor** | Course creator who may also teach directly |
| **Employer/Funder** | Third party paying for student enrollment |
| **Admin (AP Rep)** | Platform operations and oversight |
| **System** | Automated platform functionality |

---

## Admin (AP Rep) Stories

### Enrollment & Account Management

| ID | Story | Priority | Source |
|----|-------|----------|--------|
| US-A001 | As an Admin, I need to enroll teachers (Creators) so that they can offer courses on the platform | P0 | CD-003 |
| US-A002 | As an Admin, I need to cancel a teacher (with reason) so that I can remove problematic instructors | P1 | CD-003 |
| US-A003 | As an Admin, I need to cancel a student (with reason) so that I can enforce community standards | P1 | CD-003 |
| US-A004 | As an Admin, I need to vet teacher certificates so that only qualified instructors teach | P0 | CD-003 |

### Financial Operations

| ID | Story | Priority | Source |
|----|-------|----------|--------|
| US-A005 | As an Admin, I need to pay teachers from student enrollments so that the 15/15/70 revenue split is distributed | P0 | CD-003 |
| US-A006 | As an Admin, I need to refund students if they cancel so that we maintain customer satisfaction | P0 | CD-003 |
| US-A007 | As an Admin, I need to chargeback teachers for cancellations so that creators bear responsibility for their commitments | P1 | CD-003 |
| US-A008 | As an Admin, I need to allow third party organizations to pay for students so that employers can sponsor learning | P1 | CD-003 |
| US-A009 | As an Admin, I need to send success/failure assessments to funders so that sponsors can track ROI | P1 | CD-003 |

### Communication

| ID | Story | Priority | Source |
|----|-------|----------|--------|
| US-A010 | As an Admin, I need to message teachers so that I can communicate platform updates and issues | P0 | CD-003 |
| US-A011 | As an Admin, I need to message students so that I can provide support and announcements | P0 | CD-003 |
| US-A012 | As an Admin, I need to contact potential students by email re: courses and teachers referred by users so that referrals convert to enrollments | P1 | CD-003 |

### Session Facilitation

| ID | Story | Priority | Source |
|----|-------|----------|--------|
| US-A013 | As an Admin, I need to facilitate tutor sessions for any teacher-student combination so that peer learning can happen | P0 | CD-003 |
| US-A014 | As an Admin, I need video calls with recording potential so that sessions can be reviewed | P0 | CD-003 |
| US-A015 | As an Admin, I need AI-powered session summaries & transcripts so that learning is documented | P1 | CD-003 |
| US-A016 | As an Admin, I need monitored session time so that billing is accurate | P0 | CD-003 |
| US-A017 | As an Admin, I need screen sharing in sessions so that teachers can demonstrate concepts | P0 | CD-003 |
| US-A018 | As an Admin, I need to store tutor sessions with date/time/people parameters so that session history is maintained | P0 | CD-003 |

### Analytics & Monitoring

| ID | Story | Priority | Source |
|----|-------|----------|--------|
| US-A019 | As an Admin, I need to monitor user time on site and retention so that I can measure engagement | P1 | CD-003 |
| US-A020 | As an Admin, I need to monitor courses taken by user, teacher, creator stats so that I can track platform health | P1 | CD-003 |
| US-A021 | As an Admin, I need to monitor fees paid, distributed, income per creator so that I can ensure financial accuracy | P0 | CD-003 |
| US-A022 | As an Admin, I need to monitor session status (cancel, complete) so that I can track service delivery | P1 | CD-003 |
| US-A023 | As an Admin, I need to monitor student to teacher conversion so that I can validate the flywheel | P0 | CD-003, CD-004 |
| US-A024 | As an Admin, I need to monitor percentage grade averages so that I can track learning quality | P1 | CD-003 |
| US-A025 | As an Admin, I need to determine where new users originate from so that I can optimize acquisition | P2 | CD-003 |

---

## Creator-Instructor Stories

### Course Management

| ID | Story | Priority | Source |
|----|-------|----------|--------|
| US-C001 | As a Creator, I need to enter courses, training syllabi, quizzes, reference materials so that students have structured learning paths | P0 | CD-003 |
| US-C002 | As a Creator, I need to define criteria for successful completion so that certification is meaningful | P0 | CD-003 |
| US-C003 | As a Creator, I need to set training progression and criteria to level up so that students advance appropriately | P0 | CD-003 |
| US-C004 | As a Creator, I need to retire a course so that outdated content is removed | P2 | CD-003 |
| US-C005 | As a Creator, I need flexible assessments so that I can test understanding in various ways | P1 | CD-002 |

### Scheduling & Availability

| ID | Story | Priority | Source |
|----|-------|----------|--------|
| US-C006 | As a Creator, I need to offer times for tutoring via a calendar of availability so that students can book sessions | P0 | CD-003 |
| US-C007 | As a Creator, I need to cancel a particular scheduled session with a student so that I can handle conflicts | P1 | CD-003 |

### Profile & Presence

| ID | Story | Priority | Source |
|----|-------|----------|--------|
| US-C008 | As a Creator, I need to enter a profile with pictures, videos, PDFs so that students can evaluate my expertise | P0 | CD-003 |
| US-C009 | As a Creator, I need a profile card with stats (Active Student-Teachers, Avg Taught per Teacher, badges) so that my success is visible | P1 | CD-002 |
| US-C010 | As a Creator, I need a "Creator Studio" button to access course management so that I can easily edit content | P1 | CD-002 |

### Student-Teacher Management

| ID | Story | Priority | Source |
|----|-------|----------|--------|
| US-C011 | As a Creator, I need to vet student-turned-teachers so that teaching quality is maintained | P0 | CD-003 |
| US-C012 | As a Creator, I need to monitor/assess student-turned-teachers so that I can ensure ongoing quality | P1 | CD-003 |
| US-C013 | As a Creator, I need to cancel a student for cause so that I can remove problematic learners | P1 | CD-003 |

### Certification & Assessment

| ID | Story | Priority | Source |
|----|-------|----------|--------|
| US-C014 | As a Creator, I need to grant certificates to students of successful completion so that achievement is recognized | P0 | CD-003 |
| US-C015 | As a Creator, I need to capture and send assessments of students on progress/completion so that progress is documented | P1 | CD-003 |
| US-C016 | As a Creator, I need to earn a teaching certificate for each course taught (displayed on profile) so that my expertise is credentialed | P1 | CD-003 |

### Communication & Support

| ID | Story | Priority | Source |
|----|-------|----------|--------|
| US-C017 | As a Creator, I need to message students so that I can provide guidance and support | P0 | CD-003 |
| US-C018 | As a Creator, I need to message AP so that I can get platform support | P0 | CD-003 |
| US-C019 | As a Creator, I need to refer potential students to AP re: my courses so that I can grow my audience | P2 | CD-003 |
| US-C020 | As a Creator, I need to ask AI for assistance when both teacher and student are stumped so that learning continues | P1 | CD-003 |

### Community Management

| ID | Story | Priority | Source |
|----|-------|----------|--------|
| US-C021 | As a Creator, I need community hubs with forums so that students can interact | P1 | CD-001, CD-002 |
| US-C022 | As a Creator, I need to assign Community Roles (paid assistants with revenue sharing) so that I can scale my community | P2 | CD-002 |
| US-C023 | As a Creator, I need control over community organization and content delivery so that I can customize the experience | P2 | CD-002 |

---

## Student Stories

### Discovery & Enrollment

| ID | Story | Priority | Source |
|----|-------|----------|--------|
| US-S001 | As a Student, I need to see what tutor courses are available so that I can choose what to learn | P0 | CD-003 |
| US-S002 | As a Student, I need to pay for tutors so that I can access learning | P0 | CD-003 |
| US-S003 | As a Student, I need to search for courses so that I can find relevant content | P0 | CD-002 |
| US-S004 | As a Student, I need to search for Creators/Instructors with detailed profiles so that I can evaluate teachers | P0 | CD-002 |
| US-S005 | As a Student, I need to view course detail pages with curriculum outline and time estimates so that I understand the commitment | P0 | CD-002 |
| US-S006 | As a Student, I need action buttons (Enroll, Explore Teaching, Follow Course, Join Community) so that I can take next steps | P0 | CD-002 |
| US-S007 | As a Student, I need related courses suggestions so that I can continue learning | P2 | CD-002 |

### Profile & Account

| ID | Story | Priority | Source |
|----|-------|----------|--------|
| US-S008 | As a Student, I need to enter a profile with picture (public and private sections) so that I control my visibility | P0 | CD-003 |
| US-S009 | As a Student, I need a unified dashboard for student/teacher activity tracking so that I see my progress | P0 | CD-002 |
| US-S010 | As a Student, I need a calendar view so that I can manage my schedule | P1 | CD-002 |
| US-S011 | As a Student, I need quick action buttons so that common tasks are accessible | P1 | CD-002 |
| US-S012 | As a Student, I need earnings tracking so that I can see my teaching income | P0 | CD-002 |

### Session Management

| ID | Story | Priority | Source |
|----|-------|----------|--------|
| US-S013 | As a Student, I need to reschedule a session with teacher so that I can handle conflicts | P1 | CD-003 |
| US-S014 | As a Student, I need to cancel a session so that I can handle emergencies | P1 | CD-003 |
| US-S015 | As a Student, I need to cancel a course (with reason) so that I can exit if needed | P1 | CD-003 |

### Communication

| ID | Story | Priority | Source |
|----|-------|----------|--------|
| US-S016 | As a Student, I need to message teachers so that I can ask questions | P0 | CD-003 |
| US-S017 | As a Student, I need to message other students so that I can collaborate (noted as tricky) | P2 | CD-003 |
| US-S018 | As a Student, I need to message AP so that I can get support | P0 | CD-003 |
| US-S019 | As a Student, I need a private messaging system so that I can have 1-on-1 conversations | P0 | CD-002 |

### Progression & Certification

| ID | Story | Priority | Source |
|----|-------|----------|--------|
| US-S020 | As a Student, I need to apply for teacher status so that I can transition to earning | P0 | CD-003 |
| US-S021 | As a Student, I need to earn a Learning Certificate upon completion so that my achievement is recognized | P0 | CD-002 |
| US-S022 | As a Student, I need to earn a Teaching Certificate when I become a teacher so that my teaching ability is credentialed | P0 | CD-002 |
| US-S023 | As a Student, I need my Teaching Certificate to dynamically update with student count so that my experience is visible | P1 | CD-002 |
| US-S024 | As a Student, I need access to gated communities based on credentials so that I can join advanced groups | P1 | CD-002 |

### Community & Discovery

| ID | Story | Priority | Source |
|----|-------|----------|--------|
| US-S025 | As a Student, I need an X.com-style algorithmic feed of followed content so that I discover relevant posts | P1 | CD-002 |
| US-S026 | As a Student, I need to refer potential students to AP re: courses and teachers so that I can help others | P2 | CD-003 |
| US-S027 | As a Student, I need to ask AI for assistance when both teacher and student are stumped so that learning continues | P1 | CD-003 |

---

## Student-Teacher Stories

### Scheduling & Availability

| ID | Story | Priority | Source |
|----|-------|----------|--------|
| US-T001 | As a Student-Teacher, I need to offer times for tutoring via a calendar of availability so that students can book me | P0 | CD-003 |
| US-T002 | As a Student-Teacher, I need to cancel a particular scheduled session with a student so that I can handle conflicts | P1 | CD-003 |

### Profile & Presence

| ID | Story | Priority | Source |
|----|-------|----------|--------|
| US-T003 | As a Student-Teacher, I need to enter a profile with pictures, videos, PDFs so that students can evaluate me | P0 | CD-003 |
| US-T004 | As a Student-Teacher, I need a public profile showing my credentials so that students trust my expertise | P0 | CD-002 |
| US-T005 | As a Student-Teacher, I need a "Switch User" button to toggle between student and teacher modes so that I can use both functions | P0 | CD-002 |

### Teaching & Certification

| ID | Story | Priority | Source |
|----|-------|----------|--------|
| US-T006 | As a Student-Teacher, I need to grant certificates to students of successful completion so that I can certify learners | P0 | CD-003 |
| US-T007 | As a Student-Teacher, I need to conduct video sessions with screen sharing so that I can teach effectively | P0 | CD-002 |

### Communication & Support

| ID | Story | Priority | Source |
|----|-------|----------|--------|
| US-T008 | As a Student-Teacher, I need to message students so that I can provide support | P0 | CD-003 |
| US-T009 | As a Student-Teacher, I need to message AP so that I can get platform support | P0 | CD-003 |
| US-T010 | As a Student-Teacher, I need to refer potential students to AP re: my courses so that I can grow my student base | P2 | CD-003 |
| US-T011 | As a Student-Teacher, I need to ask AI for assistance when both I and student are stumped so that learning continues | P1 | CD-003 |

### Earnings

| ID | Story | Priority | Source |
|----|-------|----------|--------|
| US-T012 | As a Student-Teacher, I need to receive 70% of session fees so that I earn from teaching | P0 | CD-001 |
| US-T013 | As a Student-Teacher, I need an earnings dashboard so that I can track my income | P0 | CD-002 |

---

## Employer/Funder Stories

| ID | Story | Priority | Source |
|----|-------|----------|--------|
| US-E001 | As an Employer, I need to pay for a student to take a course so that I can sponsor employee learning | P1 | CD-003 |
| US-E002 | As an Employer, I need to receive a copy of student progress and completion status so that I can track sponsored learners | P1 | CD-003 |
| US-E003 | As an Employer, I need to receive a copy of certification so that I have proof of completion | P1 | CD-003 |
| US-E004 | As an Employer, I need to enter a profile (possibly all private) so that I can manage my account | P1 | CD-003 |
| US-E005 | As an Employer, I need to message AP so that I can get support | P1 | CD-003 |
| US-E006 | As an Employer, I need to message my funded students for their funded courses so that I can check on progress | P2 | CD-003 |

---

## Tutor Session Stories (System)

| ID | Story | Priority | Source |
|----|-------|----------|--------|
| US-V001 | As a System, I need to handle the video chat experience so that tutoring can happen | P0 | CD-003 |
| US-V002 | As a System, I need to possibly limit the number of participants so that sessions stay focused | P1 | CD-003 |
| US-V003 | As a System, I need to allow messages and files to pass between participants so that resources can be shared | P0 | CD-003 |
| US-V004 | As a System, I need to monitor time so that sessions are tracked for billing | P0 | CD-003 |
| US-V005 | As a System, I need to record conversations so that sessions can be reviewed | P1 | CD-003 |
| US-V006 | As a System, I need to enable assessment by each participant at end of session so that quality is tracked | P0 | CD-003 |
| US-V007 | As a System, I need AI-powered session summaries and transcripts so that learning is captured | P1 | CD-003 |

---

## Platform/Navigation Stories (Implied from Mockups)

| ID | Story | Priority | Source |
|----|-------|----------|--------|
| US-P001 | As a User, I need a Browse Menu for course and creator search so that I can discover content | P0 | CD-002 |
| US-P002 | As a User, I need a "My Community" feed (X.com-style) so that I see followed content | P1 | CD-002 |
| US-P003 | As a User, I need a Dashboard view so that I see my activity at a glance | P0 | CD-002 |
| US-P004 | As a User, I need a Messages section so that I can access conversations | P0 | CD-002 |
| US-P005 | As a User, I need a Profile section so that I can manage my account | P0 | CD-002 |
| US-P006 | As a User, I need session booking/purchasing integrated with teacher discovery so that I can easily book | P0 | CD-002 |

---

## Story Statistics

| Category | P0 | P1 | P2 | P3 | Total |
|----------|----|----|----|----|-------|
| Admin | 12 | 10 | 1 | 0 | 23 |
| Creator | 8 | 10 | 5 | 0 | 23 |
| Student | 12 | 9 | 6 | 0 | 27 |
| Student-Teacher | 7 | 4 | 2 | 0 | 13 |
| Employer/Funder | 0 | 5 | 1 | 0 | 6 |
| Session (System) | 4 | 3 | 0 | 0 | 7 |
| Platform/Navigation | 5 | 1 | 0 | 0 | 6 |
| **Total** | **48** | **42** | **15** | **0** | **105** |

---

## Story Index by Source Document

| ID | Document | Stories Referenced |
|----|----------|-------------------|
| CD-001 | Business Plan | US-C021, US-T012 |
| CD-002 | Feature Summary | US-C005, US-C009–C010, US-C021–C023, US-S003–S007, US-S009–S012, US-S019, US-S021–S025, US-T004–T005, US-T007, US-T013, US-V007, US-P001–P006 |
| CD-003 | User Stories | US-A001–A025, US-C001–C020, US-S001–S002, US-S008, US-S013–S018, US-S020, US-S026–S027, US-T001–T011, US-E001–E006, US-V001–V006 |
| CD-004 | Impact Filter | US-A023 |

---

## Current State

| Role | Prefix | Next Number |
|------|--------|-------------|
| Admin | US-A | US-A026 |
| Creator | US-C | US-C024 |
| Student | US-S | US-S028 |
| Student-Teacher | US-T | US-T014 |
| Employer/Funder | US-E | US-E007 |
| Session (System) | US-V | US-V008 |
| Platform/Navigation | US-P | US-P007 |

---

## Notes for Implementation

1. **P0 stories (48 total)** are required for Genesis Cohort launch with 3 founding creators
2. **Student-to-student messaging (US-S017)** flagged as "tricky" - needs careful design to prevent abuse
3. **Role switching (US-T005)** is critical UX - single account with multiple role views
4. **Post-session assessment (US-V006)** enables quality tracking for flywheel validation
5. **Earnings dashboard (US-T013, US-S012)** essential for demonstrating value to Student-Teachers
