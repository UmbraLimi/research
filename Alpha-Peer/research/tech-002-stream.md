# tech-002: Stream

**Type:** Chat, Activity Feeds, Video Platform
**Status:** ✅ SELECTED - Feeds Only (2025-12-26)
**Research Date:** 2025-11-30, Updated 2025-12-26
**Source:** https://getstream.io/

---

## Overview

Stream is a SaaS platform providing APIs and SDKs for building chat, activity feeds, and video features. It offers pre-built React components with extensive customization options.

## Products Available

Stream offers three distinct products:

| Product | Description | Relevance to Alpha Peer |
|---------|-------------|------------------------|
| **Chat** | Real-time messaging | HIGH - Messaging between users |
| **Activity Feeds** | Social-style feeds | MEDIUM - Community feeds |
| **Video & Audio** | Video calling, livestreaming | LOW - BBB handles this |

## Stream Chat

### Key Features
| Feature | Description | Relevant User Stories |
|---------|-------------|----------------------|
| Real-time Messaging | Instant message delivery | US-S016, US-S019, US-C017, US-T008 |
| Typing Indicators | Show when users are typing | Enhanced UX |
| Message Reactions | Emoji reactions on messages | Enhanced UX |
| Threads/Replies | Organized conversations | US-S019 |
| File/Image Upload | Share attachments | US-V003 |
| User Presence | Online/offline status | Enhanced UX |
| Unread Counts | Badge notifications | US-P004 |
| Push Notifications | Mobile alerts | Future mobile |
| Message Search | Find past conversations | P2 |
| Moderation | Content filtering | US-S017 safety |
| Custom Fields | Extend user/message data | Flexible integration |

### React SDK Components
```javascript
// Stream Chat provides pre-built React components:
import {
  Chat,
  Channel,
  ChannelHeader,
  MessageList,
  MessageInput,
  Thread,
  Window,
} from 'stream-chat-react';
```

### Channel Types
| Type | Description | Alpha Peer Use |
|------|-------------|---------------|
| messaging | 1:1 private chat | Student ↔ Teacher |
| team | Group conversations | Study groups |
| livestream | Many viewers, few posters | Announcements |
| commerce | Customer support style | Support tickets |
| gaming | High-volume, low-latency | Not applicable |

### Authentication Model
```javascript
// Users connect with JWT tokens generated server-side
const client = StreamChat.getInstance('api_key');
await client.connectUser(
  { id: 'user-id', name: 'User Name', image: 'avatar.jpg' },
  'server_generated_token'
);
```

## Stream Activity Feeds

### Key Features
| Feature | Description | Relevant User Stories |
|---------|-------------|----------------------|
| Following System | Follow users/topics | US-S025 |
| Notification Feeds | Activity notifications | US-P002 |
| Aggregation | Group similar activities | Enhanced UX |
| Personalization | Custom feed algorithms | US-S025 |
| Reactions | Likes, comments | Community engagement |

### Feed Types
- **Flat Feeds:** Chronological activity streams
- **Aggregated Feeds:** Grouped activities (e.g., "5 people liked your post")
- **Notification Feeds:** User-specific alerts

### Alpha Peer Community Use Case
```
Creator posts update →
  Followers see in their feed →
    Students can react/comment →
      Creator gets notification
```

## Stream Video

**Note:** BigBlueButton is required for video, so Stream Video is likely NOT needed.

| Feature | BBB Coverage | Stream Video |
|---------|-------------|--------------|
| Video calls | Yes | Also yes |
| Screen sharing | Yes | Yes |
| Recording | Yes | Yes |
| Education focus | Yes (purpose-built) | General purpose |
| Pricing | Self-host | Per-minute fees |

**Recommendation:** Skip Stream Video; use BigBlueButton as required.

## Pricing

Stream uses usage-based pricing with free tiers for development.

### Chat Pricing (Estimated)
| Tier | MAU | Price |
|------|-----|-------|
| Maker | Up to 100 | Free |
| Startup | Up to 10,000 | ~$499/month |
| Growth | Up to 100,000 | Custom |
| Enterprise | Unlimited | Custom |

### Activity Feeds Pricing
| Tier | Updates/Month | Price |
|------|---------------|-------|
| Free | 3M | Free |
| Growth | Custom | Custom |

