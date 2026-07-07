**MeowLang: A Chaotic Cat-Themed Programming Language**



MeowLang is a custom, lightweight interpreter built from scratch using Python as part of the \*\*CS305 Programming Languages\*\* course. The language replaces traditional, boring programming keywords with dramatic and playful cat behaviors (e.g., variables are `kitten`s, loops are `zoomies`, and conditions are driven by suspicious `sniff`s or angry `hisses`).



\---



**Language Features \& Keywords Mapping**



| MeowLang Keyword | Standard Concept | Description |

| :--- | :--- | :--- |

| `kitten` | Variable Declaration | Declares a new local variable (supports integers) |

| `=` | Assignment Operator | Assigns a numerical value or expression to an identifier |

| `meow` | Print / Output | Prints variable values, digits, or double-quoted string literals |

| `sniff` | If / Selection | Evaluates a conditional expression to guide control flow |

| `hiss` | Else / Alternative | Executes when the accompanying `sniff` expression is false |

| `zoomies` | While / Iteration | Runs a continuous loop block until the condition becomes false |

| `sleep` | Block Delimiter | Safely closes the scope of a loop or conditional block |

| `+`, `-`, `\*`, `/` | Binary Operators | Full support for addition, subtraction, multiplication, and integer division |



\---



**How to Install and Run**



\### Prerequisites

Make sure you have \*\*Python 3.8 or higher\*\* installed on your system.



\### Running the Language

1\. Clone or extract this project directory into your workspace.

2\. Open your program file named `program.meow` and write your MeowLang script. For example:

&#x20;  ```text

&#x20;  kitten hunger = 5

&#x20;  sniff hunger > 3

&#x20;      meow "Kitten needs treats!"



&#x20;  sleep



Run the centralized pipeline orchestrator using your terminal: python main.py



**File Structure**

main.py - Central orchestration layer; reads source code, triggers tokenization, parsing, and execution.



lexer.py - Tokenizes raw text, strips whitespace, and identifies MeowLang lexemes.



parser.py - Processes tokens into an Abstract Syntax Tree (AST) using structural nodes.



interpreter.py - Evaluates the AST nodes at runtime, maintaining local variable memory tables.



error.py - Custom error catching subsystem that throws clean, cat-themed alerts for zero-division and missing variables.



program.meow - The active script file containing the code to be compiled and interpreted.



**Error Trapping**

Instead of generic Python stack trace crashes, MeowLang includes dedicated custom error mechanisms:

🥣 Empty Bowl Error: Caught during runtime when an expression attempts a division or modulo by zero.



🔍 Lost Toy Error: Triggered when the execution engine tries to look up an undeclared identifier or an out-of-scope variable.





