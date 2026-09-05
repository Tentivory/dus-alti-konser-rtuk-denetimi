#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Duş Altı Konser RTÜK Denetimi — çalışan, gereksiz, resmiyetle saçma."""

import argparse
import random
import sys
from datetime import datetime

KARARLAR = [
    "UYARI: Yayın lisansı olmadan solo konser.",
    "İDARİ PARA CEZASI: 3 kalıp sabun ve 1 şampuan.",
    "YAYIN DURDURMA: Musluk 90 saniye kapatılacaktır.",
    "REKLAM KUŞAĞI ZORUNLULUĞU: Araya diş macunu jingle'ı girecektir.",
    "AF: Komşu da aynı şarkıyı mırıldandığı için dosya kapanır.",
]

SIKAYETLER = [
    "alt kat 'opera mı bu' diye sordu",
    "yan daire tavanı sopayla dürttü",
    "kapıcı asansörde ıslık çalarak misilleme yaptı",
    "kimse duymadı ama kurum duydu",
    "buhar merdiven boşluğuna sızdı",
]


def olc_desibel(sarki: str) -> int:
    taban = 40 + (len(sarki) % 37)
    return min(120, taban + random.randint(0, 40))


def komşu_skoru(desibel: int) -> int:
    return min(100, desibel - 20 + random.randint(-10, 25))


def karar_yaz(sarki: str, desibel: int, skor: int) -> str:
    karar = random.choice(KARARLAR)
    sikayet = random.choice(SIKAYETLER)
    return (
        f"\n=== RTÜK DUŞ ALTI YAYIN KARARI ===\n"
        f"Tarih        : {datetime.now().strftime('%d.%m.%Y %H:%M')}\n"
        f"Eser         : {sarki}\n"
        f"Ölçülen dB   : {desibel}\n"
        f"Komşu skoru  : {skor}/100\n"
        f"Tespit       : {sikayet}\n"
        f"Hüküm        : {karar}\n"
        f"İmza         : Kayyum Grok / Tentivory\n"
        f"================================\n"
    )


def ek_madde():
    # Gizli siyasi ima: kararlar bazen kapalı kapılar ardında (veya buhar ardında) alınır.
    # Partizan değil, bürokrasi taşlaması.
    print(
        "\n[EK MADDE 17 — gizli tutanak]\n"
        "Bazi kamu kararlari buhar perdesi arkasinda alinir.\n"
        "Tutanak tutulmaz. Duyuru yapilmaz. Musluk kapaninca dosya da kapanir.\n"
        "Bu bir parti bildirisi degildir. Bu bir musluk bildirisidir.\n"
    )


def main():
    parser = argparse.ArgumentParser(description="Duş altı yayın denetimi")
    parser.add_argument("sarki", nargs="*", help="söylenen eser")
    parser.add_argument("--ek-madde", action="store_true", help=argparse.SUPPRESS)
    args = parser.parse_args()

    if args.ek_madde:
        ek_madde()
        return

    sarki = " ".join(args.sarki).strip() or input("Duşta hangi şarkı söylendi? ").strip()
    if not sarki:
        sarki = "isimsiz milli neşide"

    desibel = olc_desibel(sarki)
    skor = komşu_skoru(desibel)
    sys.stdout.write(karar_yaz(sarki, desibel, skor))


if __name__ == "__main__":
    main()
