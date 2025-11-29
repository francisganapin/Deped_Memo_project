# DepEd Memo Management System

A Django-based web application for managing Department of Education (DepEd) memorandums. This system provides a comprehensive platform for uploading, searching, viewing, and managing official memos with separate interfaces for administrators and public users.

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Database Models](#database-models)
- [URL Routes](#url-routes)
- [Contributing](#contributing)
- [License](#license)

## 🎯 Overview

The DepEd Memo Management System is designed to streamline the management and distribution of educational memorandums. It provides:

- **Admin Interface**: Full CRUD operations for managing memos
- **Public Interface**: Search and view memos with advanced filtering
- **Custom User Authentication**: Email-based authentication system
- **File Management**: PDF document upload and storage
- **Pagination**: Efficient browsing of large memo collections

## ✨ Features

### Admin Features
- Upload new memorandums with metadata
- Update existing memos
- Delete memos by reference number
- View detailed memo information
- Mark memos as "recent" to highlight them
- Custom admin user model with profile images

### Public User Features
- Browse all memos with pagination (4 per page)
- Search by title, month, and year
- Direct page navigation
- View detailed memo content
- Download PDF documents
- Responsive design

### Technical Features
- Custom user authentication (email-based)
- File upload handling for PDFs and images
- Django Debug Toolbar integration
- SQLite database (development)
- Media file management
- CSRF protection
- Session-based security

## 📁 Project Structure

```
Deped/
│
├── deped/                      # Main project configuration
│   ├── settings.py            # Django settings
│   ├── urls.py                # Root URL configuration
│   ├── wsgi.py                # WSGI configuration
│   └── asgi.py                # ASGI configuration
│
├── b2_dep_model/              # Core models app
│   ├── models.py              # MemoTable & AdminUser models
│   ├── admin.py               # Admin interface configuration
│   └── migrations/            # Database migrations
│
├── a1_admin_user/             # Admin functionality
│   ├── views.py               # Admin views (CRUD operations)
│   └── urls.py                # Admin URL patterns
│
├── a2_public_function/        # Public user functionality
│   ├── views.py               # Public views (search, browse)
│   └── urls.py                # Public URL patterns
│
├── templates/                 # HTML templates
│   ├── for_admin/            # Admin templates
│   │   ├── admin-page.html
│   │   ├── admin_page2_add.html
│   │   ├── memo_content_2.html
│   │   └── page3.html
│   └── for_user/             # Public templates
│       ├── 1_memo_list.html
│       └── 2_memo_content.html
│
├── media/                     # User-uploaded files
│   ├── pdf/                  # Memo PDF files
│   └── employee_id/          # Admin profile images
│
├── static/                    # Static files (CSS, JS, images)
│   └── admin/                # Django admin static files
│
├── db.sqlite3                # SQLite database
└── manage.py                 # Django management script
```

## 🚀 Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Virtual environment (recommended)

### Step-by-Step Installation

1. **Clone or download the project**
   ```bash
   cd "c:\Users\francis\OneDrive\Desktop\DJANGO PROJECT\Deped"
   ```

2. **Create and activate a virtual environment**
   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate

   # Linux/Mac
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install Django==5.1.7
   pip install django-debug-toolbar
   pip install Pillow  # For image handling
   ```

4. **Create requirements.txt** (if not exists)
   ```bash
   pip freeze > requirements.txt
   ```

5. **Apply database migrations**
   ```bash
   python manage.py migrate
   ```

6. **Create a superuser**
   ```bash
   python manage.py createsuperuser
   ```
   Enter email, first name, last name, and password when prompted.

7. **Run the development server**
   ```bash
   python manage.py runserver
   ```

8. **Access the application**
   - Public Interface: http://127.0.0.1:8000/
   - Admin Interface: http://127.0.0.1:8000/admin-page/
   - Django Admin: http://127.0.0.1:8000/admin/

## ⚙️ Configuration

### Settings Overview

Key settings in `deped/settings.py`:

```python
# Custom User Model
AUTH_USER_MODEL = "b2_dep_model.AdminUser"

# Media Files
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Static Files
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']

# Timezone
TIME_ZONE = 'Asia/Manila'

# Debug Toolbar
INSTALLED_APPS = [
    ...
    'debug_toolbar',
]
```

### Security Settings

⚠️ **Important**: Before deploying to production:

1. Change `SECRET_KEY` in settings.py
2. Set `DEBUG = False`
3. Configure `ALLOWED_HOSTS`
4. Use PostgreSQL instead of SQLite
5. Set up proper static file serving
6. Enable HTTPS

## 📖 Usage

### For Public Users

1. **Browse Memos**: Visit the homepage to see paginated memos
2. **Search**: Use the sidebar filters to search by:
   - Title (text search)
   - Month (dropdown)
   - Year (number input)
   - Page number (direct navigation)
3. **View Details**: Click on any memo title to view full details
4. **Download**: PDF files are accessible from the detail view

### For Administrators

1. **Access Admin Panel**: Navigate to `/admin-page/`
2. **Upload Memo**: 
   - Click "Upload" button
   - Fill in title, description, reference number
   - Upload PDF file
   - Submit (automatically marks as "recent")
3. **Update Memo**: Click on a memo and edit its information
4. **Delete Memo**: Use the delete function with reference number
5. **Search**: Filter memos by title

## 🗄️ Database Models

### MemoTable

Stores all memorandum information.

| Field | Type | Description |
|-------|------|-------------|
| id | AutoField | Primary key |
| title | CharField(255) | Memo title |
| description | TextField(255) | Memo description |
| reference_data | CharField(50) | Unique reference number |
| month | CharField(50) | Month of memo |
| year | CharField(50) | Year of memo |
| recent | BooleanField | Highlight flag (default: True) |
| file | FileField | PDF file upload |

**Meta Options**:
- Ordering: By month (descending)
- Table name: `memo_table`

### AdminUser

Custom user model for authentication.

| Field | Type | Description |
|-------|------|-------------|
| id | AutoField | Primary key |
| email | EmailField | Unique login email |
| first_name | CharField(20) | User's first name |
| last_name | CharField(20) | User's last name |
| password | CharField | Hashed password |
| is_staff | BooleanField | Staff status |
| is_active | BooleanField | Active status |
| date_joined | DateTimeField | Registration date |
| image | ImageField | Profile picture |

**Authentication**:
- USERNAME_FIELD: `email`
- Inherits from AbstractBaseUser and PermissionsMixin
- Custom manager: CustomUserManager

## 🔗 URL Routes

### Public Routes (`a2_public_function`)

| URL | View | Name | Description |
|-----|------|------|-------------|
| `/` | memo_page1_view | memo_page1_views | Main memo list with search |
| `/memo/list-content/page/<page>/content/<id>/id` | memo_views_content | memo_views_content | Memo detail view |

### Admin Routes (`a1_admin_user`)

| URL | View | Name | Description |
|-----|------|------|-------------|
| `/admin-page/` | memo_views | memo_views | Admin memo list |
| `/admin-page/check_memo/page/<id>` | memo_check_view | memo_check_view | View memo details |
| `/admin-page/page2/upload_memo/` | memo_upload_views | memo_upload_views | Upload new memo |
| `/admin-page/page2/delete_memo/` | memo_delete_view | memo_delete_views | Delete memo |
| `/admin-page/page2/update_memo/<id>` | memo_update_views | memo_update_views | Update memo |

### System Routes

| URL | Description |
|-----|-------------|
| `/admin/` | Django admin interface |
| `/__debug__/` | Django Debug Toolbar |

## 🎨 Frontend

### Technologies Used
- HTML5
- CSS3 (embedded styles)
- Django Template Language
- Responsive design patterns

### Key UI Features
- Clean, modern interface
- Card-based memo display
- Sidebar search controls
- Pagination controls
- Hover effects and transitions
- Mobile-responsive layout

## 🔐 Security Considerations

### Current Implementation
✅ CSRF protection enabled
✅ Password hashing (Django's built-in)
✅ Session-based authentication
✅ XFrame protection
✅ Clickjacking protection

### Recommended Improvements
- [ ] Add HTTPS in production
- [ ] Implement rate limiting
- [ ] Add file type validation for uploads
- [ ] Implement file size limits
- [ ] Add user permission checks on all views
- [ ] Use environment variables for secrets
- [ ] Add input sanitization
- [ ] Implement audit logging

## 🐛 Known Issues & TODOs

Based on the code review:

1. **Update View Bug** (line 49-51 in `a1_admin_user/views.py`):
   - Variables have trailing commas causing tuples instead of strings
   - `reference_data` is not assigned to `memo.reference_data`

2. **Missing Features**:
   - No user authentication required for views
   - No file size/type validation
   - No error handling for file uploads
   - Month stored as string (date formatting issue)

3. **Code Quality**:
   - Commented-out code should be removed
   - Print statements in views (debugging code)
   - Inconsistent error handling

## 📝 Development History

According to `update.txt`:

- **10/11/2025**: Added page search, updated meta order date
- **5/17/2025**: Updated upload functionality
- **5/13/2025**: Added admin image and models
- **5/7/2025**: Fixed page CSS
- **5/3/2025**: Fixed URLs, updated memo page, partitioned functions
- **4/8/2025**: Added PDF download

## 🤝 Contributing

1. Create a feature branch
2. Make your changes
3. Test thoroughly
4. Submit a pull request

## 📄 License

[Add your license information here]

## 👥 Authors

Francis Ganapin

## 📞 Support

For issues and questions, please contact the development team.

---

**Last Updated**: November 29, 2025
