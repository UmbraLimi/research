# Video Platform Decisions - RUN-001

**Created:** 2025-12-24
**Related Global Research:**
- `research/tech-001-bigbluebutton.md`
- `research/tech-006-plugnmeet.md`

---

## Decision: VideoProvider Interface

RUN-001 uses an **interface abstraction** rather than committing to a specific platform.

### Rationale

| Factor | Consideration |
|--------|---------------|
| Timeline | 4 months - can't afford wrong choice |
| Options | BBB (established) vs PlugNmeet (modern, unproven) |
| Brian's Status | "Looking deeper" at PlugNmeet (CD-028) |
| Risk Mitigation | Interface allows swap without architecture change |

### Interface Contract (from API.md)

```typescript
interface VideoProvider {
  createRoom(options: CreateRoomOptions): Promise<Room>;
  deleteRoom(roomId: string): Promise<void>;
  getJoinUrl(roomId: string, participant: Participant): Promise<string>;
  startRecording(roomId: string): Promise<RecordingId>;
  stopRecording(recordingId: string): Promise<RecordingUrl>;
  getRecording(recordingId: string): Promise<RecordingUrl>;
  getRoomStatus(roomId: string): Promise<RoomStatus>;
}
```

---

## Compliant Platforms

### BigBlueButton

**From tech-001-bigbluebutton.md:**

| Aspect | Value | Run Impact |
|--------|-------|------------|
| Hosting | Self-hosted only | Need VM budget (~$80-150/mo) |
| Server Req | 16GB RAM, 8 cores | Significant infrastructure |
| API | Full meeting/recording control | ✅ Covers interface |
| Webhooks | meeting.end, recording.ready | ✅ Covers interface |
| UX | Dated interface | May affect student adoption |

**Open Questions (from tech-001):**
- Hosting model? → **Deferred to implementation**
- Recording retention? → **Deferred to implementation**

### PlugNmeet

**From tech-006-plugnmeet.md:**

| Aspect | Value | Run Impact |
|--------|-------|------------|
| Hosting | Self-hosted or Cloud Flex | More options |
| Server Req | $5-10/mo VPS | Lower cost |
| Architecture | Microservices (Go + LiveKit) | Better scaling |
| UX | Modern, Zoom-like | Better adoption |
| Maturity | Newer, less proven | Risk factor |

**Open Questions (from tech-006):**
- Production stability? → **Needs research**
- API compatibility with interface? → **Needs verification**

---

## Run-001 Approach

1. **Build to interface** - All code targets `VideoProvider` interface
2. **Start with BBB** - More proven, matches DIR-001
3. **Evaluate PlugNmeet** - Brian to complete deeper review
4. **Switch if warranted** - Interface allows seamless swap

### Implementation Order

```
Week 1-2: Build VideoProvider interface + BBB adapter
Week 3-4: Test with real sessions
Week 5+:  If PlugNmeet proven, build adapter and evaluate
```

---

## Cost Comparison (for Genesis Cohort)

| Platform | Model | Est. Monthly Cost | Notes |
|----------|-------|-------------------|-------|
| BBB (self-hosted) | VM | $80-150 | Need ops capacity |
| BBB (Blindside) | Per-session | Variable | Depends on volume |
| PlugNmeet (self-hosted) | VPS | $5-10 | Lower but unproven |
| PlugNmeet (Cloud Flex) | Capacity | TBD | Need quote |

**Recommendation:** Start with BBB self-hosted or Blindside managed, budget $150/mo for video infrastructure.

---

## Questions Still Open

These should be resolved before finalizing video platform:

| # | Question | Impact | Source |
|---|----------|--------|--------|
| 1 | PlugNmeet production stability | Risk assessment | tech-006 |
| 2 | PlugNmeet API vs our interface | Compatibility | tech-006 |
| 3 | Self-host vs managed preference | Cost/ops | Both |
| 4 | Recording storage location | Infrastructure | tech-001 |

---

## References

- `research/tech-001-bigbluebutton.md` - Full BBB research
- `research/tech-006-plugnmeet.md` - Full PlugNmeet research
- `API.md` - VideoProvider interface definition
- `CD-028` - Brian's PlugNmeet discovery
