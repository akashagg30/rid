from base.boards.models import Board

class BoardController:
    
    def create_board(self, validated_data):
        # Create a new board using the validated data
        board = Board.objects.create(**validated_data)
        return board