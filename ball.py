import pygame._sdl2

pygame.init()

w, h = 500, 500
scr = pygame.display.set_mode((w, h), pygame.RESIZABLE)
win = pygame._sdl2.Window.from_display_module()
wx, wy = win.position

clk = pygame.time.Clock()

x, y = w / 2, h / 2
vx, vy = 0, 0
r = 10
mx, my = pygame.mouse.get_pos()
grabbed = False

running = True
while running:
    old_mx, old_my = mx, my
    mx, my = pygame.mouse.get_pos()
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False

        elif e.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0] and not grabbed:
            mx, my = pygame.mouse.get_pos()
            if (mx - x) ** 2 + (my - y) ** 2 <= r ** 2:
                grabbed = True

        elif e.type == pygame.MOUSEBUTTONUP and not pygame.mouse.get_pressed()[0] and grabbed:
            grabbed = False
            vx, vy = mx - old_mx, my - old_my

    w, h = scr.get_size()

    old_wx, old_wy = wx, wy
    wx, wy = win.position

    if pygame.mouse.get_pressed()[0] and grabbed:
        x = max(r, min(w - r, mx))
        y = max(r, min(h - r, my))
    else:
        dx, dy = old_wx - wx, old_wy - wy

        x += dx
        y += dy

        if x <= r:
            vx += r - x
        elif x >= w - r:
            vx += w - r - x

        if y <= r:
            vy += r - y
        elif y >= h - r:
            vy += h - r - y

        x = max(r, min(w - r, x + vx))
        y = max(r, min(h - r, y + vy))

        if x <= r:
            vx = abs(vx) / 2
        elif x >= w - r:
            vx = -abs(vx) / 2

        if y <= r:
            vy = abs(vy) / 2
        elif y >= h - r:
            vy = -abs(vy) / 2

        vy += 1

        vx *= 0.945 if y <= r or y >= h - r else 0.99
        vy *= 0.945 if x <= r or x >= w - r else 0.99

    scr.fill((0, 0, 0))
    pygame.draw.circle(scr, (255, 255, 255), (x, y), r)
    pygame.display.flip()

    clk.tick(60)

pygame.quit()