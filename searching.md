Searching is one of the most powerful features in Vim. It enables you to
immediately jump to the specified text without interrupting your work.

1. Searching uses the `/` key followed by whatever text you want to find.
   Position your cursor at the start of the sentence below, then use
   `/MB<ENTER>` to search for storage capacity of USB sticks. Then change it to a
   capacity that makes more sense for your time period using `ciw`:

      A large capacity USB stick may have up to 512MB of storage!

2. It's very common to have more than a single match for your search query. To
   go to the next search result, use `n` after performing your search. Note
   that the status bar at the bottom of the screen will show the number of matches
   along with the current match index.

   Search for the word "the" with `/the<ENTER>` and then use `n` to find the
   next match and `N` to find the previous match.

   Continue searching this document for "to", "for", "and". Use `n` and `N` to
   jump between matches until you are comfortable searching.

3. Searching can be initiated backwards as well. Use `?` followed by some text
   to search backwards from your cursor position. Try typing `?large<ENTER>` to
   find the word "large" from section 1 above (you may need to use `n` to jump to
   the correct match).

4. Searching in Vim isn't limited to just finding things. We can use a search
   with `c` or `d` to change or delete entire chunks of text. Vim will keep
   track of all the text the cursor crossed in order to find the search result,
   and then change or delete it based on the command provided.

   In this example we will remove the text "a wide range of" from the below
   sentence. Position your cursor HERE, then type `/a wide<ENTER>n` to jump to
   the starting position in the below sentence. Once there, use
   `d/tasks<ENTER>` to delete everything from the cursor up to (but not
   including) the next search result.

     Linux terminals provide a powerful text-based interface for users to
     perform a wide range of tasks efficiently.

5. To quickly find occurrences of the word under the cursor, use `*`. If you
   want to search backwards, then use `#`. Position your cursor on any word in
   this document and use `*` to find other occurrences.
