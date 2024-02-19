"use client";
import React, { useState, useEffect } from "react";
import Dropmenu from "./dropmenu";
import { useRouter } from "next/navigation";
import Link from "next/link";

export default function SearchBar() {
  const [query, setQuery] = useState("");
  const [searchType, setSearchType] = useState("track");
  const router = useRouter();

  const handleSubmit = async (
    event: React.FormEvent<HTMLFormElement>
  ): Promise<void> => {
    event.preventDefault(); // Understands 'event' as a form event

    // Log data being sent for debugging purposes
    console.log("Sending", { search_query: query, search_type: searchType });

    try {
      const response = await fetch("http://127.0.0.1:8080/api/search", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ search_query: query, search_type: searchType }),
      });

      const data = await response.json(); // Parse the JSON response
      console.log("Received response:", data); // Log response data for debugging

      router.push("/resultpage"); // The route of the results page
    } catch (error) {
      console.error("Error sending search query:", error);
    }
  };

  return (
    <div className="text-center">
      <h3 className="text-xl">Search a track, artist or album!</h3>
      <div className="m-6">
        <form onSubmit={handleSubmit}>
          <input
            type="text"
            value={query}
            onChange={(e) => setQuery(e.target.value)}
            placeholder="Search..."
            className="rounded-lg border-2 border-slate-400 p-2 px-9 m-10"
          />
          <Dropmenu onChange={setSearchType} />
          <button
            type="submit"
            className="rounded-lg border-2 border-slate-400 p-2 mr-10 m-10"
          >
            Search
          </button>
        </form>
      </div>
    </div>
  );
}
