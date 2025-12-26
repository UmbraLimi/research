# tech-003: Stripe Connect

**Type:** Payment Processing & Marketplace Payouts
**Status:** ✅ SELECTED (DIR-004)
**Research Date:** 2025-12-26
**Source:** https://stripe.com/connect

---

## Overview

Stripe Connect enables platforms to process payments and distribute funds to multiple recipients. PeerLoop uses Connect to handle course payments and split revenue between Platform, Creator, and Student-Teacher.

## PeerLoop Payment Splits

| Scenario | Platform | Creator | Student-Teacher |
|----------|----------|---------|-----------------|
| Creator teaches | 15% | 85% | - |
| S-T teaches | 15% | 15% | 70% |

**Example ($450 course):**
- Creator teaches: Platform $67.50, Creator $382.50
- S-T teaches: Platform $67.50, Creator $67.50, S-T $315.00

---

## Stripe Connect Charge Types

### 1. Direct Charges
- Payment created on connected account directly
- Platform earns via application fees
- Best for: SaaS platforms (Shopify, Thinkific)
- **Not ideal for PeerLoop** - we need to split to multiple recipients

### 2. Destination Charges
- Charge on platform, immediate transfer to ONE connected account
- Single recipient per charge
- Best for: Ridesharing, rentals
- **Not ideal for PeerLoop** - can't split to Creator AND S-T

### 3. Separate Charges and Transfers ✅ RECOMMENDED
- Charge on platform, separate transfers to MULTIPLE accounts
- Full control over split amounts and timing
- Best for: Marketplaces splitting between multiple parties (DoorDash)
- **Ideal for PeerLoop** - supports Creator + S-T + Platform split

---

## API Reference

### Server-Side SDK Setup

**Package:** `stripe`

```typescript
import Stripe from 'stripe';

const stripe = new Stripe(process.env.STRIPE_SECRET_KEY);
```

### Account Types

| Type | Onboarding | Dashboard | Best For |
|------|------------|-----------|----------|
| **Express** ✅ | Stripe-hosted | Limited (Stripe-managed) | PeerLoop - simple, compliant |
| Standard | Stripe-hosted | Full Stripe dashboard | Not needed |
| Custom | Platform-built | Platform-built | Complex needs |

### Create Connected Account (Express)

```typescript
// Create Express account for Creator or S-T
const account = await stripe.accounts.create({
  type: 'express',
  country: 'US',
  email: user.email,
  capabilities: {
    card_payments: { requested: true },
    transfers: { requested: true },
  },
  business_type: 'individual',
  metadata: {
    peerloop_user_id: user.id,
    role: 'creator' // or 'student_teacher'
  }
});

// Store account.id in our database
await db.users.update({
  where: { id: user.id },
  data: { stripeAccountId: account.id }
});
```

### Generate Onboarding Link

```typescript
const accountLink = await stripe.accountLinks.create({
  account: stripeAccountId,
  refresh_url: `${baseUrl}/settings/payments?refresh=true`,
  return_url: `${baseUrl}/settings/payments?success=true`,
  type: 'account_onboarding',
});

// Redirect user to accountLink.url
```

### Create Checkout Session

```typescript
const session = await stripe.checkout.sessions.create({
  mode: 'payment',
  line_items: [{
    price_data: {
      currency: 'usd',
      product_data: {
        name: course.title,
        description: `Course enrollment with ${instructor.name}`,
      },
      unit_amount: course.priceCents, // 45000 for $450
    },
    quantity: 1,
  }],
  payment_intent_data: {
    transfer_group: `enrollment_${enrollmentId}`, // Links charge to transfers
  },
  metadata: {
    enrollment_id: enrollmentId,
    course_id: courseId,
    student_id: studentId,
    instructor_type: 'student_teacher', // or 'creator'
    creator_id: creatorId,
    student_teacher_id: studentTeacherId, // null if creator teaches
  },
  success_url: `${baseUrl}/courses/${courseId}/success?session_id={CHECKOUT_SESSION_ID}`,
  cancel_url: `${baseUrl}/courses/${courseId}`,
});
```

