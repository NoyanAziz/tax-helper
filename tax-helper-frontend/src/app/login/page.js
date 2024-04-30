"use client";

import React, { useState } from "react";
import axios from "axios";
import Cookies from "universal-cookie";

import { useRouter } from "next/navigation";

import { Visibility, VisibilityOff } from "@mui/icons-material";
import {
  Box,
  Button,
  Card,
  FormControl,
  Grid,
  IconButton,
  InputAdornment,
  InputLabel,
  OutlinedInput,
  TextField,
  Typography,
} from "@mui/material";
import ROUTES from "../constants/routes";

export default function Login() {
  const [showPassword, setShowPassword] = useState(false);

  const cookies = new Cookies();
  const router = useRouter();

  const handleSubmit = async (event) => {
    event.preventDefault();
    const formData = new FormData(event.target);

    const email = formData.get("email");
    const password = formData.get("password");

    axios
      .post(ROUTES.LOGIN, {
        email: email,
        password: password,
      })
      .then((response) => {
        cookies.set("token", response.data.access, { path: "/" });

        router.push("/dashboard");
        router.refresh();
      })
      .catch((error) => {
        alert("Login failed: " + error.message);
      });
  };

  return (
    <Box
      sx={{
        minHeight: "100vh",
        justifyContent: "center",
        alignItems: "center",
        display: "flex",
      }}
    >
      <Card
        sx={{
          width: 450,
          height: 600,
          color: "primary",
        }}
      >
        <Grid container>
          <Grid
            item
            xs={12}
            sx={{
              display: "flex",
              justifyContent: "center",
              alignItems: "center",
              mt: 5,
            }}
          >
            <Typography variant="h5">login</Typography>
          </Grid>
          <form style={{ width: "100%" }} onSubmit={handleSubmit}>
            <Grid
              item
              xs={12}
              sx={{
                display: "flex",
                justifyContent: "center",
                alignItems: "center",
                mt: 10,
              }}
            >
              <TextField
                fullWidth
                sx={{ m: 2 }}
                id="email"
                name="email"
                label="Email"
                type="email"
              />
            </Grid>
            <Grid
              item
              xs={12}
              sx={{
                display: "flex",
                justifyContent: "center",
                alignItems: "center",
              }}
            >
              <FormControl fullWidth sx={{ m: 2 }} variant="outlined">
                <InputLabel htmlFor="password">Password</InputLabel>
                <OutlinedInput
                  id="password"
                  name="password"
                  type={showPassword ? "text" : "password"}
                  endAdornment={
                    <InputAdornment position="end">
                      <IconButton
                        aria-label="toggle password visibility"
                        onClick={() => setShowPassword((prev) => !prev)}
                        edge="end"
                      >
                        {showPassword ? <VisibilityOff /> : <Visibility />}
                      </IconButton>
                    </InputAdornment>
                  }
                  label="Password"
                />
              </FormControl>
            </Grid>
            <Grid
              item
              xs={12}
              sx={{
                display: "flex",
                justifyContent: "center",
                alignItems: "center",
                mt: 10,
              }}
            >
              <Button
                fullWidth
                sx={{ height: 50, m: 2 }}
                variant="outlined"
                type="submit"
              >
                <Typography variant="button">login</Typography>
              </Button>
            </Grid>
          </form>
        </Grid>
      </Card>
    </Box>
  );
}
