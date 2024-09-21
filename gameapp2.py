import pygame
import sys

# Initialize Pygame
pygame.init()

# Game Window Dimensions
WIDTH, HEIGHT = 1000, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Canvas Invaders")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 252, 102)
greyish_blue = (138,144,226)

#images
# Load Background Image
background_image = pygame.image.load("bg2.jpg")  # Replace with your image file path
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))  # Scale the image to fit the screen
score_board_image = pygame.image.load("scoreboard.png")
score_board_image = pygame.transform.scale(score_board_image, (WIDTH, HEIGHT)) 
planet1 = pygame.image.load("1.png")
planet1 = pygame.transform.scale(planet1, (130, 130)) 
planet2 = pygame.image.load("4.png")
planet2 = pygame.transform.scale(planet2, (140, 160)) 
planet3 = pygame.image.load("3.png")
planet3 = pygame.transform.scale(planet3, (130, 130)) 
planet4 = pygame.image.load("2.png")
planet4 = pygame.transform.scale(planet4, (130, 130)) 
hammer = pygame.image.load("hammer.png")
hammer = pygame.transform.scale(hammer, (40, 40))
my_castle = pygame.image.load("my_castle.png")
my_castle = pygame.transform.scale(my_castle, (50, 50))
shop_npc = pygame.image.load("shop_npc.png")
shop_npc = pygame.transform.scale(shop_npc, (330, 430))
shop_upgrade = pygame.image.load("shop_upgrade.png")
shop_upgrade = pygame.transform.scale(shop_upgrade, (250, 250))
shop_repair = pygame.image.load("shop_repair.png")
shop_repair = pygame.transform.scale(shop_repair, (250, 250))
ammo_icon = pygame.image.load("ammo.png")
ammo_icon = pygame.transform.scale(ammo_icon, (40, 40))
ammo_image = pygame.image.load("ammo.png")
ammo_image = pygame.transform.scale(ammo_image, (15, 30))
shooter_image = pygame.image.load("character_red.png") 
shooter_image = pygame.transform.scale(shooter_image, (80, 80)) 
alien_image = pygame.image.load("alien.png")
alien_image = pygame.transform.scale(alien_image, (60, 60))
myCastles_image = pygame.image.load("myCastles.jpeg")
myCastles_image = pygame.transform.scale(myCastles_image, (1000, 600))

# Font
font = pygame.font.Font("PixelifySans-Regular.ttf", 30)
small_font = pygame.font.Font("PixelifySans-Regular.ttf", 20)
score_board_font = pygame.font.Font("PixelifySans-Regular.ttf", 15)

# Game Variables
player_health = 100
player_score = 0
ammo = 50
castle_level = 1

# Shooting display variables
castle_health = 100
bullets = []
alien_bullets = []
aliens = []  # List to hold alien properties

