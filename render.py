from meteorlogic import *
from blasterlogic import *
from shiplogic import *

def transform(p):
    x, y = p
    return (WIDTH/2+x, HEIGHT/2-y)

def render(surface):
    enemies = get_enemies()
    meteors = get_meteors()
    explosions = get_explosions()
    blasters = get_blasters()
    d_blasters = get_d_blasters()
    en_blasters = get_en_blasters()

    for m in meteors:
        m_surface = pygame.Surface((4*m.size,4*m.size),pygame.SRCALPHA)
        pygame.draw.polygon(m_surface, m.color, m.vertices)
        pygame.draw.lines(m_surface, (0,0,0), True, m.vertices)
        x, y = transform(m.p)
        surface.blit(m_surface,(x-2*m.size,y-2*m.size),special_flags=pygame.BLEND_ALPHA_SDL2)

    for e in enemies:
        en_surface = pygame.Surface((e.size,e.size),pygame.SRCALPHA)
        t = e.size
        pygame.draw.polygon(en_surface, ENEMY_COLOR, ([0,0],[0,t],[t,0],[t,t]))
        pygame.draw.lines(en_surface, (0,0,0), True, ([0,0],[0,t],[t/2,t/2],[t,0],[t,t]))
        x, y = transform(e.p)
        surface.blit(en_surface,(x,y),special_flags=pygame.BLEND_ALPHA_SDL2)

    for e in explosions:
        e_surface = pygame.Surface((2*e.size,2*e.size))
        pygame.draw.circle(e_surface, EXPLOSION_COLOR, (e.size,e.size), e.size)
        x, y = transform(e.p)
        surface.blit(e_surface,(x-e.size,y-e.size),special_flags=pygame.BLEND_RGB_ADD)


    for b in blasters:
        b_surface = pygame.Surface((b.size,10))
        pygame.draw.line(b_surface, b.color, (0,5),(b.size,5),width = 8)
        x,y = transform(b.p)
        surface.blit(b_surface, (x-b.size,y-5),special_flags=pygame.BLEND_RGBA_MAX)

    for b in d_blasters:
        db_surface = pygame.Surface((b.size,10))
        pygame.draw.line(db_surface, b.color, (0,5),(b.size,5),width = 8)
        x,y = transform(b.p)
        surface.blit(db_surface, (x-b.size,y-5),special_flags=pygame.BLEND_RGBA_MAX)

    for b in en_blasters:
        eb_surface = pygame.Surface((b.size,10))
        pygame.draw.line(eb_surface, b.color, (0,5),(b.size,5),width = 8)
        x,y = transform(b.p)
        surface.blit(eb_surface, (x-b.size,y-5),special_flags=pygame.BLEND_RGBA_MAX)



    ss_surface = pygame.Surface((ship.size,ship.size),pygame.SRCALPHA)
    t = ship.size
    pygame.draw.polygon(ss_surface, SHIP_COLOUR, ([0,0],[t,t/2],[0,t],[t/4,t/2]))
    pygame.draw.lines(ss_surface, (0,0,0), True, ([0,0],[t,t/2],[0,t],[t/4,t/2]))
    x, y = transform(ship.p)
    surface.blit(ss_surface,(x,y),special_flags=pygame.BLEND_ALPHA_SDL2)

    sd_surface = pygame.Surface((drone.size,drone.size),pygame.SRCALPHA)
    t = drone.size
    pygame.draw.polygon(sd_surface, DRONE_COLOUR, ([0,0],[t,t/2],[0,t],[t/4,t/2]))
    pygame.draw.lines(sd_surface, (0,0,0), True, ([0,0],[t,t/2],[0,t],[t/4,t/2]))
    x, y = transform(drone.p)
    surface.blit(sd_surface,(x,y),special_flags=pygame.BLEND_ALPHA_SDL2)

    pygame.init()
    font = pygame.font.Font(None, 32)
    t1,t2 = get_score()
    t3,t4 = get_d_score()
    t5,t6 = get_hits()
    st1 = 'Meteors: '+str(t1)
    st2 = 'Enemies: '+str(t2)
    st3 = 'Meteors: '+str(t3)
    st4 = 'Enemies: '+str(t4)
    st5 = 'Hits: '+str(t5)
    st6 = 'Hits: '+str(t6)
    text1 = font.render(st1, True, (0,255,255))
    text2 = font.render(st2, True, (0,255,255))
    text3 = font.render(st3, True, (0,255,255))
    text4 = font.render(st4, True, (0,255,255))
    text5 = font.render(st5, True, (0,255,255))
    text6 = font.render(st6, True, (0,255,255))
    texts = font.render('p1', True, (0,255,255))
    textd = font.render('p2', True, (0,255,255))
    text1Rect = text1.get_rect()
    text2Rect = text2.get_rect()
    text3Rect = text3.get_rect()
    text4Rect = text4.get_rect()
    text5Rect = text5.get_rect()
    text6Rect = text6.get_rect()
    textsRect = texts.get_rect()
    textdRect = textd.get_rect()
    text1Rect.center = (WIDTH // 1.1, HEIGHT // 9)
    text2Rect.center = (WIDTH // 1.1, HEIGHT // 7)
    text3Rect.center = (WIDTH // 10.1, HEIGHT // 9)
    text4Rect.center = (WIDTH // 10.1, HEIGHT // 7)
    text5Rect.center = (WIDTH // 1.1, HEIGHT // 5)
    text6Rect.center = (WIDTH // 10.1, HEIGHT // 5)
    textsRect.center = (WIDTH // 1.1, HEIGHT // 20)
    textdRect.center = (WIDTH // 10.1, HEIGHT // 20)
    surface.blit(text1,text1Rect)
    surface.blit(text2,text2Rect)
    surface.blit(text3,text3Rect)
    surface.blit(text4,text4Rect)
    surface.blit(text5,text5Rect)
    surface.blit(text6,text6Rect)
    surface.blit(texts,textsRect)
    surface.blit(textd,textdRect)
    
