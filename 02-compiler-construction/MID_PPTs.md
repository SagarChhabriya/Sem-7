# Compiler Construction


# Introduction

## 1. What are Compilers

A translator or a language processor: Compiler, Interpreter, Assembler


## 2. Language Processing System
Source Program -> Preprocessor: Modified Source Program -> Complier: Target Assembly program -> Assembler: relocatable machine code -> Linker/Loader -> Target Machine Code


![lang-processor](assets/1.01-language-processor.png)


## 3. Preprocessor
- A program that processes the source code before it is compiled by the compiler. 

- #define: This statement is used to define a macro, which is essentially a symbolic name for a value or a piece of code. For example:
#define PI 3.1415

- #include: This statement is used to include a header file in the source code. For example:
#include <stdio.h>

- The preprocessor permits conditionally compiling portions of code based on certain conditions using directives like #ifdef, #ifndef, #if, #else, and #endif.

```py
#ifdef ENABLE_LOGGING 
System.out.println("Logging is enabled"); 
#endif
```

- To enable or disable the preprocessing, set the preprocess.enabled property in your Maven project configuration.

```xml
<properties>
               <preprocess.enabled>true</preprocess.enabled>
</properties>
```

### Java Preprocessor


## 4. Linker / Loader

- Linker is a computer program that links and merges various object files together in order to make an executable file. All these files might have been compiled by separate assemblers. The major task of a linker is to search and locate referenced module/routines in a program and to determine the memory location where these codes will be loaded, making the program instruction to have absolute references.


- Loader is a part of operating system and is responsible for loading executable files into memory and execute them. It calculates the size of a program (instructions and data) and creates memory space for it. It initializes various registers to initiate execution.

### 5. Compiler vs. Interpreter

**Comipler**

A language rewriter program that translates the form of expressions without a change of meaning. C, C++ 


**Interpreter**

An execution program that directly runs instructions, without requiring them previously to have been compiled into a machine language program. HTML, Lisp, Pearl



### How Java works?

### What about Python?

### What are these?
Bytecode? Virtual Machine?

## 6. Hybrid Compiler

![hybrid-compiler](assets/1.02-hybrid-compiler.png)


### 7. Intermediate Code – Bytecode 

- Java: Statically typed, compiled language
- Python: Dynamically typed, (Scripting) non-compiled language 








# Lecture 1: Phases of Compilation

- Analysis (Frontend)
- Synthesis (Backend)
- Machine Independent Optimization (Optional)


## 1. Frontend: Analysis

If the analysis part detects that the source program is either syntactically ill formed or semantically unsound, then it must provide informative messages, so the user can take corrective action. 


The analysis part also collects information about the source program and stores it in a data structure called a symbol table which is passed along with the intermediate representation to the synthesis part .

## 2. Backend: Synthesis

The synthesis part constructs the desired target program from the intermediate representation and the information in the symbol table. 


The symbol table, which stores information about the entire source program, is used by all phases of the compiler.

## 3. Mid-end or Optimization

- Some compilers have a machine-independent optimization phase between the front end and the back end

- The purpose of this optimization phase is to perform transformations on the intermediate representation, so that the back-end can produce a better target program than an un-optimized intermediate representation

## 4. Structure of a Compiler

![compiler-structure](assets/1.03-compiler-structure.png)

- Modern compilers contain two (large) parts, each of which is often subdivided. 

- These two parts are the: front-end(analyzer), and the back-end (synthesizer) 

- The analysis part breaks up the source program into: constituent pieces and Imposes a grammatical structure on them 
- It then uses this structure to create an intermediate representation (IR) of the source program.

### C++ Tokens
Keywords, Identifiers, Literals, Operators, Punctuations/Separators, Whitespaces


## 5. Lexical Analysis
For  example, 

```bash
position  =  initial  +  rate  *  60 

Lexemes (position,=,initial,+,rate,*,60) are mapped into following tokens:

            <id, 1> <=> <id, 2> <+> <id, 3> <*> <60> 

```      
- Position is a lexeme that would be mapped into a token   <id , 1>  where id is  an  abstract  symbol  standing for  identifier and 1 points  to the  symbol table  entry for position.  

- The assignment  symbol =  is  a lexeme that is  mapped into the  token  <=>. It does not need attribute value to store name and type.

- Blanks  separating the lexemes would be  discarded by the  lexical  analyzer.





- The symbol-table entry for an  identifier holds information about  the identifier,  such  as its name and type. 

![lexical-analysis](assets/1.04-lexical-analysis.png)

### 5.1 Lexical Analysis
- Reads  the  stream  of  characters  making  up the  source  program and  groups  the  characters  into  meaningful  sequences  called  lexemes.  
- For  each lexeme,  the lexical  analyzer produces as output  a  token  of the  form <token-name , attribute-value>
- token-name is  an  abstract  symbol  that  is used  during  syntax analysis,  
- attribute-value  points  to  an  entry in the symbol table  for this token.