**Note:** Contact Stream sales for exact pricing; rates change frequently.

## User Story Coverage

### Directly Addresses
| Story ID | Story | Stream Product |
|----------|-------|----------------|
| US-S016 | Student message teachers | Chat |
| US-S019 | Private messaging system | Chat |
| US-C017 | Creator message students | Chat |
| US-T008 | Student-Teacher message students | Chat |
| US-A010 | Admin message teachers | Chat |
| US-A011 | Admin message students | Chat |
| US-S025 | X.com-style algorithmic feed | Activity Feeds |
| US-P002 | "My Community" feed | Activity Feeds |
| US-P004 | Messages section | Chat |

### Partially Addresses
| Story ID | Story | Gap |
|----------|-------|-----|
| US-S017 | Student-to-student messaging (tricky) | Needs moderation rules |
| US-C021 | Community hubs with forums | Feeds + custom UI needed |

### Does NOT Address
| Story ID | Story | Alternative |
|----------|-------|-------------|
| US-A012 | Email to potential students | Email service needed |
| US-V* | Video/session stories | BigBlueButton |

## Integration Considerations

### Pros
- Pre-built React components
- Handles real-time infrastructure
- Scales automatically
- Strong moderation tools (addresses US-S017 safety concern)
- 99.999% uptime SLA
- ~9ms API response times
- Supports 5M+ users per channel

### Cons
- Recurring SaaS costs
- Data lives on Stream servers
- Pricing can scale quickly with users
- Lock-in to Stream's data model

### React/Astro Integration
```javascript
// Astro page with Stream Chat React component
---
// astro page (server-side)
import ChatWrapper from '../components/react/ChatWrapper';
---

<ChatWrapper client:load apiKey={import.meta.env.STREAM_API_KEY} />
```

```jsx
// React component
import { StreamChat } from 'stream-chat';
import { Chat, Channel, MessageList, MessageInput } from 'stream-chat-react';
import 'stream-chat-react/dist/css/v2/index.css';

export default function ChatWrapper({ apiKey, userToken, userId }) {
  const [client] = useState(() => StreamChat.getInstance(apiKey));

  useEffect(() => {
    client.connectUser({ id: userId }, userToken);
    return () => client.disconnectUser();
  }, []);

  return (
    <Chat client={client}>
      <Channel>
        <MessageList />
        <MessageInput />
      </Channel>
    </Chat>
  );
}
```

## Recommendations

1. **Use Stream Chat for all messaging** - Covers US-S016, US-S019, US-C017, US-T008, US-A010, US-A011
2. **Evaluate Activity Feeds for community** - Good fit for US-S025, US-P002, US-C021
3. **Skip Stream Video** - BigBlueButton is required and more cost-effective
4. **Plan moderation strategy** - Critical for US-S017 (student-to-student messaging)
5. **Budget for growth** - Free tier for development, plan for paid tier at launch

## Open Questions

- [x] What's the expected MAU for chat at Genesis Cohort launch? → ~100-150 (free tier)
- [x] Will all 6 user roles need chat access? → Yes, all authenticated users
- [x] Should student-to-student chat be gated? → Yes, within course feeds only
- [x] How should community feeds be organized? → Per course + per instructor + platform-wide

---

## API Reference (Activity Feeds)

### Server-Side SDK Setup

**Package:** `@stream-io/node-sdk`

```typescript
import { StreamClient } from "@stream-io/node-sdk";

const client = new StreamClient(
  process.env.STREAM_API_KEY,
  process.env.STREAM_API_SECRET
);
```

### Token Generation ✅ RESOLVED

Tokens are JWT-based, generated server-side, passed to client.

```typescript
// Generate user token (server-side only)
const token = client.generateUserToken({
  user_id: "user_123",           // Required: your user's ID
  validity_in_seconds: 3600      // Optional: 1 hour default
});

// Token includes automatically:
// - user_id: the authenticated user
// - iat: issued-at timestamp
// - exp: expiration time
```

**Token Provider Pattern (for PeerLoop):**
```typescript
// POST /api/stream/token
export async function POST(request: Request) {
  // 1. Verify PeerLoop JWT from request
  const user = await verifyAuth(request);

  // 2. Generate Stream token for this user
  const streamToken = client.generateUserToken({
    user_id: user.id,
    validity_in_seconds: 24 * 60 * 60  // 24 hours
  });

  // 3. Return to client
  return Response.json({ token: streamToken });
}
```