# Player (shooter) variables
shooter_rect = pygame.Rect(WIDTH // 2 - 30, HEIGHT - 60, 60, 30)  # Gun dimensions
alien_direction = 1  # 1 for right, -1 for left
alien_speed = 2

# Opponent data for each student with initial scores
opponents = {
    "Course 1": {"students": ["Student A", "Student B", "Student C"], "scores": [100, 80, 60]},
    "Course 2": {"students": ["Student D", "Student E", "Student F"], "scores": [70, 90, 50]},
    "Course 3": {"students": ["Student G", "Student H", "Student I"], "scores": [60, 40, 30]},
    "Course 4": {"students": ["Student J", "Student K", "Student L"], "scores": [20, 10, 0]}
}

# Selected course and student
selected_course = None
selected_student = None

# Function to create aliens
def create_aliens(num_aliens):
    for i in range(num_aliens):
        alien_rect = pygame.Rect(100 + i * 150, 150, 60, 60)  # Spread aliens across the top
        aliens.append({'rect': alien_rect, 'health': 50})  # Each alien has its own health

# Function to draw text
def draw_text(text, font, color, x, y):
    screen_text = font.render(text, True, color)
    screen.blit(screen_text, (x, y))

# Function to draw the course selection screen
def draw_course_selection():
    screen.blit(background_image, (0, 0))
    draw_text("Select Course:", font, WHITE, WIDTH // 2 - 130, HEIGHT // 2 -120)

    # Starting position and spacing for planets
    start_x = WIDTH // 2 - 330  # Adjusted to center planets horizontally
    start_y = 200  # Align planets at a consistent height
    planet_spacing = 190  # Consistent spacing between planets

    
    course_buttons = list(opponents.keys())
    for i, course in enumerate(course_buttons):
        button_rect = pygame.Rect(WIDTH - 865 + (i * (160 + 30)), HEIGHT // 2-70, 160, 160)
        circle_center = button_rect.center  # Get the center of the button rectangle
        circle_radius = 80
        transparent_surface = pygame.Surface((circle_radius*2, circle_radius*2), pygame.SRCALPHA)  # Create surface with alpha
        pygame.draw.circle(transparent_surface, (0, 0, 255, 100), circle_center, circle_radius)
        if i == 0:
            screen.blit(planet1, button_rect.topleft)
        elif i ==1:
            screen.blit(planet2, button_rect.topleft)
        elif i ==2:
            screen.blit(planet3, button_rect.topleft)
        elif i==3:
            screen.blit(planet4, button_rect.topleft)

        draw_text(course, font, WHITE, button_rect.x + 7, button_rect.y + 170)
        screen.blit(hammer,(930,30))
        draw_text("SHOP", small_font, WHITE, 930, 80)
        screen.blit(my_castle,(840,20))
        draw_text("CASTLES", small_font, WHITE, 830, 80)



# Function to draw shop page
def draw_shop_page():
    screen.blit(background_image, (0, 0))
    screen.blit(shop_npc, (50,150))
    draw_text("Select Option:", font, WHITE, WIDTH//2, 120)
    button_rect = pygame.Rect(20,20, 120, 40)
    pygame.draw.rect(screen, greyish_blue, button_rect)
    draw_text("<< BACK", font, WHITE, 20, 20)
    screen.blit(shop_upgrade, (400,200))
    draw_text("UPGRADE", font, WHITE, 470, 450)
    screen.blit(ammo_icon,(470,500))
    draw_text("-20", font, WHITE, 510, 510)
    screen.blit(shop_repair, (700,200))
    screen.blit(ammo_icon,(770,500))
    draw_text("-10", font, WHITE, 810, 510)
    draw_text("REPAIR", font, WHITE, 770, 450)
    draw_text("Your ammo: "+str(ammo), font, WHITE, 780,20)
    screen.blit(ammo_icon,(730,15))

# Function to draw the dashboard after selecting a course
def draw_dashboard():
    screen.blit(background_image, (0, 0))
    draw_text(f"Selected Course: {selected_course}", font, WHITE, 20, 20)

    # Position for the "Select a Student to Attack!" text
    draw_text("Select Student To Attack! :", score_board_font, WHITE, WIDTH // 2 - 150, 100)

    # Back Button
    mouse_pos = pygame.mouse.get_pos()
    back_button_rect = pygame.Rect(20, 540, 120, 40)  # Position for the back button
    pygame.draw.rect(screen, greyish_blue, back_button_rect)
    draw_text("<< BACK", font, WHITE, back_button_rect.x + 5, back_button_rect.y + 5)

    # Get students and their scores, then sort them
    students_data = opponents[selected_course]
    students = students_data["students"]
    scores = students_data["scores"]
    
    # Create a list of tuples (student, score) and sort by score
    #student_scores = sorted(enumerate(zip(students, scores)), key=lambda x: x[1][1], reverse=True)
    student_scores = sorted(zip(students, scores), key=lambda x: x[1], reverse=True)

    
    # Starting position for the score list
    start_y = 163  
    score_spacing = 46 

    # Loop to draw each student's score
    for i, (student, score) in enumerate(student_scores):
        # Define the button rect for the student score
        button_rect = pygame.Rect(WIDTH // 2 - 200, start_y + (i * score_spacing), 400, 40)
        # Draw the rectangle outline with no fill
        pygame.draw.rect(screen, BLACK, button_rect, 2)
        # Ensure the text inside the button is properly aligned

        draw_text(f"{student}            {score} points", score_board_font, WHITE, button_rect.x + 20, button_rect.y + 10)
        # Check for hover effect and change color accordingly
        if button_rect.collidepoint(mouse_pos):
            pygame.draw.rect(screen, RED, button_rect, 2)  # Highlight on hover
            # Check if the student is clicked
            if pygame.mouse.get_pressed()[0]:  # If left mouse button is clicked
                print(f"Selected Student: {student}")

# Update shooter rect to match the new shooter size
shooter_rect = pygame.Rect(WIDTH // 2 - 60, HEIGHT - 120, 80, 80)

def draw_castles_page():
    screen.blit(myCastles_image, (0, 0))  # Display the castle image

    button_back_rect = pygame.Rect(20, 540, 120, 40)
    pygame.draw.rect(screen, greyish_blue, button_back_rect)
    draw_text("<< BACK", font, WHITE, 20, 540)

def getCastleImage(castle_health,castle_level):
    castle_image = None 

    if castle_level == 1:
        if castle_health >= 80:
            castle_image = pygame.image.load('castle/castle11.png')
        elif 60 <= castle_health < 80:
            castle_image = pygame.image.load('castle/castle12.png')
        elif 40 <= castle_health < 60:
            castle_image = pygame.image.load('castle/castle13.png')
        elif 20 <= castle_health < 40:
            castle_image = pygame.image.load('castle/castle14.png')
        elif castle_health <= 20:
            castle_image = pygame.image.load('castle/castle15.png')

    elif castle_level == 2:
        if castle_health >= 80:
            castle_image = pygame.image.load('castle/castle21.png')
        elif 60 <= castle_health < 80:
            castle_image = pygame.image.load('castle/castle22.png')
        elif 40 <= castle_health < 60:
            castle_image = pygame.image.load('castle/castle23.png')
        elif 20 <= castle_health < 40:
            castle_image = pygame.image.load('castle/castle24.png')
        elif castle_health <= 20:
            castle_image = pygame.image.load('castle/castle25.png')

    elif castle_level == 3:
        if castle_health >= 80:
            castle_image = pygame.image.load('castle/castle31.png')
        elif 60 <= castle_health < 80:
            castle_image = pygame.image.load('castle/castle32.png')
        elif 40 <= castle_health < 60:
            castle_image = pygame.image.load('castle/castle33.png')
        elif 20 <= castle_health < 40:
            castle_image = pygame.image.load('castle/castle34.png')
        elif castle_health <= 20:
            castle_image = pygame.image.load('castle/castle35.png')

    return castle_image


def draw_castle():
    castle_image = getCastleImage(castle_health, castle_level)  # Call the function to get the image
    castle_image = pygame.transform.scale(castle_image, (200, 200))  # Scale the image if needed

    # Position for the castle image
    castle_position = (400,-20)  # Adjust the position as necessary
    screen.blit(castle_image, castle_position)

# Function to handle shooting display
def draw_shooting_display():
    screen.blit(background_image, (0, 0))
    
    draw_text(f"Attacking {selected_student}'s Castle!", small_font, WHITE, 10, 10)
    draw_text(f"Castle Health: {castle_health}", small_font, WHITE, 10, 50)
    draw_text(f"Player Health: {player_health}", small_font, WHITE, 10, 90)

    # Display ammo left
    draw_text(f"x {ammo}", font, WHITE, WIDTH - 100, 20)
    screen.blit(ammo_image, (WIDTH - 120, 20)) 

    # Draw the shooter
    screen.blit(shooter_image, (shooter_rect.x, shooter_rect.y))
    
    # Draw the aliens
    for alien in aliens:
        screen.blit(alien_image, (alien['rect'].x, alien['rect'].y))
    
    # Draw bullets
    for bullet in bullets:
        screen.blit(ammo_image, (bullet.x, bullet.y))

    # Draw alien bullets
    for alien_bullet in alien_bullets:
        pygame.draw.rect(screen, WHITE, alien_bullet)

    draw_castle()

#--------
# Function to handle shooting
def shoot_bullet():
    global ammo
    if ammo > 0:
        bullet = pygame.Rect(shooter_rect.centerx, shooter_rect.top, 5, 15)
        bullets.append(bullet)
        ammo -= 1
    elif ammo == 0:
        in_shooting_display = False
        in_course_selection = True

# Function to attack the castle
def attack_castle():
    global castle_health, player_score
    for bullet in bullets[:]:
        bullet.y -= 5  # Move bullet upwards
        if bullet.y < 0:  # Remove bullet if off-screen
            bullets.remove(bullet)
        else:
            for alien in aliens:
                if bullet.colliderect(alien['rect']):
                    alien['health'] -= 50  # Damage the alien
                    bullets.remove(bullet)  # Remove bullet on hit
                    if alien['health'] <= 0:
                        aliens.remove(alien)  # Remove dead alien
                        player_score += 10  # Increase score
                    break

# Function for alien shooting
def alien_shoot():
    for alien in aliens:
        alien_bullet = pygame.Rect(alien['rect'].centerx, alien['rect'].bottom, 5, 15)
        alien_bullets.append(alien_bullet)

# Function to move alien bullets and check for collisions
def move_alien_bullets():
    global player_health

    shooter_hitbox = pygame.Rect(
        shooter_rect.x + 10,  # Shrink hitbox from the left
        shooter_rect.y + 10,  # Shrink hitbox from the top
        shooter_rect.width - 20,  # Shrink width
        shooter_rect.height - 20  # Shrink height
    )

    for bullet in alien_bullets[:]:
        bullet.y += 5  # Move the bullet downwards
        if bullet.y > HEIGHT:  # Remove bullet if it goes off-screen
            alien_bullets.remove(bullet)
        elif bullet.colliderect(shooter_rect):  # Check if it hits the player
            if player_health > 0:
                player_health -= 100  # Decrease player health
                player_health = max(0, player_health)
            alien_bullets.remove(bullet)  # Remove bullet on hit
            print(f"Player hit! Health: {player_health}")

# Function to attack the castle
def attack_castle():
    global castle_health, player_score, castle_level
    for bullet in bullets[:]:
        bullet.y -= 5  # Move bullet upwards
        if bullet.y < 0:  # Remove bullet if off-screen
            bullets.remove(bullet)
        else:
            for alien in aliens:
                if bullet.colliderect(alien['rect']):
                    alien['health'] -= 50  # Damage the alien
                    bullets.remove(bullet)  # Remove bullet on hit
                    if alien['health'] <= 0:
                        aliens.remove(alien)  # Remove dead alien
                        player_score += 10  # Increase score
                    break
            castle_image_rect = pygame.Rect(460,100, 95, 1)
           
            if bullet.colliderect(castle_image_rect) and castle_health > 0:
                castle_health -= 5

# Function to move aliens
def move_aliens():
    global alien_direction
    for alien in aliens:
        alien['rect'].x += alien_direction * alien_speed
        # Reverse direction if the alien hits the screen edges
        if alien['rect'].left < 0 or alien['rect'].right > WIDTH:
            alien_direction *= -1
            for a in aliens:
                a['rect'].y += 10  # Move aliens down when they hit the edge

#--------------
def display_game_over():
    global player_health, aliens, in_shooting_display, in_course_selection
    if player_health <= 0:
        draw_text("Game Over!", font, WHITE, WIDTH // 2 - 100, HEIGHT // 2)
        draw_text("You are defeated!", font, WHITE, WIDTH // 2 - 120, HEIGHT // 2 + 40)
    elif ammo == 0:
        draw_text("Game Over!", font, WHITE, WIDTH // 2 - 100, HEIGHT // 2)
        draw_text("No ammo left!", font, WHITE, WIDTH // 2 - 120, HEIGHT // 2 + 40)
    
    pygame.display.flip()
    pygame.time.delay(3000)

    # Return to main menu after game over
    in_course_selection = True
    in_shooting_display = False

    bullets.clear()          # Clear all bullets
    alien_bullets.clear()    # Clear alien bullets
    aliens.clear()           # Clear the aliens

    # Check if there is still ammo left
    if ammo > 0:
        # Reset player health and aliens
        player_health = 100
        #create_aliens(3)  # Reset the aliens


# Main Game Loop
clock = pygame.time.Clock()
running = True
in_course_selection = True
in_score_board = False
in_shooting_display = False
in_shop_page = False
in_castle_page = False

while running:
    clock.tick(40)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if in_course_selection and event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            course_buttons = list(opponents.keys())
            for i, course in enumerate(course_buttons):
                button_rect = pygame.Rect(WIDTH - 865 + (i * (160 + 30)), HEIGHT // 2, 160, 160)
                if button_rect.collidepoint(mouse_pos):
                    selected_course = course
                    in_course_selection = False  # Exit course selection
                    in_shooting_display = False  # Reset shooting display flag
                    in_score_board = True
            #check for shop button
            shop_button_rect = pygame.Rect(930, 20, 50, 50)
            if shop_button_rect.collidepoint(mouse_pos):
                in_shop_page = True  # Transition to shop page
                in_course_selection = False  # Exit course selection
                in_score_board = False
                in_shooting_display =False
            # Check for castle button
            castle_button_rect = pygame.Rect(840, 20, 50,50)
            if castle_button_rect.collidepoint(mouse_pos):
                in_castle_page = True  # Transition to castle page
                in_course_selection = False  # Exit course selection
                in_score_board = False
                in_shooting_display =False

        # Handle shop page
        elif in_shop_page and event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos   
            button_back_rect = pygame.Rect(20,20, 120, 40)
            if button_back_rect.collidepoint(mouse_pos):
                in_shop_page = False
                in_course_selection = True

            button_upgrade_rect = pygame.Rect(400,200, 250, 250)
            button_repair_rect = pygame.Rect(700,200, 250, 250)
            if button_upgrade_rect.collidepoint(mouse_pos):
                if ammo >= 20:  # Check if there is enough ammo
                    ammo -= 20
                    old_castle_level = castle_level
                    if castle_level < 3:
                        castle_level += 1
                        screen.blit(background_image, (0,0))
                        draw_text(f"Your castle has been successfully updated from level {old_castle_level} to level {castle_level}", small_font, WHITE, WIDTH // 2 - 300 , HEIGHT // 2)
                        pygame.display.flip() 
                        pygame.time.delay(2000)
                    else:
                        screen.blit(background_image, (0,0))
                        draw_text(f"Your castle has been reached maximum level", small_font, WHITE, WIDTH // 2 - 100, HEIGHT // 2)
                        pygame.display.flip() 
                        pygame.time.delay(2000)

                else:   
                    screen.blit(background_image, (0,0))
                    draw_text(f"You don't have enough ammo! Please submit more assignments!", small_font, WHITE, WIDTH // 2 - 300 , HEIGHT // 2)
                    pygame.display.flip() 
                    pygame.time.delay(2000)

            # Check for repair button
            elif button_repair_rect.collidepoint(mouse_pos):
                if ammo >= 10:  # Check if there is enough ammo
                    ammo -= 10
                    castle_health += 20
                    screen.blit(background_image, (0,0))
                    draw_text(f"You castle's health has been increased by 20!", small_font, WHITE, WIDTH // 2 - 300 , HEIGHT // 2)
                    pygame.display.flip() 
                    pygame.time.delay(2000)
                else:
                    screen.blit(background_image, (0,0))
                    draw_text(f"You don't have enough ammo! please submit your assignment", small_font, WHITE, WIDTH // 2 - 300 , HEIGHT // 2)
                    pygame.display.flip() 
                    pygame.time.delay(2000)

            # Check for repair button
            elif button_repair_rect.collidepoint(mouse_pos):
                if ammo >= 10:  # Check if there is enough ammo
                    ammo -= 10
                    castle_health += 20
                    screen.blit(background_image, (0,0))
                    draw_text(f"You castle's health has been increased by 20!", small_font, WHITE, WIDTH // 2 - 300 , HEIGHT // 2)
                    pygame.display.flip() 
                    pygame.time.delay(2000)
                else:
                    screen.blit(background_image, (0,0))
                    draw_text(f"You don't have enough ammo! please submit your assignment", small_font, WHITE, WIDTH // 2 - 300 , HEIGHT // 2)
                    pygame.display.flip() 
                    pygame.time.delay(2000)

        elif in_score_board and event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            students_data = opponents[selected_course]
            students = students_data["students"]
            if ammo == 0:
                draw_text(f"No ammo left!", small_font, WHITE, WIDTH // 2 - 300 , HEIGHT // 2)
                pygame.display.flip() 
                pygame.time.delay(2000)
            button_back_rect = pygame.Rect(50, 520, 200, 40)
            if button_back_rect.collidepoint(mouse_pos):
                in_shop_page = False
                in_course_selection = True
            for i, student in enumerate(students):
                button_rect = pygame.Rect(WIDTH // 2 - 200, 163 + (i * 46), 400, 40)
                if button_rect.collidepoint(mouse_pos):
                    selected_student = student
                    print(f"Selected Student: {selected_student}")
                    in_shooting_display = True  # Transition to shooting display
                    in_score_board = False
                    print(f"In Shooting Display: {in_shooting_display}")
                    bullets.clear()  # Clear previous bullets
                    castle_health = 100  # Reset castle health
                    create_aliens(3)  # Create aliens for this round

        elif in_shooting_display:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    shoot_bullet()  # Shoot bullet

        elif in_castle_page and event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos   
            button_back_rect = pygame.Rect(20,540, 120, 40)
            if button_back_rect.collidepoint(mouse_pos):
                in_shop_page = False
                in_course_selection = True

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and shooter_rect.left > 0:
        shooter_rect.x -= 10  # Move left
    if keys[pygame.K_RIGHT] and shooter_rect.right < WIDTH:
        shooter_rect.x += 10  # Move right

    if in_course_selection:
        draw_course_selection()
    elif in_shop_page:
        draw_shop_page()
    elif in_score_board:
        draw_dashboard()
    elif in_shooting_display:
        draw_shooting_display()

    # Alien shooting every 2 seconds
        if len(aliens) > 0 and pygame.time.get_ticks() % 2000 < 50:  # Simple timing check
            alien_shoot()

        if ammo == 0 or player_health <= 0: # Show game over
            display_game_over()
        else:
            attack_castle()  # Check for castle attacks
            move_aliens()  # Move aliens
            move_alien_bullets()  # Move alien bullets

    elif in_castle_page:
        draw_castles_page()
            

    pygame.display.flip()

# Quit Pygame
pygame.quit()