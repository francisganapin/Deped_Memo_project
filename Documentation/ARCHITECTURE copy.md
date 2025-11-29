# Django Project Architecture Documentation

## 🏗️ System Architecture Overview

### High-Level Architecture

```
Client Browser → Django Application → SQLite DB
     │                  │
     │            ┌─────┴─────┐
     │            │           │
  Public       Admin       Models
  Views        Views     (MemoTable, AdminUser)
```

## 📦 Application Structure

### Django Apps

#### 1. **b2_dep_model** (Core Models)
- `MemoTable`: Stores memorandum data
- `AdminUser`: Custom user authentication
- `CustomUserManager`: User management

#### 2. **a1_admin_user** (Admin Functions)
- Upload, update, delete memos
- Admin-specific UI

#### 3. **a2_public_function** (Public Interface)
- Browse and search memos
- Public UI

## 🔄 Request Flow

### Public User Flow
```
User → / → memo_page1_view → Query DB → Paginate → Render
```

### Admin Upload Flow
```
Admin → /upload → Validate → Set recent=False → Create new → Save file
```

## 📊 Data Models

### MemoTable
- title, description, reference_data
- month, year, recent, file

### AdminUser
- email (unique), first_name, last_name
- password, is_staff, is_active

## 🔐 Security Recommendations

1. Add authentication decorators
2. Validate file uploads
3. Use environment variables for secrets
4. Add permission checks

## 🚀 Performance Tips

1. Add database indexes
2. Implement caching
3. Optimize queries with `only()`
4. Use connection pooling

---

**For detailed architecture, see full documentation.**
