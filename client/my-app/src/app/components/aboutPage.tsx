import React from "react";

export default function AboutPage() {
  return (
    <div className="text-center m-80">
      <div className="m-10">
        <h1 className="text-3xl">
          Welcome to Spotify-Roots, a place to discover the origins to your
          favourite songs and albums!
        </h1>
      </div>
      <div className="flex justify-center m-10">
        <div className="w-1/2">
          <h2 className="text-2xl p-10 ">
            Leveraging Spotify API and LLM, find out more about the songs,
            creators and albums you have on loop.
          </h2>
        </div>
        <div className="w-1/2">
          <h2 className="text-2xl p-10">
            Simply search what you want to know and get a detailed summary of
            their origins, we'll even recommend you a few songs you might like!
          </h2>
        </div>
      </div>
      <h3 className="text-xl">Created by: Brian Li</h3>
    </div>
  );
}
