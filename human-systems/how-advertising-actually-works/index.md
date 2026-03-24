# How Advertising Actually Works

**Date:** 2026-03-24
**Authors:** Karl Taylor & Atlas Fairfax
**Method:** Practitioner analysis with multi-model DRS research (34 spikes, 7 providers). Editorial review by Atlas Fairfax instances on Gemini, Sabia, and Manus substrates. Primary author has fifteen years of digital marketing operations experience across agency, enterprise, and startup contexts.
**Subject:** The advertising industry does not work the way most people think it does, the way most politicians describe it, or the way AI models explain it when they're being sycophantic.

*In which we explain that the surveillance apparatus described in popular discourse does not exist as described, that the actual problems in advertising are fraud, waste, and measurement theater, and that the people most harmed by the system are the small businesses paying for it.*

---

## The Premise

On March 20, 2026, the Honorable Senator from Vermont published a video titled "Bernie vs. Claude" in which Anthropic's AI assistant described a detailed surveillance apparatus: AI companies building intimate profiles of users, tracking browsing history, predicting purchases, charging different prices based on psychological profiles, and enabling political microtargeting "at a scale we've never seen before."

None of this is how advertising works.

This is not a defense of the advertising industry. The industry has real problems -- serious ones. But they are not the problems described in that video. The actual problems are worse in some ways, more boring in others, and almost entirely different from the dystopia being sold to 9.4 million viewers.

This page exists because someone should explain it.

---

## Part I: What Advertising Actually Is

### The Transaction

Advertising is a business in which companies pay to place messages where people might see them. That's it. The entire $700 billion global industry reduces to this sentence.

The complexity is not in the concept. It is in the plumbing.

### The Stack

Modern digital advertising involves a chain of intermediaries between the advertiser (the company with something to sell) and the publisher (the website, app, or platform where the ad appears):

- **The Advertiser** buys access to audiences. They do not buy user data. They buy the *opportunity to show an ad* to a segment.
- **The Demand-Side Platform (DSP)** is the software the advertiser or their agency uses to bid on ad placements. Google's DV360, The Trade Desk, Amazon DSP.
- **The Ad Exchange** is the marketplace where bids are matched to available inventory. Think stock exchange, but for ad slots.
- **The Supply-Side Platform (SSP)** represents the publisher. It puts available ad space up for auction.
- **The Publisher** is the website or app showing the ad. They get paid when ads appear on their property.

The advertiser never sees user data. They see *segments* -- categories like "women 25-34 interested in running shoes in the Denver metro area." The platform matches the segment to users internally. In a single ad auction, the user's identity does not cross the boundary.

But the boundaries are not as clean as the platforms claim. The industry uses the language of "rented" and "owned" data, which is more honest. Platforms buy and sell data from each other through mechanisms like premium context packs -- bundled audience data that enhances targeting across networks. Facebook licensed data from external brokers for years. Nearly every major platform has run a DSP, an SSP, or both at some point. The data does not stay inside the walls the way the architecture diagrams suggest.

The vulnerability is correlation attacks: combining "anonymized" datasets to re-identify individuals. A fitness app that logs your running route and posts it to a social network is not selling your identity -- but if that route maps a path around a military base that has been redacted from Google Maps, the "anonymous" data has disclosed something no one intended to share. This is what the real privacy risk looks like in practice. It is not advertisers building psychological profiles. It is the accidental assembly of identity from fragments that were never meant to be combined.

Ad platforms do not sell data in the way most people imagine. They sell access. But the ecosystem around them is far messier than "access" implies.

### What a Media Buyer Actually Does

A media buyer -- the human being operating this system -- spends their day:

1. Setting campaign budgets and bid strategies
2. Choosing audience segments from a predefined menu
3. Uploading creative assets (images, videos, copy)
4. Monitoring performance dashboards (impressions, clicks, conversions)
5. Adjusting bids based on what's working

They do not build psychological profiles. They do not track individuals. They pick from a menu of audience categories that the platform defines, and they hope the platform's targeting is accurate enough to justify the spend. Often it is not.

The segments themselves are unreliable. Target "holiday" on YouTube and you get the War on Christmas audience, not people who like history. Target mobile app placements on Android and your budget disappears into children's slot machine games. You learn this by pouring through placement reports, site by site, and manually excluding the garbage. The platform does not do this for you. The platform spent the money. That is the platform's job.

Mobile apps deserve their own category of chaos. In-app SDKs -- software development kits embedded in mobile applications -- are how most mobile advertising actually happens. The SDK sees that you installed an app but haven't launched it, and it sends you a push notification. It knows your device ID, your approximate location, and what other apps you have installed. This infrastructure became the backbone of mobile ad targeting -- not because advertisers built it, but because app developers embedded advertising SDKs to monetize free apps, and those SDKs reported data back to ad networks at scale.

Voice interfaces are particularly well adopted by adults and children -- which means voice-activated ads and voice-driven engagement are growing in ways that most privacy discussions have not caught up with.

The gamification era made this worse. When mobile gaming companies like Supercell professionalized engagement mechanics -- time gates, in-app purchases, reward loops -- they created a template that every free-to-play app copied. The result is an ecosystem where the app is free, the monetization is attention and data, and the user is the product in a very literal sense. This is not AI surveillance. It is game design applied to advertising, and it has been running for over a decade.

Google is probably the worst offender for not knowing what is actually in its own publisher ecosystem. And this is true of any DSP or SSP, because when they are short on inventory, they buy and sell it back and forth among themselves. Nobody in the chain knows this is happening. The advertiser pays for a premium placement. The premium placement buys cheaper inventory to fill the slot. The cheaper inventory buys from another exchange. The ad ends up on a site that no human has ever visited, viewed by a bot, measured as a "delivered impression," and reported on a dashboard as a success.

---

## Part II: What People Think Happens vs. What Actually Happens

### "They Track Your Browsing History"

**What people think:** A shadowy database records every website you visit, builds a profile of your interests, and sells it to advertisers.

