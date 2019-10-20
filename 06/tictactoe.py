def TicTacDraw(board):
	row_count=0
	for i in range(len(board)):
		board_1=''
		row_count= row_count+1
		for m in range(len(board[i])):
			if board[i][m]==0:
				board_1= board_1+' O |'
			#why must use board[i][m], why m is not ok?
			elif board[i][m]==1:
				board_1= board_1+' X |'
				
			elif board[i][m]==2:
				board_1=board_1+'   |'
		board_1=board_1[:-1]
		print(board_1)
		if row_count != len(board):
			print('-'*(len(board)*4-1))
			
TicTacDraw([[0,1,1,1,2],[2,1,1,1,1],[0,1,2,1,0],[2,1,0,0,0],[1,2,1,2,1]])