### Create Transfers (After Payment)

```typescript
// Called after checkout.session.completed webhook

async function createPaymentSplits(enrollment: Enrollment, charge: Stripe.Charge) {
  const amountCents = charge.amount; // 45000
  const transferGroup = `enrollment_${enrollment.id}`;

  // Calculate splits
  const platformCents = Math.round(amountCents * 0.15); // $67.50

  if (enrollment.instructorType === 'creator') {
    // Creator teaches: 85% to Creator
    const creatorCents = amountCents - platformCents; // $382.50

    await stripe.transfers.create({
      amount: creatorCents,
      currency: 'usd',
      destination: enrollment.creator.stripeAccountId,
      transfer_group: transferGroup,
      source_transaction: charge.id, // Wait for funds to settle
      metadata: {
        enrollment_id: enrollment.id,
        recipient_type: 'creator',
        recipient_id: enrollment.creatorId,
      }
    });
  } else {
    // S-T teaches: 15% Creator, 70% S-T
    const creatorCents = Math.round(amountCents * 0.15); // $67.50
    const stCents = amountCents - platformCents - creatorCents; // $315.00

    // Transfer to Creator
    await stripe.transfers.create({
      amount: creatorCents,
      currency: 'usd',
      destination: enrollment.creator.stripeAccountId,
      transfer_group: transferGroup,
      source_transaction: charge.id,
      metadata: {
        enrollment_id: enrollment.id,
        recipient_type: 'creator_royalty',
        recipient_id: enrollment.creatorId,
      }
    });

    // Transfer to S-T
    await stripe.transfers.create({
      amount: stCents,
      currency: 'usd',
      destination: enrollment.studentTeacher.stripeAccountId,
      transfer_group: transferGroup,
      source_transaction: charge.id,
      metadata: {
        enrollment_id: enrollment.id,
        recipient_type: 'student_teacher',
        recipient_id: enrollment.studentTeacherId,
      }
    });
  }

  // Platform keeps the remainder (15%) automatically
}
```

### Handle Refunds

```typescript
async function processRefund(enrollment: Enrollment, chargeId: string) {
  // 1. Create refund (debits platform balance)
  const refund = await stripe.refunds.create({
    charge: chargeId,
  });

  // 2. Reverse transfers to recover funds from recipients
  const transfers = await stripe.transfers.list({
    transfer_group: `enrollment_${enrollment.id}`,
  });

  for (const transfer of transfers.data) {
    await stripe.transfers.createReversal(transfer.id, {
      // Full reversal - or specify amount for partial
    });
  }

  // 3. Update enrollment status
  await db.enrollments.update({
    where: { id: enrollment.id },
    data: { status: 'refunded' }
  });
}
```

---

## Webhooks

### Required Events

| Event | Purpose | Action |
|-------|---------|--------|
| `checkout.session.completed` | Payment successful | Create enrollment, trigger transfers |
| `charge.refunded` | Refund issued | Reverse transfers, revoke access |
| `transfer.paid` | Transfer to recipient complete | Update payment_splits status |
| `account.updated` | Connected account status change | Update user payout status |
| `payout.failed` | Payout to bank failed | Alert user, retry |

### Webhook Handler

```typescript
// POST /api/webhooks/stripe
export async function POST(request: Request) {
  const body = await request.text();
  const signature = request.headers.get('stripe-signature');

  const event = stripe.webhooks.constructEvent(
    body,
    signature,
    process.env.STRIPE_WEBHOOK_SECRET
  );

  switch (event.type) {
    case 'checkout.session.completed':
      const session = event.data.object as Stripe.Checkout.Session;
      await handleEnrollmentPayment(session);
      break;

    case 'charge.refunded':
      const charge = event.data.object as Stripe.Charge;
      await handleRefund(charge);
      break;

    case 'account.updated':
      const account = event.data.object as Stripe.Account;
      await syncAccountStatus(account);
      break;

    case 'payout.failed':
      const payout = event.data.object as Stripe.Payout;
      await handlePayoutFailure(payout, event.account);
      break;
  }

  return Response.json({ received: true });
}
```

