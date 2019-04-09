from sync.images import ComputedImage
from sync.images import register_image_class


@register_image_class('computed')
class ServerComputedImage(ComputedImage):
    def __init__(self, data_manager, params):
        super().__init__(self, data_manager, params)

    def handle_update(self, tile_key, data):
        # Write to krita
        pass

    def recv_computed_image(self, data):
        """
        Receive an updated image from the task runner.
        This function should synchronize with the other side, but does not need to handle any further compute dependencies
        """
        pass
