# Todo App RESTful API Documentation
```bash
git clone https://github.com/abubakirovxolmirza/TodoApi
```
```bash
docker buld -t todo:1.0
```

API ning asosiy manbalarini ishlatish uchun `.../api/todos/` endpoint'ini ishlatishingiz mumkin. 

Boshqa ma'lumotlarni olish va o'zgartirish uchun mos keladigan endpoint'larni ham ishlatishingiz mumkin.

## Endpointlar

- `GET /api/todos/`: Barcha todo ro’yxatini ko’rsatish uchun.
- `POST /api/new/`: Yangi todo yaratish uchun.
- `GET /api/todos/{id}/`: {id} li todoni qaytarish uchun.
- `DELETE /api/todos/{id}/`: {id} li todoni o’chirish uchun.
- `PUT /api/todos/{id}/`: {id} li todoni yangilash uchun.

## Todo Model

- `title` (string): Todo ning nomi.
- `description` (text): Todo ning tavsifi.
- `data` (datetime): Todo yaratilgan vaqti.
- `is_completed` (boolean): Todo muvaffaqiyatli bajarildimi yoki yo'qmi.

## HTTP So'rovlari va Javoblari

### `POST /api/todos/`

Yangi todo yaratish uchun POST so'rovi. So'rov shakli:

```json
{
    "title": "Finish Homework",
    "description": "Complete math assignment",
    "is_completed": false
}
```
Javob shakli
```json
{
    "id": 1,
    "title": "Finish Homework",
    "description": "Complete math assignment",
    "created_at": "2023-01-01T12:00:00Z",
    "is_completed": false
}
```
## Create New Todo

**Endpoint:** `/api/new/`  
**Method:** `POST`  

**Request**
```json
{
   "title": "Finish Homework",
   "description": "Complete math assignment",
   "is_completed": false
}
```
**Response**
```json
{
   "id": 1,
   "title": "Finish Homework",
   "description": "Complete math assignment",
   "created_at": "2023-01-01T12:00:00Z",
   "is_completed": false
}
```
**Request**
## Update Todo by ID


**Endpoint:** `/api/todos/{id}`  
**Method:** `PUT`  

**Request**
```json
{
   "title": "Finish Homework",
    "description": "Complete math assignment and review solutions",
    "is_completed": true
}
```
**Response**
```json
{
   "id": 1,
    "title": "Finish Homework",
    "description": "Complete math assignment and review solutions",
    "created_at": "2023-01-01T12:00:00Z",
    "is_completed": true
}
```
**Response**
## Delete 

**Endpoint:** `/api/todos/{id}`  
**Method:** `DELETE`  

**Response**
```json
{
    "xabar": "'<title>' muvaffaqiyatli o'chirildi."
}
```
