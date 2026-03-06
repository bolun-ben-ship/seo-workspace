# Post 1
"Your thinking process is flawed" - that's the message I got when working with AI.

This is a follow up post, read that for context > https://lnkd.in/gCx8_cPt

AI can give me 90% of what I want, but it's the 10% that kills me.

I spent 3 prompts and 30 mins on the 90%
And 17 prompts and 6 hours on the 10% 😂 

Absolutely ridiculous
But not unexpected

2 things stood out to me when managing AI:
- I need to think like a project manager
- I need to speak in the domain vocabulary

So to get to the print version (P3), I learned that I had to reverse engineer the entire design process and the language necessary to prompt accurately.

I'll spare you the sweat and frustration and tell you exactly how I did it:

STEP 1: Architecture
- Define the canvas (dimensions, resolution, DPI)
- Define the borders of the design
- Define the margins of those borders
- Background substrate colors, texture

STEP 2: Structure
- Define the layout of the zones (layers in photoshop terms)
- Size, dimensions, framing
- Aesthetics of the frames
- Any fringe cases, overflow rules, internal adjustment rules

STEP 3: Content
- Define what needs to go where
- Do any cases require hardcoding
- Text styles, fonts, colors, overflows, ellipses, shrinking

STEP 4: Artwork
- Prompt of the artwork design
- Dimensions and scaling, hard and invisible borders

STEP 5:
- Global rules
- Fringe and edge cases

Also it'd be really helpful if your rendering template is a JSON

# Post 2

In 2023 when I just started learning about AI, Nick Saraev is the first YouTuber that I religiously followed. Learning about AI automation, building agentic AI systems and process thinking helped both professionally and personally.

This post unlocked something for me - this is the day-to-day quality of life upgrades AI gives us.

And creativity in how we use AI goes further than the tools themselves.

We now live in a time where tasks that once required experts, certifications, or years of training… can be executed with structured thinking and the right systems.

The leverage isn’t in AI.

It’s in how clearly we think about the process.

# Post 3

POV: you got promoted to senior manager today

Plot twist: you’re managing a team of AI

The task: 
Create a set of Magic: The Gathering (MTG) style spell cards for a homebrew-ed Dungeons & Dragons character with the help of AI.

The challenge: you’re NOT a designer
- NO domain vocabulary
- NO design expertise
- NO design thinking training.

Here’re the 3 biggest problems I faced:

🪤The account manager trap
I got it to replicate what's closest to my output (referencing MTG card layouts and styles). Create a guide and get it to make adjustments based on what I think I want.

I treated it as an expert and trusted its output. Not recommended. Always second guess what it produced, a human is always needed to decide what’s necessary. It’s also for your own sanity.

🪤The design iteration trap
Every trial for every iteration, the AI 90%-ed the task within 3mins and I would probably get one ‘f*ck yeah’ output in every 4 trials.

But I’m spending 90% of my time telling it to make small adjustments to not-so-gamebreaking mistakes. 

Think slightly squashed dimensions, minor twisted geometry and hallucinated colors. They were so small that I’d just about miss it.

🪤The slow feedback loop trap
I spent 5 hours regenerating the JSON design rendering template for 17 times before realising that the prompt context window is getting way too bloated.

Here’s what I learned and what got reinforced:

❌Never treat a general AI model (such as GPT5.2) like an expert - train it to get a domain specific AI model, or do step 2. Else you’ll get randomly hallucinated rules that give you even more variability on your output. 

❌Always start with structure - a general purpose AI model is really bad at doing everything all at once. Think through the task as a project director, and split it into sequential sub tasks.

❌Iterate fast - AI is really good at making things look similar to what you want. If you really scrutinise it, you’ll find lots of deviations. Keep a sharp mind and a keen eye, catch them early and account for them in your model.

Separately - If you happen to get an output you like, ask the AI to reverse engineer THE THINGS YOU LIKE. Then incorporate it into your current model.

If you want to scrutinize my thinking process, I’m writing a process documentation in a separate post and more about the subtle differences between these 2 versions. The one on the right is the ideal output.