import pygame
import time
import random
pygame.font.init()

WIDTH, HEIGHT = 1000, 800
pygame.init()
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("DODGE")

BG = pygame.transform.scale(pygame.image.load("yaypurple.jpg"), (WIDTH, HEIGHT))


PLAYER_WIDTH = 40
PLAYER_HEIGHT = 60

PLAYER_VEL = 40
HI_WIDTH = 50
HI_HEIGHT = 50
HI_VEL = 3
STAR_VEL = 10

FONT = pygame.font.SysFont("comicsans", 30)


def draw(player, HIS, elapsed_time):
    WIN.blit(BG, (0, 0))
    
    time_text = FONT.render(f"Score: {round(elapsed_time)}s", 1, "white")
    WIN.blit(time_text, (10, 10))
    
    pygame.draw.rect(WIN, "orange", player)
    
    for HI in HIS:
        pygame.draw.rect(WIN, "red", HI)
    
    pygame.display.update()
    

def main():
    run = True
    
    player = pygame.Rect(200, HEIGHT - PLAYER_HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT)
    
    clock = pygame.time.Clock()
    start_time = time.time()
    elapsed_time = 0
    
    
    HI_add_time_thing = 10
    HI_count = 0
    
    HIS = []
    hit = False
    
    while run:
        clock.tick(60)
        elapsed_time = time.time() - start_time
        
        if HI_count > HI_add_time_thing:
            for _ in range(random.randint(6,20)):
                HI_x = random.randint(0, WIDTH - HI_WIDTH)
                HI = pygame.Rect(HI_x, -HI_HEIGHT, HI_WIDTH, HI_HEIGHT)
                HIS.append(HI)
                
                HI_add_time_thing = max(200,HI_add_time_thing - 50)
                HI_count = 0
                

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                break
            
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT] and player.x - PLAYER_VEL >= 0:
                player.x -= PLAYER_VEL
                                                                      
            if keys[pygame.K_RIGHT] and player.x + PLAYER_VEL < WIDTH:
                player.x += PLAYER_VEL
                
            if keys[pygame.K_UP] and player.y - PLAYER_VEL >= 0:
                player.y -= PLAYER_VEL
                
            if keys[pygame.K_DOWN] and player.y + PLAYER_VEL < HEIGHT:
                player.y += PLAYER_VEL
                
        for HI in HIS[:]:
            HI.y += STAR_VEL
            if HI.y > HEIGHT:
                HIS.remove(HI)
            elif HI.y >= player.y and HI.colliderect(player):
                HIS.remove(HI)
                hit = True
                break
            
            if hit:
                lost_text = FONT.render("HA HA YOU LOST!", 30, "white")
                WIN.blit(lost_text, (WIDTH/2 - lost_text.get_width()/2, HEIGHT/2 - lost_text.get_height()/2))
                pygame.display.update()
                pygame.quit()
                break
                
                
        HI_count += 1
        draw(player, HIS, elapsed_time)

if __name__ == "__main__":
    main()