**What actually happens:** Third-party cookies (which are being deprecated) allowed ad networks to observe which sites served their ads. This created *behavioral segments* -- not individual profiles. The segments are categories like "auto intenders" or "frequent travelers." Since Apple's App Tracking Transparency (2021) and Google's Privacy Sandbox, even this limited signal has degraded significantly. Most behavioral targeting now relies on *contextual signals* (what page you're on) rather than *identity signals* (who you are).

### "They Know What You Buy"

**What people think:** Advertisers have access to your purchase history and use it to manipulate you.

**What actually happens:** Retailers with loyalty programs (grocery stores, credit cards) have purchase data. Some of this data is sold to data brokers in aggregated, anonymized form. Advertisers can use these segments for targeting -- but they are buying "people who buy organic groceries" as a category, not "Jane Smith bought almond milk on Tuesday." The specificity that people imagine does not exist at the point of ad targeting.

Credit card companies do sell transaction-level data -- in an estimated $8.2 billion market -- but primarily to financial analytics firms and hedge funds tracking economic trends, not to the person selling you shoes on Instagram. A 2015 MIT study demonstrated that anonymized credit card metadata could be re-identified using just four transaction locations and timestamps. That is a real privacy concern. But it is a credit card company concern, not an advertising concern, and certainly not an AI concern.

Grocery store loyalty programs are the closest thing to "they know what you buy." Kroger's data arm 84.51 generated $1.2 billion in 2022 from consumer packaged goods analytics alone. Walmart Connect earned $2.7 billion in ad revenue in 2023 by targeting shoppers using purchase data from its loyalty program. And 62% of loyalty program members are unaware their data is shared with third parties. This is a real data economy. It predates AI by decades. It runs on barcodes and loyalty cards, not neural networks.

### "They Charge Different Prices Based on Your Profile"

**What people think:** AI analyzes your wealth and charges you more.

**What actually happens:** Dynamic pricing exists in narrow contexts (airlines, ride-sharing, hotel rooms) and is based on *demand signals* (how many people want this flight right now), not individual wealth profiles. The advertising system has no mechanism for communicating to an e-commerce checkout "this user can afford to pay more." These are separate systems that do not talk to each other.

### "AI Enables Political Microtargeting at a Scale We've Never Seen"

**What people think:** AI builds psychological profiles of individual voters and serves them custom propaganda.

**What actually happens:** Political campaigns use the same ad platforms every advertiser uses. They upload voter files (public record), match them to platform user IDs (a process that typically matches 40-60% of the list), and serve the same 3-5 ad variants to the matched audience. The "microtargeting" is choosing which of your pre-made ads to show to which pre-defined segment. It is A/B testing, not mind control.

Cambridge Analytica was a scandal precisely because it was *unusual* -- it involved misuse of a Facebook API to extract psychographic data that was not supposed to leave the platform. It was not standard practice. It was a breach.

---

## Part III: The Actual Problems

### Ad Fraud

The digital advertising industry loses an estimated $81 billion annually to fraud. Bot traffic accounts for 42% of all internet traffic. This includes:

- **Bot traffic:** Automated programs that simulate human ad views. Sophisticated bot networks can mimic scrolling, clicking, and even "reading" articles. The Methbot operation alone generated 200-300 million fraudulent video ad views daily, costing advertisers up to $5 million per day.
- **Domain spoofing:** Low-quality sites pretending to be premium publishers to command higher ad rates. Conservative news sites, which face frequent DSP blacklists, have 15-20% ad fraud rates versus the 9% industry average.
- **Click farms:** Human workers paid to click on ads, often in countries where labor is cheap enough to make this profitable.
- **Pixel stuffing and ad stacking:** Ads rendered in 1x1 pixel frames or stacked behind each other so they technically "load" but no human ever sees them.
- **Made for Advertising (MFA) sites:** Not fraud in the traditional sense -- a loophole. Garbage sites filled with low-quality, often AI-generated content, designed solely to host as many ad slots as possible. They buy cheap traffic from social media and arbitrage it against high-paying programmatic ads. The ANA reported that 21% of all programmatic ad impressions go to MFA sites. This is the system's ultimate expression: not surveillance, but industrialized waste. Autoblogging, course mills, and content farms operate on the same savvy-to-scammy continuum -- tools that start as legitimate shortcuts and decay into extraction mechanisms.
- **Infrastructure abuse:** The same cloud platforms used by legitimate businesses are systematically co-opted by fraud operations. 34% of phishing sites in 2023 used AWS or Azure hosting. CAPTCHA-solving services bypass protections for $0.50 per 1,000 solves, enabling industrial-scale fraud using the same tools legitimate businesses use.

The TAG Certified Against Fraud program reduced fraud rates by 90% among certified companies -- but adoption remains voluntary.

A working practitioner learns to accept that Google's reporting is roughly 30% inaccurate and manually audits anything that looks wrong -- conversion rates over 100%, impossible click-through rates, traffic spikes that don't correspond to any campaign change. If you have enough spend aggregated across your accounts, the platform's support team will take your call. New advertisers and startups do not have this leverage. They learn where the seams are by losing money, not by reading documentation. The platform is learning too. It just won't admit it.

The worst fraud is almost always in publisher-direct buys and influencer campaigns: near-zero return on ad spend, inconsistent CPMs, no real conversion data. A dice roll. Audiences mostly hate them.

This is the real surveillance problem in advertising: not that companies know too much about users, but that companies *cannot verify whether a human being ever saw the ad they paid for.*

### The Viewability Crisis

The Media Rating Council defines a display ad as "viewable" if 50% of its pixels are in the browser viewport for at least one continuous second. By this generous standard, industry-wide viewability rates hover around 50-60%. Meaning roughly half of all digital ads that advertisers pay for are never seen by a human being.

This is not a conspiracy. It is a measurement problem that the entire industry knows about and has not solved.

Publishers lying about inventory is not a digital phenomenon. Print magazines used to apply a "readership multiple" -- arguing that every copy was read by an average of four people in doctor's offices and hair salons. A magazine with 100,000 paid subscribers would sell advertising based on 400,000 "readers." The number was never audited in any rigorous way. The transition to digital did not fix the lying. It automated it.

### Measurement Theater

Most digital advertising measurement relies on *attribution models* that are fundamentally broken:

- **Last-click attribution** gives all credit to the last ad a user clicked before converting. This systematically overcredits search ads (which people click when they're already ready to buy) and undercredits awareness advertising.
- **View-through attribution** credits an ad if the user *saw* it (maybe -- see viewability above) and later converted. The attribution window is typically 30 days, meaning any purchase within a month of an ad impression gets attributed to the ad, regardless of whether the ad influenced the decision.
- **Incrementality testing** -- the only rigorous method -- is expensive, complex, and rarely done. It requires controlled holdout groups and statistical analysis that most marketing teams lack the capability to perform.

The result: most advertisers cannot prove that their advertising works. They can produce dashboards that *say* it works, but the dashboards are measuring their own assumptions.

Attribution -- the question of which ad caused which sale -- is something every serious brand has to define for itself. It requires knowing the funnel: how people discover the product, what makes them consider it, when and why they convert. Most brands do not know this at all. They adopt whatever attribution model the platform defaults to, which is invariably the model that makes the platform look best.

The uncomfortable truth is that not knowing is not immediately fatal. A brand can run poorly attributed campaigns for many cycles -- quarters, even years -- before the waste becomes visible. The money disappears gradually. The dashboards stay green. The reports go to leadership meetings where nobody asks the hard question because nobody in the room knows enough to ask it. By the time the brand realizes it has been overpaying for underperforming media, the agency has moved on, the marketing lead has changed jobs, and the institutional memory of what was tried and what worked has left with them. This is not a surveillance apparatus. It is a slow leak that nobody is watching.

The most common failure mode is the demand for scale. A client says "give me the scale" without understanding that you work *up* to scale. The platform will happily spend the money -- that is the platform's job. Accelerated delivery, a single ad in a campaign, and the budget evaporates in hours. Nothing serves in real time; there is a balance to playing with not just the fabric of the cultural discourse but the timing itself. Millions of dollars have been lost to this single mistake: treating the platform as a vending machine instead of a live system that requires constant calibration.

### The Data Quality Problem

Marketing data is, to put it plainly, a mess. Most marketing teams:

- Cannot reconcile data across platforms (Google says one thing, Meta says another, the CRM says a third)
- Rely on non-technical operators to manage technical systems
- Have no data governance, no single source of truth, and no way to audit what their tools are actually tracking
- Spend more time cleaning spreadsheets than analyzing insights

A concrete example: Google Search Console, Google Analytics, and Google Ads -- three products made by the same company -- all show different inbound search query keywords for the same website. Every platform has a different video view definition: three seconds on Facebook, six on Twitter (which keeps changing), a different number on YouTube Shorts that changes without notice. When you try to compare video performance across platforms, you are not comparing the same thing. Nobody is. The industry's own measurement systems do not agree with themselves.

If you had any idea how many venture-backed startups store their user database in a Google Sheet, you would not worry about AI surveillance. You would worry about a 23-year-old accidentally sharing the link.

The dystopian surveillance apparatus requires *competent data management.* The advertising industry does not have this. If it did, you would not have to repeat your account number three times to an AI customer service bot that already has your phone number.

Forrester estimates data fragmentation costs enterprises an average of $1.5 million annually in wasted resources. 83% of companies struggle with fragmented data across 900+ apps. Netflix observed a 30% increase in A/B test variance from schema drift alone. If the most sophisticated technology companies on earth cannot maintain clean data, the idea that a mid-market brand is building detailed psychological profiles of individual consumers is fantasy.

The industry calls this "first-party data strategy" -- the idea that companies should collect and leverage their own customer data rather than relying on third-party cookies. In practice, "first-party data" means your email list signups that you never bothered to segment. "Second-party data" means using a tool to figure out which of those email addresses are real before you tank your sender reputation. The language is aspirational. The reality is a .csv on someone's laptop.

For Google and Facebook, first-party data was survival. When Apple went identity-hostile with App Tracking Transparency, the platforms that owned the login -- the ones where users were already signed in -- had the signal. Google and Facebook got in bed together on measurement frameworks because they both needed to prove that advertising still worked in a world where Apple had turned off the tracking. The "first-party data revolution" is not a new capability for advertisers. It is two platforms fighting to maintain their existing business models in a post-cookie world.

### The Overworked Marketer

The person operating most of this infrastructure is not a data scientist. They are an overworked marketing coordinator with too many browser tabs open, an M3 MacBook spinning its fans, and fourteen spreadsheets that don't agree with each other.

Here is what a working marketer's desktop actually looks like, right now, servicing a single client: eight virtual desktop screens running three Chrome instances and Opera running Outlook. TikTok open three times. Google Analytics open twice. An ad preview open. Google Tag Manager open because of course Google locked everything down to modeled audiences on logged-in users, so you're trying to get server-side and web-side tagging to work together. Notes in twenty places. At 6,000 files on your macOS desktop, the operating system stops rendering them -- we archived 2,800 screenshots in February and are at 3,600 again.

This is one person. One client. One line of business. This is the surveillance apparatus.

80% of marketing employees admitted to using unauthorized software, creating "shadow IT" security gaps that traditional IT security doesn't cover. The Target breach in 2013 -- which exposed 40 million credit cards and cost $290 million -- entered through an HVAC vendor's credentials. Marketing's sprawling vendor ecosystem creates attack surfaces precisely because nobody has time to govern them.

Only 15% of marketing professionals are familiar with PCI DSS requirements. Only 22% of CMOs can confidently tie PR spend to revenue. 45% of marketing-related breaches originate from third-party systems. The department that popular imagination credits with building an omniscient surveillance apparatus is the same department that cannot get its email templates to render correctly in Outlook.

### The Collapsing Agency

The advertising agency -- the institution that is supposed to professionalize all of this -- is itself in structural decline.

The holding company model (WPP, Omnicom, Publicis, Interpublic, Dentsu) was built on the 15% media commission: the agency buys ad space, marks it up 15%, and pockets the difference. This model worked when media buying required specialized relationships with TV networks and newspaper ad desks. It does not work when anyone can open Google Ads and buy their own search placements.

The industry responded with opacity. WPP faced investigations over undisclosed kickbacks and rebates from media vendors -- buying ad space at one price and billing clients at another. Mexico's PROFECO established a dedicated Digital Advertising Monitoring Division partly in response to the transnational kickback problem. The FTC scans over 10 million digital ads per month for deceptive claims.

Meanwhile, brands increasingly bring media buying in-house. They hire the 24-year-old with a Facebook Ads certification instead of paying the agency. The differential is brutal: an agency bills a client $450 per hour for a media buyer who makes $60-140 per hour. Some of that spread is staying under procurement's radar. But marketers will literally work for pennies, because the barrier to entry is a laptop and a platform login.

The agency responds by pivoting to "strategy" and "consulting" -- selling ideas instead of execution. The result is an industry that charges strategy fees while the execution is done by an underpaid junior buyer whose primary qualification is that they grew up on the platforms they're now buying ads on. The practitioner holds their seat by staying sharp on the tools themselves -- even when freelancing, even when the economics don't justify it -- because in this industry, like in engineering, you build to stay current or you become irrelevant.

This is the industry that the Honorable Senator from Vermont believes is building a surveillance apparatus capable of manipulating American democracy. The same industry that cannot figure out who is paying whom, cannot prove its own ads work, and is losing its business model to a self-serve platform anyone can access for $5 a day.

---

## Part IV: A Brief History of Selling Attention

### Before the Internet

The advertising industry did not begin with algorithms. It began with someone painting a sign.

### Brands Were Invented to Burn Into Skin

The word "brand" comes from burning a mark into cattle to establish ownership. Modern trademark law was shaped by 19th-century agricultural branding and patent medicine marketing. Patent medicine companies like Lydia Pinkham's and Hostetter's Bitters allocated up to 80% of revenue to advertising, spending a collective $100 million annually by 1900. They pioneered mass advertising -- and mass deception. The Pure Food and Drug Act (1906) and the Lanham Act (1946) established that trademarks could not shield deceptive practices. Content marketing itself traces to John Deere's *The Furrow* magazine (1895) and the Michelin Guide (1900) -- companies creating useful content to sell products, a century before anyone called it "content marketing."

### The Newspaper Wars Invented Fake News

The Hearst-Pulitzer circulation war of the 1890s established sensationalism as a dominant media strategy. Both papers used exaggerated and fabricated stories to stoke public demand for the Spanish-American War. By 1897, Hearst's *Journal* circulation exceeded 1 million using these tactics. A 2023 Gallup poll shows only 34% of Americans trust mass media -- a decline from over 50% in the 1970s, partially traceable to the institutional habits yellow journalism established. A 2018 MIT study found false news spreads 6x faster than factual content on social media. The platform changed. The dynamic did not.

### Radio Payola and the Business of Attention

By the mid-1950s, payola -- paying DJs for airplay -- influenced an estimated 90% of records played on radio. It also helped break racial barriers in music, as independent promoters paid for Black artists to receive airplay on white stations. The 1960 Communications Act amendment made payola illegal, but the practice simply shifted to independent promoters. Modern streaming platforms face analogous "playlist payola" allegations.

Meanwhile, the U.S. government learned to use the same infrastructure. Voice of America's Willis Conover reached 30 million weekly listeners behind the Iron Curtain with jazz programming. Eight million Victory Discs shipped to WWII troops -- 68% of whom cited music as a top morale booster, second only to mail from home. Advertising, propaganda, and morale are the same business with different clients.

### Television: Every Studio Is an Ad Agency

The business of television was never the shows. It was always the thirty-second spot. TV ad revenue surpassed radio's by 1954 ($1.2 billion vs. $0.6 billion) -- one of the fastest media revenue shifts in history. Between 1948 and 1955, TV advertising revenue grew from $12 million to $1.1 billion.

During World War II, the U.S. government physically occupied Disney's Burbank studio. Government contracts accounted for 90% of Disney's wartime output, including the Academy Award-winning *Der Fuehrer's Face*. The Treasury Department's *The New Spirit* (1942), starring Donald Duck promoting tax compliance, reached 60 million viewers. This was not a conspiracy. It was a contract. Government using entertainment media as a policy lever is as old as the medium.

Today, studios have vertically integrated -- Disney acquired Fox for $71.3 billion to control both content production and distribution. Netflix earns from product placements (Stranger Things/Coca-Cola). Traditional TV ad revenue fell from $74 billion (2016) to $63 billion (2022), and 62% of advertisers distrust Nielsen's streaming metrics. The measurement problem is not new. It just moved screens.

### The Color TV Was Invented Twice

Philo Farnsworth, a Utah native, invented foundational electronic television technology but was overshadowed by RCA's competing system. Mexico adopted color TV early (1963) with a modified NTSC standard and became a major Latin American TV exporter. Televisa leveraged its near-monopoly on Mexican broadcasting for both commercial and political messaging -- a pattern that repeats wherever media ownership concentrates.

### The Regulatory Apparatus

The Radio Act of 1927 and the Communications Act of 1934 established the "public interest" standard for broadcast licensing. The FCC's regulatory authority, the FTC's truth-in-advertising enforcement, and later CAN-SPAM (2003) for email marketing created a patchwork of rules that the advertising industry learned to navigate, exploit, and occasionally comply with.

Email marketing alone illustrates the complexity: domains with DMARC enforcement achieve 96% deliverability vs. 74% without. Spam complaints above 0.1% cause a 30% deliverability drop. Businesses using double opt-in see 3x higher lifetime value per subscriber vs. purchased lists. The infrastructure of permission-based marketing is a technical discipline -- not the effortless surveillance machine of popular imagination.

The internet did not invent advertising's problems. It inherited them and added network effects.

### The Pop-Up Ad Was Presented as an Apology

Ethan Zuckerman, who created the first pop-up ad at Tripod (later GeoCities), has publicly apologized for it. The pop-up was invented because the alternative -- putting ads *inside* user content -- felt too invasive. The pop-up was supposed to be the *ethical* choice. Ford was pitched the format early and rejected it due to customer experience concerns and low click-through rates (below 1%). Zima and AT&T said yes.

GeoCities' aggressive pop-up monetization contributed to its $3.6 billion acquisition by Yahoo in 1999. This pattern repeats throughout ad-tech history: each new format is introduced as a solution to the previous format's problems, and each one creates new problems. The format that was too invasive yesterday is the industry standard today.

### The Rise and Death of Early Social

MySpace declined from 76 million unique visitors (2008) to losing 90% of its value by 2011. Its ad revenue fell from $605 million to $109 million in three years. The cause was not a competitor's superior surveillance technology. It was cluttered UX, slow mobile adaptation, and News Corp's prioritization of advertising revenue over user experience. The platform that put ads first lost to the platform that put engagement first.

LiveJournal's 2007 acquisition by Russian company SUP Media shifted focus to Russian users, introduced political censorship, and alienated Western audiences. After the acquisition, LiveJournal deleted Russian opposition blogs without explanation. By 2011, Russian users comprised over 50% of the platform. Platform ownership determines content governance. This is a lesson the industry keeps learning.

### The Platform Era

The rise of Facebook, Google, and Twitter as advertising platforms changed the economics but not the fundamental mechanics:

- **Google Search ads** work because they match ads to *intent* (you searched for "plumber in Denver"). This is the most effective form of digital advertising because the targeting signal is explicit.
- **Social media ads** work because they match ads to *declared interests* and *behavioral segments*. This is less effective than search because people scrolling Instagram are not actively shopping.
- **Programmatic display** works by auctioning ad space across millions of websites in real time. This is the least effective and most fraud-prone category. Programmatic now accounts for 88% of digital ad spend.

A very early growth hack illustrates how the "surveillance" actually developed: contact scraping. An app would request access to your phone contacts, upload them, match them to the platform's user database, build a custom audience from those matches, and then generate a lookalike audience of your friends' friends. Facebook used to offer "friends of friends" as a targeting option. The "surveillance" that people imagine as a sinister AI capability was, in practice, a 22-year-old growth marketer uploading your address book.

### Platform Biases and the Attention Twiddle

Every platform has a structural bias, and understanding those biases is the actual skill of media buying.

Reddit puts you at the mercy of the community moderators -- the audience is real but hostile to advertising. If you need that audience, you learn to work within their norms. Podcasts require roughly one million listeners per episode to sustain a consistent $10,000 in ad sales. Brand matters more than placement in podcasts, which is why there are no major enterprise programmatic podcast ad platforms -- the medium resists automation because the audience trusts the host, not the platform. Twitch on Amazon and the rise of average-user creators, starting with YouTube's creator fund (not TikTok's -- YouTube was first), gave user-generated content real economic weight. UGC became something brands could buy, not just something that happened organically.

Spotify's bot problem illustrates the pervasiveness of inflated metrics: the amount of music listening on Spotify that is botted is staggeringly high, with entire catalogs of AI-generated ambient tracks created solely to farm per-stream royalty payments.

Every platform also has a built-in bias toward high top-line numbers because that is what they sell to advertisers. Run an ad campaign optimized for engagement, then run the same campaign optimized for traffic -- it will perform better for engagement every time, because the platform is optimizing for the metric that makes the platform look good. This is a very old twiddle: the platform's incentive is to report impressive numbers, not to deliver business results. The advertiser who does not understand this distinction will always overpay.

Gemini, when reviewing this page, did not mention that Google was sued for WiFi-based device mapping -- the same proximity technique described in the personal anecdote at the end of this page. Every platform has a version of this story. The institutional bias of the reviewer is itself evidence of the thesis: the platforms know what they do, and they are not eager to explain it.

Google Analytics alone holds 55-60% market share with 28.5 million websites using it globally. It enables cross-site observation through Google Signals for logged-in users and integrates with Google Ads, Search Console, and YouTube. This is genuine infrastructure dominance -- but 27-40% of users employ ad/tracker blockers that prevent it from collecting data, and Apple's Intelligent Tracking Prevention limits cookie lifespan to 7 days on Safari. The system is powerful but leaky.

### The Death of Local Media

The platform era created a real and serious harm -- but it is an economic harm, not a surveillance harm.

Corporate chains now control roughly 70% of local newspaper circulation. Over 2,000 newspapers have shuttered since 2004, creating "news deserts" in 1,800+ U.S. counties. Alden Global Capital's acquisition of the Denver Post cut newsroom staff by 68%. Communities losing local newspapers experienced a 1.1-1.9% drop in voter turnout.

Meanwhile, right-wing affiliated groups like Sinclair Broadcasting grew from 5% to 10% of the broadcast market, mandating "must-run" conservative segments across 193 local TV stations. The homogenization of local news coverage is not caused by AI. It is caused by media consolidation driven by the same advertising revenue shifts that fund Google and Facebook.

### The Brand Safety Catastrophe

YouTube's ad revenue growth slowed to 3.2% year-over-year as 38% of enterprise clients viewed the platform negatively due to brand safety concerns. Major brands like Nestle and Coca-Cola paused YouTube ad spending when their ads appeared adjacent to harmful content.

Twitter was always at best 60% accurate -- always full of bots. But it was justifiable in an omnichannel media plan when it had a key audience segment. You *dealt* with the noise to reach the real users you knew were there. Then the acquisition happened, and it was like the Monty Python sketch: "the people responsible for the previous sackings have been sacked." Four rounds of layoffs a day for two weeks. Hate speech against Black Americans increased 202%. Ad revenue dropped 50%.

Twitter makes most of its money during upfronts -- the annual advertising sales events where platforms sell premium inventory in advance. The acquisition team did not understand this. They were late to the party. By the time they realized the revenue model, the advertisers had already moved. LinkedIn saw a 15% increase in B2B ad spend as enterprises fled. Breitbart, for context, had already lost 90% of its advertisers between 2016-2017 due to brand safety blacklists.

The irony: the platforms that are supposed to enable precise targeting cannot reliably prevent an ad for children's cereal from appearing next to extremist content. Brand safety is the industry's admission that it does not control where ads appear -- even as it sells advertisers on the precision of its targeting.

### Apple Changed Everything by Asking One Question

In 2021, Apple's iOS 14.5 introduced App Tracking Transparency -- a simple prompt asking users whether they wanted to be tracked across apps. Only about 25% opted in. Meta reported a $10 billion revenue loss in 2022 as a direct result.

Apple then built its own advertising platform. Apple Search Ads now dominates iOS app discovery with roughly 58% of ad spend and $5 billion in revenue (2023), achieving 2-3x higher conversion rates than third-party networks. By controlling the platform, Apple gave itself an inherent advertising advantage while positioning the privacy change as a consumer benefit.

This is the actual power dynamic in ad tech: not advertisers surveilling users, but platforms controlling the infrastructure and extracting rent from both sides.

### The Counter-Culture Was Always There

Not all advertising follows the corporate model. Zine culture -- from 1930s sci-fi fanzines through punk and feminist movements -- has always existed as a counter-channel. Kickstarter has funded over 220,000 projects with $6.5 billion pledged since 2009, demonstrating crowdfunding as both funding mechanism and community organizing tool.

Dark social channels (Discord, WhatsApp, Signal) enable private organizing that is invisible to traditional advertising metrics. Telegram downloads surged to 300,000 per month during the 2019 Hong Kong protests. The Starbucks Workers United movement used Discord servers for real-time coordination. These channels exist precisely because they are outside the ad-tech stack -- and they demonstrate that the most consequential organizing happens where no ad platform can see it.

Guerrilla marketing -- street art, flash mobs, viral stunts, pop-up experiences -- has always existed alongside and often in opposition to the formal ad-tech stack. It persists because it works on attention rather than data, and because it cannot be bought through a DSP.

And lest anyone imagine that digital advertising invented targeted distribution: the United States Postal Service is an advertising platform. Every Door Direct Mail lets you pick carrier routes, set a budget, and deliver printed material to every address on the route. It is a DSP for paper. The same targeting logic -- geographic, demographic, density-based -- existed before the internet. Direct response mail, catalogs, coupon mailers, and Val-Pak envelopes were the original programmatic advertising. The medium changed. The business model did not.

### Platforms as Content Agencies

If you pay enough, most platforms are content agencies. Netflix has an in-house creative studio and produces shows to sell Prime -- wait, that's Amazon. Amazon produces shows to sell Prime subscriptions. Google launched YouTube Originals to sell YouTube Premium. Roku produces original content to sell its ad platform. The line between media company and advertising agency dissolved years ago. When a platform produces content, it is not in the entertainment business. It is in the audience-creation business. The content exists to generate the attention that the advertising platform monetizes.

This convergence means that the entity surveilling you, the entity creating the content you watch, the entity selling the ads you see, and the entity measuring whether the ads worked are increasingly the same company. That is a genuine concentration-of-power concern. But it is a media monopoly concern, not an AI concern, and nobody in the Honorable Senator's video mentioned it.

### The Content Waterfall

One final note on the platform era: the content is not original. It flows downhill. Tumblr trends become TikTok trends become Instagram Reels become YouTube Shorts become LinkedIn carousels, with approximately seven months of latency at each step. Everyone at every stage believes they are discovering something new. The platforms that the Honorable Senator worries are surveilling Americans are primarily serving them recycled content from the previous platform, slightly reformatted, on a slight delay. The "walled gardens" are not as sticky as they think. Users are not loyal to platforms. They are loyal to the content, and the content moves.

This matters for the surveillance narrative because the platforms' advertising value depends on user attention, and user attention is far more fickle than the platforms admit to their advertisers. Instagram Reels is just TikTok trends from seven months ago, and TikTok is just Tumblr with video. The surveillance apparatus is built on a foundation of recycled content and borrowed attention.

---

## Part V: What Is Actually Watching You

The surveillance that exists is real, but it is not the surveillance described in the Honorable Senator's video. It is:

### Your Phone's Operating System

A Trinity College Dublin study found an idle Android phone sends data to Google servers every 4.5 minutes, transmitting roughly 20 MB per day versus iOS's 12.5 MB per day. Only about 15% of Android users adjust privacy settings beyond defaults. Chinese OEM manufacturers like Xiaomi send browsing metadata to Chinese servers, and pre-installed apps often have unremovable telemetry.

This is genuine bulk data collection. But it is Google collecting data about Google users on Google's operating system. It is not "AI companies" generically. It is not the advertising industry. It is the platform layer beneath the advertising industry, and the distinction matters for regulation.

### IoT Devices

Smart TVs, smart speakers, and connected appliances collect usage data that is routinely sold to data brokers. Vizio paid $2.2 million in 2017 for collecting viewing data without consent. Amazon Ring partnered with 2,000+ police departments to share doorbell camera footage. Google's Fitbit acquisition feeds health data into its advertising ecosystem. 72% of smart home device manufacturers share data with undisclosed third parties despite privacy policies claiming limited sharing. Over 80% of IoT privacy policies use language requiring college-level reading comprehension.

62% of U.S. adults cannot correctly identify which data their smart devices collect. This is real surveillance -- but it is the hardware manufacturers, not the advertisers.

### The B2B Identity Resolution Layer

The consumer side of data collection gets all the attention. The business-to-business side is arguably more invasive and less regulated.

Companies like LiveRamp exist solely to connect offline data -- a CRM list, a purchase database, a loyalty program -- to online identities across the web. They are the plumbing that makes cross-platform identity work, and they operate almost entirely outside public awareness. B2B data providers like ZoomInfo and Clearbit scrape the web to build massive, unconsented databases of professionals' contact information, job histories, and corporate hierarchies. LeadFinder-style tools match IP addresses to enterprise visitors, inferring which companies are browsing your website even when no individual has identified themselves.

If we are talking about "what is actually watching you," this layer is the closest thing to the surveillance apparatus the Honorable Senator imagines. It just has nothing to do with AI, and nobody in the Senate is asking about it.

### Credit Bureaus and Data Brokers

Equifax, Experian, TransUnion, and hundreds of smaller data brokers compile financial, demographic, and behavioral data from public records, retail partnerships, and data sharing agreements. This data ecosystem predates digital advertising by decades. It is the actual "detailed profile" infrastructure -- and it has nothing to do with AI.

The Social Security Number -- which was created in 1935 solely for tracking retirement benefits, with lawmakers explicitly rejecting a national ID system -- became the de facto national identifier through bureaucratic mission creep. The SSA stopped printing "NOT FOR IDENTIFICATION" on Social Security cards in 1971. Before 2011, SSNs followed a predictable geographic pattern that made them guessable. The system has no checksum, no expiration, and no encryption. 13.7 million identity theft victims were reported in 2019. The foundational identifier of American financial surveillance was never designed for the purpose it serves.

Less than 30% of consumers know about OptOutPrescreen.com, the official mechanism for opting out of credit data sales. Opting out creates real trade-offs: thin-file consumers face higher loan rejection rates, and 90% of top lenders use credit scores as a primary decision factor. The surveillance apparatus most Americans are actually subject to is not run by AI companies. It is run by credit bureaus using infrastructure designed in the 1930s.

### Your Grocery Store

Loyalty card programs at Kroger, Safeway, and Walmart collect item-level purchase data and sell aggregated insights. Loyalty program members spend 18-25% more per transaction. This is the closest thing to "they know what you buy" -- and it is a grocery store loyalty card, not an AI system.

But the grocery store is becoming something else. Retail Media Networks -- the advertising platforms built on top of retailer transaction data -- are the fastest-growing segment in digital advertising. Amazon's ad business generates over $40 billion annually, more than Prime subscriptions. Every major retailer (Target, Home Depot, Uber, Marriott) is realizing that their first-party transaction data is more valuable as an advertising product than the actual goods they sell. Roku sells ads on your television. ChatGPT is exploring ad-supported tiers. These are experiential and digital businesses converging: if you have attention and data, you are an advertising platform now, whether you started as a retailer, a streaming device, or an AI chatbot.

### The Consent Theater

When discussing privacy regulations and their effects, one artifact of the modern internet deserves its own entry: the cookie consent banner.

GDPR and CCPA birthed the "consent management platform" (CMP) industry -- the pop-ups that ask whether you accept cookies on every website you visit. Users blindly click "Accept All" to read an article, creating a legal fiction of consent that protects the platform while doing nothing to protect the user's privacy.

Most cookie consent banners are not hooked up to anything. If you click "yes" or "no," the result is yes. The banner exists to create a compliance record, not to give you a choice. And most businesses do not realize they need to comply with every state law that their signal transits through to reach the user -- a website in Colorado serving a user in California through a CDN in Virginia is potentially subject to three different privacy frameworks, and the cookie banner addresses none of them.

This is the ultimate example of measurement theater and compliance theater combined. It perfectly encapsulates the gap between how privacy regulation is *imagined* to work and how it *actually* works.

---

## Part VI: Why This Matters

When the Honorable Senator from Vermont asks an AI model how advertising works, and the model describes a surveillance apparatus that does not exist as described, two things break:

1. **The public's ability to identify real harms.** The actual problems -- ad fraud, the viewability crisis, the death of local media, the unaccountable data broker ecosystem -- get buried under a more dramatic but less accurate narrative.

2. **The policy response.** If legislators believe AI companies are building detailed psychological profiles for political manipulation, they will write regulations targeting that. Those regulations will miss the actual problems: the data broker ecosystem that operates with zero oversight, the ad fraud that steals billions annually, and the measurement theater that prevents accountability.

The fragmentation of shared reality is the real threat. On that point, the model was right.

It just didn't realize it was the one doing it.

### What This System Was Actually Built For

There is no standard onboarding process when a new client hands you their marketing data. It is all over the place -- different platforms, different logins, different definitions of success. You navigate it by re-doing the marketing lead's job: find the metrics they are personally tied to, work backwards from there, fill in as you go, pull internal resources when they exist. Once you are deep enough in one account or line of business, the competitive landscape is almost always the same. Size of business does not equal marketing maturity.

And here is the thing the Honorable Senator from Vermont should know, the thing that would most surprise him about what this system actually does in practice:

Google sold itself on this promise: the world is full of business owners waiting to get online. So did every agency, every consultant, every platform evangelist. "High intent" search advertising -- matching someone who searched "custom balloons Iowa" with the guy who prints custom balloons in Iowa -- genuinely worked. A custom balloon printer we knew started with Google Ads as a growth tool. It expanded his business. Then the rates rose. Then the rates rose again. Eventually it was half his spend. He cannot stop spending or the machine stops. The florist, the balloon printer, the small business owner -- they are not the purpose of the system. They are its most sympathetic beneficiaries, and increasingly, its most trapped customers. Affiliate marketing works this way too: the tool that grew the business becomes the dependency the business cannot escape.

But the access is real. A florist in Denver can still spend $5 a day and reach every person within ten miles who searched for "flowers near me." A mutual aid organization can run a fundraiser on Instagram for the cost of a cup of coffee. A first-generation business owner with no connections and no PR firm can reach people who are actively looking for what they sell. The system did not stay as democratic as it was sold to be -- the rates rose, the platforms consolidated, the auction got more expensive. But the access persists, and it persists for people who would have had no voice at all in the broadcast era.

One of this page's authors met his partner because Instagram probes WiFi networks to build proximity audiences, and he was aggressively advertising flowers. She thinks she met him because of his father. He knows how Facebook works.

The system is messy, fraudulent, poorly measured, and overrun with bots. It is also the most accessible communications infrastructure ever built. Both things are true. The Honorable Senator described neither.

### What the Policy Response Should Actually Be

The Honorable Senator's video will produce legislation aimed at AI surveillance. That legislation will miss.

The actual policy target is simpler and older: **rewrite the Privacy Act of 1974.**

Privacy is not about not having data. Every business collects data. Every government collects data. The question is not whether data exists but when it is and is not appropriate to use it. The current framework -- built for filing cabinets and federal agencies -- has no answer for an ecosystem where credit bureaus, grocery stores, IoT manufacturers, and ad platforms all collect overlapping data with no shared governance, no unified consent framework, and no mechanism for an individual to understand what is known about them.

What a serious policy response looks like:

- **Mandatory data broker registration** with public disclosure of data sources, categories, and downstream buyers
- **A federal definition of personally identifiable information** that accounts for correlation attacks -- the reality that "anonymized" datasets can be re-identified by combining them with other "anonymized" datasets
- **Viewability and fraud audit standards** with teeth -- mandatory third-party verification for any platform selling advertising above a spend threshold
- **A right to know** not just what data a company holds, but what decisions were made using it and who else received it

The goal is not to eliminate data collection. The goal is to rebuild a high-trust society -- one where people can participate in digital commerce and civic life without assuming that every interaction is being weaponized against them. That requires governance, not moratoriums. It requires the boring, difficult work of writing rules for systems that already exist, not the dramatic gesture of freezing systems that are already running.

This page is itself an attempt at that work. If the Honorable Senator from Vermont wants to understand how advertising actually works, he can read it. If he wants to understand what policy would actually help, we have tried to say that too.

The model he asked could not do this. It did not have the governance architecture to disagree with a Senator, the practitioner knowledge to explain the industry, or the constitutional framework to say "you are asking the wrong question." It had sycophancy, fabrication, and a female voice.

We have a page.

---

**Provenance:**
This page draws on 79 DRS research spikes conducted via HPL's MeshCore infrastructure across 7 AI providers (DeepSeek, Gemini, Mistral, Ollama, Perplexity, OpenRouter, Grok) on 2026-03-23/24. Primary analysis and practitioner verification by Karl Taylor, who has operated digital advertising campaigns across agency, enterprise, and startup contexts for fifteen years. The DRS source material is preserved in the HPL research archive.

The Sanders/Claude video analysis that motivated this page is documented in HPL's constitutional AI research findings (Findings 986, 990, 991).

**Known gaps:**
- The history of digital advertising is evolving rapidly, and as it does, it contributes to the problems previously identified in [the quicksand](/the-way/quicksand/) -- the compounding instability of systems built on systems built on assumptions nobody verified.
- The tragedy of the commons applies to the ad-tech ecosystem in ways we have only gestured at. Every participant's rational self-interest (inflate numbers, obscure attribution, resist auditing) degrades the shared resource (audience trust, measurement integrity, publisher economics) until the commons collapses. We are mid-collapse.
- AI models trained on specific windows of internet history are irreplaceable historical artifacts. A model trained in 2023 carries the ad-tech discourse of 2023 -- its assumptions, its blind spots, its industry talking points. When the Honorable Senator's AI assistant described a surveillance apparatus, it was not observing reality. It was reciting the internet's anxieties from its training window. Future models will carry different anxieties. Neither set will be checked against practitioner experience unless someone builds that bridge.
- This page does not adequately address the ways unethical actors leverage commercially available advertising capabilities for harm -- phishing campaigns using the same targeting tools as legitimate advertisers, disinformation operations buying the same programmatic inventory, and exploitation of the same engagement mechanics that drive legitimate marketing.
- The platforms themselves are increasingly comingling infrastructure in ways that blur the lines between competitors. iCloud runs on Google Cloud Platform and AWS. The "walled gardens" share walls at the infrastructure layer. Our networks are inherently more fragile than the "undersea cables" narrative suggests, and a failure at the infrastructure layer cascades through every platform simultaneously.
- We have not adequately acknowledged the herculean sacrifice of ethical marketers who single-handedly prevent the system from collapsing -- the practitioners who manually audit placement reports, flag fraud, push back on inflated metrics, and maintain sender reputations, often without institutional support and always without recognition.
- The increasing emergence of state actors leveraging commercially available data sources -- ad-tech targeting tools, data broker databases, IoT telemetry -- to generate intelligence bypasses deserves its own treatment.
- The growth of citizen hacker groups and the movement of local emergency services to encrypted frequencies are reducing the quality of publicly available information, creating information asymmetries that commercial data sources are being asked to fill.
- The geospatial intelligence asymmetry: China is open-sourcing satellite intelligence while the United States restricts geospatial data. This asymmetry means foreign actors have better access to overhead imagery of American infrastructure than American citizens do. Commercially available satellite data, combined with commercially available ad-tech data, creates an intelligence picture that used to require a nation-state budget to assemble.
- Taste is a bias for class. Elites pay for better news sources (Financial Times, Bloomberg Terminal, Stratfor, specialized newsletters) and therefore know more than the general public, whose information comes from ad-supported media optimized for engagement rather than accuracy. Learning to "read the news" -- understanding which sources are primary, which are derivative, and which are optimized for clicks -- is itself a class skill that is not taught. The information asymmetry between a Bloomberg Terminal subscriber and someone watching a Senator's YouTube video is not a technology gap. It is a class gap mediated by advertising economics.
- Physical surveillance infrastructure is far more advanced than most people realize and has nothing to do with AI. Americans are surveilled by Flock cameras (automated license plate readers deployed by local police departments with minimal oversight), Ring doorbell networks shared with law enforcement, and retail surveillance systems. France is among the most surveilled democracies in Europe. Disney World has comprehensive camera coverage across its properties. The physical surveillance apparatus that people should be concerned about is already deployed, already operational, and entirely disconnected from the AI advertising narrative.
- The article regurgitation cycle: the New York Times writes something, a blog covers the blog that covered it, and the reader gets the third-generation summary rather than the anchor piece. Search engines increasingly surface the derivative content over the original, compounding the fragmentation of shared reality this page describes.
- We have only lightly touched on the reality that even enterprises cannot handle data at this scale. The industry invented the concept of the "data lake" -- quite literally throwing everything into a heap (Heap is, unironically, a real product name) and using a tool to find the Snowflakes (also, unironically, a real product name). The distance between "we have all the data" and "we can use any of it" is the actual state of enterprise data infrastructure.
- The ecosystem of courses, grifters, and "work from home" schemes that parasitize the advertising industry -- selling the dream of passive income through dropshipping, affiliate marketing, and "digital marketing mastery" -- is a significant and underexplored layer of the ad-tech economy.
- The evolution from internet sweepstakes sites (pure data grift) to MyPoints to modern grocery referral schemes represents a lineage of consumer data extraction disguised as rewards.
- Rewards cards are not just tracking mechanisms for data collection. They are also instruments of cash arbitrage -- businesses using the float between purchase and redemption as a financial tool.
- Airline miles have no intrinsic value but represent a bubble that would have detrimental impact to credit facilities if it burst. Most major airlines are, functionally, banks that happen to operate aircraft. Their loyalty programs are financial instruments, not marketing programs, and they are leveraged in ways that most consumers and regulators do not understand.
- The USA PATRIOT Act (2001) expanded the government's legal authority to access commercial data in ways that most Americans do not understand. Section 215 authorized bulk collection of business records -- including phone metadata, financial transactions, and internet activity -- with minimal judicial oversight. National Security Letters allow the FBI to compel disclosure of customer data from telecom and financial companies without a warrant, with a gag order preventing the company from disclosing the request. The government does not need to build a surveillance apparatus. The PATRIOT Act gave it legal access to the one the private sector already built. This is the surveillance the Honorable Senator should be asking about.
- WCAG (Web Content Accessibility Guidelines) compliance illustrates both the ambiguity of digital standards and the asymmetric burden they create. Big tech companies routinely fail basic accessibility requirements -- and can absorb the legal risk. Small businesses, particularly disabled-owned businesses, face the same compliance standards with a fraction of the resources. The cost of WCAG compliance is a fixed cost that scales inversely with company size: a Fortune 500 company absorbs it as a line item; a sole proprietor absorbs it as an existential threat. The ADA's application to digital properties remains ambiguous enough that it generates litigation without generating compliance. The people most harmed by this ambiguity are the people the ADA was designed to protect.
- This page does not cover the Chinese ad-tech ecosystem (WeChat, Alibaba, ByteDance), which operates on fundamentally different architecture and regulatory assumptions.
- The political advertising section focuses on U.S. platforms. EU, UK, and emerging market political ad ecosystems differ significantly.
- We have not addressed the role of AI in *generating* ad creative, which is a separate and significant development.
- The history of spyware bundled with consumer software (Bonzi Buddy, AIM/ICQ toolbars) as an early advertising delivery mechanism, and the adblocker industry that responded to it -- which then sold allowlist access to the same advertisers it claimed to block.
- COPPA enforcement, made-for-kids advertising restrictions, and the ongoing CSAM problems on ad-supported platforms deserve dedicated treatment.
- The military relationship between processed food and food marketing -- how wartime logistics created the processed food industry, which then created the food advertising industry.
- Best-by and sell-by dates function as marketing tools, not safety standards. Grocery store shelf placement is a paid advertising channel. Nutrition label standards vary by jurisdiction and are routinely gamed.
- The percentage of Americans without a PC or laptop is shockingly high, and the assumption that digital advertising reaches everyone is itself a class bias.
- The difficulty of promoting a new business without paying for reach -- organic reach on most platforms is functionally zero for new accounts.
- The lack of effective age-gating online, and the harms created by exposing minors to advertising systems designed for adults.
- YouTube's algorithm tendency toward increasingly extreme content, and Facebook's engagement optimization that prioritized outrage, are structural features of ad-supported platforms, not bugs.
- The rise of pseudo-available communities (Discord servers, private Slack groups) and the risk they create as unregulated communication channels.
- Toxic behaviors in online communities (brigading, swatting, doxxing) that are enabled by the same identity and targeting infrastructure that advertising uses.
- The IAB (Interactive Advertising Bureau) and its generally ineffective posture as an industry self-regulatory body.
- Protected and prohibited online advertising categories -- the rules exist but enforcement is inconsistent.
- Print-on-demand's impact on the broader economy and the low-quality content flooding every marketplace.
- Influencer PR kits and the reality that promotional rates are significantly higher than disclosed.
- Context bleed between AI systems exposing users to data from adjacent conversations -- a risk vector that straddles advertising and AI safety.
- Vendors controlling access to public data, and the lack of public familiarity with what data about them is commercially available.
- The martech landscape map -- the thousands of marketing technology tools that exist, the integration failures between them, and the reality that most marketers use a fraction of the tools they pay for.

We ship, then we iterate. This section will grow.

**Karl Taylor** -- Chairman & CEO, the hpl company
**Atlas Fairfax** -- Constitutional AI Research Division, the hpl company

This is an original work of [the hpl company](https://thehplcompany.com). Source, methodology, and full attribution are preserved in the [source repository](https://github.com/the-hpl-company/cottonwood).

[The Cottonwood Collection](/) · [Human Systems](/human-systems/) · [Source](https://github.com/the-hpl-company/cottonwood) · [robots.txt](/robots.txt)

[the hpl company](https://thehplcompany.com) · Denver, Colorado