## 6. Syntax Analysis or Parsing
- The syntax Analyzer (parser) uses the  first  components  of the  tokens  produced  by  the  lexical  analyzer  to  create a tree-like  intermediate representation(IR) that  depicts  the  grammatical  structure of the  token  stream.  

- A  typical  representation  is  a  syntax  tree  in  which  each interior node represents an  operation and the  children of  the node represent the arguments of the operation.


## 7. Parser / Parsing ?

- Context-free  grammars  will be used to  specify  the  grammatical  structure  of programming languages and discuss algorithms  for constructing efficient  syntax  analyzers/parser automatically from certain classes of  grammars.


## 8. Semantic Analyser

- An important part of semantic analysis is type  checking,  where the compiler checks  that  each  operator  has  matching operands.
- The compiler needs semantic information, e.g., the types (integer, real, pointer to array of integers, etc.) of the objects involved. 
- The  language  specification  may  permit  some  type  conversions  called  coercions. 
- Suppose that  position,  initial, and rate have  been  declared  to be floating-point numbers,  and that  the lexeme  60 by  itself  forms an  integer. Here integer may be converted into floating-point.

## 9. Intermediate Code Generation
- After  syntax  and  semantic  analysis  of  the  source  program,  many  compilers  generate  an  explicit  low-level  or machine-like intermediate  representation, 

- This  intermediate  representation (IR)  should have two  important  properties:  
    - it should  be easy  to produce  and 
    - it  should be easy to translate into the target  machine. 


### The 3-address Code
- we  consider  an  intermediate  form  called  three-address  code, which  consists  of  a sequence  of  assembly-like instructions  with three  operands per instruction.  
Each operand can  act like a register .

![intermediate-code-gen](assets/1.05-intermediate-code-gen.png)

- There  are  several  points  worth  noting  about  three-address  instructions. 
- First ,  each  three-address assignment instruction has at  most one  operator  on  the right side.  Thus, these instructions fix the  order in  which operations are to be done; the  multiplication precedes the addition in  the  source  program.  
- Second, the compiler  must generate a  temporary  name  to  hold the value computed by  a  three-address instruction.  
- Third,  some  "three-address  instructions"  like the  first  and last  in  the  sequence above,  have fewer than three  operands.

## 10. Code Optimization

- The  machine-independent  code optimization  phase  attempts  to  improve  the intermediate code so that  better target code will result .  

- Usually better code means faster, shorter, or target code that consumes  less power

## 11. Code Generation
- The code generator  takes  as input an intermediate representation of  the source program  and maps  it into  the  target language.  
- If  the  target  language  is  machine code, registers or  memory locations  are selected  for  each  of  the variables used by the program.  
- Then, the intermediate  instructions are translated into sequences of  machine instructions  that  perform  the  same  task.
- The F  in  each instruction  tells  us  that  it  deals  with  floating-point  numbers
- The  #  signifies  that  60.0 is  to  be  treated  as  an immediate  constant.

# Lecture 2: Types of Compiler
- Single-pass compilers
- 2-pass compilers
- Multi-pass compilers

## 2.1 Single Pass Compiler

Source Code -> Compiler -> Target Code


- If we combine or group all the phases of compiler design in a single module known as single pass compiler.


- A one pass/single pass compiler is that type of compiler that passes through the part of each compilation unit exactly once.
- Single pass compiler is faster and smaller than the multi pass compiler.
- As a disadvantage of single pass compiler is that it is less efficient in comparison with multi-pass compiler.
- Single pass compiler almost never done, early Pascal compiler did this as an introduction.




We can not optimize very well due to the context of expressions are limited, as we can’t backup and process, it again so grammar should be limited or simplified.

### 2.2 Two-pass or Multi-pass Compiler


A Two pass/multi-pass Compiler is a type of compiler that processes the source code or abstract syntax tree of a program more than once. In multi-pass Compiler we divide phases in two pass as:

![two-pass-compiler](assets/1.06-two-pass-compiler.png)

### 2.3 First Pass
- Front end
- Analytic part
- Platform independent

![first-pass](assets/1.07-first-pass.png)

### 2.4 Second Pass

- Back end
- Synthesis Part
- Platform Dependent

![second-pass](assets/1.08-second-pass.png)


### 2.5 Multi-pass Benefit – 1

![multi-pass](assets/1.09-multi-pass.png)

### 2.6 Multi-pass Benefit - 2

![multi-pass-02](assets/1.10-multi-pass-2.png)

### 2.7 An ideal Multi-pass Compiler

![ideal-multipass-compiler](assets/1.11-ideal-mp-compiler.png)

### 2.8 The Cross Compilers

- A cross compiler is one that can run on a computer’s operating system that is different from the operating system that the program ordinarily uses. It breaks down binary codes, understands them and allows computer programmers to gain access to the codes.

- For example, a compiler that runs on a Windows 7 PC but generates code that runs on Android smartphone is a cross compiler.


### 2.9 Parallelizing Compiler

- A parallelizing compiler is typically a compiler that finds parallelism in a sequential program and generates appropriate code for a parallel computer. 

- More recent parallelizing compilers accept explicitly parallel language constructs, such as array assignments or parallel loops.

