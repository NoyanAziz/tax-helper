"use client";

import React from "react";
import { AppBar, Box, IconButton, Toolbar, Typography } from "@mui/material";
import { ChatHistory } from "../components";
import { LABELS } from "../constants/displayMessages";
import { Logout } from "@mui/icons-material";
import Cookies from "universal-cookie";
import { useRouter } from "next/navigation";

export default function Dashboard() {
  const cookies = new Cookies();
  const router = useRouter();

  return (
    <Box sx={{ flexGrow: 1 }}>
      <AppBar position="static">
        <Toolbar>
          <Typography
            color="paleturquoise"
            variant="h6"
            component="div"
            sx={{ flexGrow: 1 }}
          >
            {LABELS.DASHBOARD_TITLE}
          </Typography>
          <IconButton
            onClick={() => {
              cookies.remove("token");
              router.push("/login");
            }}
          >
            <Logout style={{ color: "indianred" }} />
          </IconButton>
        </Toolbar>
      </AppBar>
      <ChatHistory />
    </Box>
  );
}
