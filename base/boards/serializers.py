from base.boards.constants import BOARD_SLUG_MAX_LENGTH
from base.boards.models import Boards
from base.utils.model_field_utils import generate_slug
from rest_framework.serializers import ModeSerializer

class BoardsSerializer(ModeSerializer):
    class Meta:
        model = Boards
        exclude = ('board_id',)
        
    def create(self, validated_data):
        validated_data['slug'] = generate_slug(validated_data['board_name'], BOARD_SLUG_MAX_LENGTH)
        board = Boards.objects.create(**validated_data)
        return board