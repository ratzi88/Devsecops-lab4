# Use an official Nginx image to serve the frontend
FROM nginx:alpine

# Remove the default Nginx configuration
RUN rm /etc/nginx/conf.d/default.conf

# Copy your custom Nginx configuration to handle your routing
COPY nginx.conf /etc/nginx/nginx.conf

# Copy the frontend files into the Nginx HTML directory
COPY ./user_login /usr/share/nginx/html/login/
COPY ./user_register /usr/share/nginx/html/register/

# Expose port 80 for the frontend
EXPOSE 80

# Start Nginx server
CMD ["nginx", "-g", "daemon off;"]
