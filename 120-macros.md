Macros offer a way to repeat whatever you typed multiple times. Think of it
like writing a mini program that can be invoked whenever you need it. Since
macros simply repeat whatever you have done, they can do anything that you
would normally do in Vim.

The `q` key is used to start and stop recording of a macro. Macros must be
given a single character name or number.

  - To start recording a macro, use `q{name}`
  - To stop recording a macro, use `q` while recording
  - To run macro, use `@{name}`

1. We'll start with a small macro to convert data copied from documentation
   about HTTP status codes into a JavaScript object that we can use directly in
   code. The JavaScript object will act as a map where the status code will be the
   key and the name of the code will be the value. We will ignore the description.

   An example object:

     const statusCodes = {
       "418": "I'm a teapot",  // we are making this part
     };

   Read all these steps below first, and then attempt to produce them on the
   data set. Important note: if you have auto quote closing enabled, then
   you'll need to delete the extra `"` after each edit. You can move the cursor
   using `h` or `l` then hit `x` to delete an extra quote. This will be
   included in the macro, so all extra quotes will get deleted in the same way
   you did it.

     1. Position your cursor anywhere on the `const statusCodes = {` line.
     2. Begin recording the macro with `qs+`. Macros that we want to run on
        multiple successive lines should always advance the cursor to the next
        line either at the start of the macro or at the end of the macro.
     3. Add quotes around the status code with `i"<ESC>ea":<ESC>`.
     4. Move to the status code name with `w` and add one double quote.
     5. Jump to the `:` with `/:<ENTER>`. We do this because some names have
        spaces and parentheses which will interfere with `w` and `e` movement.
     6. Use `C",<ESC>` to remove the `:`, close the double quote, and add a
        comma.
     7. Finish recording the macro with `q`
     8. With the cursor still on the `200 OK` line, run the macro 19 times with
        `19@s`. The remaining data set should get converted to the proper
        format for a JavaScript object.
     9. If the macro incorrectly modified the data, undo with `u` until the
        dataset returns to it's default state and try again.

     const statusCodes = {
       200 OK: The request was successful, and the server has returned the requested data.
       201 Created: The request has been fulfilled, resulting in the creation of a new resource.
       204 No Content: The request was successful, but there is no data to return (typically used for DELETE requests).
       301 Moved Permanently: The requested resource has been permanently moved to a new URL.
       302 Found (or Temporary Redirect): The requested resource temporarily resides under a different URL.
       304 Not Modified: The client's cached copy of the resource is still valid, and there's no need to transfer the requested data.
       307 Temporary Redirect: Similar to a 302, but the client should continue to use the original URL.
       308 Permanent Redirect: Similar to a 301, indicating that the resource has been permanently moved.
       400 Bad Request: The server could not understand the request due to invalid syntax or other client-side issues.
       401 Unauthorized: The request lacks valid authentication credentials for the target resource.
       403 Forbidden: The server understood the request, but the client does not have permission to access the requested resource.
       404 Not Found: The requested resource could not be found on the server.
       405 Method Not Allowed: The HTTP method used in the request is not allowed for the requested resource.
       410 Gone: The requested resource is no longer available, and there is no forwarding address.
       413 Request Entity Too Large: The server refuses to process the request because the request entity is larger than the server is willing or able to process.
       429 Too Many Requests: The user has sent too many requests in a given amount of time (rate limiting).
       500 Internal Server Error: A generic server error occurred, indicating a problem on the server-side.
       502 Bad Gateway: The server, while acting as a gateway or proxy, received an invalid response from an upstream server.
       503 Service Unavailable: The server is currently unable to handle the request due to temporary overloading or maintenance of the server.
     };

2. Next we'll write a macro to stub out a `switch` block using a portion of the data set above.
   
   An example switch block:

     switch (code) {
       case "400":  // Bad Request
         break;
     }
   
   As before, read over the steps first and then proceed to create the macro:

     1. Position your cursor on the `switch (code)` line.
     2. Begin recording the macro with `qs+`.
     3. Surround the status code with double quotes and add a `case` statement
        using `icase "<ESC>ea":<ESC>`.
     4. Use `w` to jump to the status code name and create a comment with `i// `.
     5. Search forward using `/:<ENTER>` then delete the description with `D`.
     6. Create a new line and add a `break` statement with `o  break;<ESC>`.
     7. End macro recording with `q` and then run it 8 times using `8@s`.


     switch (code) {
       200 OK: The request was successful, and the server has returned the requested data.
       301 Moved Permanently: The requested resource has been permanently moved to a new URL.
       308 Permanent Redirect: Similar to a 301, indicating that the resource has been permanently moved.
       400 Bad Request: The server could not understand the request due to invalid syntax or other client-side issues.
       401 Unauthorized: Authentication is required, and the provided credentials are either missing or invalid.
       403 Forbidden: The server understood the request, but the client does not have permission to access the requested resource.
       404 Not Found: The requested resource could not be found on the server.
       500 Internal Server Error: A generic server error occurred, indicating a problem on the server-side.
       503 Service Unavailable: The server is currently unable to handle the request due to temporary overloading or maintenance of the server.
     }
