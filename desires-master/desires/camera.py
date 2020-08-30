import pygame

class Camera(pygame.Rect):
    camera_slack_x = 64
    camera_slack_y = 24

    def __init__(self, target_rect, screen_width, screen_height):
        super(Camera, self).__init__(target_rect.centerx-(screen_width/2),
                                     target_rect.centery-(screen_height/2),
                                     screen_width, screen_height)

    def update(self, player_rect, level):
        if self.centerx - player_rect.centerx > self.camera_slack_x:
            self.left = player_rect.centerx + self.camera_slack_x - self.width/2
        elif player_rect.centerx - self.centerx > self.camera_slack_x:
            self.left = player_rect.centerx - self.camera_slack_x - self.width/2
        if self.centery - player_rect.centery > self.camera_slack_y:
            self.top = player_rect.centery + self.camera_slack_y - self.height/2
        elif player_rect.centery - self.centery > self.camera_slack_y:
            self.top = player_rect.centery - self.camera_slack_y - self.height/2
        
        # This keeps the camera within the boundaries of the level
        if self.right > level.right_edge - level.tw:
            self.right = level.right_edge - level.tw
        elif self.left < level.tw:
            self.left = level.tw
        if self.top < level.th:
            self.top = level.th
        elif self.bottom > level.bottom_edge:
            self.bottom = level.bottom_edge

        level.view_x1 = (self.left / level.tw) - 1
        level.view_x2 = (self.right / level.tw) + 1
        level.view_y1 = (self.top / level.tw) - 1
        level.view_y2 = (self.bottom / level.tw) + 1