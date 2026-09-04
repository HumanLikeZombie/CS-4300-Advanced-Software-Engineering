# Stakeholder Feature Request — The Care Board

Tiny Dragon Daycare is growing, and the staff have noticed a problem: **different parts of the application can describe Puff's care needs differently.** That is manageable with one tiny dragon, but it will become dangerous as the system grows.

The daycare wants a new **Care Board recommendation** on Puff's home page.

## Required behavior

The Care Board must show exactly one current recommendation using the following priority order:

1. **FEED NOW** — if Puff's hunger is **8 or higher**.
2. **REST** — if Puff's energy is **2 or lower** and the FEED NOW rule does not apply.
3. **OFFER SNACK** — if Puff's hunger is **6 or 7** and neither higher-priority rule applies.
4. **ALL CLEAR** — otherwise.

If more than one condition is true, the higher-priority recommendation wins. For example, a dragon with hunger `9` and energy `1` should receive **FEED NOW**, not REST.

## Consistency requirement

The existing application already makes care decisions in more than one place. After your change:

- the home-page care messaging must agree with the Care Board recommendation;
- existing feeding behavior must remain correct unless this request explicitly changes it; and
- the care-policy thresholds used by the application should not be duplicated across presentation and domain logic.

The daycare expects these rules to change again in the future. Your design should make a future threshold or priority change safer than it is in the starter code.

## Evidence

Add tests that demonstrate:

- each Care Board recommendation;
- at least one priority case in which multiple conditions are true;
- preservation of important existing behavior; and
- the behavior of any refactored code you depend on.

Do not simply change code until the new feature appears to work. Establish the current behavior, protect it with appropriate tests, improve the design, and then implement the feature.
