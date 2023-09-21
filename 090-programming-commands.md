While the motions we have covered so far are fine for regular text, they don't
always take into account how programming languages are structured.

1. A very useful command is `%` which matches corresponding braces or
   parentheses. To use `%`, move your cursor over any `(`, `[`, or `{` and then
   press `%` to jump to the opposite one (this works for `)`, `]`, and `}` as
   well). This can be used to find missing braces and extra braces. In the below
   example, use `%` to find the extra parenthesis and then remove it with `x`:

     (((a + b) * c) - 4))

   Here's an example where a small formatting mistake resulted in code that
   looks OK at a glance, but is actually missing a curly brace. Use `%` to find
   where the missing curly brace should be placed by observing the cursor
   position movements to see if the `}` lines up with it's corresponding
   block:

     ```js
     const x = (() => {
         function test() {
             if (a || b) {
                 if (c && d) {
                     switch (e) {
                       case 1:
                         break;
                       case 2:
                         break;
                       case 3:
                         break;
                       case 4:
                         break;
                     print("hello!");
                 }
             }
         }
     });
     ```

2. When inside a block surrounded by parentheses or curly braces, use `[{` or
   `[(` to move to the nearest opening curly brace or parenthesis. To move to
   the closing one, use `]}` or `])`.

   Move the cursor to the "case 2" in the section 1 exercise, then use `[{` to
   jump to the beginning of the `switch` block. Afterwards, use `])` to jump to
   the end of the function expression.

3. The inside of paired symbols can also be changed using `ci{symbol}`. This
   works for most symbols such as `"`, `'`, `{`, `(`, `|`, `$`, etc. Vim will
   jump to the next occurrence of the symbol pair when using this
   command.

   We will change the below function using a series of delete and change
   commands. Position your cursor HERE then use `di(` to delete the function
   parameter. Afterwards, use `ci"` and change "hello" to "hi". Finally, use
   `ci{` and change the function body to `return "greetings!";`:

     function greet(message) {
       console.log("hello");
     }
   
4. Not all languages have opposite closing and opening symbols, such as HTML.
   For these situations, we can use `cit` to change the text within HTML tags.
   Use `cit` to change the below title tag of "PLACEHOLDER" to "My page":

     <title>PLACEHOLDER</title>

5. Commenting out code is a pretty routine thing to do. `gcc` will comment a
   line of code based on the file type detected by Vim. You can use
   `gc{motion}` to comment out multiple lines. Position your cursor over the
   `switch` below, then use `gc9j` to comment out the entire block:

     ```js
     switch (e) {
       case 1:
         break;
       case 2:
         break;
       case 3:
         break;
       case 4:
         break;
     }
     ```

6. Indenting code is another common task. Use `>>` to shift right (indent), and
   `<<` to shift left (unindent). As with many commands, using a motion will
   allow multiple lines to be indented.

   Position your cursor over `(b)` below, then use `>2j` to indent that line
   and the 2 lines below it. Then move to the `console.log` line and use `>>`
   to indent it further:

     ```js
     if (a) {
     if (b) {
     console.log("c");
     }
     }
     ```

   If you want to indent more than a single time, you can use visual mode.
   Position your cursor over the first `console.log` in the function below,
   enter visual mode using `vi{` to select the entire function body, and then
   indent 4 times with `4>`.

     ```js
     if (b) {
     console.log("a");
     console.log("b");
     console.log("c");
     }
     ```
