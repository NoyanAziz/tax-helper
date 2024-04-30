"use client";

import React, { useEffect, useState } from "react";

import { AttachFile, PictureAsPdf, Send } from "@mui/icons-material";
import {
  Box,
  Card,
  FormControl,
  Grid,
  IconButton,
  InputAdornment,
  OutlinedInput,
  TextField,
  Tooltip,
  Typography,
} from "@mui/material";
import axios from "axios";
import Cookies from "universal-cookie";

export default function ChatHistory() {
  const cookies = new Cookies();
  const token = cookies.get("token");
  const [prompts, setPrompts] = useState([]);

  const [message, setMessage] = useState("");
  const [file, setFile] = useState(null);

  const handleFileChange = (event) => {
    const selectedFile = event.target.files[0];
    setFile(selectedFile);
    setMessage(selectedFile.name);
  };

  const sendPromptOrFile = async () => {
    if (!file) {
      const formData = new FormData();
      formData.append("message", message);

      axios
        .post("http://localhost:8000/chats/send-prompt/", formData, {
          headers: {
            "Content-Type": "multipart/form-data",
            Authorization: `Bearer ${token}`,
          },
        })
        .then((response) => {
          const newPrompts = prompts;
          newPrompts.push({ message: response.data });
          setPrompts(newPrompts);
        })
        .catch((error) => {
          console.error("Error uploading file:", error);
        });
    } else {
      const formData = new FormData();
      formData.append("attachment", file);

      axios
        .post("http://localhost:8000/chats/send-prompt/", formData, {
          headers: {
            "Content-Type": "multipart/form-data",
            Authorization: `Bearer ${token}`,
          },
        })
        .then((response) => {
          const newPrompts = prompts;
          newPrompts.push({ message: response.data });
          setPrompts(newPrompts);
        })
        .catch((error) => {
          console.error("Error uploading file:", error);
        });
    }
  };

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
          height: "90vh",
          width: "100vh",
          display: "flex",
          flexDirection: "column",
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
            }}
          >
            <Typography variant="h5">Tax Helper Chat</Typography>
          </Grid>
          <Grid
            item
            xs={12}
            sx={{
              width: 600,
              height: "60%",
              overflow: "auto",
              background: "dimgray",
              ml: 5,
              mr: 5,
              borderRadius: 5,
            }}
          >
            {prompts.map((prompt, index) => (
              <Box key={index} sx={{ ml: 5, mr: 5, mt: 4 }}>
                <Typography sx={{ m: 1 }} variant="body1">
                  {prompt.person_name}
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
                    <Box sx={{ mt: 2 }}>
                      <Tooltip title={prompt.attachment}>
                        <TextField
                          disabled
                          value={prompt.attachment}
                          alt="Attachment Preview"
                          InputProps={{
                            startAdornment: (
                              <InputAdornment position="start">
                                <PictureAsPdf />
                              </InputAdornment>
                            ),
                          }}
                        />
                      </Tooltip>
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
              ml: 5,
              mr: 5,
            }}
          >
            <FormControl fullWidth variant="outlined">
              <OutlinedInput
                id="password"
                sx={{
                  height: 80,
                  borderRadius: 5,
                }}
                value={message}
                onChange={() => setMessage(event.target.value)}
                startAdornment={
                  <InputAdornment position="start">
                    <label htmlFor="fileInput">
                      <AttachFile />
                    </label>
                    <input
                      id="fileInput"
                      type="file"
                      style={{ display: "none" }}
                      hidden={file === null}
                      onChange={handleFileChange}
                    />
                  </InputAdornment>
                }
                endAdornment={
                  <InputAdornment position="end">
                    <IconButton
                      aria-label="toggle password visibility"
                      edge="end"
                      onClick={sendPromptOrFile}
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