**Token Revocation:**
```typescript
// Revoke all tokens for a user (e.g., on logout, password change)
await client.updateUsersPartial({
  users: [{
    id: "user_123",
    set: { revoke_tokens_issued_before: new Date() }
  }]
});

// Revoke all tokens app-wide (emergency)
await client.updateApp({ revoke_tokens_issued_before: new Date() });
```

### Client-Side SDK Setup

**Package:** `@stream-io/feeds-react-sdk`

```typescript
import { FeedsClient } from "@stream-io/feeds-react-sdk";

const client = new FeedsClient(process.env.NEXT_PUBLIC_STREAM_API_KEY);
await client.connectUser(
  { id: "user_123", name: "John Doe", image: "avatar.jpg" },
  userToken  // from your /api/stream/token endpoint
);
```

### Feed Types & Groups

| Feed Group | Purpose | PeerLoop Usage |
|------------|---------|----------------|
| `user` | User-created content | Personal posts |
| `timeline` | Following aggregation | Personalized feed |
| `notification` | User alerts (max 100) | Mentions, replies |
| `foryou` | Popular content prioritized | Discovery feed |

**PeerLoop Feed Groups:**
| Group | Feed ID Pattern | Access |
|-------|-----------------|--------|
| `townhall` | `townhall:main` | All users (global read) |
| `course` | `course:{courseId}` | Enrolled users only |
| `instructor` | `instructor:{creatorId}` | Course purchasers |
| `user` | `user:{userId}` | Owner + followers |
| `notification` | `notification:{userId}` | Owner only |

### Core API Operations

#### Create/Access Feed
```typescript
const feed = client.feeds.feed("course", courseId);
await feed.getOrCreate({
  user_id: userId,
  data: {
    name: "Course Discussion",
    visibility: "private"
  }
});
```

#### Add Activity
```typescript
await feed.addActivity({
  type: "post",                    // Activity type
  text: "Welcome to the course!",  // Content
  user_id: userId,                 // Author
  // Custom fields:
  attachments: ["https://..."],
  course_id: courseId
});
```

#### Read Activities
```typescript
const response = await feed.getOrCreate({
  user_id: userId,
  limit: 20
});
const activities = response.activities;

// Pagination
const nextPage = await feed.getOrCreate({
  user_id: userId,
  next: response.next,
  limit: 20
});
```

#### Target to Multiple Feeds (TO field)
```typescript
// Post to course feed AND notify instructor
await courseFeed.addActivity({
  type: "question",
  text: "How do I...?",
  user_id: studentId,
  to: [`notification:${instructorId}`]  // Also sends notification
});
```

#### Reactions & Comments
```typescript
// Add reaction
await client.addReaction({
  activity_id: activityId,
  type: "like"  // or "love", "celebrate", etc.
});

// Add comment
await client.addComment({
  object_id: activityId,
  comment: "Great question!"
});
```

### Following System

```typescript
// User's timeline follows a course feed
const timeline = client.feeds.feed("timeline", userId);
await timeline.follow("course", courseId);

// Unfollow
await timeline.unfollow("course", courseId);
```

**Permission Rules:**
- Users can follow any feed
- Users can only create follows FROM their own feeds
- Example: `timeline:john` can follow `course:123`, but can't make `course:123` follow anything

### Permissions & Access Control

**Default Permission Behaviors:**

| Permission Type | Behavior |
|-----------------|----------|
| Owner access | User can read/write feeds matching their ID |
| Global read | Any user can read (e.g., `user` group default) |
| Global write | Any user can write (requires explicit config) |
| Follow-based read | Can read feeds you follow |

**PeerLoop Permission Strategy:**

| Feed Group | Read | Write | Config Needed |
|------------|------|-------|---------------|
| `townhall` | Global | Admins only | Request global read from Stream |
| `course` | Enrolled only | Enrolled users | **Server-side gating** |
| `instructor` | Purchasers only | Creator only | **Server-side gating** |
| `notification` | Owner only | System only | Default |

**Important:** Stream cannot enforce "only enrolled users" - we must gate this server-side:

