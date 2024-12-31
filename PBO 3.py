
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