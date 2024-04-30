const BACKEND_BASE_ROUTE = "http://localhost:8000";
export const GET_PROMPTS = `${BACKEND_BASE_ROUTE}/chats/prompts/`;
export const SEND_PROMPT = `${BACKEND_BASE_ROUTE}/chats/send-prompt/`;

export default { GET_PROMPTS, SEND_PROMPT };
