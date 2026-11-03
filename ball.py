import pygame._sdl2

pygame.init()

w, h = 500, 500

scr = pygame.display.set_mode((w, h), pygame.RESIZABLE)
win = pygame._sdl2.Window.from_display_module()
old_pos = win.position

clk = pygame.time.Clock()
vel = pygame.Vector2()
pos = pygame.Vector2(w / 2, h / 2)
r = 10
x, y = pygame.mouse.get_pos()
grabbed = False

running = True
while running:
    old_x, old_y = x, y
    x, y = pygame.mouse.get_pos()
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False

        elif e.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0] and not grabbed:
            if (x - pos.x) ** 2 + (y - pos.y) ** 2 <= r ** 2:
                grabbed = True

        elif e.type == pygame.MOUSEBUTTONUP and not pygame.mouse.get_pressed()[0] and grabbed:
            grabbed = False
            vel += x - old_x, y - old_y

        elif e.type == pygame.MOUSEWHEEL:
            r += e.y

    w, h = scr.get_size()

    pos += old_pos[0] - win.position[0], old_pos[1] - win.position[1]
    old_pos = win.position

    if grabbed:
        pos.x, pos.y = x, y
    else:
        if pos.x < r:
            vel.x += r - pos.x
        elif pos.x > w - r:
            vel.x += w - r - pos.x

        if pos.y < r:
            vel.y += r - pos.y
        elif pos.y > h - r:
            vel.y += h - r - pos.y

        pos += vel

        if pos.x < r:
            vel.x = abs(vel.x) / 2
        elif pos.x > w - r:
            vel.x = -abs(vel.x) / 2

        if pos.y < r:
            vel.y = abs(vel.y) / 2
        elif pos.y > h - r:
            vel.y = -abs(vel.y) / 2

        vel.y += 1

        vel.x *= 0.945 if pos.y < r or pos.y > h - r else 0.99
        vel.y *= 0.945 if pos.x < r or pos.x > w - r else 0.99

    pos.x, pos.y = min(w - r, max(r, pos.x)), min(h - r, max(r, pos.y))

    scr.fill((0, 0, 0))
    pygame.draw.circle(scr, (255, 255, 255), pos, r)
    pygame.display.flip()

    clk.tick(60)

pygame.quit()
