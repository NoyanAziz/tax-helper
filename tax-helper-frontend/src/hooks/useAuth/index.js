"use client";

import { useEffect, useState } from "react";
import Cookies from "universal-cookie";

export function useAuth() {
  const [auth, setAuth] = useState(null);

  const getVerifiedToken = async () => {
    const cookies = new Cookies();
    const token = cookies.get("token") ?? null;

    setAuth(token);
  };

  useEffect(() => {
    getVerifiedToken();
  }, []);

  return auth;
}
