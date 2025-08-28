import hashlib, time

class Move:
    NONE = 0
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

    def __init__(self, commitment, move=0):
        self.commitment = commitment  ## secret string
        self.move = move
    
    @classmethod
    def move_to_str(cls, move):
        return{
            cls.NONE:"none",
            cls.ROCK:"rock",
            cls.PAPER:"paper",
            cls.SCISSORS:"scissors"
        }[move]
    
class Challenge():
    def __init__(self, creator_address, _id, commitment):
        self.creator_address = creator_address
        self.opponent_address = None
        self.id = _id
        self.commitment = {self.creator_address: Move(commitment)}
        self.winner = None
        self.created_at = time.time()

    def add_opponent(self, address, commitment):
        self.opponent_address = address
        self.commitment[address] = Move(commitment)

    def reveal_move(self, address, move, nonce):
        if not self.has_opponent_committed():
            raise Exception("Opponent not joined yet...")
        reveal_hash = Challenge.generator_hash(nonce+move)
        commitment_hash = self.commitment.get(address)
        if reveal_hash != commitment_hash.commitment:
            raise Exception("Invalid move reveal...")

        self.commitment[address].move = int(move)

    @staticmethod
    def generator_hash(input):
        return hashlib.sha256(input.encode()).hexdigest()
    
    def both_revealed(self):
        opponent_move = self.commitment.get(self.opponent_address).move
        creator_move = self.commitment.get(self.creator_address).move
        return opponent_move != Move.NONE and creator_move != Move.NONE

    def has_opponent_committed(self):
        return self.commitment.get(self.opponent_address) is not None
    
    def evaluate_winner(self):
        opponent_move = self.commitment.get(self.opponent_address).move
        creator_move = self.commitment.get(self.creator_address).move

        if creator_move == Move.ROCK and opponent_move == Move.SCISSORS:
            self.winner = self.creator_address
        elif creator_move == Move.PAPER and opponent_move == Move.ROCK:
            self.winner = self.creator_address
        elif creator_move == Move.SCISSORS and opponent_move == Move.PAPER:
            self.winner = self.creator_address

        elif opponent_move == Move.ROCK and creator_move == Move.SCISSORS:
            self.winner = self.opponent_address
        elif opponent_move == Move.PAPER and creator_move == Move.ROCK:
            self.winner = self.opponent_address
        elif opponent_move == Move.SCISSORS and creator_move == Move.PAPER:
            self.winner = self.opponent_address

        return self.winner