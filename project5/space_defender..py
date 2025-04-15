import pygame
import random
import math
import os

# Initialize pygame
pygame.init()

# Create screen
screen_width = 900
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))

# Background
background = pygame.image.load('background.png') if os.path.exists('background.png') else pygame.Surface((screen_width, screen_height))
if background.get_size() != (screen_width, screen_height):
    background = pygame.transform.scale(background, (screen_width, screen_height))
if not os.path.exists('background.png'):
    # Create a starfield background if the image doesn't exist
    background.fill((0, 0, 20))  # Dark blue background
    for i in range(200):  # Add 200 stars
        color = random.choice([(255, 255, 255), (200, 200, 255), (255, 255, 200)])  # White or slight blue/yellow tint
        size = random.randint(1, 3)
        x = random.randint(0, screen_width)
        y = random.randint(0, screen_height)
        pygame.draw.circle(background, color, (x, y), size)

# Website Name (default until changed)
website_name = "Space Defender"

# Title and Icon
pygame.display.set_caption(website_name)
icon = pygame.Surface((32, 32))
icon.fill((0, 0, 0))
pygame.draw.polygon(icon, (0, 255, 0), [(16, 0), (32, 32), (0, 32)])
pygame.display.set_icon(icon)

# Player - Enhanced spaceship design with more realistic features
player_img = pygame.Surface((64, 64), pygame.SRCALPHA)
player_img.fill((0, 0, 0, 0))  # Transparent background

# Main body - sleeker fuselage
pygame.draw.polygon(player_img, (50, 150, 50), [(32, 5), (45, 40), (32, 55), (19, 40)])  # Dark green fuselage

# Wings - more aerodynamic with gradient coloring
wing_points = [(12, 30), (52, 30), (58, 36), (6, 36)]
pygame.draw.polygon(player_img, (100, 200, 100), wing_points)  # Light green wings
pygame.draw.polygon(player_img, (0, 100, 0), [(15, 30), (49, 30), (55, 36), (9, 36)], 1)  # Wing detail line

# Cockpit - glass canopy with highlight
pygame.draw.ellipse(player_img, (100, 200, 255), (24, 12, 16, 20))  # Blue cockpit glass
pygame.draw.ellipse(player_img, (200, 230, 255), (26, 14, 6, 10))  # Cockpit highlight/reflection

# Tail fin - taller and more defined
pygame.draw.polygon(player_img, (30, 130, 30), [(26, 40), (38, 40), (32, 58)])  # Main tail
pygame.draw.line(player_img, (0, 80, 0), (32, 40), (32, 56), 2)  # Tail detail

# Engines - add twin engines with exhaust
pygame.draw.rect(player_img, (100, 100, 100), (16, 38, 8, 14), 0, 2)  # Left engine
pygame.draw.rect(player_img, (100, 100, 100), (40, 38, 8, 14), 0, 2)  # Right engine

# Engine exhaust/thrusters
pygame.draw.polygon(player_img, (200, 150, 50), [(18, 52), (22, 52), (20, 58)])  # Left exhaust flame
pygame.draw.polygon(player_img, (200, 150, 50), [(42, 52), (46, 52), (44, 58)])  # Right exhaust flame
pygame.draw.polygon(player_img, (255, 200, 50), [(19, 52), (21, 52), (20, 55)])  # Left inner flame
pygame.draw.polygon(player_img, (255, 200, 50), [(43, 52), (45, 52), (44, 55)])  # Right inner flame

# Nose cone with highlight
pygame.draw.polygon(player_img, (70, 170, 70), [(29, 5), (35, 5), (32, 0)])
pygame.draw.line(player_img, (150, 230, 150), (30, 5), (34, 5), 2)  # Nose highlight

# Additional detail lines on fuselage
pygame.draw.line(player_img, (0, 80, 0), (25, 15), (39, 15), 1)  # Upper detail line
pygame.draw.line(player_img, (0, 80, 0), (22, 25), (42, 25), 1)  # Mid detail line

# Weapon mounts on wings
pygame.draw.rect(player_img, (70, 70, 70), (12, 32, 4, 8), 0, 1)  # Left weapon
pygame.draw.rect(player_img, (70, 70, 70), (48, 32, 4, 8), 0, 1)  # Right weapon

player_x = 370
player_y = 480
player_x_change = 0
player_speed = 4.5  # Increased from 3.0 to 4.5

