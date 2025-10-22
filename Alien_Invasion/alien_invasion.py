import sys
from time import sleep
import pygame
from settings import Settings
from game_stats import GameStats
from ship import Ship
from bullet import Bullet
from alien import Alien
from button import Button
from scoreboard import Scoreboard
#from star import Star
#from random import randint

class AlienInvasion:
    """Overall class to manage game assets and behaviour"""

    def __init__(self):
        """initialise the game, create game resources."""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        #self.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
        #self.settings.screen_width = min(self.screen.get_rect().width, 1200)
        #self.settings.screen_height = min(self.screen.get_rect().height, 800)
        self.screen = pygame.display.set_mode((self.settings.screen_width,
              self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        #Create an instance to store game statistics.
        #and create a scoreboard.
        self.stats = GameStats(self)
        self.sb = Scoreboard(self)
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        #self.stars = pygame.sprite.Group()
        #self._create_group_stars()
        self._create_fleet()
        #Start Alien invasion in an inactive state.
        self.game_active = False
        self.show_difficulty_menu = False
        self.chosen_difficulty = 'medium' #default difficulty

        #Make the Play button.
        self.play_button = Button(self, "Play")

        """Make the difficulty buttons"""
        self.difficulty_button = Button(self, "Set Difficulty")
        self.difficulty_button.rect.top = self.play_button.rect.bottom + 30
        #re-center the text on repositioned button
        self.difficulty_button.msg_image_rect.center = self.difficulty_button.rect.center

        #make and position other difficulty buttons
        y_position = self.difficulty_button.rect.bottom + 20

        self.easy_difficulty_button = Button(self, "Easy")
        self.easy_difficulty_button.rect.centerx = self.screen.get_rect().centerx - 220
        self.easy_difficulty_button.rect.top = y_position
        self.easy_difficulty_button.msg_image_rect.center = self.easy_difficulty_button.rect.center

        self.medium_difficulty_button = Button(self, "Medium")
        self.medium_difficulty_button.rect.centerx = self.screen.get_rect().centerx 
        self.medium_difficulty_button.rect.top = y_position
        self.medium_difficulty_button.msg_image_rect.center = self.medium_difficulty_button.rect.center

        self.hard_difficulty_button = Button(self, "Hard")
        self.hard_difficulty_button.rect.centerx = self.screen.get_rect().centerx + 220
        self.hard_difficulty_button.rect.top = y_position
        self.hard_difficulty_button.msg_image_rect.center = self.hard_difficulty_button.rect.center


    def run_game(self):
        """start the main loop for the game."""
        while True:
            self._check_events()

            if self.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()
            
            self._update_screen()
            self.clock.tick(60)


    def _check_events(self):
        """respond to keypresses and mouse events."""
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.stats.save_high_score()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    self._check_play_button(mouse_pos)
                    self._check_difficulty_button(mouse_pos)
                    self._check_difficulty_level_buttons(mouse_pos)

                elif event.type == pygame.KEYDOWN:
                    self._check_keydown_events(event)
                elif event.type == pygame.KEYUP:
                    self._check_keyup_events(event)

    def _check_play_button(self, mouse_pos):
        """Start a new game when the player clicks Play."""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.game_active:
            self.settings.initialize_dynamic_settings(self.chosen_difficulty)
            self._start_game()
    
    def _check_difficulty_button(self, mouse_pos):
        """Allow player to pick difficulty level."""
        button_clicked = self.difficulty_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.game_active:
            self.show_difficulty_menu = not self.show_difficulty_menu #toggle the menu 
    
    def _check_difficulty_level_buttons(self, mouse_pos):
        """Handle clicks on Easy, medium and hard buttons."""
        if self.show_difficulty_menu and not self.game_active:
            if self.easy_difficulty_button.rect.collidepoint(mouse_pos):
                self._set_difficulty('easy')
                self.difficulty_button.button_color = (0,200,0) #green for easy
                self.difficulty_button._prep_msg('EASY') #change text to EASY
                self.show_difficulty_menu = False
            elif self.medium_difficulty_button.rect.collidepoint(mouse_pos):
                self._set_difficulty('medium')
                self.difficulty_button.button_color = (200,200,0) #yellow for medium
                self.difficulty_button._prep_msg('MEDIUM') #change text to medium
                self.show_difficulty_menu = False
            elif self.hard_difficulty_button.rect.collidepoint(mouse_pos):
                self._set_difficulty('hard')
                self.difficulty_button.button_color = (200,0,0) #red for hard 
                self.difficulty_button._prep_msg('HARD') #change text to EASY
                self.show_difficulty_menu = False
    
    def _set_difficulty(self, level):
        """Store the chosen difficulty."""
        self.chosen_difficulty = level  # Just store it, apply it later        
              

    def _start_game(self):
        #Reset the game statistics.
        self.stats.reset_stats()
        self.game_active = True

        #Get rid of any remaining bullets and aliens.
        self.bullets.empty()
        self.aliens.empty()

        #Create a new fleet and center the ship.
        self._create_fleet()
        self.ship.center_ship()

        #reset the game statistics
        self.stats.reset_stats()
        self.sb.prep_images()

        #Hide the mouse cursor
        pygame.mouse.set_visible(False)
    

    def _check_keydown_events(self, event):
        """respond to keypresses."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            self.stats.save_high_score()
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_p and not self.game_active:
            self._start_game()
                        
    def _check_keyup_events(self, event):
        """respond to key releases."""                            
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False 

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group."""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
    
    def _update_bullets(self):
        """Update position of bullets and get rid of old bullets."""
        #Update bullet positions.
        self.bullets.update()

        #Get rid of bullets that have disappeared.
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        """Respond to bullet-alien collisions."""
        #Remove any bullets and aliens that have collided
        collisions = pygame.sprite.groupcollide(self.bullets, 
                                                self.aliens, True, True)
        
        if collisions:   
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points * len(aliens)
            self.sb.prep_score()
            self.sb.check_high_score()

        if not self.aliens:
            self.start_new_level()
            
    def start_new_level(self):
        # Destroy existing bullets and create a new fleet
        self.bullets.empty()
        self._create_fleet()
        self.settings.increase_speed()
        #Increase level
        self.stats.level += 1
        self.sb.prep_level()

    def _update_aliens(self):
        """Check if the fleet is at an edge, then update positions. """
        self._check_fleet_edges()
        self.aliens.update()

        #monitor for alien-ship collisions.
        if pygame.sprite.spritecollideany(self.ship, self. aliens):
            self._ship_hit()
        
        #Look for aliens hitting the bottom of the screen. 
        self._check_aliens_bottom()

    def _check_aliens_bottom(self):
        """Check if any aliens have reached the bottom of the screen."""
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= self.settings.screen_height:
                #Treat this the same as if the ship got hit.
                self._ship_hit()
                break

    def _ship_hit(self):
        """Responds to the ship being hit by an alien."""
        
        if self.stats.ships_left > 0:
            #Decrement ships_left and update scoreboard.
            self.stats.ships_left -= 1
            self.sb.prep_ships()
            
            #Get rid of any remaining bullets and aliens.
            self.bullets.empty()
            self.aliens.empty()

            #Create a new fleet and center the ship.
            self._create_fleet()
            self.ship.center_ship()

            #Pause.
            sleep(0.5)
        
        else:
            self.game_active = False
            pygame.mouse.set_visible(True)

    def _update_screen(self):
        #update images on the screen, and flip to the new screen
        self.screen.fill(self.settings.bg_color)
        #self.stars.draw(self.screen)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.blitme()
        self.aliens.draw(self.screen)

        #Draw the score information.
        self.sb.show_score()

        #Draw the play button if the game is inactive.
        if not self.game_active:
            self.play_button.draw_button()
            self.difficulty_button.draw_button()

            #draw difficulty menu if menu showing
            if self.show_difficulty_menu:
                self.easy_difficulty_button.draw_button()
                self.medium_difficulty_button.draw_button()
                self.hard_difficulty_button.draw_button()

        pygame.display.flip()

    def _create_fleet(self):
        """Create the fleet of aliens."""
        #Create and alien and keep adding aliens until there's no room left
        #Spacing between aliens is one alien width.
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size

        current_x, current_y = alien_width, alien_height
        #outer loop(rows on y axis)
        while current_y < (self.settings.screen_height - 3 * alien_height):
           #inner loop: columns on x axis
            while current_x < (self.settings.screen_width - 2 * alien_width):
                self._create_alien(current_x, current_y)
                current_x += 2 * alien_width
            
        #Finished a row;reset x value and increment y value.
            current_x = alien_width
            current_y += 2 * alien_height

    def _create_alien(self, x_position, y_position):
        #Create an alien and place it in the fleet.
        new_alien = Alien(self)
        new_alien.x = x_position
        new_alien.rect.x = x_position
        new_alien.rect.y = y_position
        self.aliens.add(new_alien)
    
    def _check_fleet_edges(self):
        """Respond appropriately if any aliens have reached an edge."""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """Drop the entire fleet and change the fleet's direction."""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    #def _create_group_stars(self):
        #star = Star(self)
        #star_width, star_height = star.rect.size
        #current_x,current_y =star_width, star_height

        #outer loop(rows on y axis)
        #while current_y < (self.settings.screen_height - 3 * star_height):
            #inner loop:columns on x axis
            #while current_x < (self.settings.screen_width - 2* star_width):
                #self._create_star(current_x, current_y)
                #current_x += 2 * star_width

            #finished a row, reset x, increment y
            #current_x = star_width
            #current_y += 2*star_height
            
    #def _create_star(self, x_position, y_position):
        """create a star with a random position offset"""
        #new_star = Star(self)
        # add random offset to position
        #random_x = x_position + randint(-10, 10)
        #random_y = y_position + randint(-10, 10) 
        
        #new_star.x = random_x
        #new_star.rect.x = random_x
        #new_star.rect.y = random_y
        #self.stars.add(new_star)
        
        
if __name__ == '__main__':
    #make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()