"use client";

import React, { useEffect, useState } from "react";

import { AttachFile, Send } from "@mui/icons-material";
import {
  Box,
  Card,
  FormControl,
  Grid,
  IconButton,
  InputAdornment,
  OutlinedInput,
  Typography,
} from "@mui/material";
import Image from "next/image";
import axios from "axios";
import Cookies from "universal-cookie";

export default function ChatHistory() {
  const cookies = new Cookies();
  const token = cookies.get("token");
  const [prompts, setPrompts] = useState([]);

  const getPrompts = () => {
    axios
      .get("http://localhost:8000/chats/prompts/", {
        headers: {
          "Content-Type": "application/json",
          Authorization: `Bearer ${token}`,
        },
      })
      .then((response) => {
        setPrompts(response.data);
      });
  };

  useEffect(() => {
    getPrompts();
  }, []);

  return (
    <Box
      sx={{
        minHeight: "100vh",
        minWidth: "100vh",
        justifyContent: "center",
        alignItems: "center",
        display: "flex",
      }}
    >
      <Card
        sx={{
          width: "100vh",
          height: "90vh",
          color: "primary",
          borderRadius: 5,
        }}
      >
        <Grid container sx={{ height: "100%" }}>
          <Grid
            item
            xs={12}
            sx={{
              display: "flex",
              justifyContent: "center",
              alignItems: "center",
              m: 5,
            }}
          >
            <Typography variant="h5">Tax Helper Chat</Typography>
          </Grid>
          <Grid item xs={12} sx={{ width: 600, height: 600, overflow: "auto" }}>
            {prompts.map((prompt, index) => (
              <Box key={index} sx={{ ml: 5, mr: 5, mt: 4 }}>
                <Typography sx={{ m: 1 }} variant="body1">
                  {prompt.user}
                </Typography>
                <Grid
                  item
                  xs={12}
                  sx={{
                    p: 2,
                    backgroundColor: "background.paper",
                    borderRadius: 2,
                  }}
                >
                  {prompt.attachment ? (
                    <Box key={prompt.id} sx={{ mt: 2 }}>
                      <Typography variant="h6">{prompt.name}</Typography>
                      <Image src={prompt.attachment} alt="Attachment Preview" />
                    </Box>
                  ) : (
                    <Typography variant="body1">{prompt.message}</Typography>
                  )}
                </Grid>
              </Box>
            ))}
          </Grid>
          <Grid
            item
            xs={12}
            sx={{
              display: "flex",
              justifyContent: "center",
              alignItems: "center",
              m: 5,
            }}
          >
            <FormControl fullWidth variant="outlined">
              <OutlinedInput
                id="password"
                sx={{ height: 80, borderRadius: 5 }}
                startAdornment={
                  <InputAdornment position="start">
                    <AttachFile />
                  </InputAdornment>
                }
                endAdornment={
                  <InputAdornment position="end">
                    <IconButton
                      aria-label="toggle password visibility"
                      edge="end"
                    >
                      <Send />
                    </IconButton>
                  </InputAdornment>
                }
              />
            </FormControl>
          </Grid>
        </Grid>
      </Card>
    </Box>
  );
}
