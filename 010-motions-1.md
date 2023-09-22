1. Cursor movement is performed using `h` `j` `k` and `l`:

```text
         ↑
         k
     ← h   l →
         j
         ↓
```

2. Take a moment to move the cursor around this document until you become
   familiar with the direction that each key moves. Try both tapping the keys
   and holding the keys. Once you are comfortable moving with the `hjkl` keys,
   move the cursor to listing 4.

3. In addition to character movements, the cursor can be moved across entire
   words:

     `e`: move to the end of the current word
     `w`: move to the start of the next word
     `b`: move back to the start of the previous word

   Using `e`, `w`, and `b`, move between the words in the below paragraph to
   see how the cursor moves when various kinds of punctuation are present:

     Navigating the Linux command line is essential—commands like 'cd' (change
     directory) and 'ls' (list) help locate files and directories swiftly.
     'grep' is invaluable for text searches, finding patterns or keywords.

   Try combining the `h`, `j`, `k`, `l` keys along with `e`, `w`, and `b` to
   move around the words in the above paragraph. When you are comfortable with
   `e`, `w`, and `b` motions, continue on to listing 5.

4. Motions can be combined with a number to repeat it a specified number of
   times. Position the cursor at "zero" below, then press `3j` to move the
   cursor down 3 lines:
   
     zero
     one
     two
     three
     four
     five

  This works with other motions such as `w` and `b`. Try moving to the 5th word
  in the sentence below by positioning the cursor at "Systemd" and then
  pressing `4w`:

    Systemd is a modern init system for managing processes and services in Linux.

  Practice combining the motions in this lesson with a number until you become
  more comfortable repeating motions. Once you are ready, move on to the next
  lesson.