# Mouse cursor - keep visible
pygame.mouse.set_visible(True)

# Enemy
enemy_img = []
enemy_x = []
enemy_y = []
enemy_x_change = []
enemy_y_change = []
num_of_enemies = 6

for i in range(num_of_enemies):
    # Create enemy shape (red UFO)
    enemy = pygame.Surface((64, 64), pygame.SRCALPHA)
    enemy.fill((0, 0, 0, 0))  # Transparent background
    pygame.draw.ellipse(enemy, (255, 0, 0), (8, 24, 48, 16))  # UFO body
    pygame.draw.ellipse(enemy, (200, 200, 200), (16, 16, 32, 16))  # UFO cockpit
    enemy_img.append(enemy)
    
    enemy_x.append(random.randint(0, 736))
    enemy_y.append(random.randint(50, 150))
    enemy_x_change.append(3.5)  # Increased from 2.5 to 3.5
    enemy_y_change.append(40)

# Boss Enemy - Scarier Monster design
boss_img = pygame.Surface((128, 128), pygame.SRCALPHA)
boss_img.fill((0, 0, 0, 0))  # Transparent background

# Monster body - dark red base (more threatening)
pygame.draw.ellipse(boss_img, (150, 0, 0), (24, 32, 80, 64))  # Main body

# Monster head - blood red
pygame.draw.circle(boss_img, (200, 0, 0), (64, 40), 32)  # Head

# Monster eyes - glowing intense green
pygame.draw.circle(boss_img, (0, 255, 0), (50, 32), 12)  # Left eye (larger)
pygame.draw.circle(boss_img, (0, 255, 0), (78, 32), 12)  # Right eye (larger)
pygame.draw.circle(boss_img, (255, 255, 0), (50, 32), 4)  # Left pupil
pygame.draw.circle(boss_img, (255, 255, 0), (78, 32), 4)  # Right pupil

# Monster teeth - sharper and more menacing
for i in range(7):  # More teeth
    x_pos = 36 + i * 10
    pygame.draw.polygon(boss_img, (255, 255, 255), [(x_pos, 64), (x_pos+5, 84), (x_pos+10, 64)])  # Longer teeth
    pygame.draw.polygon(boss_img, (255, 150, 150), [(x_pos+2, 78), (x_pos+5, 84), (x_pos+8, 78)])  # Bloody tips

# Monster tentacles/arms - more aggressive looking
pygame.draw.polygon(boss_img, (150, 0, 0), [(30, 60), (5, 100), (20, 110), (40, 70)])  # Left arm - longer
pygame.draw.polygon(boss_img, (150, 0, 0), [(98, 60), (123, 100), (108, 110), (88, 70)])  # Right arm - longer

# Monster additional details - spikes on back (more threatening)
for i in range(5):  # More spikes
    x_pos = 34 + i * 15
    pygame.draw.polygon(boss_img, (255, 0, 255), [(x_pos, 32), (x_pos+8, 5), (x_pos+16, 32)])  # Taller spikes

# Create boss projectile image
boss_projectile_img = pygame.Surface((24, 24), pygame.SRCALPHA)
boss_projectile_img.fill((0, 0, 0, 0))
pygame.draw.circle(boss_projectile_img, (255, 0, 0), (12, 12), 8)  # Red center
pygame.draw.circle(boss_projectile_img, (255, 100, 0), (12, 12), 12, 3)  # Orange outer ring

boss_active = False
boss_x = 336  # Center of screen minus half boss width
boss_y = 100
boss_x_change = 4.5  # Increased from 3.5 to 4.5
boss_health = 15  # Takes 15 hits to defeat
boss_threshold = 75  # Boss appears after 75 points (changed from 100)
next_boss_score = boss_threshold  # Score threshold for next boss
boss_projectiles = []  # List to store boss attacks
boss_attack_cooldown = 60  # Frames between boss attacks
boss_attack_timer = 0

# Bullet
bullet_img = pygame.Surface((16, 16), pygame.SRCALPHA)
bullet_img.fill((0, 0, 0, 0))  # Transparent background
pygame.draw.rect(bullet_img, (0, 255, 255), (6, 0, 4, 16))  # Cyan bullet

# Rapid Fire System
bullets = []  # List to store multiple bullets
max_bullets = 5  # Maximum bullets on screen
bullet_cooldown = 15  # Frames between shots
bullet_timer = 0  # Cooldown timer
bullet_speed = 10  # Speed of bullets

