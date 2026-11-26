# Problem 4

Since the server decides the state after every move (through `OKAY` or `INVALID`), 
and the protocol sends moves instead of board state, after a click the client cannot update the board until the
server answers `OKAY` or `INVALID` and then sends its own move followed by
`READY`. In other words, our game have to wait until the server to respond to update the state,
while in a local game we don't have to (we can just update the state immidietly as we want).
