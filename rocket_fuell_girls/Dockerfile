# Dockerfile for Rocket Fuell Girls Platform
FROM node:18-alpine

# Set working directory
WORKDIR /app

# Install dependencies for Sharp (image processing)
RUN apk add --no-cache \
    vips-dev \
    python3 \
    make \
    g++

# Copy package files
COPY package*.json ./

# Install npm dependencies
RUN npm ci --only=production && npm cache clean --force

# Copy application files
COPY . .

# Create uploads directory with proper permissions
RUN mkdir -p uploads/originals uploads/thumbs && \
    chown -R node:node uploads

# Create non-root user for security
RUN addgroup -g 1001 -S nodejs && \
    adduser -S nextjs -u 1001

# Change to non-root user
USER nextjs

# Expose port
EXPOSE 3000

# Health check
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
    CMD node -e "require('http').get('http://localhost:3000/api/health', (res) => process.exit(res.statusCode === 200 ? 0 : 1))"

# Start the application
CMD ["npm", "start"]