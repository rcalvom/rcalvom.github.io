FROM node:22-bookworm-slim

WORKDIR /app

COPY package*.json ./
RUN chown -R node:node /app
USER node
RUN npm ci

COPY --chown=node:node . .

EXPOSE 4000

CMD ["npm", "run", "dev"]