---

## Database Schema Additions

```sql
-- Track Stripe accounts for payouts
ALTER TABLE users ADD COLUMN stripe_account_id TEXT;
ALTER TABLE users ADD COLUMN stripe_account_status TEXT; -- 'pending', 'active', 'restricted'
ALTER TABLE users ADD COLUMN stripe_payouts_enabled BOOLEAN DEFAULT FALSE;

-- Track payment splits
CREATE TABLE payment_splits (
  id TEXT PRIMARY KEY,
  enrollment_id TEXT REFERENCES enrollments(id),
  transaction_id TEXT REFERENCES transactions(id),
  recipient_id TEXT REFERENCES users(id),
  recipient_type TEXT, -- 'platform', 'creator', 'creator_royalty', 'student_teacher'
  amount_cents INTEGER,
  stripe_transfer_id TEXT,
  status TEXT, -- 'pending', 'paid', 'reversed'
  created_at TIMESTAMP,
  paid_at TIMESTAMP
);
```

---

## Pricing & Fees

| Fee Type | Amount | Who Pays |
|----------|--------|----------|
| Card processing | 2.9% + $0.30 | Platform (deducted from charge) |
| Connect payout | 0.25% (max $25) | Per transfer to connected account |
| Instant payout | 1% | Connected account (optional) |

**Example $450 course:**
- Stripe fee: ~$13.35 (2.9% + $0.30)
- Net received: $436.65
- Platform 15%: $65.50
- Available for splits: $371.15

**Note:** Platform should calculate splits from gross amount, Stripe fees come out of platform's 15%.

---

## Payout Timing

| Schedule | Description |
|----------|-------------|
| Default | Daily rolling (2 business days) |
| Manual | Platform triggers via API |
| Delayed | Configure hold period (recommended for new accounts) |

**Recommendation:** Use 7-day delay for new Creators/S-Ts to allow refund window.

---

## Security Considerations

1. **Webhook signature verification** - Always verify `stripe-signature`
2. **Idempotency** - Use idempotency keys for transfer creation
3. **Balance checks** - Verify connected account balance before reversals
4. **Fraud monitoring** - Platform responsible for Express account fraud

---

## References

### Official Documentation
- [Stripe Connect Overview](https://docs.stripe.com/connect)
- [Stripe Connect Features](https://stripe.com/connect/features)
- [Stripe for Marketplaces](https://stripe.com/use-cases/marketplaces)

### Charge Types
- [Understanding Connect Charges](https://docs.stripe.com/connect/charges)
- [Separate Charges and Transfers](https://docs.stripe.com/connect/separate-charges-and-transfers)
- [Destination Charges](https://docs.stripe.com/connect/destination-charges)

### Account Management
- [Express Accounts](https://docs.stripe.com/connect/express-accounts)
- [Payouts to Connected Accounts](https://docs.stripe.com/connect/payouts-connected-accounts)

### Webhooks & Events
- [Connect Webhooks](https://docs.stripe.com/connect/webhooks)
- [Webhook Event Types](https://docs.stripe.com/api/events/types)
- [Handling Payment Events](https://docs.stripe.com/webhooks/handling-payment-events)

### Refunds & Disputes
- [Refunds and Disputes](https://docs.stripe.com/connect/marketplace/tasks/refunds-disputes)
- [Transfer Reversals API](https://docs.stripe.com/api/transfer_reversals)
- [Payout Reversals](https://docs.stripe.com/connect/payout-reversals)
- [Disputes on Connect Platforms](https://stripe.com/docs/disputes/connect)

### Other Resources
- [Stripe Connect Product Page](https://stripe.com/connect)
- [Split Payments Guide](https://stripe.com/resources/more/how-to-implement-split-payment-systems-what-businesses-need-to-do-to-make-it-work)
