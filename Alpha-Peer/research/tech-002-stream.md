# tech-002: Stream

**Type:** Chat, Activity Feeds, Video Platform
**Status:** REQUIRED (Client-Specified)
**Research Date:** 2025-11-30
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

- [ ] What's the expected MAU for chat at Genesis Cohort launch?
- [ ] Will all 6 user roles need chat access?
- [ ] Should student-to-student chat be gated (e.g., only after course enrollment)?
- [ ] How should community feeds be organized (per Creator? Platform-wide?)

---

## References

- [Stream Chat React Docs](https://getstream.io/chat/docs/react/)
- [Stream Activity Feeds Docs](https://getstream.io/activity-feeds/docs/)
- [Stream Pricing](https://getstream.io/pricing/)
