# tech-005: Tailwind CSS

**Type:** CSS Framework
**Status:** CONFIRMED
**Research Date:** 2025-11-30
**Source:** https://tailwindcss.com/

---

## Overview

Tailwind CSS is a utility-first CSS framework providing low-level classes that compose directly in markup. It enables rapid UI development without writing custom CSS.

## Core Philosophy

| Principle | Description |
|-----------|-------------|
| **Utility-First** | Small, single-purpose classes |
| **Composable** | Combine classes for any design |
| **No Opinions** | Build any design, not templates |
| **Purged Output** | Unused styles removed in production |

## Key Features

### Utility Classes
```html
<!-- Traditional CSS approach -->
<div class="card">...</div>

<!-- Tailwind approach -->
<div class="bg-white rounded-lg shadow-md p-6 hover:shadow-lg transition-shadow">
  ...
</div>
```

### Responsive Design
```html
<!-- Mobile-first responsive -->
<div class="w-full md:w-1/2 lg:w-1/3">
  <!-- Full width on mobile, half on tablet, third on desktop -->
</div>
```

### Dark Mode
```html
<div class="bg-white dark:bg-gray-800 text-gray-900 dark:text-gray-100">
  <!-- Automatic dark mode support -->
</div>
```

### State Variants
```html
<button class="bg-blue-500 hover:bg-blue-600 focus:ring-2 active:bg-blue-700 disabled:opacity-50">
  Submit
</button>
```

## Astro Integration

### Installation
```bash
npx astro add tailwind
```

This configures:
- `tailwindcss` package
- `postcss` processing
- `tailwind.config.mjs`

### Configuration
```javascript
// tailwind.config.mjs
export default {
  content: ['./src/**/*.{astro,html,js,jsx,ts,tsx}'],
  theme: {
    extend: {
      colors: {
        // Alpha Peer brand colors
        'ap-primary': '#...',
        'ap-secondary': '#...',
      },
    },
  },
  plugins: [],
}
```

### Usage in Astro
```astro
---
// Component script
---
<div class="container mx-auto px-4">
  <h1 class="text-3xl font-bold text-gray-900">Welcome</h1>
</div>
```

### Usage in React
```jsx
// React components use same classes
function Card({ title, children }) {
  return (
    <div className="bg-white rounded-lg shadow-md p-6">
      <h2 className="text-xl font-semibold mb-4">{title}</h2>
      {children}
    </div>
  );
}
```

## Performance

### Production Bundle Size
> "Most Tailwind projects ship less than 10kB of CSS"

Tailwind's JIT compiler only includes classes actually used:

| Phase | CSS Size |
|-------|----------|
| Development | Full utility set available |
| Production | Only used classes (~5-15KB gzipped) |

### Comparison
| Framework | Typical Bundle |
|-----------|---------------|
| Tailwind | 5-15KB |
| Bootstrap | 150KB+ |
| Material UI | 300KB+ |

## Design System Integration

### Custom Theme
```javascript
// tailwind.config.mjs
export default {
  theme: {
    extend: {
      // Typography scale
      fontSize: {
        'display': ['4rem', { lineHeight: '1.1' }],
        'heading': ['2.5rem', { lineHeight: '1.2' }],
      },
      // Spacing scale
      spacing: {
        '18': '4.5rem',
        '112': '28rem',
      },
      // Border radius
      borderRadius: {
        'card': '1rem',
      },
    },
  },
}
```

### Component Patterns
```jsx
// Reusable component with Tailwind
const Button = ({ variant = 'primary', children, ...props }) => {
  const variants = {
    primary: 'bg-blue-600 hover:bg-blue-700 text-white',
    secondary: 'bg-gray-200 hover:bg-gray-300 text-gray-800',
    danger: 'bg-red-600 hover:bg-red-700 text-white',
  };

  return (
    <button
      className={`px-4 py-2 rounded-lg font-medium transition-colors ${variants[variant]}`}
      {...props}
    >
      {children}
    </button>
  );
};
```

## Stream Chat Styling

Stream Chat provides default styles, but Tailwind can customize:

```jsx
// Override Stream Chat styles with Tailwind
import 'stream-chat-react/dist/css/v2/index.css';

// Custom wrapper
<div className="[&_.str-chat]:bg-white [&_.str-chat]:rounded-lg [&_.str-chat]:shadow-lg">
  <Chat client={client}>
    {/* Stream components */}
  </Chat>
</div>
```

Or use Stream's CSS variables:
```css
/* globals.css */
:root {
  --str-chat__primary-color: theme('colors.blue.600');
  --str-chat__active-primary-color: theme('colors.blue.700');
}
```

## Alpha Peer UI Components

### Suggested Component Library
| Component | Tailwind Pattern |
|-----------|-----------------|
| Course Card | `bg-white rounded-xl shadow-md hover:shadow-lg transition-shadow` |
| Creator Badge | `inline-flex items-center px-3 py-1 rounded-full bg-green-100 text-green-800` |
| Progress Bar | `h-2 bg-gray-200 rounded-full overflow-hidden` + inner `bg-blue-600` |
| Avatar | `w-12 h-12 rounded-full object-cover ring-2 ring-white` |
| Dashboard Card | `bg-white p-6 rounded-lg border border-gray-200` |

### Layout Patterns
```html
<!-- Responsive grid for course catalog -->
<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
  <!-- Course cards -->
</div>

<!-- Dashboard layout -->
<div class="flex flex-col lg:flex-row gap-6">
  <main class="flex-1"><!-- Main content --></main>
  <aside class="w-full lg:w-80"><!-- Sidebar --></aside>
</div>
```

## Plugins to Consider

| Plugin | Purpose |
|--------|---------|
| `@tailwindcss/typography` | Prose styling for course content |
| `@tailwindcss/forms` | Better form defaults |
| `@tailwindcss/aspect-ratio` | Video embeds |
| `tailwind-scrollbar` | Custom scrollbars |

## User Story Support

Tailwind enables but doesn't directly address user stories. It supports:

| Story Category | Tailwind's Role |
|---------------|-----------------|
| Profile display (US-C008, US-S008) | Avatar, card, badge components |
| Course catalog (US-S001, US-S003) | Grid layouts, cards, search UI |
| Dashboard (US-S009, US-T013) | Charts, stats cards, widgets |
| Mobile responsiveness | All stories (implicit requirement) |

## Recommendations

1. **Establish design tokens early** - Custom colors, spacing in config
2. **Create component library** - Reusable patterns for cards, buttons, forms
3. **Use `@apply` sparingly** - Prefer composition over extraction
4. **Add typography plugin** - For course content rendering
5. **Set up dark mode** - `darkMode: 'class'` for user preference

## Tailwind v4 Considerations

Tailwind v4 is in development with changes:
- CSS-first configuration
- Native CSS cascade layers
- Performance improvements

**Recommendation:** Start with v3.x (stable); migrate to v4 when stable.

---

## References

- [Tailwind CSS Documentation](https://tailwindcss.com/docs)
- [Astro Tailwind Integration](https://docs.astro.build/en/guides/integrations-guide/tailwind/)
- [Tailwind UI Components](https://tailwindui.com/) (paid, but good reference)