# Score
score_value = 0
high_score = 0  # Initialize high score
font = pygame.font.SysFont('comicsans', 32)
text_x = 10
text_y = 10

# Load high score from file if it exists
def load_high_score():
    try:
        with open('highscore.txt', 'r') as file:
            return int(file.read())
    except:
        return 0

# Save high score to file
def save_high_score(score):
    with open('highscore.txt', 'w') as file:
        file.write(str(score))

# Load high score at start
high_score = load_high_score()

# Game Over Text
game_over_font = pygame.font.SysFont('comicsans', 64)

# Particles
particles = []

# Hamburger menu
menu_font = pygame.font.SysFont('comicsans', 32)
hamburger_icon = pygame.Surface((40, 40), pygame.SRCALPHA)
# Create hamburger icon (three lines)
pygame.draw.rect(hamburger_icon, (255, 255, 255), (5, 8, 30, 4))
pygame.draw.rect(hamburger_icon, (255, 255, 255), (5, 18, 30, 4))
pygame.draw.rect(hamburger_icon, (255, 255, 255), (5, 28, 30, 4))

# Menu buttons
class Button:
    def __init__(self, x, y, width, height, text, color, hover_color):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = color
        self.hover_color = hover_color
        self.is_hovered = False
        
    def draw(self, surface):
        color = self.hover_color if self.is_hovered else self.color
        pygame.draw.rect(surface, color, self.rect, border_radius=5)
        pygame.draw.rect(surface, (255, 255, 255), self.rect, 2, border_radius=5)  # Border
        
        text_surface = menu_font.render(self.text, True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=self.rect.center)
        surface.blit(text_surface, text_rect)
    
    def check_hover(self, pos):
        self.is_hovered = self.rect.collidepoint(pos)
        return self.is_hovered
    
    def is_clicked(self, pos, click):
        return click and self.is_hovered

# Create menu buttons
resume_button = Button(300, 200, 200, 50, "Resume", (50, 100, 50), (100, 200, 100))
restart_button = Button(300, 270, 200, 50, "Restart", (100, 50, 50), (200, 100, 100))
quit_button = Button(300, 340, 200, 50, "Quit", (80, 80, 100), (130, 130, 200))
# website_button = Button(300, 410, 200, 50, "Change Website", (50, 50, 100), (100, 100, 200))

# FPS control
clock = pygame.time.Clock()
FPS = 60

def show_score(x, y):
    score = font.render("Score: " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))
    
    # Display high score
    high = font.render("High Score: " + str(high_score), True, (255, 255, 255))
    screen.blit(high, (x, y + 40))

def show_boss_health(health, max_health=15):
    # Draw boss health bar when boss is active
    if boss_active:
        bar_width = 200
        bar_height = 20
        fill_width = (health / max_health) * bar_width
        
        # Draw background bar (red)
        pygame.draw.rect(screen, (200, 0, 0), (screen_width/2 - bar_width/2, 20, bar_width, bar_height))
        
        # Draw filled portion (green)
        pygame.draw.rect(screen, (0, 200, 0), (screen_width/2 - bar_width/2, 20, fill_width, bar_height))
        
        # Draw border
        pygame.draw.rect(screen, (255, 255, 255), (screen_width/2 - bar_width/2, 20, bar_width, bar_height), 2)
        
        # Boss label
        boss_text = font.render("BOSS", True, (255, 255, 255))
        screen.blit(boss_text, (screen_width/2 - boss_text.get_width()/2, 45))

def game_over_text():
    global high_score, score_value
    
    # Update high score if current score is higher
    if score_value > high_score:
        high_score = score_value
        save_high_score(high_score)
        new_high_score = font.render("NEW HIGH SCORE!", True, (255, 255, 0))
        screen.blit(new_high_score, (300, 400))
    
    over_text = game_over_font.render("GAME OVER", True, (255, 0, 0))
    restart_text = font.render("Press R to Restart", True, (255, 255, 255))
    screen.blit(over_text, (200, 250))
    screen.blit(restart_text, (300, 350))

def player(x, y):
    screen.blit(player_img, (x, y))

def enemy(x, y, i):
    screen.blit(enemy_img[i], (x, y))

def boss(x, y):
    screen.blit(boss_img, (x, y))

def fire_bullet(x, y):
    # Add a new bullet to the bullets list
    bullets.append({
        'x': x + 24,  # Center of player
        'y': y + 10,  # Top of player
    })

