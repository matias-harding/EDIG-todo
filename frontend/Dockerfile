FROM node:16-alpine as build

WORKDIR /app

COPY package.json package-lock.json ./

RUN npm install

COPY . .

RUN npm run build

# Segunda etapa para mantener la imagen lo mas pequeña posible
FROM node:16-alpine

WORKDIR /app

RUN npm install -g serve

COPY --from=build /app/dist /app

EXPOSE 3000

CMD ["serve", "-s", ".", "-l", "3000"]
