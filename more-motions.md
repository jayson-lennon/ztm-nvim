1. Vim has motions to move between specific characters. Using `f{char}` will
   move forward onto the next occurrence of `{char}`. While not particularly
   useful on it's own, combining it with `d` or `c` allows the deletion or
   changing of text in a precise manner. Position the cursor at the beginning of
   the word "favorite" below, then use `cfNn<ESC>` to change "favoriteNumber"
   to "number":

     const favoriteNumber = 12;

2. `F{char}` can be used to move backwards instead of forwards. Position the
   cursor in the space after word "Number" below, then use `dFN` to delete the
   word:
     
     const favoriteNumber = 12;

3. Functionally similar to `f`, using `t{char}` will move the cursor until the
   next occurrence of `{char}`. This is useful when you don't want to include
   the character itself when deleting or changing something. Position the cursor
   over the "A" in "Alice" below, then use `ct"` and enter your name:

     const personName = "Alice";

   Also similarly to `F`, `T{char}` will move backwards instead of forwards.
