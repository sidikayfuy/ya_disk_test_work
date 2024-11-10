
FROM node:22.1-alpine

WORKDIR /app

RUN apk add --no-cache libc6-compat

COPY package*.json ./

RUN npm ci

COPY . /app/

EXPOSE 3000
ENV PATH ./node_modules/.bin/:$PATH
CMD ["npm", "run", "dev"]
