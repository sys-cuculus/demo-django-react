FROM node:22-alpine

WORKDIR /app

COPY ../../client/package*.json ./

RUN npm update && npm install

EXPOSE 5173

CMD ["npm", "run", "dev", "--", "--host", "0.0.0.0"]