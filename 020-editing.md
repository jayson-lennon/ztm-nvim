1. "Insert mode" allows you to enter characters like you would in a traditional
   text editor. Move the cursor to the start of the word `jumped` in the
   sentence below, press `i` to enter insert mode, and then fill in anything you
   want to complete the sentence. Once the sentence is complete, press the escape
   key (`ESC`) to return to normal mode.

     The quick brown jumped over the lazy dog.

2. There are many ways to enter insert mode. Using `a` (for append) will enter
   insert mode one character in front of the cursor. Try completing the
   sentence below by moving the cursor to the end of the sentence, then append
   text using `a`:

     The sunsets by the beach are

   Practice using `i` and `a` by making any edits you wish to the previous
   sentences (or entire document) until you are comfortable entering and
   exiting insert mode. Once you are ready, move on to listing 3.

3. Not all editing requires entering insert mode. `x` will delete the character
   under the cursor and remain in normal mode. Use `x` to delete the extra
   letters in this sentence:
     
     Aartificial intelligencee continues to resshape the ttech industry.

4. Using `r{char}` will replace the character under the cursor with `{char}`.
   Use `r` to fix the spelling of the words in this sentence:

     Coffee is a beluved beverage enjoyed by millions fur itz rich,
     invigorating flaver and caffeine b00st.

5. `R` will enter replace mode. Replace mode overwrites characters instead of
   inserting them. Use `R` to change the surrounding hyphens (`-`) below to
   equals (`=`):

     -----------
      Section 5
     -----------

6. The `d` command is for deletion. It can be combined with a motion to delete
   text based on cursor movement:
    
     `dw`: delete from the cursor until the next word
     `de`: delete from the cursor until the end of the current word 
     `diw`: delete inner word (deletes the entire word regardless of cursor
     position)
   
7. Practice using the `d` command by removing words that don't belong in this
   short paragraph:

     Walking through a park is a coffee peaceful experience. The HTML sound of
     birds, the sight of swaying trees telephone, and the fresh air sidewalk
     create a soothing atmosphere for a leisurely thanks stroll.

8. To undo an edit, press the `u` key. Undo the edits made to the previous
   paragraph by pressing `u` multiple times.

9. To redo edits, press `<CTRL-R>`. Redo multiple times until the paragraph
   above is fixed again.

10. A common task is to delete lines. `j` and `k` movements can be combined
    with `d` to delete lines:

     `dd`: delete the current line
     `dk`: delete the current line and the previous line
     `dj`: delete the current line and the next line
     `d2j`: delete the current line and the next 2 lines

    Using various `d` commands, delete the duplicated lines in the list below:

    1. Python
    2. JavaScript
    2. JavaScript
    3. Java
    4. C++
    5. Ruby
    5. Ruby
    6. Swift
    7. Go
    8. Rust
    9. PHP
    9. PHP
    9. PHP
    9. PHP
    9. PHP
    10. Kotlin
    10. Kotlin

11. Use `c` to change text. "Change" automatically enters insert mode after
    deleting text. In all cases where `d` was used above, `c` can be used
    instead. Use `c` commands (like `ciw` or `ce`) to change all occurrences of
    "red" to "blue" in the sentence below:

      I spotted a vibrant red apple on the red kitchen counter, its red glossy
      skin reflecting the afternoon sun, reminding me of the red roses in the
      garden.

12. Use any combination of `a`, `i`, `x`, and `r` to fix the spelling in the
    below sentence. Try to use each command at least once. After fixing the
    sentence, change the words `hotel` and `people` to any other words you want
    using the `c` command.

      In the hotle lobby, I sat dwn and watchde many peeple coming and going, eech
      with their oown planz.

13. To create a new line, use `o`. To create a new line above the cursor, use
    `O`. To help remember, think of it like "opening" a new line. Position your
    cursor HERE, create a new line with `o`, then write "a new line!".
