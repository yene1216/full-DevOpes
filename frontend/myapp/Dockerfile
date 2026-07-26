# Stage 1: Build React app
FROM node:22-alpine AS build

WORKDIR /app

# Copy package files
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy project files
COPY . .

# Build Vite app
RUN npm run build


# Stage 2: Serve with Nginx
FROM nginx:alpine

# Copy build output to nginx
COPY --from=build /app/dist /usr/share/nginx/html

# Expose nginx port
EXPOSE 80

# Start nginx
CMD ["nginx", "-g", "daemon off;"]