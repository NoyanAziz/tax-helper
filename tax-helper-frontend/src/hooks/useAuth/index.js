"use client";

import React, { useEffect } from "react";
import Cookies from "universal-cookie";
import { verifyJwtToken } from "@/libs/auth";

export function useAuth() {
  const [auth, setAuth] = React.useState(null);

  const getVerifiedToken = async () => {
    const cookies = new Cookies();
    const token = cookies.get("token") ?? null;
    const verifiedToken = await verifyJwtToken(token);

    setAuth(verifiedToken);
  };

  useEffect(() => {
    getVerifiedToken();
  }, []);

  return auth;
}
