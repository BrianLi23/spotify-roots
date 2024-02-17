import React from "react";
import { SocialIcon } from "react-social-icons";

export default function Cover() {
  return (
    <div className="flex font-mono items-center justify-center h-screen">
      <h1 className="text-8xl font-bold text-center">Spotify Roots</h1>
      <SocialIcon
        className="m-10"
        network="spotify"
        style={{ height: 100, width: 100 }}
      />
    </div>
  );
}
