import pygame
import random
import abc
import sys

class GameObject(abc.ABC):
    def __init__(self, x, y, color):
        self._x = x
        self._y = y
        self._color = color

    @abc.abstractmethod
    def draw(self, surface):
        pass

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @x.setter
    def x(self, value):
        self._x = value

    @y.setter
    def y(self, value):
        self._y = value

class Ball(GameObject):
    def __init__(self, x, y, radius, gravitasi=0.5, tinggi_lompatan=-10):
        super().__init__(x, y, (255, 165, 0))
        self._radius = radius
        self._kecepatan = 0
        self._gravitasi = gravitasi
        self._tinggi_lompatan = tinggi_lompatan

    def draw(self, surface):
        pygame.draw.circle(surface, self._color, (int(self._x), int(self._y)), self._radius)

    def update(self):
        self._kecepatan += self._gravitasi
        self._y += self._kecepatan

    def lompat(self):
        self._kecepatan = self._tinggi_lompatan

    def get_radius(self):
        return self._radius

class Pipe(GameObject):
    def __init__(self, x, atas, bawah, lebar, warna=(0, 255, 0)):
        super().__init__(x, 0, warna)
        self._atas = atas
        self._bawah = bawah
        self._lebar = lebar

    def draw(self, surface):
        pygame.draw.rect(surface, self._color, (self._x, 0, self._lebar, self._atas))
        pygame.draw.rect(surface, self._color, (self._x, self._bawah, self._lebar, surface.get_height() - self._bawah))

    def update(self, kecepatan):
        self._x -= kecepatan

class FlappyBallGame:
    def __init__(self, lebar=600, tinggi=400):
        pygame.init()
        self._layar = pygame.display.set_mode((lebar, tinggi))
        pygame.display.set_caption("Flappy Ball")

        self._LEBAR = lebar
        self._TINGGI = tinggi
        self._FPS = 60
        self._WARNA = {
            'putih': (255, 255, 255),
            'hitam': (0, 0, 0)
        }

        # Tambahkan gambar latar belakang
        self._background = pygame.image.load("background permainann.jpg")
        self._background = pygame.transform.scale(self._background, (lebar, tinggi))

        self._ball = Ball(100, tinggi // 2, 15)
        self._pipa = []
        self._skor = 0
        self._font = pygame.font.SysFont("Arial", 30)
        self._clock = pygame.time.Clock()

    def _buat_pipa(self):
        tinggi_pipa = random.randint(100, self._TINGGI - 150 - 100)
        pipa_baru = Pipe(
            x=self._LEBAR,
            atas=tinggi_pipa,
            bawah=tinggi_pipa + 150,
            lebar=50
        )
        self._pipa.append(pipa_baru)

    def _cek_tabrakan(self):
        if (self._ball.y - self._ball.get_radius() <= 0 or
                self._ball.y + self._ball.get_radius() >= self._TINGGI):
            return False

        for p in self._pipa:
            if (self._ball.x + self._ball.get_radius() > p.x and
                    self._ball.x - self._ball.get_radius() < p.x + p._lebar):
                if (self._ball.y - self._ball.get_radius() < p._atas or
                        self._ball.y + self._ball.get_radius() > p._bawah):
                    return False
        return True

    def game_over(self):
        font = pygame.font.SysFont('Arial', 70)
        text_surface = font.render('GAME OVER', True, pygame.Color(0, 0, 139))
        text_rect = text_surface.get_rect(center=(self._LEBAR // 2, self._TINGGI // 2))

        self._layar.fill(pygame.Color(173, 216, 230))
        self._layar.blit(text_surface, text_rect)

        skor_surface = self._font.render(f"Score Akhir: {self._skor}", True, pygame.Color(0, 0, 0))
        skor_rect = skor_surface.get_rect(center=(self._LEBAR // 2, self._TINGGI // 2 + 50))
        self._layar.blit(skor_surface, skor_rect)

        pygame.display.flip()
        pygame.time.delay(5000)
        pygame.quit()
        sys.exit()

    def main_menu(self):
        judul_font = pygame.font.SysFont('Arial', 70)
        opsi_font = pygame.font.SysFont('Arial', 30)

        judul_surface = judul_font.render('FLAPPY BALL', True, pygame.Color(255, 165, 0))
        judul_rect = judul_surface.get_rect(center=(self._LEBAR // 2, self._TINGGI // 3))

        mulai_surface = opsi_font.render('Mulai', True, pygame.Color(0, 0, 0))
        mulai_rect = mulai_surface.get_rect(center=(self._LEBAR // 2, self._TINGGI // 2))

        keluar_surface = opsi_font.render('Keluar', True, pygame.Color(0, 0, 0))
        keluar_rect = keluar_surface.get_rect(center=(self._LEBAR // 2, self._TINGGI // 2 + 50))

        while True:
            self._layar.fill(self._WARNA['putih'])
            self._layar.blit(judul_surface, judul_rect)
            self._layar.blit(mulai_surface, mulai_rect)
            self._layar.blit(keluar_surface, keluar_rect)

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if mulai_rect.collidepoint(event.pos):
                        return
                    if keluar_rect.collidepoint(event.pos):
                        pygame.quit()
                        sys.exit()

    def run(self):
        self.main_menu()

        berjalan = True
        pengatur_waktu_pipa = 0

        while berjalan:
            self._clock.tick(self._FPS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    berjalan = False
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    self._ball.lompat()

            self._ball.update()
            pengatur_waktu_pipa += 1
            if pengatur_waktu_pipa > 90:
                self._buat_pipa()
                pengatur_waktu_pipa = 0

            for p in self._pipa:
                p.update(5)
            self._pipa = [p for p in self._pipa if p.x + 50 > 0]

            for p in self._pipa:
                if p.x + 50 == self._ball.x:
                    self._skor += 1

            if not self._cek_tabrakan():
                self.game_over()

            # Gambarkan latar belakang
            self._layar.blit(self._background, (0, 0))
            
            self._ball.draw(self._layar)
            for p in self._pipa:
                p.draw(self._layar)

            teks_skor = self._font.render(f"Score: {self._skor}", True, self._WARNA['hitam'])
            self._layar.blit(teks_skor, (10, 10))
            pygame.display.flip()

        pygame.quit()

if __name__ == "__main__":
    game = FlappyBallGame()
    game.run()