# Usa la imagen base de node alpine [cite: 72, 73]
FROM node:18-alpine

# Establece el directorio de trabajo [cite: 74, 75]
WORKDIR /app

# Copia el package.json e instala dependencias [cite: 76, 77, 78]
COPY package.json ./
RUN npm install

# Copia el resto del código [cite: 79, 80]
COPY . .

# Expone el puerto 3000 [cite: 81, 82]
EXPOSE 3000

# Comando para correr la app [cite: 83, 84]
CMD ["node", "app.js"]