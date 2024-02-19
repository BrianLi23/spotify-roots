import React, { useState, Key } from "react";
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
  const [selectedKey, setSelectedKey] = useState<string>("▽");

  // Calls handler when selection changes
  const handleSelectionChange = (key: Key) => {
    // Ensure the key is a string before proceeding
    if (typeof key === "string") {
      setSelectedKey(key); // Update the local state

      onChange(key); // Call the onChange callback with the string key
    }
  };

  return (
    <Dropdown>
      <DropdownTrigger>
        <Button variant="bordered" className="capitalize">
          {selectedKey.replace("_", " ")} {/* Use selectedKey directly */}
        </Button>
      </DropdownTrigger>
      <DropdownMenu
        aria-label="Single selection example"
        variant="flat"
        disallowEmptySelection
        selectionMode="single"
        onAction={handleSelectionChange} // Corrected to handleSelectionChange
      >
        <DropdownItem key="track">Track</DropdownItem>
        <DropdownItem key="artist">Artist</DropdownItem>
        <DropdownItem key="album">Album</DropdownItem>
      </DropdownMenu>
    </Dropdown>
  );
}