def boss_fire_projectile(x, y):
    # Add a new projectile from the boss
    boss_projectiles.append({
        'x': x + 64,  # Center of boss
        'y': y + 100,  # Bottom of boss
        'dx': random.uniform(-2, 2),  # Random horizontal movement
        'speed': random.uniform(4, 6)  # Random speed between 4-6
    })

def is_collision(enemy_x, enemy_y, bullet_x, bullet_y, size=64):
    # Size parameter adjusts collision detection for different sized enemies
    distance = math.sqrt((enemy_x + size/2 - bullet_x) ** 2 + (enemy_y + size/2 - bullet_y) ** 2)
    return distance < size/2.5  # Adjusted threshold based on size

def create_explosion(x, y, size=1.0):
    # Size parameter allows for bigger explosions for boss
    num_particles = int(20 * size)  # More particles for bigger explosion
    
    for _ in range(num_particles):
        particles.append({
            'x': x,  # Center of enemy
            'y': y,
            'size': random.randint(2, 5) * size,
            'color': (255, random.randint(100, 200), 0),  # Orange-red
            'velocity': [random.uniform(-2, 2) * size, random.uniform(-2, 2) * size],
            'lifetime': random.randint(20, 40)
        })

def update_particles():
    i = 0
    while i < len(particles):
        particle = particles[i]
        particle['x'] += particle['velocity'][0]
        particle['y'] += particle['velocity'][1]
        particle['lifetime'] -= 1
        
        if particle['lifetime'] <= 0:
            particles.pop(i)
        else:
            pygame.draw.circle(screen, particle['color'], 
                             (int(particle['x']), int(particle['y'])), 
                             int(particle['size']))
            i += 1

def draw_hamburger_menu():
    screen.blit(hamburger_icon, (750, 10))  # Top right corner

def check_boss_spawn():
    global boss_active, boss_health, next_boss_score
    
    # Check if it's time to spawn a boss
    if score_value >= next_boss_score and not boss_active:
        boss_active = True
        boss_health = 15  # Reset boss health

def show_menu():
    # Semi-transparent overlay
    overlay = pygame.Surface((screen_width, screen_height), pygame.SRCALPHA)
    overlay.fill((0, 0, 0, 200))
    screen.blit(overlay, (0, 0))
    
    # Draw menu title
    title = menu_font.render("MENU", True, (255, 255, 255))
    screen.blit(title, (screen_width/2 - title.get_width()/2, 130))
    
    # Draw buttons
    resume_button.draw(screen)
    restart_button.draw(screen)
    quit_button.draw(screen)
    # website_button.draw(screen)
    
    pygame.display.update()

def reset_game():
    global score_value, player_x, player_y, boss_active, boss_health, next_boss_score
    score_value = 0
    player_x = 370
    player_y = 480
    boss_active = False
    boss_health = 15
    next_boss_score = boss_threshold
    bullets.clear()
    particles.clear()
    boss_projectiles.clear()
    
    # Reset enemies
    for i in range(num_of_enemies):
        enemy_x[i] = random.randint(0, 736)
        enemy_y[i] = random.randint(50, 150)

# Function to change website name using text input
def change_website_name():
    global website_name
    
    # Font for text input
    input_font = pygame.font.SysFont('comicsans', 36)
    
    # Semi-transparent overlay
    overlay = pygame.Surface((screen_width, screen_height), pygame.SRCALPHA)
    overlay.fill((0, 0, 0, 200))
    screen.blit(overlay, (0, 0))
    
    # Prompt text
    prompt = input_font.render("Enter Website Name:", True, (255, 255, 255))
    screen.blit(prompt, (screen_width/2 - prompt.get_width()/2, 200))
    
    # Input box
    input_box = pygame.Rect(250, 250, 500, 50)
    pygame.draw.rect(screen, (50, 50, 50), input_box)
    pygame.draw.rect(screen, (255, 255, 255), input_box, 2)
    
    # Instructions
    instructions = font.render("Enter name and press ENTER, or ESC to cancel", True, (200, 200, 200))
    screen.blit(instructions, (screen_width/2 - instructions.get_width()/2, 320))
    
    pygame.display.update()
