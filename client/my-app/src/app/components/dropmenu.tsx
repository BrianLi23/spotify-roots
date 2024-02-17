"use client";
import React from "react";
import { useMemo, useState } from "react";
import {
  Dropdown,
  DropdownTrigger,
  DropdownMenu,
  DropdownItem,
  Button,
} from "@nextui-org/react";

interface DropmenuProps {
  onChange: (value: string) => void;
}

export default function Dropmenu({ onChange }: DropmenuProps) {
  const [selectedKeys, setSelectedKeys] = useState<string>("track");

  const selectedValue = useMemo(
    () => Array.from(selectedKeys).join(", ").replaceAll("_", " "),
    [selectedKeys]
  );

  // Calls handler when selection changes
  const handleSelectionChange = (key: React.Key | React.Key[]) => {
    // Ensure the key is a string before proceeding
    if (typeof key === "string") {
      onChange(key); // Call the onChange callback with the string key
    }
  };

  return (
    <Dropdown>
      <DropdownTrigger>
        <Button variant="bordered" className="capitalize">
          {selectedValue}
        </Button>
      </DropdownTrigger>
      <DropdownMenu
        aria-label="Single selection example"
        variant="flat"
        disallowEmptySelection
        selectionMode="single"
        onAction={handleSelectionChange}
      >
        <DropdownItem key="track">Track</DropdownItem>
        <DropdownItem key="artist">Artist</DropdownItem>
        <DropdownItem key="album">Album</DropdownItem>
      </DropdownMenu>
    </Dropdown>
  );
}
