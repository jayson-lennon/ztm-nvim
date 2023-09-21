// Neovim has LSP support for many popular languages. This enables renaming
// variables and function names across projects, finding references, symbol
// lookups, and more.
//
// To find references, we can use `gr`. Position your cursor over the
// `quicksort` function name, then use `gr` to show the references in
// Telescope. Once Telescope is open, use the arrow keys to select a reference
// and then press `ENTER` to jump to it.
//
// You can also filter the results in Telescope by typing additional characters
// when the Telescope window is open.
//
// After closing the Telescope window, position the cursor over the `quicksort`
// function name again, use `gr` to find references, and then use `CTRL-Q` to
// load the reference list into a Quickfix window. The Quickfix window allows
// you to jump to the locations listed by positioning your cursor over an entry
// and then pressing `ENTER`.
//
// Your cursor should automatically be placed in the Quickfix window. If not,
// navigate to it using `CTRL-J`. Next, move the cursor to the third entry in
// the Quickfix window, and then press `ENTER` to jump directly to that entry.
//
// Alternatively, you can use Leap with `gs` (instead of `s`) to leap across
// windows.
//
// To rename a symbol, position your cursor over it and type `<LEADER>cr`.
// Rename the `arr` function parameter to `array` using `<LEADER>cr`.

function quicksort(arr) {
  if (arr.length <= 1) {
    return arr;
  }

  const pivot = arr[Math.floor(arr.length / 2)];
  const left = [];
  const middle = [];
  const right = [];

  for (let element of arr) {
    if (element < pivot) {
      left.push(element);
    } else if (element === pivot) {
      middle.push(element);
    } else {
      right.push(element);
    }
  }

  return [...quicksort(left), ...middle, ...quicksort(right)];
}

const myArray = [3, 6, 8, 10, 1, 2, 1];
const sortedArray = quicksort(myArray);
console.log(sortedArray);