# Display controls at start
def show_controls():
    # Semi-transparent overlay
    overlay = pygame.Surface((screen_width, screen_height), pygame.SRCALPHA)
    overlay.fill((0, 0, 0, 200))
    screen.blit(overlay, (0, 0))
    
    title_font = pygame.font.SysFont('comicsans', 48)
    title = title_font.render(website_name, True, (0, 255, 0))
    screen.blit(title, (screen_width/2 - title.get_width()/2, 100))
    
    controls_font = pygame.font.SysFont('comicsans', 32)
    controls = [
        "Controls:",
        "Left/Right Arrow Keys - Move Ship",
        "Space Bar - Fire Weapon (hold for rapid fire)",
        "ESC or Click Hamburger Menu - Pause Game",
        "",
        "BEWARE: Every 75 points, the Monster Boss appears!",
        "The boss will attack you with deadly projectiles!",
        "",
        "High Score: " + str(high_score),
        "",
        "Press Any Key to Start"
    ]
    
    y_pos = 200
    for line in controls:
        rendered = controls_font.render(line, True, (255, 255, 255))
        screen.blit(rendered, (screen_width/2 - rendered.get_width()/2, y_pos))
        y_pos += 40
    
    pygame.display.update()
    
    # Wait for a key press
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                waiting = False

# Game states
show_intro = True
game_active = False
game_paused = False
running = True
space_pressed = False

