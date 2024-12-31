
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
