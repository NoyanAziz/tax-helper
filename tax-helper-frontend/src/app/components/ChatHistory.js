"use client";

import React, { useEffect, useState, useRef } from "react";

import { AttachFile, PictureAsPdf, Send } from "@mui/icons-material";
import {
  Box,
  Card,
  CircularProgress,
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
import { SENDER_USER, USER_ROLE } from "../constants/misc";
import { LABELS } from "../constants/displayMessages";
import ROUTES from "../constants/routes";

export default function ChatHistory() {
  const cookies = new Cookies();
  const token = cookies.get("token");

  const scrollRef = useRef(null);

  const [loading, setLoading] = useState(false);
  const [prompts, setPrompts] = useState([]);
  const [message, setMessage] = useState("");
  const [file, setFile] = useState(null);

  const getPrompts = () => {
    axios
      .get(ROUTES.GET_PROMPTS, {
        headers: {
          "Content-Type": "application/json",
          Authorization: `Bearer ${token}`,
        },
      })
      .then((response) => {
        setPrompts(response.data);
        setLoading(false);
      })
      .catch((error) => {
        console.error("Error fetching prompts:", error);
        setLoading(false);
      });
  };

  useEffect(() => {
    if (!loading) {
      setLoading(true);
      getPrompts();
    }
  }, []);

  useEffect(() => {
    if (scrollRef.current) {
      scrollRef.current.scrollIntoView({ behaviour: "smooth" });
    }
  }, [prompts, loading]);

  const handleFileChange = (event) => {
    const selectedFile = event.target.files[0];
    setFile(selectedFile);
    setMessage(selectedFile.name);
  };

  const sendPromptOrFile = async () => {
    setLoading(true);
    if (!file) {
      const formData = new FormData();
      formData.append("message", message);
      const newPrompts = prompts;
      newPrompts.push({
        sender: SENDER_USER,
        message: message,
        role: USER_ROLE,
      });
      setPrompts(newPrompts);
      setMessage("");

      axios
        .post(ROUTES.SEND_PROMPT, formData, {
          headers: {
            "Content-Type": "multipart/form-data",
            Authorization: `Bearer ${token}`,
          },
        })
        .then((response) => {
          const newPrompts = prompts;
          newPrompts.push({
            sender: SENDER_USER,
            message: response.data,
            role: USER_ROLE,
          });
          setPrompts(newPrompts);
          setLoading(false);
        })
        .catch((error) => {
          console.error("Error uploading file:", error);
        });
    } else {
      const formData = new FormData();
      formData.append("attachment", file);

      const newPrompts = prompts;
      newPrompts.push({
        sender: SENDER_USER,
        attachment: file.name,
        role: USER_ROLE,
      });
      setPrompts(newPrompts);
      setFile(null);
      setMessage("");

      axios
        .post(ROUTES.SEND_PROMPT, formData, {
          headers: {
            "Content-Type": "multipart/form-data",
            Authorization: `Bearer ${token}`,
          },
        })
        .then(() => {
          setLoading(false);
        })
        .catch((error) => {
          console.error("Error uploading file:", error);
          setLoading(false);
        });
    }
  };

  return (
    <div style={{ display: "flex", justifyContent: "center" }}>
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
            <Typography color="paleturquoise" variant="h5">
              {LABELS.CHAT}
            </Typography>
          </Grid>
          <Grid
            item
            xs={12}
            sx={{
              width: 600,
              height: "60%",
              overflow: "auto",
              background: "darkslategray",
              ml: 5,
              mr: 5,
              borderRadius: 5,
            }}
          >
            {!loading &&
              prompts.map((prompt, index) => (
                <Box ref={scrollRef} key={index} sx={{ ml: 5, mr: 5, mt: 4 }}>
                  <Typography sx={{ m: 1 }} variant="body1">
                    {prompt.sender}
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
            {loading ? (
              <CircularProgress />
            ) : (
              <FormControl fullWidth variant="outlined">
                <OutlinedInput
                  id="password"
                  sx={{
                    height: 80,
                    borderRadius: 5,
                  }}
                  disabled={loading}
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
                        disabled={loading}
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
                        disabled={loading}
                        onClick={sendPromptOrFile}
                      >
                        <Send style={{ color: "paleturquoise" }} />
                      </IconButton>
                    </InputAdornment>
                  }
                />
              </FormControl>
            )}
          </Grid>
        </Grid>
      </Card>
    </div>
  );
}