# Game Loop
while running:
    # Limit FPS
    clock.tick(FPS)
    
    # Show intro screen with controls
    if show_intro:
        show_controls()
        show_intro = False
        game_active = True
    
    # RGB background
    screen.blit(background, (0, 0))
    
    mouse_pos = pygame.mouse.get_pos()
    mouse_click = False
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # Save high score before quitting
            if score_value > high_score:
                high_score = score_value
                save_high_score(high_score)
            running = False
            
        # Mouse events
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_click = True
            # Check if hamburger menu is clicked
            if pygame.Rect(750, 10, 40, 40).collidepoint(mouse_pos) and not game_paused and game_active:
                game_paused = True
                
        # Key controls
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_x_change = -player_speed
            if event.key == pygame.K_RIGHT:
                player_x_change = player_speed
            if event.key == pygame.K_SPACE:
                space_pressed = True
            if event.key == pygame.K_r and not game_active:
                game_active = True
                reset_game()
            if event.key == pygame.K_ESCAPE:
                if game_paused:
                    game_paused = False
                elif game_active:
                    game_paused = True
                
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_x_change = 0
            if event.key == pygame.K_SPACE:
                space_pressed = False
    
    # Check for menu interactions when paused
    if game_paused:
        # Check button hover
        resume_button.check_hover(mouse_pos)
        restart_button.check_hover(mouse_pos)
        quit_button.check_hover(mouse_pos)
        # website_button.check_hover(mouse_pos)
        
        # Check button clicks
        if resume_button.is_clicked(mouse_pos, mouse_click):
            game_paused = False
        elif restart_button.is_clicked(mouse_pos, mouse_click):
            game_paused = False
            reset_game()
        elif quit_button.is_clicked(mouse_pos, mouse_click):
            # Save high score before quitting
            if score_value > high_score:
                high_score = score_value
                save_high_score(high_score)
            running = False
       
        
        show_menu()
        continue  # Skip the rest of the loop when paused
    
    if game_active:
        # Check if boss should spawn
        check_boss_spawn()
        
        # Player movement
        player_x += player_x_change
        
        # Boundaries
        if player_x <= 0:
            player_x = 0
        elif player_x >= 736:  # 800 - 64 (player width)
            player_x = 736
        
        # Rapid fire system
        if space_pressed and bullet_timer <= 0 and len(bullets) < max_bullets:
            fire_bullet(player_x, player_y)
            bullet_timer = bullet_cooldown
        
        if bullet_timer > 0:
            bullet_timer -= 1
        
        # Update bullets
        i = 0
        while i < len(bullets):
            bullet = bullets[i]
            bullet['y'] -= bullet_speed
            
            # Remove bullet if it goes off screen
            if bullet['y'] < 0:
                bullets.pop(i)
            else:
                # Draw bullet
                screen.blit(bullet_img, (bullet['x'], bullet['y']))
                i += 1
        
        # Boss logic
        if boss_active:
            # Boss movement (side to side and slightly up and down)
            boss_x += boss_x_change
            
            # Boss boundaries
            if boss_x <= 0:
                boss_x_change = abs(boss_x_change)  # Move right
            elif boss_x >= screen_width - 128:  # Screen width minus boss width
                boss_x_change = -abs(boss_x_change)  # Move left
            
            # Occasionally change Y position to make it harder to hit
            if random.random() < 0.01:  # 1% chance each frame
                boss_y = random.randint(50, 150)
            
            # Boss attacks
            boss_attack_timer -= 1
            if boss_attack_timer <= 0:
                boss_fire_projectile(boss_x, boss_y)
                boss_attack_timer = boss_attack_cooldown
                
                # Add some randomness to attack frequency
                boss_attack_cooldown = random.randint(40, 80)
            
            # Update boss projectiles
            i = 0
            while i < len(boss_projectiles):
                proj = boss_projectiles[i]
                proj['y'] += proj['speed']
                proj['x'] += proj['dx']  # Move horizontally as well
                
                # Check if hit player
                player_hit = math.sqrt((player_x + 32 - proj['x']) ** 2 + (player_y + 32 - proj['y']) ** 2) < 40
                if player_hit:
                    # Player is hit by boss projectile
                    boss_projectiles.pop(i)
                    create_explosion(player_x + 32, player_y + 32, 1.5)
                    game_active = False  # Game over
                    break
                
                # Remove projectile if it goes off screen
                if proj['y'] > screen_height or proj['x'] < 0 or proj['x'] > screen_width:
                   boss_projectiles.pop(i)
                else:
                    # Draw boss projectile
                    screen.blit(boss_projectile_img, (proj['x'] - 12, proj['y'] - 12))
                    i += 1
            
            # Check collision with bullets
            i = 0
            while i < len(bullets):
                bullet = bullets[i]
                if is_collision(boss_x, boss_y, bullet['x'], bullet['y'], 128):  # Use boss size
                    bullets.pop(i)  # Remove bullet
                    boss_health -= 1
                    create_explosion(bullet['x'], bullet['y'], 0.5)  # Small hit effect
                    
                    if boss_health <= 0:
                        # Boss defeated
                        create_explosion(boss_x + 64, boss_y + 64, 3.0)  # Big explosion
                        boss_active = False
                        score_value += 25  # Extra points for defeating boss (increased from 20)
                        next_boss_score = score_value + boss_threshold  # Set next boss threshold
                        boss_projectiles.clear()  # Clear all projectiles when boss dies
                    break
                i += 1
            
            # Draw boss
            boss(boss_x, boss_y)
            
            # Show boss health
            show_boss_health(boss_health)
            
        # Enemy movement
        for i in range(num_of_enemies):
            # Skip enemy logic if boss is active
            if boss_active:
                continue
                
            # Game Over condition
            if enemy_y[i] > 440:
                for j in range(num_of_enemies):
                    enemy_y[j] = 2000  # Move enemies off screen
                game_active = False
                break
                
            enemy_x[i] += enemy_x_change[i]
            
            # Boundary check and move down
            if enemy_x[i] <= 0:
                enemy_x_change[i] = 3.5  # Keep increased speed
                enemy_y[i] += enemy_y_change[i]
            elif enemy_x[i] >= 736:
                enemy_x_change[i] = -3.5  # Keep increased speed but negative
                enemy_y[i] += enemy_y_change[i]
            
            # Collision detection with all bullets
            j = 0
            while j < len(bullets):
                bullet = bullets[j]
                collision = is_collision(enemy_x[i], enemy_y[i], bullet['x'], bullet['y'])
                if collision:
                    bullets.pop(j)  # Remove bullet
                    score_value += 1
                    create_explosion(enemy_x[i] + 32, enemy_y[i] + 32)  # Center explosion
                    enemy_x[i] = random.randint(0, 736)
                    enemy_y[i] = random.randint(50, 150)
                    break  # Skip to next enemy after collision
                j += 1
                
            # Draw enemy
            enemy(enemy_x[i], enemy_y[i], i)
        
        # Game over condition for boss (if it reaches bottom)
        if boss_active and boss_y > 400:
            boss_active = False
            game_active = False
            
        # Draw player
        player(player_x, player_y)
        
        # Draw hamburger menu icon
        draw_hamburger_menu()
    
    else:
        game_over_text()
    
    # Update particles
    update_particles()
    
    # Show score
    show_score(text_x, text_y)
    
    # Update display
    pygame.display.update()

# Save high score before quitting
if score_value > high_score:
    save_high_score(score_value)

pygame.quit()