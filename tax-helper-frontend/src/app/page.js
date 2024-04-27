import Image from "next/image";
import styles from "./page.module.css";
import { Box } from "@mui/material";
import { ChatHistory } from "./components";

export default function Home() {
  return (
    <Box sx={{ 
      minHeight: '100vh',
      justifyContent: 'center',
      alignItems: 'center',
      display: 'flex',
    }}>
      <ChatHistory />
    </Box>
  );
}
