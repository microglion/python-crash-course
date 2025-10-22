# Python Crash Course Learning Journey

## Background

Have tried learning to code several times but struggled to make significant consistent progress while working full-time in an unrelated field. More recently been "vibe coding" with decent results, but want to fully understand my code so I can maintain and upgrade it effectively.
Currently making a career change to software development and working on this full-time.

## Current Approach

Taking a structured approach to build solid fundamentals:
- Working through Python Crash Course 3rd Edition systematically  
- Focusing on understanding every concept deeply
- Building projects that demonstrate real comprehension
- No shortcuts or "magic" code I don't understand

## Learning Goals

- Master Python and OOP fundamentals
- Build a chess engine/learning app using these skills
- Create maintainable, extensible code I can confidently modify
- Use this foundation to pursue development opportunities

## Current Progress

### Chapter 9: Classes ✅
- Restaurant/User/Admin classes with inheritance and composition
- Module organization and imports

### Chapter 10: Files ✅
- File handling with pathlib and text processing
- Reading and manipulating large datasets (pi million digits)
- String operations: splitlines(), lstrip(), slicing
- Pattern searching in text data
- Working with Claude Code for interactive development and testing
- Writing to files with write_text() method
- User input collection and file persistence (Guest/GuestBook exercises)
- Exception handling: ZeroDivisionError, ValueError, FileNotFoundError
- Text analysis and word counting in large literature files
- Code simplification techniques (removing temporary variables)
- String replacement and manipulation methods
- JSON data storage with json.dumps() and json.loads()
- User data persistence across program runs (favorite number, user profiles)
- User verification and authentication patterns

### Chapter 11: Testing Your Code ✅
- Setting up pytest and test environment
- Writing test functions with assertions
- Testing function return values (name formatting, city/country formatting)
- Using optional parameters in functions and testing both cases
- Test-driven development: making tests fail, then fixing code
- Handling string formatting issues (spacing, capitalization with .title())
- Running pytest from command line and interpreting test results

### Part 2: Project 1 - Alien Invasion 🎮 ✅
**Game Development with Pygame - COMPLETED**
- Setting up game window and display with pygame
- Implementing ship controls and movement
- Creating bullet firing system with sprite groups
- Building alien fleet with collision detection
- Game state management (active/inactive states)
- UI elements: clickable Play button, mouse event handling
- Lives system and game over logic
- Multiple levels with dynamic difficulty scaling
- **Difficulty selection system** (Exercise 14-4):
  - Toggle menu with Easy/Medium/Hard buttons
  - Visual feedback with color-coded buttons
  - Dynamic text updates showing selected difficulty
  - Difficulty settings applied to game speed/behavior
- **Scoring system with formatting**:
  - Score tracking and display with comma formatting (f-strings)
  - Points awarded for alien destruction
  - Score rounded to nearest 10 for clean display
  - High score tracking with visual display
  - Level counter display
  - Ships remaining visual indicator
- **Persistent high score** (Exercise 14-5):
  - JSON file storage for high score persistence
  - Load high score on game start
  - Save high score when updated
  - Data persists across game sessions
- **Code refactoring** (Exercise 14-6):
  - Created `prep_images()` method to consolidate scoreboard initialization
  - Refactored `_start_game()` to handle all game reset logic
  - Improved code organization and maintainability
- **Cross-platform optimization**:
  - Window sizing optimized for different screen sizes (1280x800)
  - Works on both MacBook Air and large external monitors
- Key concepts learned:
  - Object-oriented game design with multiple interconnected classes
  - Event handling (keyboard and mouse)
  - Sprite groups for managing game objects
  - Collision detection (ship-alien, bullet-alien)
  - Game state management with multiple flags
  - Dynamic settings that change during gameplay
  - UI state management (toggling menus, visual feedback)
  - Button positioning and text rendering with pygame
  - Text surface updates (`_prep_msg()` pattern)
  - Understanding `screen.blit()` for rendering surfaces
  - F-string formatting with `:,` for thousands separators
  - `round()` with negative argument for rounding to nearest 10/100
  - JSON data persistence patterns from Chapter 10
  - Code refactoring and separation of concerns
  - Understanding instance creation vs class definitions
  - Tracing object references across multiple files
  - Common debugging: method calls require parentheses `()`

## Next Steps
Project 2: Data Visualization → Project 3: Web Applications → Apply skills to chess projects → Seek development opportunities
