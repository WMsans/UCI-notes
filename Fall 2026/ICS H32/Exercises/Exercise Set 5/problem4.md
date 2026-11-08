# Problem 4

## 1. Why it was important to specify an encoding

`read()` gives back bytes, and bytes carry no information about which
characters they represent. The same sequence decodes to different text under
different encodings, so decoding is only correct if you know which mapping
the server used.

## 2. How you would find out the appropriate encoding

The HTTP response says so itself, in the `Content-Type` header, usually as
`application/json; charset=UTF-8`. Python will pull that value out for you
with `response.headers.get_content_charset()`, so in practice the server
tells the client what to use and the client only has to read the header
instead of assuming.