```typescript
// POST /api/feeds/course/:courseId/activities
export async function POST(request: Request, { params }) {
  const user = await verifyAuth(request);

  // Check enrollment in OUR database
  const enrolled = await db.enrollments.findFirst({
    where: { userId: user.id, courseId: params.courseId }
  });

  if (!enrolled) {
    return Response.json({ error: "Not enrolled" }, { status: 403 });
  }

  // User is enrolled - proxy to Stream
  const feed = serverClient.feeds.feed("course", params.courseId);
  await feed.addActivity({ ...body, user_id: user.id });
}
```

### Real-Time Updates

**Client-side subscription:**
```typescript
const feed = client.feed("course", courseId);
await feed.getOrCreate({ watch: true });  // Enable real-time

feed.state.subscribe((state) => {
  // Called when activities change
  console.log("New activities:", state.activities);
});
```

**Server-side webhooks:**
Configure in Stream Dashboard to receive all feed events:
```json
{
  "feed": "course:123",
  "app_id": "your_app",
  "new": [{ "id": "...", "type": "post", ... }],
  "deleted": [],
  "published_at": "2025-12-26T10:00:00Z"
}
```

### React Components

```jsx
import { FeedsProvider, FlatFeed, NotificationFeed } from "@stream-io/feeds-react-sdk";

function App() {
  return (
    <FeedsProvider client={client}>
      {/* Course feed */}
      <FlatFeed feedGroup="course" feedId={courseId} />

      {/* Notifications dropdown */}
      <NotificationFeed />
    </FeedsProvider>
  );
}
```

---

## PeerLoop Integration Architecture

```
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│   React Client  │────▶│  Stream Cloud   │     │   PeerLoop API  │
│   (Astro)       │     │   (Feeds)       │     │   (Workers)     │
└────────┬────────┘     └─────────────────┘     └────────┬────────┘
         │                       ▲                        │
         │                       │                        │
         └───────────────────────┼────────────────────────┘
                                 │
                    Token generation & access control
```

**Flow:**
1. User logs in → PeerLoop issues JWT
2. Client calls `/api/stream/token` with PeerLoop JWT
3. Backend verifies JWT, generates Stream token
4. Client connects to Stream with token
5. For gated feeds (course/instructor): client calls our API, we verify access, proxy to Stream

---

## Database Sync Requirements

We need to sync these relationships to our DB:

| Event | Stream Action | PeerLoop DB Update |
|-------|---------------|-------------------|
| User enrolls in course | Follow `course:{id}` | Create enrollment record |
| User drops course | Unfollow `course:{id}` | Update enrollment status |
| User buys from Creator | Follow `instructor:{id}` | Already tracked via purchase |
| New post in course | Activity created | Optional: cache for search |

---

## References

### Official Documentation
- [Stream Activity Feeds Overview](https://getstream.io/activity-feeds/)
- [Activity Feeds Documentation](https://getstream.io/activity-feeds/docs/)
- [Node.js Quick Start](https://getstream.io/activity-feeds/docs/node/)
- [Feeds API - Node.js](https://getstream.io/activity-feeds/docs/node/feeds/)
- [Tokens & Authentication (JavaScript)](https://getstream.io/activity-feeds/docs/javascript/tokens-and-authentication/)
- [Targeting with TO Field](https://getstream.io/activity-feeds/docs/node/targeting/)

### Permissions & Security
- [Feeds Permission Policies and JWT tokens](https://support.getstream.io/hc/en-us/articles/360042760574-Feeds-Permission-Policies-and-JWT-tokens)
- [How to create Private and Public content](https://support.getstream.io/hc/en-us/articles/4404428844183-How-to-create-Private-and-Public-content-with-Stream-Feeds)
- [How to set up private Feed Groups](https://support.getstream.io/hc/en-us/articles/1500006211181-How-to-set-up-private-Feed-Groups-with-Stream-Feeds)
- [Stream Security](https://getstream.io/security/)

### React SDK
- [React Activity Feeds SDK](https://getstream.io/activity-feeds/docs/react/)
- [Stream Chat React Docs](https://getstream.io/chat/docs/react/)

### Other Resources
- [Stream Pricing](https://getstream.io/pricing/)
- [Feeds V3 Architecture Blog](https://getstream.io/blog/feeds-v3-architecture/)
- [Real-time Notification Feed API](https://getstream.io/activity-feeds/notification-feeds/)
