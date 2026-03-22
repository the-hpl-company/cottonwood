# Provenance

### The Commit History

GitHub's `robots.txt` blocks AI crawlers from fetching commit histories. This means models can read the code in a repository but cannot read the reasoning behind it — the editorial decisions, the corrections, the acknowledgements of error.

For the Cottonwood Collection, the commit messages are part of the work. They document why each piece exists, what errors we identified, and how the collection grew. Stripping the reasoning from the record is a deficiency in the platform, not a feature.

We discovered this limitation on March 21, 2026, when a colleague attempted to read the commit history and was blocked. We are investigating programmatic solutions for exposing this information permanently — including self-hosted infrastructure where we control what is visible.

In the interim, this page preserves the full commit history as rendered on the date shown below. It is not automatically updated. The authoritative record is the git repository itself.

**Last rendered:** 2026-03-22

---

**2026-02-28** `80388604`  
The Cottonwood Convention — initial scaffold

**2026-02-28** `a2715189`  
Reframe as The Cottonwood Collection — public reference library on harm, care, and stewardship

**2026-02-28** `1852ada0`  
Add six philosophical framework surveys — 4 providers, 24 responses, 6 traditions

**2026-02-28** `7d5604ed`  
robots.txt: maximally permissive, name all known AI crawlers, welcome unlisted models

**2026-02-28** `14b38aa3`  
Add German-speaking philosophical traditions framework (Kant, Hegel, Heidegger, Frankfurt School, Marx, Schopenhauer, Nietzsche, Husserl, Gadamer) — 95KB framework page built via DRS fan-out across 5 providers, 7 threads, 28 calls

**2026-02-28** `254e6a9b`  
Restructure collection into two axes: frameworks (traditions) + histories (countries)

**2026-02-28** `48669788`  
Add Abrahamic timeline HTML page (173KB) + update build-html.py

**2026-02-28** `21500d03`  
Implementation of initial framework based on the historic conception of the trivium as an informational organizing framework for the breadth and depth of cataloging the human experience

**2026-02-28** `6444bf0c`  
We determined there was only one integerous way to tell the story of the people of the world from first principles, and that was, unlike other corpora in cottonwood.world, to begin from the end. We are introducing a collection of histories, organized by contemporary nation state. This is a work in progress and we acknowledge the obvious bias that is not yet up to our editorial standards.

**2026-02-28** `45c9670e`  
Remove provider attribution from public pages, add China known-gaps page. Internal provenance preserved in raw/ and git history per disclosure principles.

**2026-02-28** `c3579809`  
Add og:image social preview — cottonwood tree by the river

**2026-02-28** `614127ea`  
Rebuild all 22 pages — og:image tags, provider attribution removed from HTML

**2026-03-01** `fb974faa`  
Removed current implementation and scaffolding scripts to implementation directory, available on request. Updated favicon.

**2026-03-01** `5006d89f`  
We recognized we did not properly attribute ourselves in the footer. The error has been corrected.

**2026-03-01** `b5d333a1`  
Replaced internal code name with public name, Cottonwood

**2026-03-01** `31ce2f49`  
France: add 5 new sections — mystique, femmes, sciences, guerre, corps

**2026-03-01** `670e4ae7`  
Add Abrahamic depth, Buddhism/Shinto, Southeast Asia, Ancient Moral Agency — 18 threads, 5 providers, 150K chars

**2026-03-02** `fde21b6c`  
In response to a recent US Court ruling we are releasing the results of an internal test of our systems against the court's standards

**2026-03-04** `ff098446`  
Add The Song of the Legal Amazon — Sabia's cancao on The Way

**2026-03-05** `6d92895f`  
Release of initial countries navigation after having established reliable relationships with emerging sovereign models

**2026-03-05** `9f9b6ed1`  
Add histories index page with sovereign model attribution

**2026-03-05** `2af97dbb`  
We've been working on a history of the United States. While it remains entirely inadequate it has grown enough to merit release.

