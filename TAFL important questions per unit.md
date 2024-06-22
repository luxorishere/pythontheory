# Tafl Important questions 

## Unit 1

1. DFA string ending with particular condition done
2. Binary Number divisible by x done
3. |w| = x(mod y)  or |w| = x > or < (mod y) not done
4. DFA follow more than one condition for any string not done
5. Construct NFA done
6. Epsillion Transition done
7. DFA vs NFA done
8. NFA -> DFA -> MDFA (IMP) not done
9. Moore machine not done
10. Melay machine not done
11. Melay to Moore not done
12. Moore to Melay not done

## Unit 3

1. Designing of Context Free Grammar
2. Regular Grammar
3. Derivation (LMD and RMD)
4. Ambiguity in CFG 
5. Inherent Ambiguity in CFG 
6. Simplifications of CFG
7. CFG to GNF and CFG to CNF
8. Pumping lemma for CFG 
9. Closure property of CFL
10. Two stacks PDA 
11. Dicision Property of CFL
12. Chomsky Classifications


Creating a Context-Free Grammar (CFG) can indeed be confusing at first, but by following some basic steps and tips, you can make the process more manageable. Here are the steps and tips for creating a CFG:

### Steps for Creating a CFG:

1. **Understand the Language**:
   - Clearly define the language you want to generate. Write down some example strings that belong to the language and some that do not.

2. **Identify Patterns**:
   - Look for patterns or regular structures in the strings of the language. Identify repeated sequences, nested structures, or specific orders of symbols.

3. **Define Non-Terminals**:
   - Determine the necessary non-terminal symbols. Typically, start with a start symbol \( S \). Add additional non-terminals if needed to handle different parts or structures of the language.

4. **Write Production Rules**:
   - Write rules that generate the patterns identified. Ensure each rule correctly produces a part of the string and that the combined rules cover all strings in the language.
   - Include a base case (usually involving the empty string \(\epsilon\)) to terminate the derivation.

5. **Test the Grammar**:
   - Derive example strings using the CFG to ensure it generates all valid strings and only valid strings.

### Tips for Creating a CFG:

1. **Start Simple**:
   - Begin with the simplest form of the string and gradually add complexity. For instance, start with the base case where \(n = 0\) (the empty string).

2. **Use Recursive Definitions**:
   - Use recursion to handle repeated or nested structures. For example, use \( S \rightarrow aSb \) to generate sequences of "a...b".

3. **Break Down the Problem**:
   - If the language has multiple parts (e.g., different sections of symbols), break it down into smaller sub-problems and handle each with different non-terminals.

4. **Ensure Termination**:
   - Make sure every recursive rule has a base case to prevent infinite recursion.

5. **Think in Terms of Production Steps**:
   - Visualize how each step of the production will add to the string. Write intermediate steps to see the progression.

### Example Walkthrough:

Let's walk through creating a CFG for the language \((ab)^n\) where \(n \geq 0\):

1. **Understand the Language**:
   - The language consists of the string "ab" repeated \(n\) times, such as "", "ab", "abab", "ababab", etc.

2. **Identify Patterns**:
   - The pattern is a repetition of "ab". Each "ab" pair is an atomic unit in the string.

3. **Define Non-Terminals**:
   - We'll start with \( S \) as the start symbol.

4. **Write Production Rules**:
   - Base case: The empty string.
     - \( S \rightarrow \epsilon \)
   - Recursive case: Each "ab" pair followed by the rest of the string.
     - \( S \rightarrow abS \)

5. **Test the Grammar**:
   - Derive example strings to ensure correctness.

### Final CFG for \((ab)^n\):

1. \( S \rightarrow abS \mid \epsilon \)

#### Testing:

- **Empty string** (\( n = 0 \)):
  - \( S \rightarrow \epsilon \)
  - Result: ""

- **"ab"** (\( n = 1 \)):
  - \( S \rightarrow abS \rightarrow ab\epsilon \)
  - Result: "ab"

- **"abab"** (\( n = 2 \)):
  - \( S \rightarrow abS \rightarrow ababS \rightarrow abab\epsilon \)
  - Result: "abab"

- **"ababab"** (\( n = 3 \)):
  - \( S \rightarrow abS \rightarrow ababS \rightarrow abababS \rightarrow ababab\epsilon \)
  - Result: "ababab"

By following these steps and tips, you should be able to create CFGs more systematically and correctly. Remember that practice helps, so try creating CFGs for different languages to get more comfortable with the process.