"use client";
import { useEffect, useState } from "react";
import React from "react";
import Image from "next/image";

export default function ResultPage() {
  const [data, setData] = useState({
    artist_name: "",
    album_name: "",
    album_release: "",
    song_name: "",
    picture_url: "",
    output: "",
  });

  useEffect(() => {
    fetch("http://127.0.0.1:8080/api/search", {
      method: "GET",
      headers: { "Content-Type": "application/json" },
    })
      .then((response) => response.json())
      .then((data) => setData(data))
      .catch((error) => console.error("Error fetching data:", error));
  }, []);

  return (
    <div className="flex">
      <div>
        <Image
          src={data.picture_url}
          width={1200}
          height={1200}
          alt="picture"
          className="m-10"
        />
      </div>
      <div className="m-12 mr-8">
        <h1 className="text-5xl pl-10">
          {data.song_name} | {data.album_name}
        </h1>
        <h2 className="text-xl pt-2 pl-10">{data.artist_name}</h2>
        <h4 className="text-lg p-10 whitespace-pre-line">{data.output}</h4>
      </div>
    </div>
  );
}
