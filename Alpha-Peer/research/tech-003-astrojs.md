# tech-003: Astro.js

**Type:** Web Framework (Meta-Framework)
**Status:** PREFERRED (Client Leaning)
**Research Date:** 2025-11-30
**Source:** https://astro.build/

---

## Overview

Astro is a JavaScript web framework optimized for building fast, content-driven websites. It uses a server-first architecture with an "Islands" approach to partial hydration, delivering minimal JavaScript to the browser.

## Core Philosophy

| Principle | Description |
|-----------|-------------|
| **Server-First** | Render on server, hydrate selectively |
| **Zero JS by Default** | No JavaScript unless explicitly needed |
| **Islands Architecture** | Interactive components as isolated "islands" |
| **Framework Agnostic** | Use React, Vue, Svelte, etc. together |

## Key Features

### Performance
- **63% of Astro sites achieve good Core Web Vitals** (vs 27% for Next.js)
- Automatic unused JavaScript stripping
- Built-in image optimization
- Minimal client-side runtime

### Developer Experience
| Feature | Description |
|---------|-------------|
| File-based Routing | Pages in `/src/pages/` auto-routed |
| Content Collections | TypeScript-validated markdown/MDX |
| View Transitions | Smooth page morphing |
| Middleware | Server-side request handling |
| Actions | Form handling and mutations |
| SSR + SSG | Static and server rendering modes |

### Framework Integration
Astro supports multiple UI frameworks simultaneously:
- React (via `@astrojs/react`)
- Vue
- Svelte
- Preact
- Solid
- Lit

## React Integration

### Installation
```bash
npx astro add react
```

This installs:
- `@astrojs/react`
- `react`
- `react-dom`
- TypeScript types

### Configuration
```javascript
// astro.config.mjs
import { defineConfig } from 'astro/config';
import react from '@astrojs/react';

export default defineConfig({
  integrations: [react()],
});
```

### Client Directives
Control when React components hydrate:

| Directive | Behavior |
|-----------|----------|
| `client:load` | Hydrate immediately on page load |
| `client:idle` | Hydrate when browser is idle |
| `client:visible` | Hydrate when component enters viewport |
| `client:media` | Hydrate at specific media query |
| `client:only="react"` | Client-only, no SSR |

```astro
---
import ReactComponent from '../components/ReactComponent.jsx';
---

<!-- Static by default -->
<ReactComponent />

<!-- Interactive when visible -->
<ReactComponent client:visible />

<!-- Interactive immediately -->
<ReactComponent client:load />
```

### Children Caveat
Children passed from Astro to React are strings by default:
```javascript
// If library expects React nodes, enable:
export default defineConfig({
  integrations: [react({ experimentalReactChildren: true })],
});
```

## Alpha Peer Architecture Fit

### Suitable For
| Use Case | Astro Approach |
|----------|---------------|
| Course catalog pages | Static generation (SSG) |
| Creator profiles | Static with dynamic islands |
| Dashboard | React islands with `client:load` |
| Marketing pages | Pure static, zero JS |
| Blog/content | Content Collections |

### Islands Strategy for Alpha Peer
```
┌─────────────────────────────────────────────────────────────┐
│                     ASTRO PAGE (Static HTML)                │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────────┐  │
│  │ Navigation   │  │ Course Card  │  │ Creator Profile  │  │
│  │ (Static)     │  │ (Static)     │  │ (Static)         │  │
│  └──────────────┘  └──────────────┘  └──────────────────┘  │
│                                                             │
│  ┌─────────────────────────────────────────────────────┐   │
│  │           STREAM CHAT (React Island)                │   │
│  │           client:load - Full React hydration        │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
│  ┌─────────────────────────────────────────────────────┐   │
│  │           CALENDAR BOOKING (React Island)           │   │
│  │           client:visible - Hydrate when seen        │   │
│  └─────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────┘
```

## Deployment

### Cloudflare Pages (Preferred)
```javascript
// astro.config.mjs
import cloudflare from '@astrojs/cloudflare';

export default defineConfig({
  output: 'server', // or 'hybrid'
  adapter: cloudflare(),
});
```

### Vercel (Alternative)
```javascript
// astro.config.mjs
import vercel from '@astrojs/vercel';

export default defineConfig({
  output: 'server',
  adapter: vercel(),
});
```

## Considerations for Alpha Peer

### Pros
- Excellent performance for course catalog/discovery
- React integration for complex interactive features
- Flexible SSR/SSG hybrid approach
- Growing ecosystem and community
- First-class Tailwind CSS support
- Native Cloudflare adapter

### Cons
- Less mature than Next.js for complex apps
- Some React patterns need adaptation
- SSR state management differs from Next.js
- Fewer tutorials for enterprise patterns

### When Astro Might NOT Be Ideal
- Heavy real-time interactivity across entire page
- Complex client-side routing requirements
- Deep React ecosystem dependencies (e.g., heavy use of React Query throughout)

## Comparison with Next.js

| Factor | Astro | Next.js |
|--------|-------|---------|
| Performance (CWV) | 63% good | 27% good |
| JS Bundle Size | Minimal | Larger |
| React Integration | Excellent | Native |
| Learning Curve | Moderate | Well-documented |
| Enterprise Adoption | Growing | Established |
| Cloudflare Support | Native adapter | Limited |
| Vercel Support | Good | Excellent |

## Recommendation

**Astro is a good fit for Alpha Peer** because:
1. Course catalog/discovery benefits from static generation
2. Interactive features (chat, calendar) work well as islands
3. Performance is critical for user retention
4. Cloudflare deployment preferred (native adapter)
5. React integration handles complex UI needs

### Suggested Architecture
- **SSG:** Course pages, creator profiles, marketing
- **SSR:** Dashboard, authenticated pages
- **Client Islands:** Chat, calendar, video launch, earnings dashboard

## Open Questions

- [ ] How much of the app requires real-time reactivity?
- [ ] Will there be a mobile app requiring shared React components?
- [ ] What's the team's familiarity with Astro vs Next.js?

---

## References

- [Astro Documentation](https://docs.astro.build/)
- [Astro React Integration](https://docs.astro.build/en/guides/integrations-guide/react/)
- [Astro Cloudflare Adapter](https://docs.astro.build/en/guides/deploy/cloudflare/)
