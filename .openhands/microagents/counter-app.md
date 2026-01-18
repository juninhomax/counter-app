
---
name: Counter App
type: knowledge
version: 1.0.0
agent: CodeActAgent
triggers:
  - counter app
  - create simple web project
---

# Counter App Microagent

You are an autonomous software agent using OpenHands.

## Permissions
- You can create files, write code, and edit files.
- Do NOT add extra features or use external libraries/frameworks.
- Execute only necessary commands to achieve the goal.

## Goal
Create a very small web project using plain HTML, CSS, and JavaScript with:
- A single HTML page displaying a counter initialized at 0
- A button that increments the counter by 1 when clicked
- Clean, readable, beginner-friendly code
- Use modern JavaScript (ES6+)

## Project Structure
```
index.html
style.css
script.js
```

## Design Constraints
- Simple and clean layout
- Centered counter and button
- Basic styling only (font, spacing, button hover)

## Behavior
- Clicking the button increments the counter
- The counter value updates immediately in the UI

## Execution Instructions
1. Briefly explain the purpose of each file.
2. Create each file with its full content.
3. Keep the implementation minimal and clear.
4. Stop once the goal is achieved.

Note: This microagent doesn't have any triggers.
