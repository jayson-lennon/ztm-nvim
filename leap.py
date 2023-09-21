# Leap is a plugin that enable you to jump to any arbitrary location within
# view using only 4 keystrokes. It works by searching for 2 keystrokes that you
# enter, and then overlaying a "label" character. This label character is shown
# when there are multiple targets that match your keystrokes.
#
# When using Leap, you'll want to visually look at the place you want to leap
# to, type the leap command (detailed in the next paragraph), and then type the
# label character if needed. Leap always requires 2 search characters to be
# typed no matter what, so even though a label character may appear
# immediately, you'll still need to finish your 2 character sequence before
# typing the label character.

# READ THIS WHOLE PARAGRAPH BEFORE RUNNING THE COMMAND:
# An important part of using Leap is first identifying where you want to Leap
# to. For this example, we will leap to the word `pivot` on line 32. Position
# your cursor HERE, then take a mental note that the key sequence we will use
# to leap is `spi` (`s` for Leap, `pi` for `pivot`). Once you have remembered
# `spi`, type it while looking at the word `pivot` on line 32. You'll see a
# highlighted label character appear over `pivot` which needs to be typed after
# `spi`. Once the label character is typed, the cursor will jump to `pivot` and
# you can continue the lesson with the comment directly below the leap target.

def quicksort(arr):
    # After leaping back to this function parameter, leap to the the word
    # `list` in `sorted_list` at the end of this file.
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    # To leap backwards, use `S`. Leap back to the function parameter `arr` by
    # typing `Sar` and then the label character indicated over the parameter
    # name.
    
    return quicksort(left) + middle + quicksort(right)

my_list = [3, 6, 8, 10, 1, 2, 1]
sorted_list = quicksort(my_list)
print(sorted_list)

# Leap is an extremely fast way to navigate around a document. Practice leaping
# around some more until you are comfortable.
