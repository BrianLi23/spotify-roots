"use client";
import React from "react";
import Dropmenu from "./dropmenu";
import { useState, FormEvent } from "react";

export default function SearchBar() {
  const [query, setQuery] = useState(""); // State to keep track of the search query
  const [searchType, setSearchType] = useState("track"); // Assuming "track" as default

  const handleSubmit = async (
    event: FormEvent<HTMLFormElement>
  ): Promise<void> => {
    event.preventDefault(); // Prevent default form submission behavior
    const requestOptions = {
      // Create an options object for the fetch request
      method: "POST", // Specify the request method
      headers: {
        // Set headers to specify the type of data being sent
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ query, searchType }), // Convert the query state to JSON and set as request body
    };
    try {
      // Use fetch API to send the request to the Flask backend
      const response = await fetch(
        "http://localhost:8080/api/search",
        requestOptions
      );
      const data = await response.json(); // Parse JSON response body
      console.log(data); // Log the response from the server
    } catch (error) {
      // Log an error if the request fails
      console.error("There was an error sending the query:", error);
    }
  };

  return (
    <div className="flex justify-center gap-10">
      <form onSubmit={handleSubmit}>
        <input
          type="text" // Text input for the search query
          value={query} // Set the input value to the state's query
          onChange={(e) => setQuery(e.target.value)} // Update state on input change
          placeholder="Search..." // Placeholder text for the input
          className="rounded-lg border-2 border-slate-950 p-2 px-9"
        />

        <Dropmenu onChange={setSearchType} />
        <button
          className="rounded-lg border-2 border-slate-950 p-2 mr-10"
          type="submit"
        >
          Submit
        </button>
      </form>
    </div>
  );
}
