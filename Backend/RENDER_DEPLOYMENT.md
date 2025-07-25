# Render Deployment Guide for Deliveroo

## 1. Database Setup

### Create PostgreSQL Database on Render:
1. Go to https://render.com
2. Click "New +" → "PostgreSQL"
3. Fill in details:
   - Name: `deliveroo-db`
   - Database: `deliveroo_db`
   - User: `deliveroo_user`
   - Region: Choose closest to your users
4. Click "Create Database"
5. Copy the External Database URL

## 2. Web Service Setup

### Create Web Service on Render:
1. Click "New +" → "Web Service"
2. Connect your Git repository
3. Configure settings:
   - **Name**: `deliveroo-api`
   - **Environment**: `Python 3`
   - **Region**: Same as your database
   - **Branch**: `main`
   - **Root Directory**: `Backend`
   - **Build Command**: `./build.sh`
   - **Start Command**: `./start.sh`

## 3. Environment Variables

Add these environment variables in Render:
- `SQLALCHEMY_DATABASE_URL`: [Your Render PostgreSQL External URL]
- `JWT_SECURITY_KEY`: rHBFgsys_5s48656vHGSTCTDTV_187GFGYGijsh
- `ALGORITHM`: HS256
- `ENV`: production
- `PORT`: 10000 (Render will set this automatically)

## 4. Database Migration

The build script will automatically run migrations when deploying.

## 5. Testing the Deployment

After deployment, test your API endpoints:
- `GET https://your-app-name.onrender.com/`
- `GET https://your-app-name.onrender.com/docs` (FastAPI documentation)

## 6. Common Issues and Solutions

### Database Connection Issues:
- Ensure SQLALCHEMY_DATABASE_URL is correct
- Check that the database is in the same region as your web service
- Verify environment variables are set correctly

### Migration Issues:
- Check logs in Render dashboard
- Ensure all migration files are committed to Git
- Verify database permissions

### Application Issues:
- Check application logs in Render dashboard
- Ensure all dependencies are in requirements.txt
- Verify CORS settings if needed for frontend

## 7. Monitoring

- Use Render dashboard to monitor:
  - Application logs
  - Resource usage
  - Database connections
  - Response times
