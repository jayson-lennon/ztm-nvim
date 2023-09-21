There are many editing commands available. Here are a handful that I have found
useful in day-to-day editing.

1. Lines can be automatically joined together using `J`. Position the cursor
   anywhere on the first line in the block below, then use `J` to join all the
   lines into a single line. You can hold the key, or tap it multiple times:

     In Vim, the 'j' key is
     a fundamental command
     for moving the cursor
     downward by one line,
     allowing for efficient
     navigation and editing of
     text.

   You can also use `{count}J` to join a specified number of lines. This will
   include the current line, so when using relative line numbers you'll need to
   add 1 to the line count. Try joining this entire paragraph into a single
   line by moving to the first line of this paragraph and running `4J`.

2. Changing the case of letters and words comes in handy, especially when
   writing out variable and function names while coding. To change the case of
   a single letter, use the `~` key.

     Try changing the case of this entire sentence by holding `~`.

   To change the case based on a motion, we can use `g~{motion}`. `g` is sort
   of a catch-all key where miscellaneous/less commonly used commands are
   placed. Try changing the case of the above example sentence by moving the
   cursor to the first letter of the sentence and using `g~$`.

   A shorthand way to change the case of an entire line is `g~~`.

3. If you have something where you want all the letters to be uppercase, then
   you can use `gU{motion}`. Change the case to uppercase of the constant
   "my_super_useful_value" listed below by positioning the cursor anywhere in the
   constant's name and using `gUiw`:

     const my_super_useful_value = 42;

   If you need something all lowercase, then use `gu{motion}`. Change the above
   constant name back to lowercase by positioning the cursor somewhere in the
   name and using `guiw`.

4. Many editors will automatically wrap text once it reaches a certain length
   (like when writing code comments). This works fine until you make edits to
   the comment block and now some lines are too short and it looks awful. Vim can
   automatically wrap lines using `gw{motion}` or `gq{motion}` (depending on your
   configuration). Format the below block by positioning you cursor on the
   first line of the block and using `gw10j` (Neovim) or `gq10j` (VSCode):

     This is a simple implementation of the Bubble Sort algorithm.
     Bubble Sort is a comparison-based
     sorting algorithm that repeatedly
     steps through the
     list, compares adjacent elements, and swaps them
     if they are in the wrong order. This process continues until the
     entire list is sorted. While Bubble Sort is not the
     most efficient
     sorting algorithm for large lists,
     it is easy to understand and
     implement, making it a good choice for educational purposes.

5. Using `.` will repeat the last edit you made. This comes in handy when
   deleting multiple things in succession, or when changing multiple instances
   of something. Use `/book` followed by some number of `n` to jump to the first
   occurrence of the word "book" in the below paragraph. Then use `ciw` to change
   the first occurrence to "magazine". After changing the first occurrence,
   repeatedly press `n.` to quickly change the remaining occurrences of the word
   "book":

     I believe that a good book can be a loyal companion, so I spend hours
     searching the library for the perfect book to take home. Once I find a
     promising book, I like to sit in the cozy reading nook and lose myself in
     its pages. Reading a book allows me to escape the everyday routine and
     embark on incredible adventures. I often find that a well-written book can
     inspire, educate, and entertain all at once. There's something magical
     about the way a book can transport you to different places and times. So,
     I continue my quest for the next extraordinary book to add to my
     ever-growing collection.
