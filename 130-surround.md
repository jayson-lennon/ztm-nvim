Adding/removing/changing quotes and other symbols is a common thing when
writing code. Using the `mini.surround` plugin, we can automatically update
surrounding symbols.

1. Surround keybinds are under `gz`:

     `gza{motion}{symbol}`: add `{symbol}` as the surrounding symbol
     `gzd{symbol}`: delete surrounding `{symbol}`
     `gzr{old}{new}`: replace `{old}` surrounding symbol with `{new}` symbol
   
   Place your cursor HERE then use `gzaiw"` to add double quotes.

   Place your cursor "HERE" then use `gzr"'` to replace the double quotes with
   single quotes.
