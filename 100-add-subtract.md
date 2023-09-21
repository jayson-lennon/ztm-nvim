1. Vim has a shortcut for adding and one for subtracting. This is useful for
   incrementing and decrementing numbers in code. To increment a number, use
   `<CTRL-A>`. To decrement a number, use `<CTRL-X>`. Position your cursor at the `1)`
   below, then hit `<CTRL-A>` a few times to increment it to 5:

     1)

2. If you want to add more than 1 to a number, you can prefix the increment or
   decrement command with the number of times you want to repeat it. Position
   your cursor on the `15)` below, and use `10<CTRL-X>` to decrement it to 5:

     15)

3. Combining the increment and decrement commands with visual mode allow the
   creation of lists of numbers. While in visual mode, pressing `[count]g
   <CTRL-A>` will increment a list of numbers in a sequence.

   Let's create a list numbered 1 through 20. Move the cursor down to the `0.`
   below, then duplicate the line 19 times with `yy19p`:

     0.
   
   After duplication, move the cursor to the last `0` above then enter visual
   block mode with `<CTRL-V>19k` to select all the `0`. Next type `g<CTRL-A>`
   to generate a list of numbers from 1 through 20.

4. We don't have to increment by 1 when generating lists. Using `{visual}5g
   <CTRL-A>` will increment the list by 5. Position the cursor to the first `0`
   below, then run `<CTRL-V>9j5g<CTRL-A>` to generate a list that increments by 5:
   
     0.
     0.
     0.
     0.
     0.
     0.
     0.
     0.
     0.
     0.
