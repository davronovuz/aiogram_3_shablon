# Telegram Bot Template — aiogram v3.0+

Ushbu shablon `aiogram v3.0+` kutubxonasi yordamida Telegram botlarini ishlab chiqish uchun mo‘ljallangan.

## Texnologiyalar

- **Aiogram v3.0+** — asosan Telegram bot logikasi uchun.
- **SQLAlchemy 2.0** — ma’lumotlar bazasi bilan ishlash uchun.
- **Alembic** — migratsiyalarni boshqarish uchun.
- **Docker** — konteynerda ishga tushirish imkoniyati bilan.

## SQLAlchemy + Alembic

Ushbu loyihada `User` jadvali namunasi bilan ishlovchi SQLAlchemy 2.0 kodi mavjud. Shuningdek, Alembic orqali quyidagi amallarni bajarishingiz mumkin:

- Alembicni ishga tushirish
- Migratsiyalar yaratish
- Migratsiyalarni qo‘llash


## Boshlang‘ich sozlamalar

1. `.env.dist` faylini `.env` nomi bilan nusxa ko‘chiring.
2. `.env` fayl ichidagi kerakli ma’lumotlarni to‘ldiring.
3. Yangi handlerlar yarating va loyihangiz logikasini kengaytiring.

### Docker'siz:

- `venv` yarating
- `requirements.txt` faylidan quyidagi buyruq yordamida kutubxonalarni o‘rnating:

  ```bash
  pip install -r requirements.txt 
  
  python3 bot.py




## Docker orqali ishga tushirish

Agar sizda Docker mavjud bo‘lsa, loyihani quyidagi buyruq bilan ishga tushiring:

```bash
docker-compose up