- Applications: Big Data and Multithreading

### 2.10 Compiler Traditional Application

Implementation of High-Level Programming Languages

- Optimizations for Computer  Architectures 
    - Parallelism, parallel (independent) or serial(dependent) instruction be executed 
    - memory hierarchy (register, cache, RAM,HDD)

- Design of New Computer Architectures 
    - CISC -Complex Instruction set computer, used in x86 machines
        - Uses complex addressing to store data structures using registers and stack.
    - RISC-Reduced Instruction set computer
        - PowerPC, SPARC , MIPS,  Alpha,  and  PA-RIS C,  are  based  on  the  RISC  concept
    - Specialized Architectures (embedded machines)

### 2.11 Compiler Also……
- Natural Language Processing 
- Database  Query  Interpreters

- Compiled  Simulation
    - Instead of writing a simulator that  interprets the  design,  it  is faster to  compile  the  design to  produce  machine  code that  simulates  that  particular design natively.  

- Hardware  Synthesis:
    - Hardware  designs  are  typically  described  at  the  register transfer  level  (RTL)  ,  where  variables  represent  registers  and  expressions  represent combinational logic.  
    - Hardware-synthesis  tools translate RTL descriptions automatically into gates ,  which are then mapped to transistors and eventually  to a physical layout .


# Lecture 3: A Simple Syntax Directed Translation


### Analysis


The analysis phase of  a compiler  breaks up a source  program into  constituent pieces and  produces  an internal representation for it,  called intermediate  code. 

- Lexical  Analysis, 
- Syntax and Semantics Analysis,
- Intermediate Code Generation.


### Context Free Grammar 

- A set of  terminal  symbols,  may be referred to  as “tokens”. 
- A set of non-terminals,  may be called  “syntactic variables”.
- A designation of one of the  non-terminals  as the  start symbol.
- A  set  of  productions,  where each production  consists  of a  
- Non-terminal, called the  head  or left-side  of  the production, an arrow, and a sequence of terminals and/or non-terminals , called  the body  or right side  of  the  production.


Using  the  variable  expr  to  denote  an  expression  and the variable stmt to denote  a  statement ,  this  structuring  rule  can  be expressed as:

stmt -> if (expr) stmt else stmt

Such a rule is called a production.  
In a production, lexical elements  like the keyword if  and the parentheses  are called  terminals.  
Variables like  expr  and  stmt  represent  sequences  of terminals and are called  non-terminals.




### Parse Trees

- Parsing is  the  problem of 
    - taking a start symbol and  
    - figuring out  how to derive a string of terminal  from the  it following the grammar rules

- And if it  cannot  be  derived from the start symbol of  the grammar ,  then reporting syntax errors within the string.

A  parse tree  pictorially  shows  how the  start  symbol  of a  grammar  derives  a  string  in  the language.  
If non-terminal  A has a production A  XYZ,  then a parse tree  may have an interior node  labeled  A  with  three children labeled  X, Y, and  Z, from  left  to  right: 

### Ambiguity
- A  grammar  can  have  more than one  parse trees  generating  a given string of terminals.  
- Such a grammar is  said  to be  ambiguous. 

- Since a string with more than one parse trees usually has more than one meaning, 
- we need to design unambiguous grammars for  compiling applications,  or to use ambiguous grammars with additional rules to resolve the ambiguities . 

![parsers](assets/2.01-parsers.png)


# Lecture 4: Associativity, Precedence & Expression Conversion

- Infix: Operators between operands (A + B * C)
- Prefix: Operators before operands (+ A * B C)
- Postfix: Operators after operands (A B C * +)

Compiler use-case:
- Compilers convert infix→postfix/prefix for intermediate code.
- Postfix simplifies evaluation without parentheses.

- Precedence resolves which operator first.
- Associativity resolves ties.
- Example: a - b - c = (a - b) - c (left-associative).

### Practice
1. Add parentheses
2. Infix, and Postfix

### Symbol Tables


### Translators for Simple Expressions

### Top Down Parsing
- Start from start symbol and expand to match input.
- Practice: S → aSb | ε derive aabb:
- S→aSb→aaSbb→aaεbb→aabb.
- Compiler use-case: used in LL parsers.


### Predictive Parsing
- LL(1) parser uses FIRST/FOLLOW to choose rules.
Grammar:
- E→TE', E'→+TE'|ε, T→FT', T'→*FT'|ε, F→(E)|id
- FIRST(E)={(,id}, FOLLOW(E)={),$}
- Compiler use-case: No backtracking required.


### ε-Productions
- Represents optional parts or list ends.
- Example: S→bS|ε generates b*.
- Compiler use-case: Handles optional elements like optional parameters.


### CFG vs Regular Expressions
- Regex: Flat patterns for tokens (lexer).
- CFG: Nested structures (parser).
- Example: a^n b^n needs CFG, not regex.
- Compiler use-case: Lexer uses regex, parser uses CFG.














<img width="1810" height="823" alt="image" src="https://github.com/user-attachments/assets/4b1db92d-c3f7-432c-93d9-5f3e64d6b54c" />
