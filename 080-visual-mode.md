Visual mode allows multiple chunks of text to be selected visually and then
operated upon. Vim has two visual modes: line and block. Line mode selects
entire lines, whereas block mode lets you draw a rectangle around characters
and selects everything within.

1. To enter visual line mode, use `v{motion}`. Move the cursor to "The" below,
   and then select the entire block by using `v8j`. After the selection has
   been made, press `J` to join all the lines.

     The
     quick
     brown
     fox
     jumped
     over
     the
     lazy
     dog.

  Visual mode has most of the same editing commands we have used so far and
  acts mostly as a visual confirmation of the text that will be impacted by a
  command.

  Just like in regular mode, visual mode allows the case of characters to be
  switched with `~`, or made uppercase with `U`. The entire selection can be
  cut with `x`, or replaced with a character by using `r`.

2. Visual block mode has a few more useful capabilities over visual line mode.
   Since it can select just a column, it can be used to add or replace things
   across multiple rows.

   We will add `.` after each number below by using visual block mode. Move
   your cursor over the `1` below then enter visual block mode with `<CTRL-V>`.
   Next select all the numbers using `8j` and then append with `A.`.

     1
     2
     3
     4
     5
     6
     7
     8
     9

3. To replace multiple characters we can use `r`. Position your cursor on the
   `.` in `1.` above (complete task 2 first), then enter visual block mode with
   `<CTRL-V>`. Select all the `.` with `8j` and then replace them with `r)`.

4. We can use `I` to enter insert mode at the cursor location (instead of
   appending at the end like we did with `A`). Move the cursor to the `9` in
   `9)` above (complete task 3 first) and then enter visual block mode with
   `<CTRL-V>`. Select up through `1)` by using `8k` and then enter insert mode
   with `I`. Once in insert mode, type `- ` to prepend each item with a dash.

5. To replace text we use "substitute". Substitute is a command that must be
   entered on the Vim command line. We will substitute the programming language
   below with your favorite (or any other) programming language. First position
   the cursor on the beginning of the line below, and then open the Vim command
   line with `:`. The cursor will move to the command line at the bottom of the
   screen. Once on the command line, type `s/Vimscript/JavaScript/g` then press
   `<ENTER>`.

     My favorite programming language is Vimscript!
   
   The syntax for the substitute command is `s/OLD/NEW`. It only changes the
   first occurrence by default, but appending `/g` (global) to the end will
   replace all occurrences.

6. Using `:s/OLD/NEW/g` only replaces text on the current line. To replace text
   in the whole file, use `:%s/OLD/NEW/g`. Try replacing all occurrences of the
   word "cursor" with "pointer" by using `:%s/cursor/pointer/g`.

7. Oftentimes we'll only want to substitute text in a specified area. We can
   use visual mode to accomplish this. Create a visual selection over the
   paragraph below, and then use `:s/\%Vbook/novel` to replace occurrences of
   "book" with "novel".

     I often find solace in the company of a good book. The book's pages hold a
     world of adventure and imagination, transporting me to different realms.
     Reading a book is like embarking on a journey, discovering new
     perspectives and experiences.
   
   The `\%V` constrains the substitution to just the visual selection.
