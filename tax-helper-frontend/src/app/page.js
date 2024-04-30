"use client";

import { useEffect } from "react";
import { useRouter } from "next/navigation";
import { useAuth } from "@/hooks/useAuth";

export default function App() {
  const auth = useAuth();
  const router = useRouter();

  useEffect(() => {
    if (auth) {
      router.push("/dashboard");
    } else {
      router.push("/login");
    }
  }, [auth, router]);

  return null;
}
