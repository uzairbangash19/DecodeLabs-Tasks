# Phishing Awareness Analysis

## Goal
Analyze sample emails/messages to identify phishing attempts, list red flags, and explain why each message is unsafe.

---

## Sample 1: Fake IT Password Reset

**Message:**
```
From: IT Security Team <support@login-updates.com>
Subject: URGENT: Your password expires in 24 hours

Dear Employee,

Your company account password will expire in 24 hours. Failure to
update it immediately will result in permanent account suspension.

Click below to reset your password now:
http://secure-login.company-verify.net/reset

Regards,
IT Support Team
```

### Suspicious Links / Keywords
- Sender domain `login-updates.com` does not match the company's real domain.
- Reset link points to `company-verify.net`, a lookalike domain, not the organization's actual site.
- Keywords: **"URGENT"**, **"24 hours"**, **"permanent suspension"** — designed to create panic.

### Red Flags Identified
1. **Sender-domain mismatch** — display name says "IT Security Team" but the email address is external.
2. **Urgency/fear trigger** — artificial deadline to prevent careful thinking.
3. **Domain spoofing (combosquatting)** — "company-verify.net" adds a trust word to look legitimate.
4. **Generic greeting** — "Dear Employee" instead of the recipient's actual name.

### Why It's Unsafe
The email pressures the recipient into clicking a credential-harvesting link before they have time to verify it. The real company domain is spoofed with a similar-looking one, a classic technique to steal login credentials via a fake sign-in page.

---

## Sample 2: CEO Wire Transfer Request (Business Email Compromise)

**Message:**
```
From: CEO Name <ceo.office@executive-update.com>
Subject: IMMEDIATE ACTION REQUIRED - Confidential

I'm currently in a meeting and can't take calls. I need you to
process an urgent wire transfer of $18,500 to a new vendor before
end of day. This is time-sensitive and confidential — do not
discuss with anyone else on the team.

I'll send account details shortly.

Thanks,
[CEO Name]
```

### Suspicious Links / Keywords
- No malicious link here — the "payload" is the instruction itself.
- Keywords: **"IMMEDIATE ACTION"**, **"confidential"**, **"do not discuss"**, **"urgent wire transfer"**.

### Red Flags Identified
1. **Authority impersonation** — pretends to be a senior executive.
2. **Urgency trigger** — "before end of day" removes time to verify.
3. **Secrecy/bypass request** — asking to skip normal approval processes and stay silent.
4. **Sender domain mismatch** — `executive-update.com` is not the company's real domain.
5. **Unusual request pattern** — CEOs rarely request wire transfers directly over email without following standard procurement steps.

### Why It's Unsafe
This is a textbook **Business Email Compromise (BEC)** attempt. It combines authority + urgency + secrecy to bypass an employee's normal judgment and financial controls, aiming to trick them into an unauthorized wire transfer.

---

## Sample 3: Fake Package Delivery SMS (Smishing)

**Message:**
```
FedEx: Your package could not be delivered due to an incomplete
address. Update your delivery details within 12 hours to avoid
return to sender: http://fedex-tracking-update.info/confirm
```

### Suspicious Links / Keywords
- Link domain `fedex-tracking-update.info` is not FedEx's real domain (typosquatting/combosquatting).
- Keywords: **"could not be delivered"**, **"within 12 hours"**, **"avoid return to sender"**.

### Red Flags Identified
1. **Smishing (SMS-based phishing)** — delivered via text to bypass email filters.
2. **Urgency trigger** — short deadline forces a quick, unverified click.
3. **Lookalike domain** — uses "fedex" as a keyword but the actual root domain is unrelated to FedEx.
4. **Unsolicited tracking notice** — sent without the recipient necessarily expecting a delivery.

### Why It's Unsafe
Mobile users are especially vulnerable to smishing because phones often show shortened or partial URLs, making it harder to spot the fake domain. Clicking the link would likely lead to a fake tracking/payment page designed to harvest personal or card details.

---

## Bonus: Employee Red Flag Checklist

A quick-reference checklist non-experts can use when triaging a suspicious message:

- [ ] Does the sender's actual email address match the display name and known domain?
- [ ] Is there unusual urgency, pressure, or a threat of negative consequences?
- [ ] Does it ask you to bypass normal procedures or keep the request secret?
- [ ] Are there spelling/grammar irregularities or a generic greeting?
- [ ] Do links, when hovered over, lead to a different or misspelled domain?
- [ ] Are you being asked for passwords, MFA codes, or payment details over email/text?
- [ ] Is there an unexpected attachment with an unusual file type (.iso, .js, .scr)?
- [ ] Would this request normally go through a different, verified channel?

**Rule of thumb: Pause → Verify (via a separate, known channel) → Report.**

---

## Key Skills Demonstrated
- Threat analysis and phishing pattern recognition
- Awareness of social engineering tactics (authority, urgency, curiosity, fear/greed)
- Practical security thinking applicable to non-technical employees
