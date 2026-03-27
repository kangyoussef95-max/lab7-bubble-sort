# Project Report: AI-Assisted Development

## 1. Initial Approach
* **Understanding:** Briefly describe your strategy for tackling the requirements.
* **Assumptions:** What did you assume about the project before starting?

## 2. Prompting & AI Interaction
* **Successes:** What types of prompts or context worked best for you?
* **Failures:** Describe specific instances where CoPilot failed (hallucinations, over-engineering, or logical errors).
* **Analysis:** Why do you think these failures happened, and how did they impact your progress?

## 3. Key Learnings
* **Technical Skills:** What CS concepts or tools did you discover or master during this project?
* **AI Workflow:** How will you change your use of AI tools in your next project?


## 1. Initial Approach
* **Understanding:** The goal was clear from the start — implement bubble sort and
build two visualizations around it, one in the terminal and one with Pygame. I
decided to tackle it in layers: get the algorithm working first, then layer the
terminal visualization on top, then move to Pygame. That way each step had
something concrete to test before moving on.

* **Assumptions:** I assumed bubble sort would be trivial to implement and that
the visualization would be the hard part. I also assumed CoPilot would basically
write everything if asked nicely, which turned out to be both true and a problem.

## 2. Prompting & AI Interaction
* **Successes:** Asking for stubs and TODOs rather than full implementations
worked really well. It forced me to actually think through the logic instead of
just reading code I didn't write. Giving CoPilot context about what I already had
before asking for something new also made a big difference — it stopped
suggesting things that clashed with the existing structure. The code review
prompts were genuinely useful too, it caught a few edge cases I'd missed.

* **Failures:** When I asked CoPilot to "clean up the code," it went way further
than expected — it restructured the entire project, added command-line arguments
I didn't ask for, and renamed functions in ways that broke the tests. Another
time I asked it to implement the Pygame visualization and the first version closed
the window the moment sorting finished, with no way to pause or inspect the
result. It also occasionally suggested using libraries that weren't installed and
didn't flag that they needed to be.

* **Analysis:** The cleanup failure happened because the prompt was too vague —
"clean up" meant something much more drastic to CoPilot than it did to me. The
Pygame issue was more of a missing requirements problem; I didn't specify what the
user experience should feel like, just that it should visualize the sort. CoPilot
filled in the blanks with whatever seemed complete, not necessarily what was
useful. These issues didn't block progress but they did cost time reviewing and
rolling back changes.

## 3. Key Learnings
* **Technical Skills:** I got a much clearer understanding of how bubble sort
actually behaves at each step, especially once I had to think about what
"visualizing a swap" means in practice versus visualizing a full pass. On the
tools side, I learned the basics of Pygame — the event loop, drawing rectangles,
handling keyboard input — and got more comfortable with pytest for writing
structured tests. The refactoring phase also made the idea of separation of
concerns feel concrete rather than abstract.

* **AI Workflow:** I'll be more specific with prompts going forward, especially
for anything that touches existing code. Asking for stubs instead of full
implementations is something I'll keep doing — it's a better way to actually
learn rather than just review. I'll also commit more frequently before letting
CoPilot make large changes, so there's always a clean rollback point if things go
sideways.