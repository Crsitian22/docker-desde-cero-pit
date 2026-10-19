FROM php:8.2-cli-alpine

# Instalar extensión pdo_mysql oficial requerida por PHP/Laravel para MySQL
RUN docker-php-ext-install pdo pdo_mysql

WORKDIR /var/www/html

COPY . .

EXPOSE 8000

CMD ["php", "-S", "0.0.0.0:8000"]
