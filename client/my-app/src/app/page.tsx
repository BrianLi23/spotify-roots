"use client";
import React, { useEffect, useState } from "react";
import Cover from "./components/cover";
import SearchBar from "./components/searchBar";
import AboutPage from "./components/aboutPage";
import Image from "next/image";

export default function Home() {
  const [data, setData] = useState({
    artist_name: "",
    album_name: "",
    album_release: "",
    song_name: "",
    picture_url: "",
  });

  useEffect(() => {
    fetch("http://localhost:8080/api/home", {
      method: "GET",
      headers: { "Content-Type": "application/json" },
    })
      .then((response) => response.json())
      .then((data) => setData(data))
      .catch((error) => console.error("Error fetching data:", error));
  }, []);

  return (
    <React.Fragment>
      <Cover />
      <AboutPage />
      <SearchBar />
      {/* <Image src={data.picture_url} width={520} height={500} alt="picture" /> */}
    </React.Fragment>
  );
}
