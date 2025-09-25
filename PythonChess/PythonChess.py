import chess

class PositionAnalyzer:
    def __init__(self, board):
        self.board = board
        self.piece_values = {1: 1, 2: 3, 3: 3, 4: 5, 5: 9, 6: 0}  # King worth 0 for material count
    
    def piece_activity_score(self, color):
        """Score how active pieces are based on attacks"""
        total_score = 0

        # Look at every square on the board
        for square in chess.SQUARES:
            piece = self.board.piece_at(square)

            # Analyse pieces that exist AND belong to specified colour
            if piece and piece.color == color:
                attacks = self.board.attacks(square)

                # Check each square this piece can attack
                for attack_square in attacks:
                    target = self.board.piece_at(attack_square)

                    if target is None:  
                        total_score += 0.01 
                    elif target and target.color != color:
                        total_score += 0.1
                    elif target and target.color == color:
                        total_score -= 0.01
        return total_score  

    def material_balance(self):
        """Calculate material advantage"""
        white_material = sum([len(self.board.pieces(piece_type, chess.WHITE)) * value 
                             for piece_type, value in self.piece_values.items()])
        black_material = sum([len(self.board.pieces(piece_type, chess.BLACK)) * value 
                             for piece_type, value in self.piece_values.items()])
        
        return white_material - black_material
    
    def mobility_count(self):
        """Count legal moves (basic activity measure)"""
        return len(list(self.board.legal_moves))
    
    def evaluate_position(self):
        #evaluate position from White's perspective (traditional scoring)
        material = self.material_balance()
        activity = self.piece_activity_score(chess.WHITE) - self.piece_activity_score(chess.BLACK)
        return material + activity * 0.1 #material worth 10x more than activity
    
    def evaluate_move(self, move):
        #evaluate move from current player's perspective (engine scoring)
        self.board.push(move)
        score = self.evaluate_position()
        #flip sign because it's now opponent's turn
        if self.board.turn == chess.BLACK:
            score = -score
        self.board.pop()
        return score 

    def search_depth(self, depth):
    #Search to a given depth using minimax
        if depth == 0:  
            return self.evaluate_position()
    
        best_score = float('-inf')
        for move in self.board.legal_moves:
            self.board.push(move)
            score = -self.search_depth(depth - 1)  # Opponent's turn, so negate
            print(f"{' ' * (2-depth)}Depth {depth}: {self.board.peek().uci()} = {score:+.1f}")
            self.board.pop()
            best_score = max(best_score, score)
        return best_score
    
    def find_best_move(self, depth=2):
    #Find the move using search to given depth
        best_move = None
        best_score = float('-inf')
    
        for move in self.board.legal_moves:
            self.board.push(move)
            score = self.search_depth(depth-1)
            self.board.pop()
            if score > best_score:
                best_score = score
                best_move = move
    
        return best_move, best_score

    def analyze(self):
        """Run basic position analysis"""
        print(f"=== Position Analysis ===")
        print(f"Turn: {'White' if self.board.turn else 'Black'}")
        print(f"Material balance: {self.material_balance():+d}")
        print(f"Legal moves: {self.mobility_count()}")
        print(f"White activity: {self.piece_activity_score(chess.WHITE):.2f}")
        print(f"Black activity: {self.piece_activity_score(chess.BLACK):.2f}")
        print(f"In check: {self.board.is_check()}")
        print(f"Checkmate: {self.board.is_checkmate()}")

if __name__ == "__main__":
    # Create the position and analyze it
    board = chess.Board("r1bqkb1r/pppp1ppp/2n2n2/4p3/2B1P3/3P1N2/PPP2PPP/RNBQK2R b KQkq - 0 4")
    print(board.unicode())
    print()
    
    analyzer = PositionAnalyzer(board)
    analyzer.analyze()
    best_move, score = analyzer.find_best_move(2)
    print(f"Best move: {board.san(best_move)} (score: {score:+.1f})")
