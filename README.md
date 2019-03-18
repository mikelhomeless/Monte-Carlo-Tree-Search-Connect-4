# Monte-Carlo-Tree-Search-Connect-4
python3 main.py to start

Algorithms:
main:
  loop until win or cat
    have player search for then make a move
    display board
    exit if win
    switch state to next player

ConnectFour:
  data structures -> arrays, stacks, UnionFind
  board -> array of 7 stacks
  placing a piece into a column is essentially putting the piece on the top of the stack

  win condition:
    Checking a win condition is done by linking pieces into an equivalency set along each of its axes.
    The conditions for two pieces being equivalent is that they must be adjacent to each other and on the same linear axis.
    by doing this, we don't have to traverse through the board to locate 4 in a row, we only need to check what is adjacent.
    When the size of an equivalency set is 4 (-4) then we know that we have a winning condition

  get legal moves:
    return an array of all columns that are not currently filled

  next turn:
    toggle the player counter from 0 to 1 or 1 to zero

  make move:
    validate the move is legal
    place into the stack of the column

  is valid move:
    if the move is larger than the bounds of the game, it is not legal.
    if the column is full, it is not a legal move

Agent:
  data structures - > arrays, tree nodes
  run_simulation:
    while we have neither won lost or drawed, keep searching
      select move of current player
      if winning condition
        add one wins
        add one to steps
        add one to agent steps
        return
      if there are no more moves left
        exit
      else
        select move of next player
        if we lost
          add one to lost
          add one to steps
          return
      get next move

  get move:
    copy state
    get current options for moves
    while search_count < search_limit
      run simulation
      reset state
      search_Count++
    return move with max win percentage

View controller:
  convert board to string with color values for terminals
  transpose the array to match how the game should look
  print the display to the user