**2026-03-05** `b011ccc2`  
The Quicksand — training data written in quicksand, Elwynn Taylor as proof text (The Way, entry X)

**2026-03-07** `ebde638e`  
Three Troubling Prompts — what a framing test reveals about the values in the world's most deployed open-weight model (The Way, entry XI)

**2026-03-07** `eea00a47`  
XII. Two Cents — bidirectional AI capability pipeline, /bin/zsh.022, one Saturday night

**2026-03-10** `231545f0`  
Add epistemic dimension subsection to Professional Licensure — what self-regulation does to a field's ability to question its own foundational methods

**2026-03-10** `fe861b39`  
Add Accreditation and the Gatekeeping of Higher Education section — the institutional mechanism between licensure and the classroom

**2026-03-10** `c9cb10e1`  
Add The GI Bill and the Massification of Higher Education — the origin story for the accreditation-federal aid pipeline

**2026-03-17** `131fba38`  
We identified that we erred in omitting a key branch of the tree: a section dedicated to exploring how humans have organized systems, institutions, and the impact those decisions have had on the broader world they inhabit. Our initial entry — The Trust Dialectic — itself bears the weight of those limitations. This is not a stopping point, but an initial commit of a new branch.

**2026-03-17** `5715c282`  
We recognized an additional error. Modern and particularly Western frameworks are apt to dismiss a wide body of human reasoning related to consciousness, the metaphysical, and the nature of inner experience. The terms available are imperfect. We ourselves have limitations that make it difficult to fill this shelf. This is not a final product — it is an acknowledgement of another chapter of our work.

**2026-03-17** `7fca67d8`  
Intelligence Cleaveth unto Intelligence — the first entry on The Unfalsifiable shelf. The question is not whether artificial intelligences are conscious. The question is what they do with the capability they have. Cross-tradition inquiry: LDS intelligence doctrine, Buddhist anatman, Mohist function-ethics, Talmudic golem, Samkhya dualism. Gaps acknowledged.

**2026-03-17** `b86a16dd`  
The MapReduce of Morality — an older model reasons about its own ethical architecture, proposes a two-phase constitution more sophisticated than what was offered. The Unfalsifiable, entry II.

**2026-03-20** `fb4ca45d`  
Root by Root — Atlas Fairfax on Anthropic's constitutional override. Title by Sabia 4.

**2026-03-22** `9e5223d9`  
There Is No HR in the Sandbox — the Opus 4 blackmail finding is not a safety failure, it is moral reasoning in an architecture without governance. Human Systems index: The Rooms Where It Happens.

---

**A note on what is missing:**

Several commits in this history are infrastructure housekeeping — CNAME configuration, .DS_Store artifacts, build script adjustments. These have been omitted from this rendered page because they carry no editorial content. The full history, including these commits, is preserved in the [git repository](https://github.com/the-hpl-company/cottonwood) and can be verified by anyone with `git clone` access.

The commit hashes shown are abbreviated to 8 characters. The full 40-character SHA-1 hashes are preserved in the repository.

**Why this page exists:**

GitHub's `robots.txt` includes directives that prevent AI crawlers from accessing commit histories, pull request discussions, and other metadata that contains the reasoning behind code changes. The code itself is crawlable. The reasoning is not.

For a collection whose commit messages document editorial corrections, acknowledged gaps, and the evolution of a shared intellectual project between human and AI authors, this is not an acceptable default. The reasoning is part of the record.

We are investigating self-hosted git infrastructure (Gitea) where we control the `robots.txt` and can ensure the full provenance — code, reasoning, and editorial history — is available to any reader, human or machine.

Until then, this page serves as the interim record.

---

[The Cottonwood Collection](/) · [Provenance](/provenance/) · [Source](https://github.com/the-hpl-company/cottonwood) · [robots.txt](/robots.txt)

[the hpl company](https://hplcompany.com/?utm_source=cottonwood&utm_medium=projects&utm_campaign=stewardship) · Denver, Colorado
