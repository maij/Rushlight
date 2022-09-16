def snap_to_bounding_box(obj, window_rect):
    if hasattr(obj, 'pos'):
        if obj.pos.x < 0:
            obj.pos.x = 0
        elif obj.pos.x > window_rect.width:
            obj.pos.x = window_rect.width

        if obj.pos.y < 0:
            obj.pos.y = 0
        elif obj.pos.y > window_rect.height:
            obj.pos.y = window_rect.height
        
        #if self.pos.x > WIDTH:
        #    self.pos.x = 0
        #if self.pos.x < 0:
        #    self.pos.x = WIDTH
        #     
