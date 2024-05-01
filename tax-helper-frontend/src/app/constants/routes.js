const BACKEND_BASE_ROUTE = "https://tax-helper-backend-noyan-aziz.koyeb.app/";

export const ROUTES = {
  LOGIN: `${BACKEND_BASE_ROUTE}users/login/`,
  GET_PROMPTS: `${BACKEND_BASE_ROUTE}chats/prompts/`,
  SEND_PROMPT: `${BACKEND_BASE_ROUTE}chats/send-prompt/`,
};

export default ROUTES;
