1. Copying is referred to as "yanking" in Vim. The `y` key is used to yank text
   based on a motion:

     `yy`: yank the current line
     `yiw`: yank the current word
     `y3j`: yank the current line + the next 3 lines

2. To paste yanked text, use the `p` key. Try duplicating the next line using
   `yyp`:

     To understand recursion, one must first understand recursion.
   
   You can also paste above the cursor position using `P`.

3. As with other Vim commands, `p` can be repeated by providing a number. Lots
   of coffee went into the production of these practice lessons, duplicate the
   "Coffee Shop" line below and paste it 3 times using `yy3p`:

     2023-09-25   Electronics Store   $35.75
     2023-09-20   Bookstore           $25.50
     2023-09-15   Streaming Service   $12.99
     2023-09-12   Coffee Shop         $7.20
     2023-09-10   Gas Station         $45.80
     2023-09-05   Grocery Store       $85.50
     2023-09-01   Amazon              $199.00

4. When a yank is performed, it gets saved into a `register`. Registers are
   Vim's way of storing small bits of information about the state of the editor.
   For the purposes of yanking, registers are like mini clipboards.

   Registers for normal usage are named `a-z` and `0-9`. So there are 36
   registers available to yank into.

   To yank into a specific register, use `"{register}y{motion}`. Yank the
   all-caps word below into register `v` by positioning your cursor over the
   first character and typing `"vyw`:

     VIM

   Next, paste the contents of register `v` below using by positioning your
   cursor at the space after HELLO and typing `"vp`:

     HELLO 


