# Problem 3

JSON would have made the problem easier. `json.load` hands back a dictionary
ready to use, so the entire parsing problem can be solved using existing libraries. No scanning the file
line by line, no remembering that you are inside a description until
`END DESCRIPTION` shows up, no splitting command lines on commas and colons,
and no chance of getting that bookkeeping wrong.
