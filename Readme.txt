# FavoriteTunes

FavoriteTunes is a Django web application that allows users to track and showcase their favorite songs and the artists who perform them.

## Project Setup

### Prerequisites
- Python (3.x)
- Django

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/FavoriteTunes.git
   cd FavoriteTunes

2.Run migrations to set up the database:
  python manage.py migrate

3.Create a superuser for accessing the Django Admin panel:
  python manage.py createsuperuser

4.Run the development server:
  python manage.py runserver


###URLs
Django Admin Panel: http://127.0.0.1:8000/admin/
Use this link to access the Django Admin panel and manage artists and songs.

Song List: http://127.0.0.1:8000/songs/
View a list of all songs.

Song Detail: http://127.0.0.1:8000/songs/<song_id>/
View details of a specific song.

Add New Song: http://127.0.0.1:8000/songs/add/
Use this link to add new songs and artists directly from the webpage.

List of All Artists: http://127.0.0.1:8000/artists/
View a list of all artists.

Songs by Artist: http://127.0.0.1:8000/artists/<artist_id>/songs/
View a list of all songs by a particular artist