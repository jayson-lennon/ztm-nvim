Small cursor movements using `hjkl` and `w` are great for fine-grained control,
but oftentimes we need to move a large distance.

1. `gg` will move the cursor to the first line of the document. Conversely, `G`
   will move the cursor to the last line. Try hopping to the end of this
   document with `G` and then hop back with `gg`.

2. `+` will move down a line, and then position the cursor at the first
   character in that line. `-` will do the same, but go up a line instead of
   down a line.

     Use `+` to move to the next section.

3. `0` moves to the very beginning of a line, whether the character is a space
   or not. `^` will move to the first non-blank character. Try out `0` and `^`
   on the below sentence:

     JavaScript is a versatile programming language commonly used for web
     development, enabling interactive and dynamic features on websites.

   Due to the positioning of `^`, and the need to hold `<SHIFT>`, it may be
   easier to combine multiple movement commands to achieve the same effect.
   Position your cursor on the word "Hypertext" below, then use `0w` to jump to
   the beginning of the sentence:

     HTML is an acronym for Hypertext Markup Language.

4. To move to the end of the line, use `$`. Try jumping between the beginning
   and end of the example lines above using `$` and `0` or `^`.

5. For programming, we will often need to refer to specific line numbers. To
   jump to any line number, use `{num}G`. Type `26G` to jump to the example
   sentence in section 3 and then type `35G` to jump to the next lesson.

6. To scroll just a few lines, `<CTRL-E>` can be used to scroll down, and
   `<CTRL-Y>` can be used to scroll up. Try scrolling up and down by using taps
   and holds. As with other Vim commands, scrolling can be combined with a number
   in order to scroll multiple lines. Use `10CTRL-E` to scroll down 10 lines.

     .
     .
     .
     .
     .
     .
     .
     .
     .
     .
     .
     .
     .
     .
     .
     .
     .
     .
     .
     .
     .
     .
     .

7. Use `<CTRL-D>` to move the cursor down half a page, and use `<CTRL-U>` to move
   the cursor up half a page. Go to the beginning of this document using
   `<CTRL-U>` and then jump back down here using `<CTRL-D>` followed by smaller
   motions as needed.

8. The `zz` command will center the window to the current cursor position. This
   is useful after making large jumps across the document so the cursor is not
   at the edge of the window. Position your cursor HERE then type `zz` to center
   the window.

     .
     .
     .
     .
     .
     .
     .
     .
     .
     .
     .
     .
     .
     .
     .
     .
     .
     .
     .
     .
     .
     .
     .
